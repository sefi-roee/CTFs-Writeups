# Natas Level 20
```bash
Username: natas20
Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF
URL:      http://natas20.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas20.png" />
    <div align="center">Natas 20</div>
</figure>

And from the “View sourcecode” link we can extract the following script:
```php
function debug($msg) { /* {{{ */ 
    if(array_key_exists("debug", $_GET)) { 
        print "DEBUG: $msg<br>"; 
    } 
} 
/* }}} */ 
function print_credentials() { /* {{{ */ 
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) { 
        print "You are an admin. The credentials for the next level are:<br>"; 
        print "<pre>Username: natas21\n"; 
        print "Password: <censored></pre>"; 
    } else { 
        print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21."; 
    } 
} 
/* }}} */ 

/* we don't need this */ 
function myopen($path, $name) {  
    //debug("MYOPEN $path $name");  
    return true;  
} 

/* we don't need this */ 
function myclose() {  
    //debug("MYCLOSE");  
    return true;  
} 

function myread($sid) {  
    debug("MYREAD $sid");  
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) { 
        debug("Invalid SID");  
        return ""; 
    } 
    $filename = session_save_path() . "/" . "mysess_" . $sid; 
    if(!file_exists($filename)) { 
        debug("Session file doesn't exist"); 
        return ""; 
    } 
    debug("Reading from ". $filename); 
    $data = file_get_contents($filename); 
    $_SESSION = array(); 
    foreach(explode("\n", $data) as $line) { 
        debug("Read [$line]"); 
        $parts = explode(" ", $line, 2); 
        if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1]; 
    } 
    return session_encode(); 
} 

function mywrite($sid, $data) {  
    // $data contains the serialized version of $_SESSION 
    // but our encoding is better 
    debug("MYWRITE $sid $data");  
    // make sure the sid is alnum only!! 
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) { 
        debug("Invalid SID");  
        return; 
    } 
    $filename = session_save_path() . "/" . "mysess_" . $sid; 
    $data = ""; 
    debug("Saving in ". $filename); 
    ksort($_SESSION); 
    foreach($_SESSION as $key => $value) { 
        debug("$key => $value"); 
        $data .= "$key $value\n"; 
    } 
    file_put_contents($filename, $data); 
    chmod($filename, 0600); 
} 

/* we don't need this */ 
function mydestroy($sid) { 
    //debug("MYDESTROY $sid");  
    return true;  
} 
/* we don't need this */ 
function mygarbage($t) {  
    //debug("MYGARBAGE $t");  
    return true;  
} 

session_set_save_handler( 
    "myopen",  
    "myclose",  
    "myread",  
    "mywrite",  
    "mydestroy",  
    "mygarbage"); 
session_start(); 

if(array_key_exists("name", $_REQUEST)) { 
    $_SESSION["name"] = $_REQUEST["name"]; 
    debug("Name set to " . $_REQUEST["name"]); 
} 

print_credentials(); 

$name = ""; 
if(array_key_exists("name", $_SESSION)) { 
    $name = $_SESSION["name"]; 
}
```

Here we have custom session storage functions:
* *myopen* - always returns true
* *myclose* - always returns true
* *myread($sid)* - checks that $sid contains only chars from "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM".
sets $filename to session_save_path() . "/" . "mysess_" . $sid;
checks that the file exists (on the server)
reads its contents to $data.
for each line, it splits the line by " " and set the key/value in the session variables.
then it encodes the session data and returns the result.
* *mywrite($sid, $data)* - validates $sid sשme as *myread*.
sets $filename in the same manner.
save all the session data as key value (delimited with newline character).
stores this in $filename and set its mode to 600 (read/write only to owner).
* *mydestroy* - always returns true
* *mygarbage* - always returns true

When the page loads, _SESSION["name"] is being set to the GET  parameter.

Our goal (looking in *print_credentials*) is to have admin=1 in _SESSION.

Exploiting the vulnerability in *mywrite* we can append "\nadmin 1" to the "name" GET parameter, and it will be written as another key/value in the session data.

Lets [encode](https://meyerweb.com/eric/tools/dencoder/) this with URL encoding:

```bash
blabla
admin 1
```

We get:
```bash
3Dblabla%0Aadmin%201
```

Enter this value and click "Change name", we got:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas20-exploit.png" />
    <div align="center">Natas 20 - Exploit</div>
</figure>

We got the password for the next level: **IFekPyrQXftziDEsUr3x21sYuahypdgJ**