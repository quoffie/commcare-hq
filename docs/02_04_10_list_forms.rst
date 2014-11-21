 

**Purpose:** Get a list of form submissions.

**Base URL:** https://www.commcarehq.org/a/[domain]/api/v0.4/form/

**Input parameters:**

The forms can be filtered using the following parameters, which also
control paging of the output records.

Name

Description

Example

Status

xmlns

Form XML namespace (optional)

xmlns=http://openrosa.org/formdesigner/dd3190c7dd7e9e7d469a9705709f2f6b4e27f1d8

Supported

received\_on\_start

Date Time (optional)

received\_on\_start=2012-01-01 (or with Time 2012-01-01T06:05:42)

Supported

received\_on\_end

Date Time (optional)

received\_on\_end=2013-02-03 (or with Time 2013-11-25T06:05:42)

Supported

limit

The maximum number of records to return. Default: 20.\ **Maximum: 1000**

limit=100

Supported

offset

The number of records to offset in the results. Default: 0.

offset=100

Supported

appVersion

The exact version of the CommCare application used to submit the form
(this will be large and involved; it is intended for programmatic use)

appVersion=v2.6.1%20(3b8ee4-e3dc9f-unvers-2.1.0-Nokia%2FS40-native-input)%20build%207313%20App%20%237300%20b%3A2013-Jun-04%20r%3A2013-Jul-18

Supported

**Sample usage:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/[domain]/api/v0.5/form/                 |
                                                                          
+--------------------------------------------------------------------------+

**Sample output**:

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|         "meta": {                                                        |
|             "limit": 20,                                                 |
|             "next": "/a/corpora/api/v0.5/form/?limit=20&offset=20",      |
|             "offset": 0,                                                 |
|             "previous": null,                                            |
|             "total_count": 6909                                          |
|         },                                                               |
|         "objects": [                                                     |
|             {                                                            |
|                 "app_id": "572e968957920fc3e92578988866a5e8",            |
|                 "archived": false,                                       |
|                 "build_id": "78698f1516e7d16689e05fce852d1e9c",          |
|                 "form": {                                                |
|                     "#type": "data",                                     |
|                     "@name": "Case Update",                              |
|                     "@uiVersion": "1",                                   |
|                     "@version": "186",                                   |
|                     "@xmlns": "http://openrosa.org/formdesigner/4B1B717C |
| -0CF7-472E-8CC1-1CC0C45AA5E0",                                           |
|                     "case": {                                            |
|                         "@case_id": "8f8fd909-684f-402d-a892-f50e607fffe |
| f",                                                                      |
|                         "@date_modified": "2012-09-29T19:10:00",         |
|                         "@user_id": "f4c63df2ef7f9da2f93cab12dc9ef53c",  |
|                         "@xmlns": "http://commcarehq.org/case/transactio |
| n/v2",                                                                   |
|                         "update": {                                      |
|                             "data_node": "55",                           |
|                             "dateval": "2012-09-26",                     |
|                             "geodata": "5.0 5.0 5.0 5.0",                |
|                             "intval": "5",                               |
|                             "multiselect": "b",                          |
|                             "singleselect": "b",                         |
|                             "text": "TEST"                               |
|                         }                                                |
|                     },                                                   |
|                     "data_node": "55",                                   |
|                     "geodata": "5.0 5.0 5.0 5.0",                        |
|                     "meta": {                                            |
|                         "@xmlns": "http://openrosa.org/jr/xforms",       |
|                         "appVersion": {                                  |
|                             "#text": "v2.1.0dev (1d8fba-0884f9-unvers-2. |
| 1.0-Nokia/S40-generic) build 186 App #186 b:2012-Sep-27 r:2012-Sep-28",  |
|                             "@xmlns": "http://commcarehq.org/xforms"     |
|                         },                                               |
|                         "deviceID": "0LRGVM4SFN2VHCOVWOVC07KQX",         |
|                         "instanceID": "00460026-a33b-4c6b-a4b6-c47117048 |
| 557",                                                                    |
|                         "timeEnd": "2012-09-29T19:10:00",                |
|                         "timeStart": "2012-09-29T19:08:46",              |
|                         "userID": "f4c63df2ef7f9da2f93cab12dc9ef53c",    |
|                         "username": "afrisis"                            |
|                     },                                                   |
|                     "old_data_node": "",                                 |
|                     "question1": "OK",                                   |
|                     "question11": "5",                                   |
|                     "question12": "2012-09-26",                          |
|                     "question14": "OK",                                  |
|                     "question3": "b",                                    |
|                     "question7": "b",                                    |
|                     "text": "TEST"                                       |
|                 },                                                       |
|                 "id": "00460026-a33b-4c6b-a4b6-c47117048557",            |
|                 "md5": "OBSOLETED",                                      |
|                 "metadata": {                                            |
|                     "@xmlns": "http://openrosa.org/jr/xforms",           |
|                     "appVersion": "@xmlns:http://commcarehq.org/xforms,  |
| #text:v2.1.0dev (1d8fba-0884f9-unvers-2.1.0-Nokia/S40-generic) build 186 |
|  App #186 b:2012-Sep-27 r:2012-Sep-28",                                  |
|                     "deprecatedID": null,                                |
|                     "deviceID": "0LRGVM4SFN2VHCOVWOVC07KQX",             |
|                     "instanceID": "00460026-a33b-4c6b-a4b6-c47117048557" |
| ,                                                                        |
|                     "timeEnd": "2012-09-29T19:10:00",                    |
|                     "timeStart": "2012-09-29T19:08:46",                  |
|                     "userID": "f4c63df2ef7f9da2f93cab12dc9ef53c",        |
|                     "username": "afrisis"                                |
|                 },                                                       |
|                 "received_on": "2012-09-29T17:24:52",                    |
|                 "resource_uri": "",                                      |
|                 "type": "data",                                          |
|                 "uiversion": "1",                                        |
|                 "version": "186"                                         |
|             }                                                            |
|         ]                                                                |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
