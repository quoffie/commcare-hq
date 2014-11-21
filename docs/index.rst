.. This is the main index for HQ's docs.

Welcome to CommCareHQ's documentation!
======================================

**Contents:**

..
    list rst documents here, and it'll be added to the index,
    including any subsections inside those docs (up to the maxdepth).
    For reference on generating a toc, check out the sphinx docs on
    the subject: http://sphinx-doc.org/markup/toctree.html
    Here's a sample well-organized toc:
    https://github.com/kennethreitz/python-guide/blob/master/docs/contents.rst.inc


.. toctree::
   :maxdepth: 2

   intended_audience
   getting_started
   diving_in
   technical_overview
   deploy
   reporting
   api
   maps
   ui_helpers
   class_views
   forms
   management_commands
   commtrack
   cloudcare
   translations
   profiling
   elasticsearch
   test_coverage


CommCareHQ API
--------------

.. toctree::
   :maxdepth: 2

   02_commcarehq_apis
   02_01_submission_api
   export_api
   02_03_ota_restore_api
   02_04_data_apis
   02_04_01_api_standards
   02_04_02_application_structure_api
   02_04_03_case_data
   02_04_04_concept_sharing
   02_04_05_data_forwarding
   02_04_06_01_bulk_upload_lookup_tables
   02_04_06_fixture_data
   02_04_07_form_data
   02_04_08_list_cases
   02_04_09_list_cases_version_3+
   02_04_10_list_forms
   02_04_11_list_groups
   02_04_12_list_mobile_workers
   02_04_13_list_web_users
   02_04_14_single_sign_on
   02_05_enabling_data_integration
   02_06_user_creation_mobile_worker
   02_07_user_creation_web_user
   02_08_edit_user_mobile_worker
   02_09_edit_user_web_user
   02_10_create_group
   02_11_edit_group
   02_12_authentication


Mobile Development
------------------

.. toctree::
   :maxdepth: 2

   04_common_commcare_mobile_dev_workspace_build_errors
   04_01_source_control_usage_for_commcare_mobile_devs
   05_installing_odk_application_offline_for_mobile_devs
   06_integrating_external_applications_with_commcare_odk
   06_01_integrating_with_area_mapping_application
   06_02_integrating_with_breath_counter_app


Advanced Users
--------------

.. toctree::
   :maxdepth: 2

   07_transferring_an_application_between_projects_or_servers


Tips for Documenting
--------------------

.. toctree::

    documenting


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
