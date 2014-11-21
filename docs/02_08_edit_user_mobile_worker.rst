 

**Purpose**: Edit CommCare(mobile-worker) user.

**URL**:` https://www.commcarehq.org/a/[domain]/api/[version]/user/[id] <http://www.commcarehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/%5Bid>`__ 

**Method**: PUT

**Input Parameters**: 

Name 

Description 

Example 

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

This will replace existing phone numbers for user.

groups 

List of all group ids belonging to the user 

(see examples) 

This will replace existing groups for the user.

user\_data 

Any additional custom data associated with the user 

(see examples) 

This will replace existing custom data for the user.

language

User language

en

**Sample input:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|        "first_name": "John",                                             |
|        "last_name": "Doe",                                               |
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

 
