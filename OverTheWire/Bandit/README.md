# [Bandit](http://overthewire.org/wargames/bandit/)

The Bandit wargame is aimed at absolute beginners. It will teach the basics needed to be able to play other wargames. *If you notice something essential is missing or have ideas for new levels, please let us know!*

## Note for beginners
This game, like most other games, is organised in levels. You start at Level 0 and try to “beat” or “finish” it. Finishing a level results in information on how to start the next level. The pages on this website for “Level <X>” contain information on how to start level X from the previous level. E.g. The page for Level 1 has information on how to gain access from Level 0 to Level 1. All levels in this game have a page on this website, and they are all linked to from the sidemenu on the left of this page.

You will encounter many situations in which you have no idea what you are supposed to do. *Don’t panic! Don’t give up!* The purpose of this game is for you to learn the basics. Part of learning the basics, is reading a lot of new information.

There are several things you can try when you are unsure how to continue:

First, if you know a command, but don’t know how to use it, try the manual (man page) by entering “man <command>” (without the quotes). e.g. if you know about the “ls” command, type: man ls. The “man” command also has a manual, try it. Press q to quit the man command.
Second, if there is no man page, the command might be a shell built-in. In that case use the “help <X>” command. E.g. help cd
Also, your favorite search-engine is your friend. Learn how to use it! I recommend Google.
Lastly, if you are still stuck, you can join us on IRC
You’re ready to start! Begin with [Level 0](http://overthewire.org/wargames/bandit/bandit0.html), linked at the left of this page. Good luck!

Note for VMs: You may fail to connect to overthewire.org via SSH with a “broken pipe error” when the network adapter for the VM is configured to use NAT mode. Adding the setting IPQoS throughput to /etc/ssh/ssh_config should resolve the issue. If this does not solve your issue, the only option then is to change the adapter to Bridged mode.

```bash
Username: bandit0
Password: bandit0
Server:   bandit.labs.overthewire.org
Port:     2220
```

| Level                                                          | Password                         | Solution                      |
| -------------------------------------------------------------- | -------------------------------- | ------------------------------|
| [Level 0](http://overthewire.org/wargames/bandit/bandit1.html) |                                  | [Link](./level_0/README.md)   |
| [Level 1](http://overthewire.org/wargames/bandit/bandit2.html) | boJ9jbbUNNfktd78OOpsqOltutMc3MY1 | [Link](./level_1/README.md)   |
| [Level 2](http://overthewire.org/wargames/bandit/bandit3.html) | CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9 | [Link](./level_2/README.md)   |
| [Level 3](http://overthewire.org/wargames/bandit/bandit4.html) | UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK | [Link](./level_3/README.md)   |
| [Level 4](http://overthewire.org/wargames/bandit/bandit5.html) | pIwrPrtPN36QITSp3EQaw936yaFoFgAB | [Link](./level_4/README.md)   |
| [Level 5](http://overthewire.org/wargames/bandit/bandit6.html) | koReBOKuIDDepwhWk7jZC0RTdopnAYKh | [Link](./level_5/README.md)   |
| [Level 6](http://overthewire.org/wargames/bandit/bandit7.html) | DXjZPULLxYr17uwoI01bNLQbtFemEgo7 | [Link](./level_6/README.md)   |
| [Level 7](http://overthewire.org/wargames/bandit/bandit8.html) | HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs | [Link](./level_7/README.md)   |