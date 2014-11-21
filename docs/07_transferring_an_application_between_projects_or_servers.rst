 

If you need to transfer an application between projects on the same
server it is very easy:

#. Go to the application page of the app you want to copy.
#. At the bottom left, click on "Copy Application".
#. Enter the project name and new application name and click "Copy...".

This will copy the application with Multimedia. 

If you need to transfer an application between servers (for example, if
you are a developer running CommCare HQ locally, or have a second
instance of CommCare HQ running elsewhere):

#. On the server containing the app you want to copy, go to the
   URL: http://[SERVER ADDRESS]/a/[PROJECT NAME]/apps/source/<APP\_ID>. 
   For
   example: https://www.commcarehq.org/a/demo/apps/source/071abeb39a1039df30613c494caa9bc3
#. You should see a block of JSON-formatted text. **First view source
   (ctrl-u)**, then copy the whole thing.  (ctrl+a, ctrl+c)
#. On the new server, go to the following
   URL http://[SERVER ADDRESS]/a/[PROJECT NAME]/apps/import\_app/.
#. Add an application name, and paste the source that you copied into
   the source box.
#. Click "Import Application".

 
