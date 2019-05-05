# Natas Level 3

```bash
Username: natas3
Password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
URL:      http://natas3.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas3.png" />
    <div align="center">Natas 3</div>
</figure>

Lets check the page source:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas3-source.png" />
    <div align="center">Natas 3 - Page source</div>
</figure>

```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```

Not even google? is that a reference to google crawler? Lets check out the robots file:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas3-robots.png" />
    <div align="center">Natas 3 - Robots file</div>
</figure>

Is “/s3cr35/” directory disallowed? Lets check what is inside:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas3-secret.png" />
    <div align="center">Natas 3 - Secret directory</div>
</figure>

Again, directory listing isn’t disabled and we can see “users.txt” file:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas3-users-file.png" />
    <div align="center">Natas 3 - Users file</div>
</figure>

We got the password for the next level: **Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ**