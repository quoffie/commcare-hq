 

+--------------------------------------------------------------------------+
| This feature (API Access) is only available to CommCare users with a     |
| Standard Plan or higher. For more details, see the `CommCare Software    |
| Plan page <http://www.commcarehq.org/software-plans/>`__.                |
+--------------------------------------------------------------------------+

|image0|
--------

This section is for you if...
-----------------------------

- You are a \ **programmer** 

- You are looking to write code that interacts directly with CommCare HQ
through its APIs

Things we take for granted...
-----------------------------

- You should have a familiarity with HTTP conventions, such as GET and
POST and url parameters

- To follow the examples, you should be familiar with the standard
command line tool **curl**. Here's the
manual: \ `http://www.cs.sunysb.edu/documentation/curl/ <http://www.cs.sunysb.edu/documentation/curl/>`__

- Character encoding is UTF-8. Dates should be compliant \ `ISO
8601 <http://en.wikipedia.org/wiki/ISO_8601>`__. (In some cases we're
still using RFC 3339, but we're moving towards ISO 8601.) Guids should
be generated in accordance with RFC 4122.

Authentication
--------------

Read the
`Authentication <https://confluence.dimagi.com/display/commcarepublic/Authentication>`__
page for information about how to authenticate your requests with
CommCare HQ.

Documented APIs and use of Standards
------------------------------------

In the following, [version] should always be replaced with one of v0.5,
v0.3, etc. These documents only describe the latest version - prior
versions remain available only to support backwards compatibility
with \ *deployed systems*, not for general use. The latest version
is \ **v0.5**.

API

Description

URL Endpoint

Permission required

 

`Submission <https://confluence.dimagi.com/display/commcarepublic/Submission+API>`__

API to submit data to CommCareHQ.

See Documentation

Set per domain

✓

`User Creation (Mobile
Worker) <https://confluence.dimagi.com/pages/viewpage.action?pageId=22708569>`__

API to create a mobile worker on CommCareHQ

https://www.commcatehq.org/a/[domain]/api/[version]/user/

Edit Mobile Workers

✓

`User Edit (Mobile
Worker) <https://confluence.dimagi.com/pages/viewpage.action?pageId=22708635>`__

API to edit a mobile worker on CommCareHQ

https://www.commcarehq.org/a/[domain]/api/[version]/user/[id] 

Edit Mobile Workers

✓

`User Creation (Web
User) <https://confluence.dimagi.com/pages/viewpage.action?pageId=22708582>`__

API to create a web user on CommCareHQ

https://www.commcarehq.org/a/[domain]/api/[version]/web-user/ 

Edit Web Users

✓

`Create
Group <https://confluence.dimagi.com/display/commcarepublic/Create+Group>`__

API to create a mobile worker group on CommCareHQ

https://www.commcatehq.org/a/[domain]/api/[version]/group/

Edit Mobile Workers

✓

`Edit
Group <https://confluence.dimagi.com/display/commcarepublic/Edit+Group>`__

API to edit a mobile worker group on CommCareHQ

https://www.commcatehq.org/a/[domain]/api/[version]/group/[id]

Edit Mobile Workers

 

`User Edit (Web
User) <https://confluence.dimagi.com/pages/viewpage.action?pageId=22708639>`__

API to edit a web user on CommCareHQ

https://www.commcarehq.org/a/[domain]/api/[version]/web-user/[id]

Edit Web Users

✓

`User
Registration <https://bitbucket.org/javarosa/javarosa/wiki/UserRegistrationAPI>`__\ :sup:`†`

API for registering users on CommCareHQ.

https://www.commcarehq.org/a/\\[domain\\]/receiver

Set per domain

✓

`OTA Restore (Case
List) <https://confluence.dimagi.com/display/commcarepublic/OTA+Restore+API>`__

API to retrieve data payload consumable to restore a users current state
of cases.

See Documentation

Valid login

✓

`Data
Export <https://confluence.dimagi.com/display/commcarepublic/Export+API>`__

API to export data from CommCareHQ.

See Documentation

Set per domain

✓

`Groups <https://confluence.dimagi.com/display/commcarepublic/List+Groups>`__

list groups

https://www.commcarehq.org/a/[domain]/api/[version]/group/

Edit Mobile Workers

✓

`Mobile
Workers <https://confluence.dimagi.com/display/commcarepublic/List+Mobile+Workers>`__

list mobile workers or access individual user data

https://www.commcarehq.org/a/[domain]/api/[version]/user/

Edit Mobile Workers

✓

`Web
Users <https://confluence.dimagi.com/display/commcarepublic/List+Web+Users>`__

list web users or access individual user data

http://www.commcarehq.org/a/[domain]/api/[version]/web-user/

Edit Web Users

✓

`Cases <https://confluence.dimagi.com/pages/viewpage.action?pageId=12224287>`__

list cases

https://www.commcarehq.org/a/[domain]/api/[version]/case/

Edit Data

✓

`Case
Data <https://confluence.dimagi.com/display/commcarepublic/Case+Data>`__

find a single case

https://www.commcarehq.org/a/[domain]/api/[version]/case/[case\_id]/

Edit Data

✓

`Forms <https://confluence.dimagi.com/display/commcarepublic/List+Forms>`__

list form submissions

https://www.commcarehq.org/a/[domain]/api/[version]/form/

Edit Data

✓

`Form
Data <https://confluence.dimagi.com/display/commcarepublic/Form+Data>`__

list/search forms or access a single form

https://www.commcarehq.org/a/[domain]/api/[version]/forms/[form\_id]/

Edit Data

✓

`Data
Forwarding <https://confluence.dimagi.com/display/commcarepublic/Data+Forwarding>`__

manage your data forwarding endpoints

https://www.commcarehq.org/a/[domain]/api/[version]/data-forwarding/

Domain Admin

✓

`Application
Structure <https://confluence.dimagi.com/display/commcarepublic/Application+Structure+API>`__

view the schema of modules, cases, and forms for your application

https://www.commcarehq.org/a/[domain]/api/[version]/application/

Edit Apps

✓

`Single Sign
On <https://confluence.dimagi.com/display/commcarepublic/Single+Sign+On>`__

check login credentials and get the user details

https://www.commcarehq.org/a/[domain]/api/[version]/sso/

Valid login

✓

Standards used in APIs

Standard

Description

`OpenRosa
Request <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaRequest>`__\ :sup:`†`

The standard for HTTP(S) interactions between CommCare client and server

`Meta Data
Schema <https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaMetaDataSchema>`__\ :sup:`†`

Open Rosa standard meta data tags. (Taken care of by default by
CommCareHQ.)

`Case
XML <https://bitbucket.org/javarosa/javarosa/wiki/casexml>`__\ :sup:`†`

XML spec for case-related transactions. (Taken care of by default by
CommCareHQ.)

`Authentication <https://bitbucket.org/javarosa/javarosa/wiki/AuthenticationAPI>`__\ :sup:`†`

How authentication is done between a CommCare device and the server 

`CommCare 2.0
Specs <https://bitbucket.org/commcare/commcare/wiki/CommCare20Specs>`__\ :sup:`†`

Additional documentation for CommCare APIs

:sup:`†` External links to the JavaRosa/CommCare docs

Enabling Data Integration 
--------------------------

`How to enable Forms and Case
Forwarding <https://confluence.dimagi.com/pages/viewpage.action?pageId=12224128>`__

API Clients
-----------

Note that any third party libraries are not supported by Dimagi.

-  Ruby

   -  `https://github.com/gdeflaux/commcare\_api <https://github.com/gdeflaux/commcare_api>`__ (third
      party)

 

 

 

.. |image0| image:: 02_commcarehq_apis_files/macro.png
