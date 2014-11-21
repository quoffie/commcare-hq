 

**Purpose**: Create group.

**URL**:` https://www.commcatehq.org/a/[domain]/api/[version]/group/ <http://www.commcatehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/>`__

**Method**: POST for one group, PATCH for multiple groups

** **\ **Input Parameters**:

Name 

Description 

Example 

name\*

Group name

Wozzle 

case\_sharing

Whether users within this group will share cases with other members of
this group

true/false (default=false)

reporting

Whether this group's name will appear in the group filter list for
reports

true/false (default=true)

users

List of all users ids belonging to the group 

(see examples)

This is optional to specify.

metadata 

Any additional custom data associated with the group 

(see examples) 

This is optional to specify.

**Output Parameters**:

Name 

Description 

Example 

id

Group UUID

3c5a623af057e23a32ae4000cf291339 

**Sample input**:

Single Group:

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|      "case_sharing": false,                                              |
|      "metadata": {                                                       |
|       "localization": "Ghana"                                            |
|      },                                                                  |
|      "name": "Wozzle",                                                   |
|      "reporting": true,                                                  |
|      "users": [                                                          |
|       "91da6b1c78699adfb8679b741caf9f00",                                |
|       "8a642f722c9e617eeed29290e409fcd5"                                 |
|      ]                                                                   |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

Multiple Groups (can include all other information from single group
creation):

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|      "objects": [                                                        |
|       {                                                                  |
|        "case_sharing": false,                                            |
|        "name": "Test 1",                                                 |
|        "reporting": true                                                 |
|       },                                                                 |
|       {                                                                  |
|        "case_sharing": true,                                             |
|        "name": "Test 2",                                                 |
|        "reporting": true                                                 |
|       }                                                                  |
|      ]                                                                   |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
