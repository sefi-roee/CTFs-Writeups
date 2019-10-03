# Problem
What do the [flags](https://2019shell1.picoctf.com/static/ae23b7df04365ab0213f0158c5b5d694/flag.png) mean?

## Hints:
The flag is in the format PICOCTF{}

## Solution:

First, we need to download the file:
```bash
wget https://2019shell1.picoctf.com/static/ae23b7df04365ab0213f0158c5b5d694/flag.png
```

Let's take a look:
![flag](./flag.png)

Let's try to place the characters we already know:
PICOCTF{FabcdbefdTgFF}

Let's use [Wikipedia](https://en.wikipedia.org/wiki/International_Code_of_Signals) to check the missing flags:
![ICS_flags](./ICS-flags.png)
PICOCTF{FaAGdANDdTUFF}

Use [this](http://www.quadibloc.com/other/flaint.htm) for the digits:
PICOCTF{F1AG5AND5TUFF}


Flag: PICOCTF{F1AG5AND5TUFF}
