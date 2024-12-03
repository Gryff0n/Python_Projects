#import des modules
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 

#Read csv & fabrication des groupes et tables
def read_titanic_data(file_name, separator):
    global titanic_data,titanic_label,titanic_csv
    #import du csv par pandas
    titanic_csv = pandas.read_csv(file_name, sep=separator)
    #on abondonne les données inutiles
    titanic_csv = titanic_csv.drop(["Name","SibSp","Parch","Ticket","Fare","Embarked"], axis=1)
    #on abondonne ligne qui possèdes des données imcomplètes 
    titanic_csv = titanic_csv.dropna(subset=['Sex', 'Cabin', 'Pclass', "Age"])
    titanic_csv = titanic_csv[titanic_csv['Cabin'].str.len()<5]
    #modification de la colonne Sex pour la rendre utilisable pour Sklearn 
    titanic_csv = titanic_csv.replace("female", 0) #remplace "female" par 0
    titanic_csv = titanic_csv.replace("male", 1) #remplace "male" par 1
    #modification de la colonne Cabin pour rendre les données utilisable par sklearn
    for element in titanic_csv["Cabin"]:
        if len(element)>1:
            if element[0] != int():
                titanic_csv = titanic_csv.replace(element, (ord(element[0].lower())-96) + int(element[1:])/1000) #ramplacement des lettres par des nombres
            else:
                titanic_csv = titanic_csv.replace(element, "0" + int(element[0:])/1000)
        else:
            if element[0] != int():
                titanic_csv = titanic_csv.replace(element, (ord(element[0].lower())-96))
            else:
                titanic_csv = titanic_csv.replace(element, int(0) + int(element[0:])/1000)
    #création de deux tables différentes : une avec le Label "Survived" et une autre avec les données selectionnées si dessus
    titanic_label = titanic_csv.loc[:, titanic_csv.columns == "Survived"]
    titanic_data = titanic_csv.loc[:, titanic_csv.columns != 'Survived']   
    #affichage des tableaux ==> (pas forcement necessaire)

def modeltraining():
    global model, auccuracy
    #decoupage de la table avec le methode "train_test_split" de sklearn
    X_train, X_test, y_train, y_test= train_test_split(titanic_data.loc[:,titanic_data.columns != 'PassengerId'], titanic_label.loc[:,"Survived"], train_size=0.80, test_size=0.20)
    k = 3
    #entrainement de l'algorithme
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    #prediction de l'algorithme pour la table de test
    prediction = model.predict(X_test)
    #affichage des stats 
    print("*" * 50, "stats de prediction", "*" *50)
    print("longeur total de la table titanic_csv :", len(titanic_csv))
    print("Longeur de la table d'entrainement :", len(X_train), "("+str(round(100*(len(X_train)/len(titanic_csv))))+"%)")
    print("Longeur de la table de test :", len(X_test), "("+str(round(100*(len(X_test)/len(titanic_csv))))+"%)")
    print("Nombre d'exemples (k, voisins) utilisés :", k)
    auccuracy = round((accuracy_score(prediction, y_test)*100),2)
    print("Taux de prediction juste :",auccuracy,"%") #afiiche de le taux de prediction en pourcentage
    print("*" * 121) 

def Survivor_prediction():
    #Demande l'ID du passager
    PassengerId = (input("Id du passager : "))
    while not PassengerId.isnumeric():
        PassengerId = (input("Id du passager : "))
    #demande la Class du Passager
    PassengerPclass = (input("Pclass du passager : "))
    while not PassengerPclass.isnumeric():
        PassengerPclass = (input("Pclass du passager : "))
    #demande l'age du passager
    PassengerAge = (input("Age du passager : "))
    while not PassengerAge.isnumeric():
        PassengerAge = (input("Age du passager : "))
    #Demande le sexe du passager
    PassengerSex = input("Sexe du passager (male/female) : ")
    while not PassengerSex == "male" and not PassengerSex == "female":
        PassengerSex = input("Veuillez entrez une des options proposées (male/female) : ")
    #remplacement du sex renseigné
    if PassengerSex=="female" :
        PassengerSex=0
    else:
        PassengerSex=1
    #Demande la Cabin du Passager
    PassengerCabin = input("Entrez la cabine du passager : ")
    #transforme les infos Age et class en type int
    PassengerPclass = int(PassengerPclass) 
    PassengerAge = int(PassengerAge)
    #on crèe une DataFrame avec pandas qui sera exploitable 
    Data = { 'PassengerId' : [PassengerId], 'Pclass' : [PassengerPclass],'Sex' : [PassengerSex], 'Age' : [PassengerAge], 'Cabin' : [PassengerCabin]}
    PassengerDataFrame = pandas.DataFrame(data=Data)
    #changement des infos Cabin en nombre exploitable par sklearn
    for element in PassengerDataFrame['Cabin']:
        if len(element)>1:
            if element[0] != int():
                PassengerDataFrame = PassengerDataFrame.replace(element, (ord(element[0].lower())-96) + int(element[1:])/1000) #remplacement des lettres par des nombres
            else:
                PassengerDataFrame = PassengerDataFrame.replace(element, "0" + int(element[0:])/1000)
        else:
            if element[0] != int():
                PassengerDataFrame = PassengerDataFrame.replace(element, (ord(element[0].lower())-96))
            else:
                PassengerDataFrame = PassengerDataFrame.replace(element, int(0) + int(element[0:])/1000)
    #phase de prediction de la survie du passager
    survive_prediction = model.predict(PassengerDataFrame.loc[:,PassengerDataFrame.columns != 'PassengerId'])
    #Print le resultat
    print("*" * 50, "Prediction de survie", "*" *49)
    if survive_prediction==1:
        print(f"Le passager portant l'Id : {PassengerId} à potentiellement survécu.\nCe programme ayant un taux de prédiction a : {auccuracy} % il se peut qu'il y ait de petites erreurs")
    else:
        print(f"Le passager portant l'Id : {PassengerId} est potentiellement décédé lors du naufrage.\nCe programme ayant un taux de prédiction a : {auccuracy} % il se peut qu'il y ait de petites erreurs")
    print("*"*121)

read_titanic_data("Titanic.csv", ";")
modeltraining()
Survivor_prediction()