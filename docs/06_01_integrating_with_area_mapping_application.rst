 

This page will walk you through the steps of integrating Dimagi's area
mapping application with your CommCare ODK app.

**Configuration**

#. Download and install the `area mapping
   application <https://confluence.dimagi.com/download/attachments/28773688/AreaMap.apk?version=1&modificationDate=1408058336374&api=v2>`__ on
   your device
   -Plug your Android device into your computer
   -Drag the downloaded AreaMap.apk file from your downloads folder on
   your desktop onto your Android device icon
   -Confirm that the file appears on your device storage
   -If you do not have one already, download a File Explorer from the
   Google Play store onto your Android device
   -Using the File Explorer, search for and locate the AreaMap.apk file
   on your Android device
   -Select the AreaMap icon and install the application onto your phone
   -Note: You will likely be prompted to change the settings on your
   phone to allow for this installation to occur, namely allowing
   applications to be installed from unknown sources. 
#. Navigate to the form builder for your app on CommCare HQ
#. Navigate to where you want to insert the question
#. Add an "Android App Callout" question type under the "Advanced" tab
#. Create an ID and label as you would a normal question
#. Under "Intent ID" write: org.commcare.mapping.AreaCalculator
#. Under "Logic" you can enforce the same things as you would a normal
   question, IE enforce this must be a realistic value, non-null, etc
#. That's it! To read more about what's going on under the hood see
   `this
   page <https://confluence.dimagi.com/display/commcarepublic/Integrating+External+Applications+with+CommCareODK>`__.

 

 
