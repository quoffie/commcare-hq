 

**Purpose:** get all of the data associated with a case, including all
case property values, a list of associated forms and a list of
associated referrals. The case data may be presented to the end user as
a case details screen.

**Base URL:**
https://www.commcarehq.org/a/[domain]/api/[version]/case/[case\_id]/

**Input parameters:**

Name

Description

Values

Example

Status

format

Return data format

xml, json

format=xml

Supported

properties

Whether to include properties

all, **none**

properties=all

Proposed

indices

Whether to include indices

all, **none**

indices=all

Proposed

xforms\_by\_name\_\_full

Whether to include all xforms by name

true

xforms\_by\_name\_\_full=true

Supported

xforms\_by\_xmls\_\_full

Whether to include all xforms by xmlns

true

xforms\_by\_xmlns\_\_full=true

Supported

**Output values:** 

Name

Description

Example

case\_id

Case UUID

0X9OCW3JMV98EYOVN32SGN4II

user\_name

User name of case owner, including domain

jdoe@example.commcarehq.org

user\_id

UUID of user that owns the case

3c5a623af057e23a32ae4000cf291339

date\_modified

Date and time case was last modified

2011-12-13T15:09:47Z

closed

Status of the case (open, closed)

false

date\_closed

Date and time case was closed

2011-12-20T15:09:47Z

properties

List of all editable case properties, including both special predefined
properties and user-defined dynamic properties

**Special Properties**

owner\_id

ID of the owner of the case (can be user or group)

case\_name

Name of case

Rose

external\_id

External ID associated with the case

123456

case\_type

Type of case

pregnancy

date\_opened

Date and time case was opened

2011-11-16T14:26:15Z

**End Special Properties**

indices

List of references to other cases with properties <case\_type/> and
<case\_id/>

**Start of data from for each form associated with the case
Repeats for each form, as seen in sample output below**

form\_id

UUID of form associated with the case

1J9NF7B4FTH73435PYJJSL5SJ

form\_name

Name of form associated with the case

Prenatal visit

started\_on

Date and time form was started

2011-11-16T14:26:15Z

ended\_on

Date and time form was completed

2011-11-16T14:27:35Z

 

**Sample usage:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/demo/api/v0.4/case/0X9OCW3JMV98EYOVN32S |
| GN4II/?format=xml&properties=all&indices=all                             |
                                                                          
+--------------------------------------------------------------------------+

**Sample output:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     <case>                                                               |
|         <domain>example</domain>                                         |
|         <case_id>0X9OCW3JMV98EYOVN32SGN4II</case_id>                     |
|         <username>jdoe@example.commcarehq.org</user_name>                |
|         <user_id>3c5a623af057e23a32ae4000cf291339</user_id>              |
|         <closed>false</closed>                                           |
|         <date_closed>2011-12-20 15:09:47Z</date_closed>                  |
|         <date_modified>2011-12-13 15:09:47Z</date_modified>              |
|         <properties>                                                     |
|             <case_name>Rose</case_name>                                  |
|             <case_type>pregnancy</case_type>                             |
|             <date_opened>2011-11-16T14:26:15Z</date_opened>              |
|             <external_id>123456</external_id>                            |
|             <owner_id>3c5a623af057e23a32ae4000cf291339</owner_id>        |
|             <case_property1>Dynamic property value 1</case_property1>    |
|             <case_property2>Dynamic property value 2</case_property2>    |
|             ...                                                          |
|         </properties>                                                    |
|         <indices>                                                        |
|             <case_ref1>                                                  |
|                 <case_type>other_case_type</case_type>                   |
|                 <case_id>8GPM05TVPIUH0Q4XLXVIURRTA</case_id>             |
|             </case_ref1>                                                 |
|             ...                                                          |
|         </indices>                                                       |
|         <forms>                                                          |
|             <form>                                                       |
|                 <form_id>1J9NF7B4FTH73435PYJJSL5SJ</form_id>             |
|                 <form_name>Prenatal visit</form_name>                    |
|                 <started_on>2011-11-16T14:26:15Z</started_on>            |
|                 <ended_on>2011-11-16T14:27:35Z</ended_on>                |
|                 <properties>                                             |
|                     <form_property1>Dynamic property value 1</form_prope |
| rty1>                                                                    |
|                     <form_property2>Dynamic property value 2</form_prope |
| rty2>                                                                    |
|                     ...                                                  |
|                 </properties>                                            |
|             </form>                                                      |
|             ...                                                          |
|         </forms>                                                         |
|         <referrals>                                                      |
|             <referral>                                                   |
|                 <referral_id>D8LZS28LEUWU7W9QNDM89XWPL</referral_id>     |
|                 <referral_type>referred_to_health_center</referral_type> |
|                 <opened_on>2011-11-17T14:26:15Z</opened_on>              |
|                 <modified_on>2011-11-17T14:27:10Z</modified_on>          |
|                 <followup_on>2011-11-19T00:00:00Z</followup_on>          |
|                 <referral_status>open</referral_status>                  |
|             </referral>                                                  |
|             ...                                                          |
|         <referrals>                                                      |
|         ...                                                              |
|     </case>                                                              |
                                                                          
+--------------------------------------------------------------------------+

 

 

 

 
