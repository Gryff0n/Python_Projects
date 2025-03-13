function getAge(date) { 
    var diff = Date.now() - date.getTime();
    var age = new Date(diff); 
    return Math.abs(age.getUTCFullYear() - 1970);
}

function validate() {
    a=document.getElementById('birth_date').value;
    a=a.split('-');
    b=getAge(new Date(a[0], a[1], a[2]));

    if (document.getElementById('last_name').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer votre nom !";
        return false;
    }
    if (document.getElementById('first_name').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer votre prénom !";
        return false;
    }
    if (document.getElementById('birth_date').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer votre date de naissance !";
        return false;
    }
    if (b<18) {
    document.getElementById("alert").innerHTML = "Vous devez avoir plus de 18 ans pour vous inscrire.";
        return false;
    }
    if (document.getElementById('adress').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer votre adresse !";
        return false;
    }
    if (document.getElementById('tel').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer votre numéro de téléphone !";
        return false;
    }
    if (document.getElementById('mail').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez entrer votre email !";
        return false;
    }
    if (document.getElementById('password').value == ""){
        document.getElementById("alert").innerHTML ="Veuillez saisir un mot de passe !";
        return false;
    }

    
}