Diving In
=========

The quickest way to get a feel for the code is to work in it. To do
that, let's look at where things are.


Navigating The Codebase
-----------------------

The core CommCareHQ functionality is in the ``corehq/`` directory. 
Once-off projects are in ``custom/``. And this documentation lives in
``docs/``.


A Django App
------------

This documentation assumes that you are familiar with Django. 
CommCare HQ currently uses `Django 1.5`_. 
Check out its documentation for more information about what a Django
project is, and what a Django app is, if you are not sure.

"corehq" is the name of the CommCareHQ Django project, and in the
``corehq/apps/`` directory you will find the various Django apps that
make up the project.

Let us pick the "appstore" app. 
It's a nice app to start with because it has a bit of everything; views,
templates, a model (kind of) and even a static file.
In CommCareHQ, the appstore app is called the Exchange, and allows users
to share the applications (i.e. modules and forms) that they build.
We will look at the "project_info" view. 

Start with the ``urls.py`` file. HTTP requests will arrive here first.
The relevant line is ::

    url(r'^(?P<domain>[\w\.-]+)/info/$', 'project_info', name='project_info'),

We can see from this that the URL will include a "domain" parameter made
up of alphanumeric characters, fullstops and dashes. It will call the
"project_info" view.

Open ``views.py``, and jump to the line ::

    def project_info(request, domain, template="appstore/project_info.html"):

There's that "domain" parameter passed from ``urls.py``


.. TODO:: Continue


.. _Django 1.5: https://docs.djangoproject.com/en/1.5/
