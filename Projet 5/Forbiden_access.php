<?php
    session_start();
    if(isset($_POST['disconnect_button'])) {
        session_destroy();
        header('location: http://localhost/login.php');
        }  
?>

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
            <div id="text">
                <font color= #ff0000>
                <h1>Accès non autorisés</h1>
                <p>Connectes-toi avec un compte dont les permissions d'accès sont valides<font</p>
                <font color= #000000>
                <br/><br/>  
                <?php
                if (isset($_SESSION["user"])){
                    if (isset($_SESSION["status"])){
                        if ($_SESSION["status"] != "admin"){
                            echo "Logged as <br/>";
                            echo "<ul>User : <strong>" . $_SESSION['user']."</strong><br/>" . "<br/>Acoount status : <strong>" . $_SESSION['status']."</strong></ul><br/>";
                            echo "<form method=\"POST\"> " . "<input type=\"submit\" name=\"disconnect_button\" value=\"Log out\"/>" . "</form><br/>";
                        }
                    } 
                }else {
                    echo "<strong>No logged user detected</strong>";
                    
                }
                ?>
            </div>
        </header>
    </body>
</html>