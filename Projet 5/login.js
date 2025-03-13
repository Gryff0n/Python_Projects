function tamere() {

var tableau1 = new Array(6) ;

    tableau1[0]=document.getElementById('Nom').value;
    tableau1[1]=document.getElementById('Prenom').value;
    tableau1[2]=document.getElementById('BD').value;
    tableau1[3]=document.getElementById('Adresse').value;
    tableau1[4]=document.getElementById('phone_number').value;
    tableau1[5]=document.getElementById('mail').value;

    document.getElementById('info').innerHTML =tableau1

}
