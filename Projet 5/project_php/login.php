<?php
//ouvre une nouvelle session jusqu'a la deconnection
session_start();
// ouvrir le fichier json
$json_file = file_get_contents("../project_json/users.json");
// le transformer en table php

$json_array = json_decode($json_file, true);
// parcourir cette table php

foreach ($json_array["users"] as $user) {

    // si le username correspond et regarder si le mot de passe aussi
    if (($user["username"] == $_POST["log_id"]) && ($user["password"] == $_POST["password"])) {

        // si ya correspondance recuperer le statut du compte
        // En fonction du type de compte faire la bonne redirection 
        $check_perm =  $user["perm_type"];
        if ($check_perm == "admin") {
            $_SESSION["user"] = $user["username"];
            $_SESSION["status"] = $check_perm;
            $_SESSION["stay_connected"] = True;
            header('location: http://localhost/admin_space.php');
            exit();
        } elseif ($check_perm == "member") {
            $_SESSION["user"] = $user["username"];
            $_SESSION["status"] = $check_perm;
            $_SESSION["stay_connected"] = True;
            header('location: http://localhost/member_list.php');
            exit();
        }
        
    } else {
        // Sinon ça bloque et affiche un msg d'erreur 
        $_SESSION['incorrect_values'] = True;
    } 

}
header('location: http://localhost/login.php');
?>