# Problem
We found a hidden flag server hiding behind a proxy, but the proxy has some... _interesting_ ideas of what qualifies someone to make HTTP requests. Looks like you'll have to do this one by hand. Try connecting via ```nc 2018shell1.picoctf.com 42496```, and use the proxy to send HTTP requests to `flag.local`. We've also recovered a username and a password for you to use on the login page: `realbusinessuser`/`potoooooooo`.

## Hints:

_Be the browser._ When you navigate to a page, how does your browser send HTTP requests? How does this change when you submit a form?

## Solution:

Lets connect and try to make some requests.

Attempt 1:
```bash
nc 2018shell1.picoctf.com 42496

Real Business Corp., Internal Proxy
Version 2.0.7
To proceed, please solve the following captcha:

 __           ______         
/  |         |___  /  ______ 
`| |  __  __    / /  |______|
 | |  \ \/ /   / /    ______ 
_| |_  >  <  ./ /    |______|
\___/ /_/\_\ \_/             
                             
                             


> 7
Validation succeeded.  Commence HTTP.

GET /

HTTP/1.1 400 Missing Host header
Date: Tue, 16 Oct 2018 12:49:11 GMT
Connection: close
```

Attempt 2:
```bash
nc 2018shell1.picoctf.com 42496

Real Business Corp., Internal Proxy
Version 2.0.7
To proceed, please solve the following captcha:

 _____           ____          
/ __  \         / ___|  ______ 
`' / /' __  __ / /___  |______|
  / /   \ \/ / | ___ \  ______ 
./ /___  >  <  | \_/ | |______|
\_____/ /_/\_\ \_____/         
                               
                               


> 12
Validation succeeded.  Commence HTTP.

GET /
Host: flag.local

HTTP/1.1 200 OK
x-powered-by: Express
content-type: text/html; charset=utf-8
content-length: 321
etag: W/"141-LuTf9ny9p1l454tuA3Un+gDFLWo"
date: Tue, 16 Oct 2018 12:51:16 GMT
connection: close


    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="main.css" />
      </head>
      <body>
        <header>
          <h1>Real Business Internal Flag Server</h1>
          <a href="/login">Login</a>
        </header>
        <main>
          <p>You need to log in before you can see today's flag.</p>
        </main>
      </body>
    </html>
```

Attempt 3:
```bash
nc 2018shell1.picoctf.com 42496

Real Business Corp., Internal Proxy
Version 2.0.7
To proceed, please solve the following captcha:

 _____          ______         
|  ___|        |___  /  ______ 
|___ \  __  __    / /  |______|
    \ \ \ \/ /   / /    ______ 
/\__/ /  >  <  ./ /    |______|
\____/  /_/\_\ \_/             
                               
                               


> 35
Validation succeeded.  Commence HTTP.

POST /login HTTP/1.1
Host: flag.local
Content-Type: application/x-www-form-urlencoded
Content-Length: 38

user=realbusinessuser&pass=potoooooooo
HTTP/1.1 302 Found
x-powered-by: Express
set-cookie: real_business_token=PHNjcmlwdD5hbGVydCgid2F0Iik8L3NjcmlwdD4%3D; Path=/
location: /
vary: Accept
content-type: text/plain; charset=utf-8
content-length: 23
date: Tue, 16 Oct 2018 12:52:27 GMT
connection: close

Found. Redirecting to /
```

Attempt 4:
```bash
Real Business Corp., Internal Proxy
Version 2.0.7
To proceed, please solve the following captcha:

 _____           _____          
|  _  |    _    / __  \  ______ 
| |_| |  _| |_  `' / /' |______|
\____ | |_   _|   / /    ______ 
.___/ /   |_|   ./ /___ |______|
\____/          \_____/         
                                
                                


> 11
Validation succeeded.  Commence HTTP.

GET / HTTP/1.1
Host: flag.local
Cookie: real_business_token=PHNjcmlwdD5hbGVydCgid2F0Iik8L3NjcmlwdD4%3D

HTTP/1.1 200 OK
x-powered-by: Express
content-type: text/html; charset=utf-8
content-length: 438
etag: W/"1b6-eYJ8DUTdkgByyfWFi6OJJSjopFg"
date: Tue, 16 Oct 2018 13:01:14 GMT
connection: close


    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="main.css" />
      </head>
      <body>
        <header>
          <h1>Real Business Internal Flag Server</h1>
          <div class="user">Real Business Employee</div>
          <a href="/logout">Logout</a>
        </header>
        <main>
          <p>Hello <b>Real Business Employee</b>!  Today's flag is: <code>picoCTF{0nLY_Us3_n0N_GmO_xF3r_pR0tOcol5_2e14}</code>.</p>
        </main>
      </body>
    </html>
```

Flag: picoCTF{0nLY_Us3_n0N_GmO_xF3r_pR0tOcol5_2e14}
