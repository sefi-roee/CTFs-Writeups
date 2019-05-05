# Natas Level 5

```bash
Username: natas5
Password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
URL:      http://natas5.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas5.png" />
    <div align="center">Natas 5</div>
</figure>

```html
Access disallowed. You are not logged in
```

How does the server save the state? In this case, he IS NOT!

Lets check which cookies this site stores (We can use chrome developer tools -> Application -> Cookies):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas5-cookies.png" />
    <div align="center">Natas 5 - Cookies</div>
</figure>

We can see the “loggedin” cookie with value: 0.

Lets change it to something else:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas5-cookie-update.png" />
    <div align="center">Natas 5 - Cookie update</div>
</figure>

And after we refresh the page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas5-loggedin.png" />
    <div align="center">Natas 5 - Logged in</div>
</figure>

Access granted!

We got the password for the next level: **aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1**