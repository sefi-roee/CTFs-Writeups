# Problem
Can you unzip this [file](https://2019shell1.picoctf.com/static/37762a7e5774d7d6c1bc79e8e1758ef9/flag.zip) and get the flag?

## Hints:
put the flag in the format picoCTF{XXXXX}

## Solution:

First, let's download the file:
```bash
wget https://2019shell1.picoctf.com/static/37762a7e5774d7d6c1bc79e8e1758ef9/flag.zip
```

Now, let's unzip it:
```bash
unzip flag.zip

Archive:  flag.zip
  inflating: flag.png
```

Let's take a look:
![flag](./flag.png)

Flag: picoCTF{unz1pp1ng_1s_3a5y}
