# Problem
The [numbers](https://2019shell1.picoctf.com/static/eb3589c566dd3f809908053460acb817/the_numbers.png)... what do they mean?

## Hints:
The flag is in the format PICOCTF{}

## Solution:

First we need to download the image:
```bash
wget https://2019shell1.picoctf.com/static/eb3589c566dd3f809908053460acb817/the_numbers.png
```

Let's take a look:
![the_numbers](./the_numbers.png)

And then, using a simple script:
```python
#!/usr/bin/env python

numbers = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'

s = ''
for number in numbers.split():
    try:
        n = int(number)
        s += chr(ord('a') + n - 1)
    except:
        s += number

print '{}'.format(s.upper())
```

Flag: PICOCTF{THENUMBERSMASON}
