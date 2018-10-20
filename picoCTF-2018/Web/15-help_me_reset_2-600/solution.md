# Problem
There is a website running at [http://2018shell1.picoctf.com:47150](http://2018shell1.picoctf.com:47150). We need to get into any user for a flag!

## Hints:
Try looking past the typical vulnerabilities. Think about possible programming mistakes.

## Solution:
Lets take a look:

![screenshot 1](./screenshot-1.png)

And the source:

![screenshot 2](./screenshot-2.png)

Lets try to login as ```batool```:

![screenshot 3](./screenshot-3.png)
![screenshot 4](./screenshot-4.png)

Lets try "password reset":

![screenshot 5](./screenshot-5.png)
![screenshot 6](./screenshot-6.png)

After refreshing few times, we got this question, Lets try ```black```:

![screenshot 7](./screenshot-7.png)

Too many wrong, lets try another user:

![screenshot 7](./screenshot-8.png)

Nice, you I got this right. Refresh the page until same question back again, answer correctly 3 times and we can reset password:

![screenshot 9](./screenshot-9.png)
![screenshot 10](./screenshot-10.png)
![screenshot 11](./screenshot-11.png)
![screenshot 12](./screenshot-12.png)

**Note: I'm sure there is a way to solve this without guessing, no idea**

Flag: picoCTF{i_thought_i_could_remember_those_e3063a8a}
