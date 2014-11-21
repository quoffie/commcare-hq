 

**Authenticating with Digest authentication**
---------------------------------------------

The export URLs support HTTP-Digest authentication in addition to the
normal session-based authentication used on the rest of CommCare HQ.
This makes it easy to access these urls programmatically. For example,
with curl you can use the --digest flag and specify a username with -u
as follows:

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     curl -v --digest -u [USERNAME] '[URL]'                               |
                                                                          
+--------------------------------------------------------------------------+

 

This will prompt you for your password. You can also include the
password in the request as follows:

+--------------------------------------------------------------------------+
| ::                                                                       |
|                                                                          |
|     curl -v --digest -u [USERNAME]:[PASSWORD] '[URL]'                    |
                                                                          
+--------------------------------------------------------------------------+

 
