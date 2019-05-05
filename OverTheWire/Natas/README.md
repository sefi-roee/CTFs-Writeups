# [Natas](http://overthewire.org/wargames/natas/)

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in /etc/natas_webpass/. E.g. the password for natas5 is stored in the file /etc/natas_webpass/natas5 and only readable by natas4 and natas5.

Start here:

```bash
Username: natas0
Password: natas0
URL:      http://natas0.natas.labs.overthewire.org
```

| Level                                                          | Password                         | Solution                      |
| -------------------------------------------------------------- | -------------------------------- | ------------------------------|
| [Level 0](http://overthewire.org/wargames/natas/natas0.html)   |                                  | [Link](./level_0/README.md)   |
| [Level 1](http://overthewire.org/wargames/natas/natas1.html)   | gtVrDuiDfck831PqWsLEZy5gyDz1clto | [Link](./level_1/README.md)   |
| [Level 2](http://overthewire.org/wargames/natas/natas2.html)   | ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi | [Link](./level_2/README.md)   |
| [Level 3](http://overthewire.org/wargames/natas/natas3.html)   | sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 | [Link](./level_3/README.md)   |
| [Level 4](http://overthewire.org/wargames/natas/natas4.html)   | Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ | [Link](./level_4/README.md)   |
