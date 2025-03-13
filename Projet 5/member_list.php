
<!-- Ouvre une sessino-->
<?php
session_start();
// ferme la session si le boutton deconnection est préss
if(isset($_POST['disconnect_button'])) {
        session_destroy();
        header('location: http://localhost/login.php');
        
}
if(isset($_POST['Login_page'])) {
    header('location: http://localhost/login.php');
    
}
?>

<!-- strucure html par defaut -->
<!DOCTYPE html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="project_css/default.css"/>
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
                <h1>Liste des Adhérents au club de L'aurora</h1>
                <p></p>
        </div>
        <!-- php verifie si quelqu'un est connecté -->
        <?php    
        if (isset($_SESSION["user"])){
            if (isset($_SESSION["status"])){
                if ($_SESSION["status"] == "admin"){
                    echo "Account connected <strong>status : " . $_SESSION['status'] . "</strong>" . " / <strong>User : ". $_SESSION["user"] . "</strong><br/>";
                    // ouvre le fichier ou sont stocker nos données 
                    $json_file = file_get_contents("./project_json/users.json");
                    $json_array = json_decode($json_file, true);
                    $data = array();
                    // Affiche sous forme de liste les caractéristique de chaque abonnés
                    foreach ($json_array["users"] as $member_data) {
                        print_r("<ul><li>
                            <strong>nom : </strong>" . $member_data["name"] . "  " . " / " .
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
                    echo "<form method=\"POST\">
                    <input type=\"submit\" name=\"disconnect_button\" value=\"Log out\"/>
                </form>";
                                   
                } else {
                    echo "Account connected <strong>status : " . $_SESSION['status'] . "</strong>" . " / <strong>User : ". $_SESSION["user"] . "</strong><br/>";
                    $json_file = file_get_contents("./project_json/users.json");
                    $json_array = json_decode($json_file, true);
                    $data = array();
                    // même chose qu'au-dessus mais montre que le nom et prenom  
                    foreach ($json_array["users"] as $member_data) {
                        print_r("<ul><li>
                            <strong>nom : </strong>" . $member_data["name"] . "  " . " / " .
                            "<strong>prénom</strong> : " . $member_data["fname"]  . 
                            "</ul></li>" 
                        );
                    }
                    echo "<form method=\"POST\">
                    <input type=\"submit\" name=\"disconnect_button\" value=\"Log out\"/>
                </form>";

                }
            }
            //interdit l'accès aux infos du club   
        } else {
            echo "<strong>Accèe non autorisé, vous devez vous connecté avec un compte valide ou administrateur</strong><br/>";
            echo "<form method=\"POST\"><input type=\"submit\" name=\"Login_page\" value=\"Login\"/></form>";
            
        }
        echo '<br/>'
        ?>
    </body>
</html>


