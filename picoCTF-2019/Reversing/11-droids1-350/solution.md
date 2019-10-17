# Problem
Find the pass, get the flag. Check out this [file](https://2019shell1.picoctf.com/static/6bf44e4070f1d2173e72a28e77f0d086/one.apk). You can also find the file in /problems/droids1_0_b7f94e21c7e45e6604972f9bc3f50e24.

## Hints:

Try using apktool and an emulator

https://ibotpeaches.github.io/Apktool/

https://developer.android.com/studio

## Solution:

First download the source and look at it:
```bash
wget https://2019shell1.picoctf.com/static/6bf44e4070f1d2173e72a28e77f0d086/one.apk
```

Executing the apk and clicking the button gives us nothing:
![screenshot-1](./screenshot-1.png)

Let's decompile:
```bash
../../../tools/Apktool/apktool d ./one.apk

roee@Roee-Ubuntu:~/CTFs-Writeups/picoCTF-2019/Reversing/10-droids1-350$ ../../../tools/Apktool/apktool d ./one.apk 
I: Using Apktool 2.4.0 on one.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
S: WARNING: Could not write to (/home/roee/.local/share/apktool/framework), using /tmp instead...
S: Please be aware this is a volatile directory and frameworks could go missing, please utilize --frame-path if the default storage directory is unavailable
I: Loading resource table from file: /tmp/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```

Now we observe the resources:
```bash
l one/res/values

total 260K
-rw-r--r-- 1 roee roee  26K אוק 17 17:16 attrs.xml
-rw-r--r-- 1 roee roee  240 אוק 17 17:16 bools.xml
-rw-r--r-- 1 roee roee 4.5K אוק 17 17:16 colors.xml
-rw-r--r-- 1 roee roee 7.9K אוק 17 17:16 dimens.xml
-rw-r--r-- 1 roee roee  228 אוק 17 17:16 drawables.xml
-rw-r--r-- 1 roee roee 3.9K אוק 17 17:16 ids.xml
-rw-r--r-- 1 roee roee  377 אוק 17 17:16 integers.xml
-rw-r--r-- 1 roee roee  95K אוק 17 17:16 public.xml
-rw-r--r-- 1 roee roee 3.4K אוק 17 17:16 strings.xml
-rw-r--r-- 1 roee roee 100K אוק 17 17:16 styles.xml

cat one/res/values/strings.xml

<?xml version="1.0" encoding="utf-8"?>
<resources>
    ...
    <string name="manatee">caribou</string>
    <string name="myotis">jackrabbit</string>
    <string name="password">opossum</string>
    <string name="porcupine">blackbuck</string>
    <string name="porpoise">mouflon</string>
    ...
</resources>
```

And we can see the password: `opossum`. Let's put this in the app:

![screenshot-1](./screenshot-1.png)

Got it!

Flag: picoCTF{pining.for.the.fjords}
