 

CommCare HQ offers a way to download the case list of a single CHW.

Making the Request
------------------

Assuming your domain is called "demo", the request must be sent to
`https://www.commcarehq.org/a/demo/phone/restore/ <https://www.commcarehq.org/a/demo/phone/restore/>`__
using HTTP digest to supply the username and password of the CHW. In
curl, the request would look something like this: :: bash

    $ curl --digest -u jason@demo.commcarehq.org:1988 https://www.commcarehq.org/a/demo/phone/restore/

In this example, we are on domain "demo", our CHW's username is "jason",
and his password is 1988. You'll note that the username, instead of
being just "jason" is the much longer "jason@demo.commcarehq.org". This
is to distinguish him from any other "jason"s on any other domain. The
format for the full-length username is: ::

    {username}@{domain}.commcarehq.org


To view the OTA Restore data hit
www.commcarehq.org/a/[domain]/user/restore and then enter
[username]@[domain].commcarehq.org and the user's commcare password.

Understanding the data format
-----------------------------

The data that you will look exactly the same as a normal user
registration response, but with a list of case blocks following the
registration data (see
`https://bitbucket.org/javarosa/javarosa/wiki/UserRegistrationAPI <https://bitbucket.org/javarosa/javarosa/wiki/UserRegistrationAPI>`__).
Here is an example:

:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <OpenRosaResponse xmlns="http://openrosa.org/http/response">
        <message>Successfully restored account danny!</message>
        <Sync xmlns="http://commcarehq.org/sync">
            <restore_id>83226e1e05ebe146685b93a9a312efa3</restore_id>
        </Sync>
        <Registration xmlns="http://openrosa.org/user/registration">
            <username>danny</username>
            <password>sha1$13f7c$5b22f7ef1b05b0b81f6009146f5da173baf27761</password>
            <uuid>da77a254-56dd-11e0-a55d-005056aa7fb5</uuid>
            <date>2011-03-25</date>
        </Registration>

        <!-- this is where all the case blocks go-->

        <!-- this is where fixtures go-->

    </OpenRosaResponse>

To understand the casexml spec,
see \ `https://bitbucket.org/javarosa/javarosa/wiki/casexml <https://bitbucket.org/javarosa/javarosa/wiki/casexml>`__;
to understand the fixtures spec,
see \ `https://bitbucket.org/commcare/commcare/wiki/fixtures <https://bitbucket.org/commcare/commcare/wiki/fixtures>`__.

When the phone receives the case blocks, for example, it applies them
all in order to its internal database, thus reconstructing the case
list.
