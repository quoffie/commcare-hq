 

**Purpose**: Edit group.

**URL**:` https://www.commcatehq.org/a/[domain]/api/[version]/group/[id] <http://www.commcatehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/>`__

**Method**: PUT 

**Input Parameters**: 

Name 

Description 

Example 

name

Group name

Wozzle 

case\_sharing

Whether users within this group will share cases with other members of
this group

true/false

reporting

Whether this group's name will appear in the group filter list for
reports

true/false  

users

List of all users ids belonging to the group 

(see examples)

This will replace any existing users for the group.

metadata 

Any additional custom data associated with the group 

(see examples) 

This will replace any existing custom data for the group.

 **Sample input**:

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

 

 
