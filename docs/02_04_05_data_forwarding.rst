 

**Purpose:** view or modify data forwarding endpoints (See
`documentation for data integration and
forwarding <https://confluence.dimagi.com/pages/viewpage.action?pageId=12224128>`__)

**Base URL:**
https://www.commcarehq.org/a/[domain]/api/[version]/data-forwarding/

**Single Item
URL**: https://www.commcarehq.org/a/[domain]/api/[version]/data-forwarding/[id]

**Input parameters:**\ None

**Supported Operations**

The following API operations are supported. See the sample output below
for details on the JSON format.

API

Endpoint

HTTP Operation

GET/POST data

List forwarding rules

Base URL

GET

None

Create new forwarding rule

Base URL

POST

JSON Formatted data

Update forwarding rule

Single Item URL

PUT

JSON Formatted data

Delete forwarding rule

(not yet supported)

 

 

**Sample usage:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     https://www.commcarehq.org/a/demo/api/v0.4/data-forwarding/          |
                                                                          
+--------------------------------------------------------------------------+

**Sample output:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|        "meta":{                                                          |
|           "limit":20,                                                    |
|           "next":null,                                                   |
|           "offset":0,                                                    |
|           "previous":null,                                               |
|           "total_count":3                                                |
|        },                                                                |
|        "objects":[                                                       |
|           {                                                              |
|              "domain":"demo",                                            |
|              "id":"ccbadc6655b2e7692dccbbd884c14418",                    |
|              "resource_uri":"/a/demo/api/v0.4/data-forwarding/ccbadc6655 |
| b2e7692dccbbd884c14418/",                                                |
|              "type":"CaseRepeater",                                      |
|              "url":"http://www.example.com/case-endpoint/",              |
|              "version":"2.0"                                             |
|           },                                                             |
|           {                                                              |
|              "domain":"demo",                                            |
|              "id":"ccbadc6655b2e7692dccbbd884c148b3",                    |
|              "resource_uri":"/a/demo/api/v0.4/data-forwarding/ccbadc6655 |
| b2e7692dccbbd884c148b3/",                                                |
|              "type":"FormRepeater",                                      |
|              "url":"http://www.example.com/form-endpoint/",              |
|              "version":null                                              |
|           },                                                             |
|           {                                                              |
|              "domain":"demo",                                            |
|              "id":"ccbadc6655b2e7692dccbbd884c13d60",                    |
|              "resource_uri":"/a/demo/api/v0.4/data-forwarding/ccbadc6655 |
| b2e7692dccbbd884c13d60/",                                                |
|              "type":"ShortFormRepeater",                                 |
|              "url":"http://www.example.com/short-form-endpoint/",        |
|              "version":"2.0"                                             |
|           },                                                             |
|           {                                                              |
|              "domain":"demo",                                            |
|              "id":"ccbadc6655b2e7692dccbbd884c13d60",                    |
|              "resource_uri":"/a/demo/api/v0.4/data-forwarding/ccbadc6655 |
| b2e7692dccbbd884c13d60/",                                                |
|              "type":"AppStructureRepeater",                              |
|              "url":"http://www.example.com/app-structure-endpoint/",     |
|              "version":"2.0"                                             |
|           }                                                              |
|        ]                                                                 |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
