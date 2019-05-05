# Natas Level 1

```bash
Username: natas1
Password: gtVrDuiDfck831PqWsLEZy5gyDz1clto
URL:      http://natas1.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas1.png" />
    <div align="center">Natas 1</div>
</figure>

When trying to right click, a messages pops up:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas1-popup.png" />
    <div align="center">Natas 1 - Popup</div>
</figure>

To bypass this we have two options:
* Use the keyboard shorcut (in chrome: CTRL-U)
* Add "view-source" to the URL (view-source:http://natas1.natas.labs.overthewire.org/)

We will see the page source:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas1-source.png" />
    <div align="center">Natas 1 - Page source</div>
</figure>

We got the password for the next level: **ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi**