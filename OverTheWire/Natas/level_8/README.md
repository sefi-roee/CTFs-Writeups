# Natas Level 8

```bash
Username: natas8
Password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
URL:      http://natas8.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas8.png" />
    <div align="center">Natas 8</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas8-view-sourcecode.png" />
    <div align="center">Natas 8 - View sourcecode</div>
</figure>

We can see the a script.

It first declares a variable:
```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
```
Then it declares *encodeSecret* function:
```php
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
```
which gets a parameter, encodes it in base64, reverses the result and returning the hex representation of the string.
```php
if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
        print "Access granted. The password for natas9 is <censored>";
    } else {
        print "Wrong secret";
    }
}
```
Finally, it compares the "encoding" of the POST parameter (from the input box) with the variable.

All we need is a PHP script which reverses this:
```php
bin2hex(strrev(base64_encode($secret))) == $encodedSecret
strrev(base64_encode($secret)) == hex2bin($encodedSecret)
base64_encode($secret) == strrev(hex2bin($encodedSecret))
$secret == base64_decode(strrev(hex2bin($encodedSecret)))
```

Lets try this:
```bash
php -r 'print(base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362"))) . "\n");'
```

The output is:
```bash
oubWYf2kBq
```

Lets send this value to the server:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas8-value-entered.png" />
    <div align="center">Natas 8 - Send value</div>
</figure>

Nailed it:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas8-access-granted.png" />
    <div align="center">Natas 8 - Access granted</div>
</figure>

We got the password for the next level: **W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl**