 

**Purpose**: Create CommCare(mobile-worker) user.

**URL**:` https://www.commcatehq.org/a/[domain]/api/[version]/user/ <http://www.commcatehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/>`__

**Method**: POST

**Input Parameters:**

Name 

Description 

Example

 

username\* 

User name of user, including domain 

`jdoe@example.commcarehq.org <mailto:jdoe@example.commcarehq.org>`__ or
jdoe 

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

List of all phone numbers of the user. The first one will be set to the
default number

(see examples) 

groups 

List of all group ids belonging to the user 

(see examples) 

user\_data 

Any additional custom data associated with the user 

(see examples) 

language

User language

en

**Output Parameters:**

Name

| 
|  

Description 

Example 

user\_id 

User UUID 

3c5a623af057e23a32ae4000cf291339 

| 

 

Sample input:

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|        "username": "jdoe@example.commcarehq.org",                        |
|        "password": "qwer1234",                                           |
|        "first_name": "John",                                             |
|        "last_name": "Doe",                                               |
|        "default_phone_number": "+50253311399",                           |
|        "email": "jdoe@example.org",                                      |
|        "language": "en",                                                 |
|        "phone_numbers": [                                                |
|           "+50253311399",                                                |
|           "50253314588"                                                  |
|        ],                                                                |
|        "groups": [                                                       |
|           "9a0accdba29e01a61ea099394737c4fb",                            |
|           "b4ccdba29e01a61ea099394737c4fbf7"                             |
|        ],                                                                |
|        "user_data": {                                                    |
|           "chw_id": "13/43/DFA"                                          |
|        }                                                                 |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

| 

 

| 

 
