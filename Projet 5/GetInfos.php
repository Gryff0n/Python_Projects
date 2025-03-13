<?php

$file=fopen("abonnés.txt", "a+");

$info=array(
    "name"=>$_POST["last_name"],
    "fname"=>$_POST["first_name"],
    "bdate"=>$_POST["birth_date"],
    "adress"=>$_POST["adress"],
    "tel"=>$_POST["tel"],
    "mail"=>$_POST["mail"],
    "password"=>$_POST["password"],
);

$List = implode(',', $info);

fwrite($file,"\n".$List);
header('location: http://localhost/index.html');
?>
