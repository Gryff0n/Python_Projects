<?php
    session_start();
    if (isset($_SESSION["user"])){
        if (isset($_SESSION["status"])){
            if ($_SESSION["status"] != "admin"){
                header('location: http://localhost/Forbiden_access.php');
            }
        } 
    }else {
        header('location: http://localhost/login.php');
    }
    if(isset($_POST['disconnect_button'])) {
        session_destroy();
        header('location: http://localhost/login.php');
        }
?>

<!DOCTYPE html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="./project_css/default.css"/>
        <title>L'Aurora</title>
    </head>
    <body>
        <header>
            <div class="topnav">
                <a class="active" href="index.html">Home</a>
                <a href="sub.html">S'inscrire</a>
                <a href="login.php">Mon espace</a>
            </div>
        </header>
            <div id="Maintext">
                <h1>Espace de supression d'adhérents</h1>
                <p>Entrez l'<strong>ID</strong> de l'adhérents qui sera suprimé</p>
            </div>
            <?php
            // affiche les infos du compte utilisé actuellement 
            echo "Account connected status : <strong>". $_SESSION['status'] ."</strong>" . " / user : <strong>" . $_SESSION["user"] . "</strong><br/>";

            // ouvre le fichier ou sont stocker nos données 
            $json_file = file_get_contents("./project_json/users.json");
            $json_array = json_decode($json_file, true);
            $ID = 0;

            // affichage de la liste de tous les abonnés avec toutes leur caractéristiques 
            foreach ($json_array["users"] as $member_data) {
                $ID = $ID+1;
                print_r("<ul><li>
                    <strong>ID : </strong>" . $ID. " / " . "<strong>nom : </strong>" . $member_data["name"] . "  " . " / " .
                    "<strong>Prénom : </strong>" . $member_data["fname"] . "  " . " / " .
                    "<strong>Adresse : </strong>" . $member_data["adress"] . "  " . " / " .
                    "<strong>Date de naissance : </strong>" . $member_data["bdate"] . "  " . " / " .
                    "<strong>Numéros de téléphone : </strong>" . $member_data["tel"] . "  " .  " / " .
                    "<strong>Mail : </strong>" . $member_data["mail"] . "  " .  " / " .
                    "<strong>Identifiant : </strong>" . $member_data["username"] . "  " .  " / " .
                    "<strong>Mot de Passe : </strong>" . $member_data["password"] . "  " .  " / " .
                    "<strong>Status : </strong>" . $member_data["perm_type"] . 
                    "</ul></li>" 
                );
            }
            // input pour suprimer le compte voulu 
            echo "<form method=\"POST\"> " . "ID of account to delete : " . "<input type=\"number\" name=\"user_id\"/>" . "  " . "<button type=\"submit\">Delete</button>" ."    "." <input type=\"submit\" name=\"disconnect_button\" value=\"Log out\"/>"."</form><br/>";

            if (isset($_POST['user_id'])) {
                $json_file = file_get_contents('./project_json/users.json');
                $json_array = json_decode($json_file, true);
                $user_id = $_POST['user_id'];
                $account_number = count($json_array['users']);
                
                //     <tr><td></td></tr>
                // </table>
            
                // check si L'ID du compte exist
                if ($user_id <=  $account_number) {
                    // vérifie et block si l'ID envoyer n'est pas un chiffre ou est NULL
                    if (($user_id  == NULL) || ($user_id != is_numeric($user_id))) {
                        echo "<font color=#ff0000>Operation not allowed, incorrect value was entered";

                    // Verifie le status du compte, et interdit la supresion des comptes type admin   
                    }else if ($json_array['users'][($user_id)-1]['perm_type']  == "admin") {
                        echo "<font color=#ff0000>Operation not allowed beacause account status = ADMIN";

                    }elseif ($json_array['users'][($user_id)-1]['perm_type']  == "member") {
                        // supresion de l'adhérent choisi or admin
                        unset($json_array['users'][($user_id)-1]);

                        // TRe-index the array, (pour eviter les bug)
                        Sort($json_array['users']);
                        
                        // ouverture du fichier json
                        $file_json = fopen("./project_json/users.json", "w+");

                        // remplace le contenu
                        fwrite($file_json, json_encode($json_array, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ));

                        // ferme le fichier 
                        fclose($file_json);
                        header("Refresh:0");
                    }
                        
                }else {
                    // si l'id de compte entré ne correspond a aucun inscrit affiche un message d'erreur
                    echo "<font color=#ff0000>No account with Id : " . $user_id . " found";
                }
            
            }
            
            ?>
    </body>
</html>
