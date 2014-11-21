 

**Purpose**: Create Web-Users

**URL**:
`https://www.commcarehq.org/a/[domain]/api/[version]/web-user/ <http://www.commcarehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/%5Bid>`__ 

**Method**: POST 

**Input Parameters:**

Name 

Description 

Example 

username\*

User name of user, including domain

`jdoe@example.com <mailto:jdoe@example.com>`__

password

User password

qwer1234

first\_name

First name of user

John

last\_name

Last name of user

Doe

email

Email address of user

`john.doe@example.org <mailto:john.doe@example.org>`__

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

true/false

 

**Output Parameters:**

Name

| 
|  

Description 

Example 

user\_id 

User UUID 

3c5a623af057e23a32ae4000cf291339 

**Sample Input:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|             "default_phone_number":null,                                 |
|             “password”: qwer1234,                                        |
|             "email":"admin@example.com",                                 |
|             "first_name":"Joe",                                          |
|             "is_admin": true,                                            |
|             "last_name":"Admin",                                         |
|             "permissions":{                                              |
|                "edit_apps":true,                                         |
|                "edit_commcare_users":true,                               |
|                "edit_data":true,                                         |
|                "edit_web_users":true,                                    |
|                "view_report_list":[                                      |
|                ],                                                        |
|                "view_reports":true                                       |
|             },                                                           |
|             "phone_numbers":[                                            |
|             ],                                                           |
|             "role":"Admin",                                              |
|             "username":"admin@example.com"                               |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 

 

| 

 
