# Problem
A musician left us a [message](https://2019shell1.picoctf.com/static/46e165b0a953075440f3a544fdb4cff1/message.txt). What's it mean?

## Hints:

## Solution:

First, we need to download the file:
```bash
wget https://2019shell1.picoctf.com/static/46e165b0a953075440f3a544fdb4cff1/message.txt
```

```text
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

Let's put the coordinates on google maps, we get:

35.028309, 135.753082   -   Nakanocho, Kamigyo Ward, Kyoto, Japan
46.469391, 30.740883    -   Odesa, Odessa Oblast, Ukraine, 65000
39.758949, -84.191605   -   Dayton, OH 45402, United States
41.015137, 28.979530    -   İstanbul, Hoca Paşa, 34110 Fatih/İstanbul, Turkey
24.466667, 54.366669    -   Hazza Bin Zayed the First St - Abu Dhabi - United Arab Emirates
3.140853, 101.693207    -   Unnamed Road, 50480 Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia

9.005401, 38.763611     -   Unnamed Road, Addis Ababa, Ethiopia
-3.989038, -79.203560   -   Av Nueva Loja, Loja, Ecuador
52.377956, 4.897070     -   Martelaarsgracht 5, 1012 TN Amsterdam, Netherlands
41.085651, -73.858467   -   Sleepy Hollow, NY 10591, United States
57.790001, -152.407227  -   Kodiak, AK 99615, United States
31.205753, 29.924526    -   Faculty Of Engineering, Al Azaritah WA Ash Shatebi, Qism Bab Sharqi, Alexandria Governorate, Egypt

Let's take first letter from city names:
picoCTF{KODIAK_ALASKA} 


Flag: picoCTF{KODIAK_ALASKA}
