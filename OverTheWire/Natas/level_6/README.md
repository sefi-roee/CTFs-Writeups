# Natas Level 6

```bash
Username: natas6
Password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
URL:      http://natas6.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas6.png" />
    <div align="center">Natas 6</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas6-view-sourcecode.png" />
    <div align="center">Natas 6 - View sourcecode</div>
</figure>

We can see the a script.

It first includes the file: "includes/secret.inc", lets see [its contents](http://natas6.natas.labs.overthewire.org/includes/secret.inc):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas6-secret-inc.png" />
    <div align="center">Natas 6 - Secret file</div>
</figure>

We can see variable declaration:
```php
$secret = "FOEIUWGHFEEUHOFUOIU";
```
After that, the script compares this variable with the value of the "secret" POST parameters (the value entered in the input box).
We just need to post this value.
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas6-value-entered.png" />
    <div align="center">Natas 6 - Send value</div>
</figure>

<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas6-access-granted.png" />
    <div align="center">Natas 6 - Access granted</div>
</figure>

Access granted!

We got the password for the next level: **7z3hEENjQtflzgnT29q7wAvMNfZdh0i9**