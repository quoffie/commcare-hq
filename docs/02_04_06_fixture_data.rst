 

**Purpose:** get all of the data associated with a fixture.
(see `https://bitbucket.org/commcare/commcare/wiki/fixtures <https://bitbucket.org/commcare/commcare/wiki/fixtures>`__ for
the definition of *fixture*)

**Base URLs:**

-  **(for individual fixture
   items):** https://www.commcarehq.org/a/[domain]/api/[version]/fixture/[fixture\_item\_id]/
-  **(for a specific fixture
   table):** https://www.commcarehq.org/a/[domain]/api/[version]/fixture/\ `?fixture\_type= <https://www.commcarehq.org/a/bihar/api/v0.4/fixture/?fixture_type=asha>`__'[`name
   of
   table <https://confluence.dimagi.com/pages/createpage.action?spaceKey=commcarepublic&title=name+of+table&linkCreation=true&fromPageId=12226705>`__\ ]'` <https://www.commcarehq.org/a/bihar/api/v0.4/fixture/?fixture_type=asha>`__\ ` <https://www.commcarehq.org/a/bihar/api/v0.4/fixture/?fixture_type=asha>`__
-  **(for a list of all fixture
   types):** https://www.commcarehq.org/a/[domain]/api/[version]/fixture/

**Input parameters (for the list of all fixtures):**

Name

Description

Example

fixture\_type

Returns the fixtures of a in a given domain whose data\_type

fixture\_type="city"

**Output values:**

Name

Description

Example

id

Fixture UUID

1J9NF7B4FTH73435PYJJSL5SJ

fixture\_type

Name of the fixture's data\_type

city

fields

Values for the custom fields in the fixture.

{"name": "Boston", "population": 617594, "state": "Massachusetts"

**Note:** A call to the Fixture List API endpoint will return a JSON
list of objects with these output values

In order to get the full table via API, use the 'name of the table',
which is the same as you would find without the API call
from \ `https://www.commcarehq.org/a/[domain]/fixtures <https://www.commcarehq.org/a/bihar/fixtures>`__ (the
string in the Table ID column)

**Sample input:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/demo/api/v0.4/fixture/1J9NF7B4FTH73435P |
| YJJSL5SJ/                                                                |
                                                                          
+--------------------------------------------------------------------------+

**Sample output:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|         "fields": {                                                      |
|             "name": "Boston",                                            |
|             "population": 617594,                                        |
|             "state": "Massachusetts",                                    |
|         },                                                               |
|         "fixture_type": "city",                                          |
|         "resource_uri": "",                                              |
|         "id": "1J9NF7B4FTH73435PYJJSL5SJ"                                |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
