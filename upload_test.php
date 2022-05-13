<?php

$command = escapeshellcmd('Upload.py');
    $output = shell_exec($command);
    echo $output;


?>