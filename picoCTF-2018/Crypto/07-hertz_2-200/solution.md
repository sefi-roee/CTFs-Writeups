# Problem
This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with ```nc 2018shell1.picoctf.com 39961```.

## Hints:
These kinds of problems are solved with a frequency that merits some analysis.

## Solution:

This is just a simple substitution cipher.

Connect to the remote server and obtain ciphertext

```bash
nc 2018shell1.picoctf.com 39961

Let's decode this now!
Ner xbsuj clmkd wma qbgfp mvrl ner ihzo tmy. S uhd'n crisrvr nesp sp pbue hd rhpo flmcirg sd Fsum. Sn'p higmpn hp sw S pmivrt h flmcirg hilrhto! Mjho, wsdr. Erlr'p ner wihy: fsumUNW{pbcpnsnbnsmd_usferlp_hlr_nmm_rhpo_pypyndfscm}
```

Go to [https://www.guballa.de/substitution-solver](https://www.guballa.de/substitution-solver) and paste the cipertext, this is fast.

The key is:
> abcdefghijklmnopqrstuvwxyz     This clear text ...
> hcutrwyesqjigdmfxlpnbvkaoz     ... maps to this cipher text

And we get:

```
The quick brown fox jumps over the lazy dog. I can't believe this is such an easy problem in Pico. It's almost as if I solved a problem already! Okay, fine. Here's the flag: picoCTF{substitution_ciphers_are_too_easy_sgsgtnpibo}
```

Flag: picoCTF{substitution_ciphers_are_too_easy_sgsgtnpibo}
