<!DOCTYPE html>
<link rel="stylesheet" href="style.css">
<html>
<head>
    <title>LED Controller</title>
</head>
<body>
    <h1 class="center">LED Controller</h1>
    <form method="post">
    <input type="submit" name="ledsoff"
                class="button" value="Turn LEDs Off" />

    </form> 
    
    
    <?php
    if(array_key_exists('ledsoff', $_POST)) {
        ledsoff();
    }
    function ledsoff() {
        $output=null;
        $retval=null;
        exec('sudo python ledsoff.py', $output, $retval);
        if ($retval == 0){
            echo "Retval is 0";
        }
    }    
    ?>

    


</body>
</html>