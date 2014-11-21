 

**Purpose**: Create or Edit lookup tables by uploading excel file
containing Table data

**URL**:`  <http://www.commcatehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/>`__\ `https://www.commcatehq.org/a/[domain]/fixtures/fixapi <http://www.commcatehq.org/a/%5Bdomain%5D/api/%5Bversion%5D/user/>`__/

**Method**: POST

| **Authorization: **\ Digest Authorization

**Input Parameters:**

Name

Description

Example

file-to-upload

Path to the excel file containing Table Data

/home/username/fixtures.xlsx

replace

True if the existing tables should be deleted, otherwise False

False

**Sample cURL request:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     curl -v --digest https://www.commcatehq.org/a/sravan-test/fixapi/ -u |
|  user@domain.com:password                                                |
|          -F "file-to-upload=@fixtures.xlsx"                              |
|          -F "replace=true"                                               |
                                                                          
+--------------------------------------------------------------------------+

**Response: **\ JSON output with following Parameters.

Name

Description

Example

code

200: Success

402: Warning

405: Fail

402

message

Warning or Failure message

"Error processing your file. Submit a valid (.xlsx) file"

 
