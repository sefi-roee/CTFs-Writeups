# Problem
I made a website so now you can log on to! I don't seem to have the admin password. See if you can't get to the flag. [http://2018shell1.picoctf.com:6153](http://2018shell1.picoctf.com:6153/)

## Hints:
Hmm it doesn't seem to check anyone's password, except for admins?

How does check the admin's password?

## Solution:

Lets fuzz with the website a little.
login as 1/1

![alt text](./screenshot-1.png)

No flag, damn!

Lets try to login ad admin

![alt text](./screenshot-2.png)

We dont know the password.

Lets login again as 1/1 and check for cookie:

![alt text](./screenshot-3.png)

We can just change ```admin``` cookie to ```True``` (using chrome developer tools) and reload the page.

![alt text](./screenshot-4.png)

Flag: picoCTF{l0g1ns_ar3nt_r34l_82e795f4}
