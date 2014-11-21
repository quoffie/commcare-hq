 

**Purpose:** get a list of user groups. The list of groups may be
presented to the user as a simple list of group names, where each group
name includes a hyperlink to access a list of group members. Group names
could, for example, mirror the geographic distribution of CHWs, with a
separate group name used for each health district. Access control may be
applied, with each web user having access to one or more groups
associated with the CommCare domain. Only groups that the user is
permitted to access are included in the output.

**Base URL:** https://www.commcarehq.org/a/[domain]/api/[version]/group/

**Input parameters:**

Name

Description

Example

Format

| Return data format (optional)
| Supported: json (default), xml

format=xml

**Output values:**

Name

Description

Example

group\_id

Group UUID

ac9d34ff59cf6388e4f5804b12276d8a

group\_name

Group name (e.g. health district)

Senahú

**Sample usage:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/demo/api/v0.4/group/                    |
                                                                          
+--------------------------------------------------------------------------+

**Sample output:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|       "meta": {                                                          |
|      "limit": 20,                                                        |
|      "next": null,                                                       |
|      "offset": 0,                                                        |
|      "previous": null,                                                   |
|      "total_count": 3                                                    |
|      },                                                                  |
|      "objects": [                                                        |
|      {                                                                   |
|      "case_sharing": false,                                              |
|      "domain": "cloudcaredemo",                                          |
|      "id": "1eb59d6938fc7e510254d8c2f63d944f",                           |
|      "metadata": {},                                                     |
|      "name": "Wozzle",                                                   |
|      "path": [],                                                         |
|      "reporting": true,                                                  |
|      "users": ["91da6b1c78699adfb8679b741caf9f00", "8a642f722c9e617eeed2 |
| 9290e409fcd5"]                                                           |
|      },                                                                  |
|      ...                                                                 |
|      ]                                                                   |
|     }                                                                    |
|                                                                          |
                                                                          
+--------------------------------------------------------------------------+

 
