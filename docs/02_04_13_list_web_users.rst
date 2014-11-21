 

**Purpose:** get a list of web users, or a single user. 

**Base
URL:** https://www.commcarehq.org/a/[domain]/api/[version]/web-user/

**Single User
URL:** https://www.commcarehq.org/a/[domain]/api/[version]/web-user/[user\_id]

**Input parameters: **

Name

Description

Example

username

Filter list by username

username=bob@example.com

**
**

**Output parameters:**

Name

Description

Example

id

User UUID

3c5a623af057e23a32ae4000cf291339

username

User name of user, including domain

jdoe@example.com

first\_name

First name of user

John

last\_name

Last name of user

Doe

default\_phone\_number

Primary phone number of user

+50253311399

email

Email address of user

 john.doe@example.org

phone\_numbers

List of all phone numbers of the user

(see examples)

role

Name of user role

(see examples)

permissions

Object representing user's permissions

(see examples)

is\_admin

Whether the user is a project admin

(see examples)

**Output values:**

**Sample usage:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/demo/api/v0.4/web-user/                 |
                                                                          
+--------------------------------------------------------------------------+

**Sample output:**

**JSON:**

 

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|        "meta":{                                                          |
|           "limit":20,                                                    |
|           "next":null,                                                   |
|           "offset":0,                                                    |
|           "previous":null,                                               |
|           "total_count":2                                                |
|        },                                                                |
|        "objects":[                                                       |
|           {                                                              |
|              "default_phone_number":null,                                |
|              "email":"admin@example.com",                                |
|              "first_name":"Joe",                                         |
|              "id":"8f9756be9b1c7f28057d707b405d18f6",                    |
|              "is_admin": true,                                           |
|              "last_name":"Admin",                                        |
|              "permissions":{                                             |
|                 "doc_type":"Permissions",                                |
|                 "edit_apps":true,                                        |
|                 "edit_commcare_users":true,                              |
|                 "edit_data":true,                                        |
|                 "edit_web_users":true,                                   |
|                 "view_report_list":[                                     |
|                 ],                                                       |
|                 "view_reports":true                                      |
|              },                                                          |
|              "phone_numbers":[                                           |
|              ],                                                          |
|              "resource_uri":"",                                          |
|              "role":"Admin",                                             |
|              "username":"admin@example.com"                              |
|           },                                                             |
|           {                                                              |
|              "default_phone_number":null,                                |
|              "email":"reporter@dimagi.com",                              |
|              "first_name":"Bob",                                         |
|              "id":"73a1ce78809f7d077b4b3a01163e9186",                    |
|              "is_admin": false,                                          |
|              "last_name":"Reporter",                                     |
|              "permissions":{                                             |
|                 "doc_type":"Permissions",                                |
|                 "edit_apps":false,                                       |
|                 "edit_commcare_users":false,                             |
|                 "edit_data":false,                                       |
|                 "edit_web_users":false,                                  |
|                 "view_report_list":[                                     |
|                 ],                                                       |
|                 "view_reports":true                                      |
|              },                                                          |
|              "phone_numbers":[                                           |
|              ],                                                          |
|              "resource_uri":"",                                          |
|              "role":"Read Only",                                         |
|              "username":"reporter@example.com"                           |
|           }                                                              |
|        ]                                                                 |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
