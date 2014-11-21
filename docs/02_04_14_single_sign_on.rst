 

**Purpose:** validate login credentials and get user profile for a
mobile worker or a web user

**
**

**Single Sign On
URL:** https://www.commcarehq.org/a/[domain]/api/[version]/sso/

 

**Sample URL:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/[domain]/api/[version]/sso/             |
                                                                          
+--------------------------------------------------------------------------+

 

**Post a urlencoded username an password such as**:

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     username=MY_USERNAME&password=MY_PASSWORD                            |
                                                                          
+--------------------------------------------------------------------------+

 

If your credentials are correct, output will be identical to the `User
API <https://confluence.dimagi.com/display/commcarepublic/List+Mobile+Workers>`__
or `Web User
API <https://confluence.dimagi.com/display/commcarepublic/List+Web+Users>`__,
as appropriate.

 

 
