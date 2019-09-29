# Problem
Can you break into this super secure portal? [https://2019shell1.picoctf.com/problem/45147/](https://2019shell1.picoctf.com/problem/45147/) or http://2019shell1.picoctf.com:45147

## Hints:
Never trust the client

## Solution:

Lets look at the source of the website.
```bash
curl https://2019shell1.picoctf.com/problem/45147/

<html>
<head>
<title>Secure Login Portal</title>
</head>
<body bgcolor=blue>
<!-- standard MD5 implementation -->
<script type="text/javascript" src="md5.js"></script>

<script type="text/javascript">
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'a60f') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_4') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '3}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }
</script>
<div style="position:relative; padding:5px;top:50px; left:38%; width:350px; height:140px; background-color:yellow">
<div style="text-align:center">
<p>This is the secure login portal</p>
<p>Enter valid credentials to proceed</p>
<form action="index.html" method="post">
<input type="password" id="pass" size="8" />
<br/>
<input type="submit" value="verify" onclick="verify(); return false;" />
</form>
</div>
</div>
</body>
</html>
```

We can see the code validating the password, and we can reconstruct it.

Simple script:
```python
#!/usr/bin/env python

import requests

r = requests.get('https://2019shell1.picoctf.com/problem/45147')
lines = r.text.split('\n')

lines = [l for l in lines if 'if ' in l]
lines = [l.split('==') for l in lines]
lines = list(sorted(map(lambda x: (x[0].strip(), x[1].split('\'')[1]), lines)))

s = ''
s += lines[0][1]
s += lines[-1][1]
for l in lines[1:-1]:
  s += l[1]

print s
```

Flag: picoCTF{no_clients_plz_4a60f3}
