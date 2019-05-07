# Natas Level 27
```bash
Username: natas27
Password: 55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ
URL:      http://natas27.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas27.png" />
    <div align="center">Natas 27</div>
</figure>

And the code is:
```php
// morla / 10111 
// database gets cleared every 5 min  


/* 
CREATE TABLE `users` ( 
  `username` varchar(64) DEFAULT NULL, 
  `password` varchar(64) DEFAULT NULL 
); 
*/ 


function checkCredentials($link,$usr,$pass){ 
  
    $user=mysql_real_escape_string($usr); 
    $password=mysql_real_escape_string($pass); 
     
    $query = "SELECT username from users where username='$user' and password='$password' "; 
    $res = mysql_query($query, $link); 
    if(mysql_num_rows($res) > 0){ 
        return True; 
    } 
    return False; 
} 


function validUser($link,$usr){ 
     
    $user=mysql_real_escape_string($usr); 
     
    $query = "SELECT * from users where username='$user'"; 
    $res = mysql_query($query, $link); 
    if($res) { 
        if(mysql_num_rows($res) > 0) { 
            return True; 
        } 
    } 
    return False; 
} 


function dumpData($link,$usr){ 
     
    $user=mysql_real_escape_string($usr); 
     
    $query = "SELECT * from users where username='$user'"; 
    $res = mysql_query($query, $link); 
    if($res) { 
        if(mysql_num_rows($res) > 0) { 
            while ($row = mysql_fetch_assoc($res)) { 
                // thanks to Gobo for reporting this bug!   
                //return print_r($row); 
                return print_r($row,true); 
            } 
        } 
    } 
    return False; 
} 


function createUser($link, $usr, $pass){ 

    $user=mysql_real_escape_string($usr); 
    $password=mysql_real_escape_string($pass); 
     
    $query = "INSERT INTO users (username,password) values ('$user','$password')"; 
    $res = mysql_query($query, $link); 
    if(mysql_affected_rows() > 0){ 
        return True; 
    } 
    return False; 
} 


if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) { 
    $link = mysql_connect('localhost', 'natas27', '<censored>'); 
    mysql_select_db('natas27', $link); 
    

    if(validUser($link,$_REQUEST["username"])) { 
        //user exists, check creds 
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){ 
            echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>"; 
            echo "Here is your data:<br>"; 
            $data=dumpData($link,$_REQUEST["username"]); 
            print htmlentities($data); 
        } 
        else{ 
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>"; 
        }         
    }  
    else { 
        //user doesn't exist 
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){  
            echo "User " . htmlentities($_REQUEST["username"]) . " was created!"; 
        } 
    } 

    mysql_close($link); 
} else { 
```

The functionality is going like this:

When entering username/password (via POST parameters), we are:
* Checking if the user is *validUser* (SELECT * from users where username='$user' and return *True* if more then 0 rows returned).
* If true:
* * Checking user credentials with *checkCredentials* (SELECT username from users where username='$user' and password='$password' and return *True* if more then 0 rows returned).
* * If true:
* * * Dumping user data with *dumpData* (SELECT * from users where username='$user' and if more then 0 rows returned, fetching the first result *[mysql_fetch_assoc](http://php.net/manual/en/function.mysql-fetch-assoc.php)* and returning it.
* * If false:
* * * Echoing "Wrong password" message.
* If false:
* * Creating user with *createUser* (INSERT INTO users (username,password) values ('$user','$password')).
* * Echoing "User created" message.

In all this functionality, username/password are being escaped with *mysql_real_escape_string* (so we can't inject SQL code).

This is the definition of users table:
```php
/* 
CREATE TABLE `users` ( 
  `username` varchar(64) DEFAULT NULL, 
  `password` varchar(64) DEFAULT NULL 
); 
*/
```

When trying to login as "natas28" (with blank password), we get the following:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas27-wrong-password.png" />
    <div align="center">Natas 27 - Wrong password</div>
</figure>

In mysql ([strict mode](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html)), when inserting data exceeding field length the value is being truncated (Strict mode produces an error for attempts to create a key that exceeds the maximum key length. When strict mode is not enabled, this results in a warning and truncation of the key to the maximum key length.)

If we login with user "natas28                                                            a" for example, the user validation check will fail, and a new user will be created. This username is too long (68 chars) and it will be truncated (to "natas28"), resulting in two rows with "natas28" username (the password for the last row is created by us).

Now, when we login as "natas28" (with our password), a row will be returned, and the credentials of the <strong>FIRST</strong> row will be returned.
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas27-pwned.png" />
    <div align="center">Natas 27 - PWNed</div>
</figure>

We got the password for the next level: **JWwR438wkgTsNKBbcJoowyysdM82YjeF**