# Problem
Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_3_7c0eade7faf60ffe3485e12098e2a6c2 on the shell server and run this [program](https://2018shell1.picoctf.com/static/40fdfa8d8bce92a4b965c80caf124a4f/run) to retreive the flag?

## Hints:
If you are searching online, it might be worth finding how to exeucte a program in command line.

## Solution:

First, we download the program
```bash
wget https://2018shell1.picoctf.com/static/40fdfa8d8bce92a4b965c80caf124a4f/run
```

Then we give it execute permissions, and execute it:
```bash
chmod +x ./run
./run
```

Flag: picoCTF{welc0m3_t0_r3VeRs1nG}
