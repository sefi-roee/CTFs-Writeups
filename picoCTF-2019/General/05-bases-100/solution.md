# Problem
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution:

We can use a basic bash script:
```bash
#!/usr/bin/bash

printf "picoCTF{%s}\n" $(echo bDNhcm5fdGgzX3IwcDM1 | base64 --decode)
```

Flag: picoCTF{l3arn_th3_r0p35}
