# Natas Level 23
```bash
Username: natas23
Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE
URL:      http://natas23.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas23.png" />
    <div align="center">Natas 23</div>
</figure>

And the [source code](http://natas23.natas.labs.overthewire.org/index-source.html):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas23-view-sourcecode.png" />
    <div align="center">Natas 23 - View sourcecode</div>
</figure>

The script is:
```php
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>
```

We need to send a GET parameter which includes the substring "iloveyou" and which is greater the 10 (implicit casting to int take the int prefix from the string). Lets [>try](http://natas23.natas.labs.overthewire.org/?passwd=11iloveyou) "11iloveyou":

<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas23-pwned.png" />
    <div align="center">Natas 23 - PWNed</div>
</figure>

We got the password for the next level: **OsRmXFguozKpTZZ5X14zNO43379LZveg**