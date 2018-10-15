# Problem
'...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in /problems/you-can-t-see-me_3_1a39ec6c80b3f3a18610074f68acfe69.

## Hints:
What command can see/read files?

What's in the manual page of ls?

## Solution:

After connecting the remote server (via ssh/webshell) and going the this directory, we can see a file named ".", how is this possible? mb there are some spaces.

```bash
ls -alQ

total 60
drwxr-xr-x   2 root       root        4096 Sep 28 08:29 "."
-rw-rw-r--   1 hacksports hacksports    57 Sep 28 08:29 ".  "
drwxr-x--x 576 root       root       53248 Sep 30 03:45 ".."

cat ".  "

picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}
```

Easy!

Flag: picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_cf5156ef}