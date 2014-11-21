 

**Purpose:** get a list of applications for a project, with their
module, form, and case schemata.

**Base
URL:** https://www.commcarehq.org/a/[domain]/api/[version]/application/

**Input parameters: None**

**Output description:**

The output of the API in the "objects" field is a list of configurations
for your applications. Each one has a list of its modules with all case
properties and forms.

-  name: The name of the application
-  modules: This is a list of the modules with their forms, case type,
   and case properties

   -  case\_type: The case type for the enclosing module
   -  case\_properties: The names of all properties for the case type
      for the enclosing module
   -  forms: A list of all forms for the module

      -  questions: A list of the schema for each question of the module

 

**Sample JSON Output:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     {                                                                    |
|       meta: {                                                            |
|         limit: 20,                                                       |
|         next: null                                                       |
|         offset: 0,                                                       |
|         previous: null,                                                  |
|         total_count: 4                                                   |
|       },                                                                 |
|       objects: [ {                                                       |
|         name: "My application",                                          |
|         case_types: {                                                    |
|             type_of_case_from_app_builder: [                             |
|                 "case_prop1",                                            |
|                 "case_prop2",                                            |
|                 ...                                                      |
|             ]                                                            |
|         },                                                               |
|         modules: [ {                                                     |
|           case_type: "type_of_case_from_app_builder",                    |
|           forms: [ {                                                     |
|             name: {                                                      |
|               en: "Name in English",                                     |
|               es: "Nombre en Español",                                   |
|               ...                                                        |
|             },                                                           |
|             questions: [ {                                               |
|                 label: "The question",                                   |
|                 repeat: "",                                              |
|                 tag: "input",                                            |
|                 value: "/name_in_english/the_question"                   |
|               },                                                         |
|             ...                                                          |
|             ]                                                            |
|           }                                                              |
|         ]                                                                |
|       }                                                                  |
|     }                                                                    |
                                                                          
+--------------------------------------------------------------------------+

 
