<?php
require('textlocal.class.php');

$textlocal = new Textlocal(false, false, "K3yhzXr3MyQ-0WP5pGoTlOeIlbUqFo2CryAmQfz03U");

$numbers = array(919692673579,919861567114,919431922371,919668797307);
$sender = 'TXTLCL';
$message = 'You are in danger zone';

try {
    $result = $textlocal->sendSms($numbers, $message, $sender);
    print_r($result);
} catch (Exception $e) {
    die('Error: ' . $e->getMessage());
}
?>