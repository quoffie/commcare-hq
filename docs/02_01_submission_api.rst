.. NOTE:: This feature (API Access) is only available to CommCare users
          with a Standard Plan or higher. For more details, see the
          `CommCare Software Plan page <http://www.commcarehq.org/software-plans/>`__.

Form Submission API
-------------------

The form submission API can be found here: 
`https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI <https://bitbucket.org/javarosa/javarosa/wiki/FormSubmissionAPI>`__.

There are two ways to submit a form to CommCare HQ, which are as
multipart/form-data and as the body of a post, currently used by the
J2ME and Android implementations, respectively. Here, sample commands
are given for submitting a file called "file.xml" to the domain called
"demo". (You will need to change these two values in the commands below
to suit your own purposes.)

Submission as multipart/form-data
---------------------------------

:: bash

    $ curl -F "xml_submission_file=@file.xml" "https://www.commcarehq.org/a/demo/receiver/"

One way to think of this is that the incoming request looks exactly like
a request sent by submitting the following html form: :: html

    <form method="post" enctype="multipart/form-data" action="https://www.commcarehq.org/a/demo/receiver/">
        <input type="file" name="xml_submission_file"/>
        <input type="submit" value="Submit Form"/>
    </form>


Submission as body of a post
----------------------------

:: bash

    $ curl -d @file.xml "https://www.commcarehq.org/a/demo/receiver/"

There is no equivalent of this in an html form, because rather than
submitting a body which is a mapping from names onto values, the curl
command above submits the files contents *as* the entire body.

Additional Notes
================

For compatibility with CommCare ODK, the Android CommCare client, the
urls above can also be replaced with 
``https://www.commcarehq.org/a/demo/receiver/submission/``. 
That is, you can append the string "submission/" to the end of the url
and it works exactly as before.
