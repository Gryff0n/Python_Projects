<?php
    session_start();
    if (isset($_SESSION["stay_connected"])){
        if(isset($_SESSION["status"])){
            if ($_SESSION["status"] == "admin"){
                header('location: http://localhost/admin_space.php');
            }elseif ($_SESSION["status"] == "member") {
                header('location: http://localhost/member_list.php');
            }
        }
    }
        
?>

<!DOCTYPE html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="project_css/default.css"/>
        <link rel="stylesheet" href="project_css/login.css"/>
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
        <form action="/project_php/login.php" method="POST">
            <div id="logger">
            <form>
                <table>
                    <tr>
                        <td>Identidiant : </td>
                        <td><input type="text" name="log_id"/></td>
                    </tr>
                    <tr>
                        <td>Mot de passe : </td>
                        <td><input type="password" name="password" /></td>
                    </tr>
                    <tr><td><button type="submit" value="Se connecter">Se connecter</button></td></tr>
                </table>
            </form>
            <?php
                if(isset($_SESSION["incorrect_values"])) {
                    if($_SESSION['incorrect_values'] == True) {
                        echo "<font color =  #ff0000><li>Incorrect username or password submited</li><br/>"."<li>Please submit valid informations</li>";
                    } else {
                        $_SESSION['incorrect_values'] = False;

                    }
                    
                }
            ?>
            </div>
            <div id="Advice">
                <strong><p>Astuce :</p></strong>
                <ul><li><p>Identifiant se presente sous cette forme : prénom.nom</p></li></ul>
                <ul><li><p>Le mot de passe est celui que vous aviez définit lors de l'inscription.</p></li></ul>
                <ul><li><p>Une fois connecté vous resterez connecté jusqu'a que vous vous déconnecté.</p></li></ul>
            </div>
        </form>
    </body>
</html>