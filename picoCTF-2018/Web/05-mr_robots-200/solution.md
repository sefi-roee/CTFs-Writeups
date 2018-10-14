# Problem
Do you see the same things I see? The glimpses of the flag hidden away? [http://2018shell1.picoctf.com:15298](http://2018shell1.picoctf.com:15298)

## Hints:
What part of the website could tell you where the creator doesn't want you to look?

## Solution:

We need to read a little about [robots.txt](http://www.robotstxt.org/robotstxt.html)

Lets try to view the contents:
```bash
curl http://2018shell1.picoctf.com:15298/robots.txt

User-agent: *
Disallow: /c4075.html
```

OK, lets view this file:
```bash
curl http://2018shell1.picoctf.com:15298/c4075.html

<html>
  <head>
    <title>Mr. Robots</title>
    <link href="https://fonts.googleapis.com/css?family=Monoton|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="container">
      <header>
	<h1>Mr. Robots</h1>
      </header>
      <div class="content">
	<p>So much depends upon a red flag<br />
	  <flag>picoCTF{th3_w0rld_1s_4_danger0us_pl4c3_3lli0t_c4075}</flag></p>
      </div>
      <footer></footer>
  </body>
</html>
```

The flag is right there!

Flag: picoCTF{th3_w0rld_1s_4_danger0us_pl4c3_3lli0t_c4075}
