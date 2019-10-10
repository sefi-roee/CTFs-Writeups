# Problem
I wrote you a [song](https://2019shell1.picoctf.com/static/e0b32d09ed9e6cf0d4a7ded906a29e21/lyrics.txt). Put it in the picoCTF{} flag format

## Hints:

Do you think you can master rockstar?

## Solution:

Let's download it and take a look:
```bash
wget https://2019shell1.picoctf.com/static/e0b32d09ed9e6cf0d4a7ded906a29e21/lyrics.txt
cat lyrics.txt

Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico
```

The hint suggesting the [rockstar programming language](https://en.wikipedia.org/wiki/Esoteric_programming_language#Rockstar)

We can use some [online interpreter](https://codewithrockstar.com/online) for this, we get:
```bash
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```

And using a simple script:
```python
#!/usr/bin/env python

r = [114, 114, 114, 111, 99, 107, 110, 114, 110, 48, 49, 49, 51, 114]

print 'picoCTF{{{}}}'.format(''.join(map(chr, r)))
```

*Maybe sometime, I will solve it by myself...*

Flag: picoCTF{rrrocknrn0113r}
