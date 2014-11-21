 

**NOTE:** use of this feature will require at least some dev support

**Background**

Sometimes you will need to use a data gathering method outside the
standard toolkit of ODK widgets such as text entry, GPS locating, taking
pictures, etc. In these instances, ODK allows you to easily "call out"
to an external app, use that application, and return the data to your
form just as if it had been entered via a more standard method.

This feature uses `Android
Intents <http://developer.android.com/reference/android/content/Intent.html>`__ to
call an external application. When returning data back to CommCareODK,
the external application needs appropriate permissions and needs to
follow a specific format for returned data, see
the \ `details <https://bitbucket.org/commcare/commcare-odk/wiki/ODKActivityCallout>`__. 

**Using the Form Builder
**

Assuming you have your external application installed (and it obeys the
contract in the link above) you can use the form builder to create an
Android Intent that will launch this application.

Under the Advanced tab of the form builder choose the "Android App
Callout" option.

-  **Question ID:** as usual
-  **Intent ID:** intent action for your activity - for example
   "android.intent.action.DIAL" to launch the phone dialer
-  **Extra:** keys and paths to form fields containing the values of
   arguments for the intent activity

   -  The paths point to the **location of this data** - no hard-coding
      of values. The paths can point to hidden values that calculate the
      desired value

-  **Response:** any extra values for ODK to store, along with the paths
   of where to store them

 
