# Natas Level 2

```bash
Username: natas2
Password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
URL:      http://natas2.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas2.png" />
    <div align="center">Natas 2</div>
</figure>

Lets check the page source:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas2-source.png" />
    <div align="center">Natas 2 - Page source</div>
</figure>

There is a file named "pixel.png" in the "files" directory, lets check [this directory](http://natas2.natas.labs.overthewire.org/files/) (sadly, directory listing isn't disabled):

We will see the page source:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas2-direcory-listing.png" />
    <div align="center">Natas 2 - "files" directory listsing</div>
</figure>

We can see file named "users.txt", lets [view it](http://natas2.natas.labs.overthewire.org/files/users.txt):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas2-users-file.png" />
    <div align="center">Natas 2 - Users file</div>
</figure>

We got the password for the next level: **sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14**