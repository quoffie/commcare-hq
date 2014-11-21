 

**Purpose:** get a list of cases. The list of cases may be presented to
the end user a simple list of cases, where each case name incudes a
hyperlink to access detailed information about the case.

**Base URL:** https://www.commcarehq.org/a/[domain]/api/v0.4/case/

**Input parameters:**

In addition to all `Case
Data <https://confluence.dimagi.com/display/commcarepublic/Case+Data>`__
parameters, you may use the following input parameters to filter results
and control paging\ **
**

Name

Description

Example

Status

Summary

owner\_id

User or Group UUID (optional)

owner\_id=ac9d34ff59cf6388e4f5804b12276d8a

Supported

All cases owned by that entity (should not use with user)

user\_id

User UUID (optional)

user=3c5a623af057e23a32ae4000cf291339

Supported

All cases **last modified** by that user

type

Type of case (optional)

type=pregnant\_mother

Supported

All cases matching the type

closed

| Case status (optional)
| Supported: false, true (defaults to both)

closed=true

Supported

All open/closed/both cases

date\_modified\_start

Modified after this date (phone date)

date\_modified\_start=2012-05-20

date\_modified\_start=2013-09-29T10:40Z

Supported

Defaults to the first submission date.

date\_modified\_end

Modifed before this date (phone date)

date\_modified\_end=2012-05-27

Supported

Defaults to the current date.

server\_date\_modified\_start

Modified after this date (server date)

server\_date\_modified\_start=2012-05-20

Supported

Defaults to the first submission date.

server\_date\_modified\_end

Modifed before this date (server date)

server\_date\_modified\_end=2012-05-27

Supported

Defaults to the current date.

name

Name

name=NEAL

Supported

 

limit

The maximum number of records to return.

limit=100

Supported

Defaults to 20. **Maximum is 100.**

offset

The number of records to offset in the results.

offset=100

Supported

Defaults to 0.

 

**Output values:**

Name

Description

Example

case\_id

Case UUID

0X9OCW3JMV98EYOVN32SGN4II

username

User name of case owner, including domain

jdoe@example.commcarehq.org

user\_id

UUID user that owns the case

3c5a623af057e23a32ae4000cf291339

owner\_id

UUID group/user that owns the case

ac9d34ff59cf6388e4f5804b12276d8a

case\_name

Name of case

Rose

external\_id

External ID associated with the case

123456

case\_type

Type of case

pregnant\_mother

date\_opened

Date and time case was opened

2011-11-16T14:26:15Z

date\_modified

Date and time case was last modified

2011-12-13T15:09:47Z

closed

Case status

false

date\_closed

Date and time case was closed

2011-12-20T15:09:47Z

**Sample usage:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/[domain]/api/v0.3/case/?format=xml      |
                                                                          
+--------------------------------------------------------------------------+

**Sample XML output (Proposed):**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     <cases>                                                              |
|         <case>                                                           |
|             <case_id>0X9OCW3JMV98EYOVN32SGN4II</case_id>                 |
|             <username>jdoe@example.commcarehq.org</username>             |
|             <user_id>3c5a623af057e23a32ae4000cf291339</user_id>          |
|             <owner_id>3c5a623af057e23a32ae4000cf291339</owner_id>        |
|             <case_name>Rose</case_name>                                  |
|             <external_id>123456</external_id>                            |
|             <case_type>pregnancy</case_type>                             |
|             <date_opened>2011-11-16T14:26:15</date_opened>               |
|             <date_modified>2011-12-13 15:09:47</date_modified>           |
|             <closed>false</closed>                                       |
|             <date_closed>2011-12-20 15:09:47</date_closed>               |
|         </case>                                                          |
|         ...                                                              |
|     </cases>                                                             |
                                                                          
+--------------------------------------------------------------------------+

**Sample JSON Output:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     [ { "case_id" : "45WKYXQRFFU3AT4Y022EX7HF2",                         |
|         "closed" : false,                                                |
|         "date_closed" : null,                                            |
|         "date_modified" : "2012-03-13T18:21:52Z",                        |
|         "domain" : "demo",                                               |
|         "indices" : {  },                                                |
|         "properties" : {                                                 |
|             "case_name" : "ryan",                                        |
|             "case_type" : "programmer",                                  |
|             "date_opened" : "2012-03-13T18:21:52Z",                      |
|             "external_id" : "45WKYXQRFFU3AT4Y022EX7HF2",                 |
|             "gender" : "m",                                              |
|             "languages" : "python java javascript c php erlang love",    |
|             "owner_id" : null,                                           |
|             "role" : "artisan"                                           |
|           },                                                             |
|         "server_date_modified" : "2012-04-05T23:56:41Z",                 |
|         "server_date_opened" : "2012-04-05T23:56:41Z",                   |
|         "user_id" : "06414101dc45bcfdc963b8cb1a1ebdfd",                  |
|         "version" : "1.0",                                               |
|         "xform_ids" : [ "3HQEXR2S0GIRFY2GF40HAR7ZE" ]                    |
|       },                                                                 |
|       ...                                                                |
|     ]                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
