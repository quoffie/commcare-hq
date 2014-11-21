 

This page will walk you through the steps of integrating Dimagi's breath
counter application with your CommCare ODK app.

#. Download and install the breath counter app from the play store to
   your device at
   `https://play.google.com/store/apps/details?id=org.commcare.respiratory <https://play.google.com/store/apps/details?id=org.commcare.respiratory>`__
#. Navigate to the form builder for your app on CommCare HQ
#. Navigate to where you want to insert the question
#. Add an "Android App Callout" question type under the "Advanced" tab
#. Create an ID and label as you would a normal question
#. Under "Intent ID" write: org.commcare.respiratory.BREATHCOUNT
#. Under "Logic" you can enforce the same things as you would a normal
   question, IE enforce this must be a realistic value, non-null, etc
#. That's it! To read more about what's going on under the hood see
   `this
   page <https://confluence.dimagi.com/display/commcarepublic/Integrating+External+Applications+with+CommCareODK>`__.

 
