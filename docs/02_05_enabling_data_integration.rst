 

+--------------------------------------------------------------------------+
| This feature (API Access) is only available to CommCare users with a     |
| Standard Plan or higher. For more details, see the `CommCare Software    |
| Plan page <http://www.commcarehq.org/software-plans/>`__.                |
+--------------------------------------------------------------------------+

You can configure your project to forward any incoming forms and/or
cases to a specified URL. To do so, in CommCare HQ navigate to
**Project** **Settings** and then to \ **Data Forwarding**. It will look
something like this:

|image0|

Data will be forwarded, and the contents of what is forwarded will be in
the body of the HTTP POST. This does not use HTML form-style parameters.

The three options are described below

Forwarding Type

What you receive at the specified URL every time a mobile worker submits
a form

Example

**Forward Form**

... the complete form (one POST per form)

In addition to the form there will be an extra header
'``received-on``\ ' that is the time the form was received by CommCare
HQ.

.. code:: prettyprint

    <?xml version='1.0' ?>
    <data uiVersion="1"

.. code:: prettyprint

          version="41"

.. code:: prettyprint

          name="New Form"

.. code:: prettyprint

          xmlns:jrm="http://dev.commcarehq.org/jr/xforms"

.. code:: prettyprint

          xmlns="http://openrosa.org/formdesigner/84FA38A2-93C1-4B9E-AA2A-0E082995FF9E">
      <number>8</number>
      <n0:case case_id="e098a110-6b83-4ff7-9093-d8e0e8bfb9a3"

.. code:: prettyprint

               user_id="9ad3659b9c0f8c5d141d2d06857874df"

.. code:: prettyprint

               date_modified="2012-10-23T17:15:21.966-04"

.. code:: prettyprint

               xmlns:n0="http://commcarehq.org/case/transaction/v2">
        <n0:update>
          <n0:number>8</n0:number>
        </n0:update>
      </n0:case>
      <cc_delegation_stub delegation_id="0e6db0c4-d07f-435c-89e5-64855440605c">
        <n1:case case_id="0e6db0c4-d07f-435c-89e5-64855440605c"

.. code:: prettyprint

                 user_id="9ad3659b9c0f8c5d141d2d06857874df"

.. code:: prettyprint

                 date_modified="2012-10-23T17:15:21.966-04"

.. code:: prettyprint

                 xmlns:n1="http://commcarehq.org/case/transaction/v2">
          <n1:close />
        </n1:case>
      </cc_delegation_stub>
      <n2:meta xmlns:n2="http://openrosa.org/jr/xforms">
      <n2:deviceID>cloudcare</n2:deviceID>
      <n2:timeStart>2012-10-23T17:15:18.324-04</n2:timeStart>
      <n2:timeEnd>2012-10-23T17:15:21.966-04</n2:timeEnd>
      <n2:username>test</n2:username>
      <n2:userID>9ad3659b9c0f8c5d141d2d06857874df</n2:userID>
      <n2:instanceID>c24a85f9-703d-434c-b087-5759f3fa9937</n2:instanceID>
      <n3:appVersion xmlns:n3="http://commcarehq.org/xforms">2.0</n3:appVersion>
      </n2:meta>
    </data>

**Forward Cases**

... a case block representing the latest state of any cases affected by
the form (one POST per case).

When you turn on case forwarding, every time a case changes on HQ, it
will forward the case \ *in its entirety* to your URL (not just the last
change). We expect that you will receive the case, look to see if
there's a case with the same id already in your system, and then either
create or update the case with all the information given. If the case
has been closed, we will send the case with just a close block.

The URL you set up to deal with the in-coming information can expect to
receive one <case/> block at a time, in the format specified above.

In addition to the case there will be an extra header
'``server-modified-on``\ ' that is the last time the case was modified
in CommCare HQ.

::

    <case case_id="e098a110-6b83-4ff7-9093-d8e0e8bfb9a3"

::

          date_modified="2012-10-23"

::

          user_id="9ad3659b9c0f8c5d141d2d06857874df"

::

          xmlns="http://commcarehq.org/case/transaction/v2">

::

      <create>

::

        <case_type>test</case_type>

::

        <case_name>asdf</case_name>

::

        <owner_id>9ad3659b9c0f8c5d141d2d06857874df</owner_id>

::

      </create>

::

      <update>

::

        <number>8</number>

::

      </update>

::

    </case>

(Newlines and indentation added here for clarity.)

**Forward Form Stub**

... a timestamp (GMT), the form's id, and the ids of any affected cases

 

This works especially well in conjunction with our `Data
APIs <https://confluence.dimagi.com/display/commcarepublic/Data+APIs>`__;
you can get notified of a change using Form Stub Forwarding and then use
the Data APIs to look up the form and cases affected, either right away
or at a later date.

::

    {

::

      "received_on": "2012-10-22T12:15:25Z",

::

      "form_id": "c24a85f9-703d-434c-b087-5759f3fa9937",

::

      "case_ids": [

::

        "0e6db0c4-d07f-435c-89e5-64855440605c",

::

        "e098a110-6b83-4ff7-9093-d8e0e8bfb9a3"

::

      ]

::

    }

(Newlines and indentation added here for clarity.)

 

.. |image0| image:: 02_05_enabling_data_integration_files/Screen%2520Shot%25202014-09-26%2520at%252010.png
