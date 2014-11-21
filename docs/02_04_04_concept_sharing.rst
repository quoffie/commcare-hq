 

**Purpose:** Share concept across forms that have semantic meaning.
 This could be within the context of a yet-to-be-designed CommCareHQ
Data Dictionary, or more immediately, upon forwarding to 3rd party
system like OpenMRS.  

**Base URL:** Not applicable

**Input parameters:  **\ The level of sharing will appear in a
concept-id attribute.  The value of the concept-id may currently be any
valid string.  In the future, we may add syntactic requirements to the
string values in order to utilize certain features.  For example, we
plan to add pre-defined reports to CommCareHQ that utilize the `Maternal
Concept Lab <http://www.maternalconceptlab.com/wiki/Main_Page>`__
concept-ids, and we may require specific namespacing in the concept-id
like "org.mcl:1234."  

**Sample usage of Concepts:**

CommCare and CommCareHQ honor all attributes in the xform data that is
defined in the instance block.  Therefore, you add an concept-id
attribute for any data element that you wish to have a concept-id to.  .
 

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     <data xmlns:jrm="http://dev.commcarehq.org/jr/xforms" xmlns="http:// |
| openrosa.org/formdesigner/B095F533-6226-40EE-9045-38EA21D214DB" uiVersio |
| n="1" version="1" name="Dinosaur Reg">                                   |
|         <name concept-id="name"/>                                        |
|         <color concept-id="1234"/>                                       |
|         <type />                                                         |
|         <favorite_food concept-id="food preference"/>                    |
|     </data>                                                              |
                                                                          
+--------------------------------------------------------------------------+

**Sample filled in xform instance:**

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     <data xmlns:jrm="http://dev.commcarehq.org/jr/xforms" xmlns="http:// |
| openrosa.org/formdesigner/B095F533-6226-40EE-9045-38EA21D214DB" uiVersio |
| n="1" version="1" name="Dinosaur Reg">                                   |
|         <name concept-id="name">Barney</>                                |
|         <color concept-id="1234">Purple</>                               |
|         <type>T-Rex</>                                                   |
|         <favorite_food concept-id="food preference">kosher</>            |
|     </data>                                                              |
                                                                          
+--------------------------------------------------------------------------+

 
