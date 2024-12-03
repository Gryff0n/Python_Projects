# Créé par Nathan, Corentin, Elsa, le 25/09/2021 en Python 3.7

#on importe le module json car on utilise un fichier de type json, pour stocker et structurer nos données
import json

#Cette ligne va d'abord créer le fichier répertoire qui stockera toutes nos données
file = open("repertoire.json", "a")
file.close()


def menu():
    # Boucle qui se lance tout le temps, sans limite
    while True:
        # essaie et exception si la valeur choice n'est pas un chiffre le programme re-essaie
        try:
            choice = int(input("Que voulez-vous faire ?\n\n 0-Quitter le programme\n 1-Rechercher un contact\n 2-Ajouter un contact\n 3-Suprimer un contact\n\nVotre choix ? : "))
            #on créé une boucle qui se répete si choice non = 0.1.2
            if choice == 0:
                print("Votre choix est 0\nFermeture du programme")
                exit()
            elif choice == 1:
                print("Votre choix est 1\n")
                lecture()
            elif choice == 2:
                print("Votre choix est 2\n")
                ecriture()
            elif choice == 3:
                print("Votre choix est 3\n")
                delete()
            # Affiche ce message si le choix n'est pas compris entre 0, 1 et 2
            else:
                print("Entrez un bon choix parmi ceux ci-dessus")
        # Message en cas d'exeption si la valeur n'est pas numérique
        except ValueError:
            print("Le choix est incorect. Entrez un bon nombre")
        except KeyboardInterrupt :
            print("Arrêt forcé.")
            exit()



#Fonction de lecture
def lecture():
    #try pour protéger la fonction et pour un petit détail plus tard
    try:
        #je créé un dictionnaire vide dans lequel je place le contenu de "répertoire.json"
        contact= {}
        with open('repertoire.json','r') as file:
            contact=json.load(file)
            #j'affiche les clés du dictionnaires qui correspondent au nom des contacts
            print(f"Voici la liste de tous les nom disponible dans le répertoire : \n{list(contact.keys())}")
            #l'utilisateur rentre le nom dont il veut recupérer le numéro
            recherche = input("Quel nom souhaitez vous rechercher ?\nRespectez les majuscules : ")
            #j'affiche la clé et la valeur associé, donc le nom et le numéro du contact recherché
            print(f"le numéro de {recherche} est",contact[recherche])
    #que se passe t-il si le nom recherché n'est pas dans le dans le dictionnaire ?
    #une erreur se produit, je me sers de ça pour faire comme si tout
    #allait bien en utilisant un try/except KeyError avec un message a l'utilisateur
    except KeyError:
        print(f"{recherche} ne se trouve pas dans votre repertoire.")
        file.close()
        return()



#Fonction d'écriture
def ecriture():
# création d'un nouveau dictionnaire vide
    contact = {}
    #ouverture du fichier en tant que lecture
    with open("repertoire.json", "r") as file:
        contact = json.load(file)
    #demande au client le nom du nouveau contact
    nom_contact = input("entrez le nom de votre nouveau contact : ")
    # while not et isalpha(), boucle qui verifie une condition, ici la condition est si nom_contact ne comporte pas que des lettres.
    while not nom_contact.isalpha():
        nom_contact = input("Un nom ne comporte pas de chiffres ou de caractères spéciaux, entrez le nom de votre nouveau contact : ")
    assert nom_contact.isalpha(), "le nom du contact ne doit contenir que des lettres"
    #utilisation du formatage de chaînes de caractères : f-string pour implémenter des arguments dans un type input()
    numero_contact = input(f"Entrez le numero de {nom_contact} : ")
    while not numero_contact.isnumeric():
        numero_contact = input(f"Un numéro ne comporte pas de lettres ou caractères spéciaux Entrez le numero de {nom_contact} : ")
    assert numero_contact.isnumeric(), "Le numero du contact ne doit contenir que des chiffres"
    #ajoute dans le dictionnaire nom_contact(clé) et numero_contact sa valeur
    contact[nom_contact] = numero_contact
    print(contact)
    #Ouvre le fichier en lecture + écriture et ajoute les donneés stockées dans {contact}
    with open("repertoire.json", "r+") as file:
        #écriture, dump() car il s'agit d'un fichier Json
        json.dump(contact, file)
        file.close()
        print(f"Le contact {nom_contact} avec le numero {numero_contact} a été ajouté avec succès dans le répertoire")
    #choix pour retourner au menu ou continuer d'ajouter de nouveaux contacts
    while True:
        try:
            continue_choice = int(input("Voulez vous continuer d'ajouter des contacts\n1-Ajoutez de nouveau un contact\n0-Retour au menu principal"))
            if continue_choice == 1:
                ecriture()
            if continue_choice == 0:
                menu()
        except ValueError:
            print("Choix incorect, Veuillez entrer un bon choix")


#Fonction de suppression
def delete():
    #je créé un dictionnaire vide que je rempli avec le contenu de "repertoire.json"
    contact={}
    with open("repertoire.json", "r+") as file:
            contact=json.load(file)
            #while true et try/except pour gérer les erreurs et relancer la fonction en cas d'erreur
            while True:
                try :
                    #affichage des noms dans le dictionnaire de contact
                    print(list(contact.keys()))
                    #on demande a l'utilisateur qui il veut supprimer de la liste
                    ct_del=input("Quel contact voulez vous supprimer ?\n0 pour annuler\nVotre choix : ")
                    if ct_del =="0":
                        file.close()
                        menu()
                    #on met la valeur associé au nom (qui correspond au numero de telephone) dans une variable spécifique
                    ct_num=contact[ct_del]
                    #petit message de confirmation au cas ou...
                    confirm = int(input(f"Voulez vous supprimez {ct_del} ayant le numero {ct_num} ?\n 1 pour confirmer\n 0 pour annuler\nVotre choix : "))
                    if confirm == 0:
                        print("suppression annulée.")
                        file.close()
                        menu()
                    elif confirm == 1:
                        #la commande de suppresion
                        del contact[ct_del]
                        #modification du fichier repertoire.json pour le mettre a jour apres la suppression du contact
                        with open ("repertoire.json", "w+") as file:
                            json.dump(contact, file)
                            file.close()
                            #message de validation et retour a la fonction menu
                            print("Suppresion effectuée.")
                            menu()
                    #si la valeur entré dans le message de confirmaton est invalide, ce message ci dessous s'affichera et réaffiche le message de confirmation
                    else :
                        confirm=input(f"choix invalide, chosissez parmi les options ci-dessous.\n voulez vous supprimez {ct_del} ayant le numero {ct_num} ?\n 1 pour confirmer\n 0 pour annuler :")
                #des except en tout genre pour protéger le programme
                except ValueError:
                    print ("choix incorrect, choisissez parmi les choix disponibles.")
                except KeyError :
                    print ("Le contact n'existe pas.")
                #si dans une fenêtre input l'utilisateur clique "annuler", le message "opération annulé" s'affiche et l'on retourne a la fonction menu.
                except KeyboardInterrupt :
                    print ("Opération annulée")
                    file.close()
                    menu()



#Execution la fonction menu
menu()