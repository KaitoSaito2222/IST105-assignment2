<?php
// escapeshellcmd() is used to escape dangerous characters
$command = escapeshellcmd("python3 calculate.py ");
// shell_exec() is used to execute the command
$output = shell_exec($command);
echo $output;
?>