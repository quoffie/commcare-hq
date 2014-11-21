 

+--------------------------------------------------------------------------+
| This feature (API Access) is only available to CommCare users with a     |
| Standard Plan or higher. For more details, see the `CommCare Software    |
| Plan page <http://www.commcarehq.org/software-plans/>`__.                |
+--------------------------------------------------------------------------+

Data APIs
---------

These APIs are intended for building project specific applications and
integrations, including:

-  Custom end-user applications that address project-specific needs
-  Custom integrations with external back-end systems, such as an
   electronic patient record system 

In the following, [version] should always be replaced with one of v0.4,
v0.3, etc. These documents only describe the latest version - prior
versions remain available only to support backwards compatibility
with \ *deployed systems*, not for general use. The latest version is
**v0.5**.

 

API

Description

URL Endpoint

Permission required

Status

`Groups <https://confluence.dimagi.com/display/commcarepublic/List+Groups>`__

list groups

https://www.commcarehq.org/a/[domain]/api/[version]/group/

Edit Mobile Workers

✓

`Users <https://confluence.dimagi.com/display/commcarepublic/List+Mobile+Workers>`__

list users

https://www.commcarehq.org/a/[domain]/api/[version]/user/

Edit Mobile Workers

✓

`Cases <https://confluence.dimagi.com/display/commcarepublic/List+Cases>`__

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

find a single form

https://www.commcarehq.org/a/[domain]/api/[version]/forms/[form\_id]/

Edit Data

✓

`Fixture
Data <https://confluence.dimagi.com/display/commcarepublic/Fixture+Data>`__

find a single fixture

https://www.commcarehq.org/a/[domain]/api/[version]/fixture/[fixture\_id]/

Edit Apps

✓

`Single Sign
On <https://confluence.dimagi.com/display/commcarepublic/Single+Sign+On>`__

check login credentials

https://www.commcarehq.org/a/[domain]/api/[version]/sso/

Valid Login

✓

 
