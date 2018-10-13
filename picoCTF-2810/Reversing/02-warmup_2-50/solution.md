# Problem
Can you decode the following string ```dGg0dF93NHNfczFtcEwz``` from base64 format to ASCII?

## Hints:
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution:

We can use a basic bash script:
```bash
#!/usr/bin/bash

printf "picoCTF{%s}\n" $(echo dGg0dF93NHNfczFtcEwz | base64 --decode)
```

Flag: picoCTF{th4t_w4s_s1mpL3}
