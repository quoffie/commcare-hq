from corehq.apps.commtrack.models import StockState
from corehq.apps.locations.models import SQLLocation
from corehq.apps.reports.datatables import DataTablesHeader, DataTablesColumn
from corehq.apps.reports.filters.fixtures import AsyncLocationFilter
from corehq.apps.users.models import CommCareUser
from custom.ilsgateway.filters import ProductByProgramFilter
from custom.ilsgateway.models import SupplyPointStatusTypes, ILSNotes
from custom.ilsgateway.tanzania import ILSData, MultiReport
from custom.ilsgateway.tanzania.reports.utils import decimal_format, float_format, latest_status
from dimagi.utils.decorators.memoized import memoized
from django.utils.translation import ugettext as _


class InventoryHistoryData(ILSData):

    title = 'Inventory History'
    slug = 'inventory_history'
    show_chart = False
    show_table = True

    @property
    def headers(self):
        headers = DataTablesHeader(*[
            DataTablesColumn(_('Product')),
            DataTablesColumn(_('Stock on Hand')),
            DataTablesColumn(_('Months of stock'))
        ])
        return headers

    @property
    def rows(self):
        rows = []
        if self.config['location_id']:
            sp = SQLLocation.objects.get(location_id=self.config['location_id']).supply_point_id
            ss = StockState.objects.filter(sql_product__is_archived=False,
                                           case_id=sp,
                                           product_id__in=self.config['products'])
            for stock in ss:
                def calculate_months_remaining(stock_state, quantity):
                    consumption = stock_state.get_monthly_consumption()
                    if consumption is not None and consumption > 0 and quantity is not None:
                        return float(quantity) / float(consumption)
                    elif quantity == 0:
                        return 0
                    return None
                rows.append([stock.sql_product.name, decimal_format(stock.stock_on_hand),
                             float_format(calculate_months_remaining(stock, stock.stock_on_hand))])
        return rows


class RegistrationData(ILSData):
    show_chart = False
    show_table = True

    @property
    def title(self):
        return '%s Contacts' % self.config['loc_type']

    @property
    def slug(self):
        return '%s_registration' % self.config['loc_type'].lower()

    @property
    def headers(self):
        return DataTablesHeader(*[
            DataTablesColumn(_('Name')),
            DataTablesColumn(_('Role')),
            DataTablesColumn(_('Phone')),
            DataTablesColumn(_('Email')),
        ])

    @property
    def rows(self):
        location = SQLLocation.objects.get(location_id=self.config['location_id'])
        if self.config['loc_type'] == 'DISTRICT':
            location = location.parent
        elif self.config['loc_type'] == 'REGION':
            location = location.parent.parent

        users = CommCareUser.get_db().view(
            'locations/users_by_location_id',
            startkey=[location.location_id],
            endkey=[location.location_id, {}],
            include_docs=True
        ).all()
        if users:
            for user in users:
                u = user['doc']
                yield [
                    '{0} {1}'.format(u['first_name'], u['last_name']),
                    u['user_data']['role'],
                    u['phone_numbers'][0] if u['phone_numbers'] else '',
                    u['email']
                ]


class RandRHistory(ILSData):
    slug = 'randr_history'
    title = 'R & R History'
    show_chart = False
    show_table = True

    @property
    def rows(self):
        return latest_status(self.config['location_id'], SupplyPointStatusTypes.R_AND_R_FACILITY)


class Notes(ILSData):
    slug = 'ils_notes'
    title = 'Notes'
    show_chart = False
    show_table = True

    @property
    def headers(self):
        return DataTablesHeader(*[
            DataTablesColumn(_('Name')),
            DataTablesColumn(_('Role')),
            DataTablesColumn(_('Date')),
            DataTablesColumn(_('Phone')),
            DataTablesColumn(_('Text'))
        ])

    @property
    def rows(self):
        location = SQLLocation.objects.get(location_id=self.config['location_id'])
        rows = ILSNotes.objects.filter(domain=self.config['domain'], location=location).order_by('date')
        for row in rows:
            yield [
                row.user_name,
                row.user_role,
                row.date.strftime('%Y-%m-%d %H:%M'),
                row.user_phone,
                row.text
            ]


class RecentMessages(ILSData):
    slug = 'ils_notes'
    title = 'Recent messages'
    show_chart = False
    show_table = True

    @property
    def headers(self):
        return DataTablesHeader(*[
            DataTablesColumn()
        ])


class FacilityDetailsReport(MultiReport):

    title = "Facility Details Report"
    fields = [AsyncLocationFilter, ProductByProgramFilter]
    name = "Facility Details"
    slug = 'facility_details'
    use_datatables = True

    @classmethod
    def show_in_navigation(cls, domain=None, project=None, user=None):
        return False

    @property
    @memoized
    def data_providers(self):
        config = self.report_config

        return [
            InventoryHistoryData(config=config),
            RandRHistory(config=config),
            Notes(config=config),
            RegistrationData(config=dict(loc_type='FACILITY', **config), css_class='row_chart_all'),
            RegistrationData(config=dict(loc_type='DISTRICT', **config), css_class='row_chart_all'),
            RegistrationData(config=dict(loc_type='REGION', **config), css_class='row_chart_all')
        ]
