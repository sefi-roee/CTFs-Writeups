# Problem
Can you find the robots? [https://2019shell1.picoctf.com/problem/4159/](https://2019shell1.picoctf.com/problem/4159/) or http://2019shell1.picoctf.com:4159

## Hints:
What part of the website could tell you where the creator doesn't want you to look?

## Solution:

We need to read a little about [robots.txt](http://www.robotstxt.org/robotstxt.html)

Lets try to view the contents:
```bash
curl https://2019shell1.picoctf.com/problem/4159/robots.txt

User-agent: *
Disallow: /a44f7.html
```

OK, lets view this file:
```bash
curl https://2019shell1.picoctf.com/problem/4159/a44f7.html

<!doctype html>
<html>
  <head>
    <title>Where are the robots</title>
    <link href="https://fonts.googleapis.com/css?family=Monoton|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="container">
      
      <div class="content">
  <p>Guess you found the robots<br />
    <flag>picoCTF{ca1cu1at1ng_Mach1n3s_a44f7}</flag></p>
      </div>
      <footer></footer>
  </body>
</html>
```

The flag is right there!

Flag: picoCTF{ca1cu1at1ng_Mach1n3s_a44f7}
