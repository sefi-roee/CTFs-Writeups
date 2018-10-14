# Problem
Can you unzip this [file](https://2018shell1.picoctf.com/static/1c1504eeb8236a26646a02bb29620923/flag.zip) for me and retreive the flag?

## Hints:
Make sure to submit the flag as picoCTF{XXXXX}

## Solution:

First we need to unzip the file
```bash
unzip flag.zip
```

And then we open the file
```bash
xdg-open flag.jpg
```

![alt text](./flag.jpg)

Flag: picoCTF{welcome_to_forensics}
