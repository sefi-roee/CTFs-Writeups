# Bandit Level 15

```bash
Username: bandit15
Password: BfMYroe26WYalil77FoDi9qh59eK5xNr
Server:   bandit.labs.overthewire.org
Port:     2220
```

## Level Goal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost **using SSL encryption**.

Lets do it:
```bash
ssh bandit15@bandit.labs.overthewire.org -p2220
bandit15@bandit:~$ echo BfMYroe26WYalil77FoDi9qh59eK5xNr | openssl s_client -ign_eof -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEBadydTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMTkwMjI3MDg1MTQ5WhcNMjAwMjI3MDg1MTQ5WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMyEZzRA
+5ll7Ap2bwla+8x39mTviZKqrjnmLuTZj1U3mugt3G2JI5loXyjnFxlXnHUGy/xI
OiACFOEJCce2VIkarMa1Cy13wtGuLoZxjcYSAIMzIOPykCh9+FJ89Tt1TIVXmO0C
TJaxFMhKdX0ALZlxjN1+xoZgeOtN7yfhprjjAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBACNP1/t8pfANluA2MuoxCAkie0bDCUL/ZV7FDaH1YUAEG7wEZVFJ
Pt8+6L8HkLYcuCPtjc2uxA8yEiqS7fiYRU26PmrQXzm09W0ah1pq+7NGMLKz596B
AIpiTkVpA7YCUvGcYvz6yXS202e2GbLOulF2l9kx6hhhBCWubeqh2IjR
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 005EB1C3DDDF231DCA44F40D3DE59BCA5ABB69F7C5D903C857DE27F74735FF73
    Session-ID-ctx: 
    Master-Key: 2BAFCFCECB96690077DD70CC3910C1264F4640B91CDAA766B5A0DD6032103C2C55001513B0C290BA78DA525216B0D1A3
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - df 12 86 44 83 09 d4 62-75 55 25 0c f8 4f 2c 53   ...D...buU%..O,S
    0010 - 94 cf c0 a0 76 c6 8a 1b-4c a5 68 c0 da d9 88 25   ....v...L.h....%
    0020 - e0 5b 91 b0 5f 15 55 30-09 3b f0 9d 69 ff da 4f   .[.._.U0.;..i..O
    0030 - 8b f3 d1 7a 26 f8 12 2f-f7 4f ae 4e 8f d2 1c b8   ...z&../.O.N....
    0040 - 4f 8b 86 7d 49 9e 57 a5-bc 64 0d f5 11 d3 47 fa   O..}I.W..d....G.
    0050 - 48 36 02 97 ed f5 75 86-d9 42 cf e9 0e e7 59 5f   H6....u..B....Y_
    0060 - f5 b7 0a eb b0 8c ed 03-d6 60 33 92 2e 1c 5c a0   .........`3...\.
    0070 - 9b a1 53 14 a0 f7 d6 1d-f4 3a 5d 9f 1c 4c 32 20   ..S......:]..L2 
    0080 - cf 57 4a 20 3f 42 0a 73-13 78 60 88 eb 36 7e 24   .WJ ?B.s.x`..6~$
    0090 - f1 76 a7 d0 72 e0 64 43-23 a2 c5 a7 57 c1 72 bc   .v..r.dC#...W.r.

    Start Time: 1557826365
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

Nice!

We got the password for the next level: **cluFn7wTiGryunymYOu4RcffSxQluehd**

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit15',
                password='BfMYroe26WYalil77FoDi9qh59eK5xNr',
                port=2220
           )

    print shell['cat /etc/bandit_pass/bandit15 | openssl s_client -ign_eof -connect localhost:30001']

if __name__ == "__main__":
    main()
```