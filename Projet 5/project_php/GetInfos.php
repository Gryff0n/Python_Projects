<?php

// Version JSON
$file_json = file_get_contents("../project_json/users.json");

// Transforme le json en array php
$json_array = json_decode($file_json, true);

// Recupere les donnes post de la page 
$info = array(
    "name" => $_POST["last_name"],
    "fname" => $_POST["first_name"],
    "bdate" => $_POST["birth_date"],
    "adress" => $_POST["adress"],
    "tel" => $_POST["tel"],
    "mail" => $_POST["mail"],
    "password" => $_POST["password"],
    "username" => $_POST["first_name"] . "." . $_POST["last_name"],
    "perm_type" => "member"
);

// Ajoute le nouvelle utilisateur dans la table php users
array_push($json_array["users"], $info);

// ouvre le fichier 
$file_json = fopen("../project_json/users.json", "w+");

// remplace le contenu
fwrite($file_json, json_encode($json_array, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ));

// ferme le fichier;
fclose($file_json);

header('location: http://localhost/login.php');
?>




