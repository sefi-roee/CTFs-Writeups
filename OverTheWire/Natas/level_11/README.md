# Natas Level 11

```bash
Username: natas11
Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
URL:      http://natas11.natas.labs.overthewire.org
```
We enter the site, and see the following page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas11.png" />
    <div align="center">Natas 11</div>
</figure>

Clicking on the "View sourcecode" link:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas11-view-sourcecode.png" />
    <div align="center">Natas 11 - View sourcecode</div>
</figure>

Lets understand the script:
```php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
        $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
        if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
            if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
                $mydata['showpassword'] = $tempdata['showpassword'];
                $mydata['bgcolor'] = $tempdata['bgcolor'];
            }
        }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
```

*xor_encrypt* just encrypts its parameter with the (repeated) secret key (xor encryption).

While loading the page, the variable
```php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
```
is declared, and the saved with *saveData* (*json_encode* -&gt; *xor_encrypt* -&gt; *base64_encode*).

Before that we try to load the data from the cookie (*base64_decode* -&gt; *xor_encrypt* -&gt; *json_decode*) and if successful, we update the values (*showpassword* and *bgcolor*).

Lets check the value of the cookie:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas11-cookie.png" />
    <div align="center">Natas 11 - Cookie</div>
</figure>

the value is:
```bash
ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D
```

if we *xor_encrypt* the *json_encode* of the default value with the *base64_decrypt* of the cookie, we will be able to find the secret key.

The following PHP code will do the job:
```php
<?php

function xor_encrypt2($a, $b) {
    $key = '';

    // Iterate through each character
    for($i=0;$i<min(strlen($a), strlen($b));$i++) {
        $key .= $a[$i] ^ $b[$i];
    }

    return $key;
}

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$encrypted_cookie = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");

echo xor_encrypt2(json_encode($defaultdata), $encrypted_cookie);
?>
```

the result is:
```bash
qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq
```

So the secret key is probably:
```bash
qw8J
```

Now lets encrypt the desired value (showpassword = yes) with that key:
```php
<?php

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$wanted_value = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

echo base64_encode(xor_encrypt(json_encode($wanted_value)));
?>
```

We get:
```bash
ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK
```

We just need to update the cookie and to refresh the page:
<figure>
    <img src="https://raw.githubusercontent.com/sefi-roee/CTFs-Writeups/master/OverTheWire/Natas/images/natas11-updated-cookie.png" />
    <div align="center">Natas 11 - Updated cookie</div>
</figure>

We got the password for the next level: **EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3**