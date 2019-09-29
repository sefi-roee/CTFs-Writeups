# Problem
This [garden](https://2019shell1.picoctf.com/static/86137520022d967547d5a2c99f4231f2/garden.jpg) contains more than it seems. You can also find the file in /problems/glory-of-the-garden_2_258af8e13bd7259207af0b0ee6fab645 on the shell server.

## Hints:
What is a hex editor?

## Solution:

Let's search for a string
```bash
strings garden.jpg | grep pico

Here is a flag "picoCTF{more_than_m33ts_the_3y31e0af5C7}"
```
Nice.

Flag: picoCTF{more_than_m33ts_the_3y31e0af5C7}
