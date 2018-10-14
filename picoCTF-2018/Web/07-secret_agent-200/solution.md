# Problem
Here's a little website that hasn't fully been finished. But I heard google gets all your info anyway. [http://2018shell1.picoctf.com:46162](http://2018shell1.picoctf.com:46162)

## Hints:
How can your browser pretend to be something else?

## Solution:

Lets try to view the website:
```bash
curl http://2018shell1.picoctf.com:46162

<!DOCTYPE html>
<html lang="en">

<head>
    <title>My New Website</title>

    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="#">Home</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign In</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign Out</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">My New Website</h3>
        </div>
         
        <!-- Categories: success (green), info (blue), warning (yellow), danger (red) -->
        
      
        <div class="jumbotron">
            <p class="lead"></p>
            <p><a href="/flag" class="btn btn-lg btn-success btn-block"> Flag</a></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF 2018</p>
        </footer>

    </div>
    <script>
    $(document).ready(function(){
        $(".close").click(function(){
            $("myAlert").alert("close");
        });
    });
    </script>
</body>

</html>
```

Nothing, lets use the hint, and send custom user-agent string. Lets take a look [here](https://support.google.com/webmasters/answer/1061943?hl=en)
```bash
#!/bin/bash

curl -A "Googlebot"  http://2018shell1.picoctf.com:46162/flag | grep picoCTF

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2111  100  2111    0     0   6218      0 --:--:-- --:--:-- --:--:--  6264
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{s3cr3t_ag3nt_m4n_ac87e6a7}</code></p>
```

OWNed it!

Flag: picoCTF{s3cr3t_ag3nt_m4n_ac87e6a7}
