# Problem
There is a website running at https://2019shell1.picoctf.com/problem/7411/ ([link](https://2019shell1.picoctf.com/problem/7411/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://2019shell1.picoctf.com:7411

## Hints:

The password is being filtered.

## Solution:

We first try to observe the site:
![screenshot-1](./screenshot-1.png)
![screenshot-2](./screenshot-2.png)

We need to login, let's set the `debug` field (using DevTools) and try a simple query:
![screenshot-3](./screenshot-3.png)

Let's try a simple [SQL Injection](https://en.wikipedia.org/wiki/SQL_injection):
![screenshot-4](./screenshot-4.png)

Got it!

Flag: picoCTF{m0R3_SQL_plz_c1c3dff7}
