# Bandit Level 16

```bash
Username: bandit16
Password: cluFn7wTiGryunymYOu4RcffSxQluehd
Server:   bandit.labs.overthewire.org
Port:     2220
```

## Level Goal
This is similar to the last level, the only difference is that we first need to find the relevant port [31000-32000].

We start with a port scanning:
```bash
bandit16@bandit:~$ nmap -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-05-14 11:43 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00022s latency).
Not shown: 1000 closed ports
PORT      STATE SERVICE
31790/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds
```

*Weird, we got only 1 open port*.

Now, same as at last level:
```bash
ssh bandit16@bandit.labs.overthewire.org -p2220
bandit16@bandit:~$ echo cluFn7wTiGryunymYOu4RcffSxQluehd | openssl s_client -ign_eof -connect localhost:31790
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
MIICBjCCAW+gAwIBAgIEcujsaTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMTkwNDEwMTc0MDI2WhcNMjAwNDA5MTc0MDI2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMDAOx2/
Ga7z8/V6MZZt59YEZuKoMjCnGLvQRA10J/ax10I2sGzSShN8uHx3ywmE31uNlez0
/qWApc3c/SW2N7W+KFBlQ+2KAUaStDfa1q4vVFK9fjDqFMdrBH5M6xfkp6C29P7H
b5PjdyBUwa39Bzq6OmMCa43jR4a7rk7xf9ttAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAACt03iHqhg+NDoq/67pv7HgoEIdDeL9CemAvuiAYd3Njh97KI+6
Zfw2KJP4umFox/uicJLNqPLEvFmMCiUq5mIJc3DoQRJUFrem15mpDDtBvyYOi2eQ
kuRuSdEGJhl61CtLJ+srxuU9K7jFfzOrUL2K5bA2i7GhLalLbo5cMTXd
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
    Session-ID: 3159CDA2398D810A1C207599EEDE90AB61E57820D63EE4191C645CE4CCAB05A9
    Session-ID-ctx: 
    Master-Key: 65F752CAF388917B6689ABF725F9BA9EE72F0B8A6B24FE2DB9B3E356929F9E66ECD1DB7C532A562B1FDFDCFB0E562488
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 80 db 3c 95 5a fe 5f ed-71 c2 67 d2 82 29 e8 58   ..<.Z._.q.g..).X
    0010 - 8c 82 a9 71 8e ac 51 3e-27 1b 1f 7e b9 06 5c bc   ...q..Q>'..~..\.
    0020 - 36 ad 69 d3 fe 76 79 29-12 14 47 b1 a7 cc f1 06   6.i..vy)..G.....
    0030 - 61 81 4c 66 c4 fb b9 14-67 b5 ba dc e4 30 22 94   a.Lf....g....0".
    0040 - d3 a7 d5 e0 27 68 77 dd-20 af 51 ba 21 fc c1 60   ....'hw. .Q.!..`
    0050 - ec f1 2c a1 df e7 76 ef-b2 9d 0e 0f 8b 31 1a 4a   ..,...v......1.J
    0060 - 19 47 80 0b fc 15 9e dd-f9 19 9c c3 13 6f 83 58   .G...........o.X
    0070 - e3 0e 0b 57 f6 69 5c 7e-f1 df fd 1f 3d 06 5f 5b   ...W.i\~....=._[
    0080 - be 3c 1a ad a7 83 da 9b-ca c5 17 d9 b0 bc 42 f6   .<............B.
    0090 - 4b 65 9f a2 12 33 08 48-d3 fd 0e 2d 66 6b dd bc   Ke...3.H...-fk..

    Start Time: 1557827071
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```

We got an RSA private key, Nice!

**A single script is:**
```python
#!/usr/bin/env python

from pwn import *


def main():
    shell = ssh(host='bandit.labs.overthewire.org',
                user='bandit16',
                password='cluFn7wTiGryunymYOu4RcffSxQluehd',
                port=2220
           )

    nmap_ports = shell['nmap -v -p 31000-32000 localhost']
    nmap_ports = nmap_ports.split('\n')

    i = [i for i in range(len(nmap_ports)) if 'PORT' in nmap_ports[i]][0]
    i += 1

    while True:
        port = int(nmap_ports[i].split('/')[0])
        i += 1

        r = shell.remote('localhost', port)
        r.sendline('test')
        out = r.read()
        r.close()
        
        if "test" in out:
            continue
        else:
            r_ssl = shell.process('cat /etc/bandit_pass/bandit16 | openssl s_client -ign_eof -connect localhost:%d' % (port), shell=True)

            out_ssl = ''
            t = 0

            try:
                while True:
                    r = r_ssl.read(timeout=1)
                    out_ssl += r

                    if r == '':
                        break
            except EOFError:
                    pass

            print out_ssl

            if 'Correct' in out_ssl:
                out_ssl = out_ssl.split('\n')
                i = [i for i in range(len(out_ssl)) if 'Correct' in out_ssl[i]][0]
                i += 1

                out_key = open('bandit17.sshkey', 'w')
                while '-----END RSA PRIVATE KEY-----' not in out_ssl[i]:
                    out_key.write(out_ssl[i] + '\n')
                    i += 1
                out_key.write('-----END RSA PRIVATE KEY-----' + '\n')
                out_key.close

                print 'SSH key for bandit17 saved in bandit17.sshkey'
                break

    shell.close()

if __name__ == "__main__":
    main()
```