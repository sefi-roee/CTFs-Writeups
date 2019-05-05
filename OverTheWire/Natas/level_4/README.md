# Natas Level 4

```bash
Username: natas4
Password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
URL:      http://natas4.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas4.png" />
    <div align="center">Natas 4</div>
</figure>

```html
Access disallowed. You are visiting from "http://localhost/" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
```

We need to set the HTTP referrer header to: “http://natas5.natas.labs.overthewire.org/”.

We can user burp or fiddler, but the easiest way is to use cURL.

```bash
curl -u natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ -e http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org
```
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas4-cURL.png" />
    <div align="center">Natas 4 - cURL</div>
</figure>

We got the password for the next level: **iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq**