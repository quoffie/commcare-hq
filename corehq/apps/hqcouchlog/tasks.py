from datetime import timedelta, datetime
from celery.schedules import crontab
from celery.task.base import periodic_task
from couchdbkit.exceptions import ResourceNotFound
from couchlog.models import ExceptionRecord
from django.conf import settings


def get_results(key):
    return ExceptionRecord.view(
        "couchlog/all_by_date",
        reduce=False,
        endkey=[key.isoformat()],
        limit=1000,
        include_docs=False)


@periodic_task(run_every=crontab(minute=0, hour=0), queue=getattr(settings, 'CELERY_PERIODIC_QUEUE', 'celery'))
def purge_old_logs():
    key = datetime.now() - timedelta(weeks=52)

    db = ExceptionRecord.get_db()

    results = get_results(key)
    while results.count():
        docs = []
        for result in results:
            try:
                rev = db.get_rev(result['id'])
            except ResourceNotFound:
                pass
            else:
                docs.append({
                    '_id': result['id'],
                    '_rev': rev,
                    '_deleted': True,
                })

        db.bulk_save(docs, use_uuids=False)
        results = get_results(key)
