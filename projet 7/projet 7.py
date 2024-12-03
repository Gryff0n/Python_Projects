#on importe les modules dont on a besoin, ici, on a juste besoin du module random
import random



#La fonction start demande la liste de nombre a l'utilisateur et la transforme en liste compréhensible par le programme
def start() :                       
    global L
    while True :
        try :
            L=input("Veuillez entrer votre liste de nombre : (syntaxe : a, b, c,... votre liste ne doit pas contenir de doublons)\n>>>")    #On demande la liste a l'utilisateur en précisant la syntaxe a utiliser
            L=L.split(", ")                      #On transforme le str en liste avec cette commande
            L = list(map(int, L))                #Cette commande transforme la liste de str en liste de int, de cette manière le programme verra chaque élément comme un nombre
            menu() 
        except ValueError :
            print("Veuillez utiliser la syntaxe correcte.")     #protection de la fonction pour être sûr que l'utilisateur a entré une liste avec la bonne syntaxe
        


#la fonction menu sert de passerelle a toutes les opérations possible envers la liste
def menu() :
    m=""
    while m!=0 and m!=1 and m!=2 and m!=3 and m!=4 :
        #On demande tout d'abord ce que l'utilisateur souhaite faire      
        m=int(input("Que souhaitez-vous faire ?\n0 - Quitter le programme\n1 - Trier ma liste\n2 - Trouver un élément de ma liste\n3 - Informations de ma liste\n4 - Consulter ma liste\n>>>"))

        #On créé les ponts vers les différentes fonctions
        if m==0 :
            print("Votre choix : 0\n-----------------------\nFermeture du programme.\n-----------------------")     #le choix "0" ferme le programme
            exit()
        elif m==1 :
            print("Votre choix : 1")        #le choix "1" mène aux options de tri
            menu_tri()
        elif m==2 :
            print("Votre choix : 2")        #le choix "2" mène aux options de recherche
            menu_dicho()
        elif m==3 :
            print("Votre choix : 3")        #le choix "3" mène aux options d'analyse
            menu_infos()
        elif m==4 :                         
            print(L)                        #le choix "4" permet de consulter la liste actuelle
            menu()




#La fonction menu_tri sert de sous menu, qui s'occupe seulement des différentes possibilités de tris offertes a l'utilisateur
def menu_tri() :
    sub_menu=""
    while sub_menu!=0 and sub_menu!=1 and sub_menu!=2 and sub_menu!=3 :
        sub_menu=int(input("Bienvenue dans le menu de tri, quel tri souhaitez-vous effectuer ?\n0 - Retour au menu principal\n1 - Tri dans l'ordre croissant\n2 - Tri dans l'ordre décroissant\n3 - Tri aléatoire\n>>>"))

        if sub_menu==0 :            
            print("Vous avez choisi : 0\n-----------------------\nRetour au menu principal.\n-----------------------")       #on se base sur le même système de choix que le menu principal, le choix "0" permet de retourner au menu principal
            menu()
        elif sub_menu==1 :
            print("Vous avez choisi : 1\nTri dans l'ordre croissant")          #le choix "1" lance un tri de la liste dans l'ordre croissant
            procedure_tri(L)
            menu_tri()
        elif sub_menu==2 :
            print("Vous avez choisi : 2\nTri dans l'ordre décroissant")        #le choix "2" lance un tri de la liste dans l'ordre décroissant
            tri_decroissant(L)
            menu_tri()
        elif sub_menu==3 :
            print("Vous avez choisi : 3\nTri aléatoire")                       #le choix "3" lance un tri aléatoire de la liste
            random.shuffle(L)   #cette commande permet de réarranger la liste aléatoirement
            print(f"Voici votre liste triée aléatoirement :\n{L}")
            menu_tri()
    


#La fonction menu_dicho sert de sous menu qui s'occupe exclusivement des différentes possibilités de recherches offertes a l'utilisateur
def menu_dicho() :
    a=""
    while a!=0 and a!=1 and a!=2 :
        a=int(input("Quelle méthode de recherche voulez-vous ?\n0 - Retour au menu principal\n1 - Recherche séquentiel\n2 - Recherche dichotomique (méthode plus rapide pour les très longues listes, nécessite une liste triée dans l'ordre croissant)\n>>>"))

        if a==0 :
            print("Vous avez choisi : 0\n-----------------------\nRetour au menu principal.\n-----------------------")      #on se base une fois de plus sur le même système de choix que précédemment, le choix "0" permet toujours de retourner au menu principal
            menu()
        elif a==1 :
            print("Vous avez choisi : 1\n Recherche séquentiel")        #cette fois ci le choix "1" permet de mener une recherche séquentielle dans la liste
            x=input("quel est l'élément recherché ?\n>>>")
            while not x.isnumeric() :
                x=input("Veuillez rechercher un entier. quel est l'élément recherché ?\n>>>")
            recherche_sequentiel(L, x)
            menu_dicho()
        elif a==2 :
            print("Vous avez choisi : 2\n Recherche dichotomique")      #et le choix "2" permet de mener une recherche dichotomique dans la liste
            x=input("quel est l'élément recherché ?\n>>>")
            while not x.isnumeric() :
                x=input("Veuillez rechercher un entier. quel est l'élément recherché ?\n>>>")
            recherche_dicho(L, x)


#La fonction menu_infos sert de sous menu qui s'occupe uniquement des différentes possibilités d'informations offertes a l'utilisateur
def menu_infos() :
    b=""
    while b!=0 and b!=1 and b!=2 and b!=3 and b!=4 :
        b=int(input("Quelles informations souhaitez vous avoir sur votre liste ?\n0 - Retourner au menu principal\n1 - Longueur de ma liste\n2 - Minimum de ma liste\n3 - Maximum de ma liste\n4 - Moyenne de ma liste\n>>>"))

        if b==0 :
            print("Vous avez choisi : 0\n-----------------------\nRetour au menu principal.\n-----------------------")      #toujours le même principe de choix, le choix "0" ramène au menu principal
            menu()
        elif b==1 :
            print("Vous avez choisi : 1\nLongueur de ma liste")
            print("Il y a ",len(L)," éléments dans votre liste :)\n---------------------")      #le choix "1" donne a l'utilisateur la longueur de sa liste
            menu_infos()
        elif b==2:
            print("Vous avez choisi : 2\nMinimum de ma liste")                                  #le choix "2" donne a l'utilisateur la valeur minimum de sa liste
            mini = L[0]                 #on prend la première valeur comme minimum par défaut
            for element in L:
                if element <= mini:     #on le compare a chaque élément de la liste, a chaque fois qu'on trouve un nombre plus petit en cours de route, on le délégue comme minimum et on continue de parcourir la liste
                    mini = element
            print("Le minimum de votre liste est de :", mini,"\n---------------------")         
            menu_infos()
        elif b==3 :
            print("Vous avez choisi : 3\nMaximum de ma liste")                                  #le choix "3" donne a l'utilisateur la valeur maximum de sa liste
            maxi = L[0]                 #on prend la première valeur comme maximum par défaut
            for element in L:
                if element >= maxi:     #on le compare a chaque élément de la liste, a chaque fois qu'on trouve un nombre plus grand en cours de route, on le décalre comme maximum et on continue de parcourir la liste
                    maxi = element
            print("Le maximum de votre liste est de :", maxi,"\n---------------------")         
            menu_infos()
        elif b==4 :
            print("Vous avez choisi : 4\nMoyenne de ma liste")
            moyenne(L)




#La fontion recherche_dicho est la fonction qui sera appelé quand l'utilisateur prend le choix 2 dans le sous menu menu_dicho
def recherche_dicho(lt, x):

    while True :
        try :
            x=int(x)
            trouve=0
            deb=0
            fin=len(lt)
            while (trouve==0 and deb<=fin):
                m=(deb+fin)//2              #on définit le milieu de la liste
                if lt[m]==x:
                    trouve=1                                                                                #on regarde si la valeur du milieu est celle qu'on cherche
                    print ("l'élément que vous cherchez porte l'index : ", m,"\n---------------------")
                    menu_dicho()
                elif x>lt[m]:               #sinon on compare aux valeurs adjacentes et on adapte nos valeurs qui définissent le début et la fin de la zone de recherche
                    deb=m+1
                else :
                    fin=m-1
            if trouve==0 :
                print("Cet élément ne se trouve pas dans votre liste :(\n---------------------")
                menu_dicho()                                                                                                       #quelques lignes qui protègent la fonction au cas où la valeur recherché ne se trouve pas dans la liste
        except IndexError :
            print("Cet élément ne se trouve pas dans votre liste :(\n---------------------")
            menu_dicho()


#La fonction recherche_sequentiel est la fonction qui sera appelée quand l'utilisateur prend le choix 1 dans le sous menu menu_dicho
def recherche_sequentiel(lt, x) :
    x=int(x)
    trouve=0
    i=0                             #on compte a quel élément dans la liste on se trouve
    for elements in lt :
        if elements==x :               #on compare chaque élément de la liste a celui cherché 1 par 1 et on ajoute 1 a la variable i chaque fois qu'on avance dans la liste sans succès
            trouve=1
            print(f"L'élément {x} que vous cherchez possède l'index : ", i,"\n---------------------" )      #une fois l'élément trouvé, on peut se servir de la variable i pour connaitre sa position dans la liste
        else :
            i=i+1                                                       
    if trouve==0 :
        print("cet élément n'est pas dans votre liste :(\n---------------------")           #quelques lignes pour protéger la fonction si l'élément cherché n'est pas dans la liste
        menu_dicho()


#La fonction procedure_tri est la fonction appelé quand l'utilisateur décide de trier sa liste dans l'ordre croissant
def procedure_tri(L) :
    n=len(L)                #on définit la longueur de la liste
    i=0                     #on créé i
    while i<n :             
        j=i                 #on créé j
        while j<n :
            if L[j]<=L[i] :
                a=L[i]
                L[i]=L[j]       #on parcours la liste en comparant i a j, dès que j est plus grand, on les échange de place, on fini donc avec une liste rangée dans l'ordre croissant
                L[j]=a
                j=j+1
            else :
                j=j+1
        i=i+1
    print("Voici votre liste triée dans l'ordre croissant : ",L,"\n---------------------")


#La fonction tri_decroissant  est la fonction appelée quand l'utilisateur souhaite triée sa liste dans l'ordre décroissant
def tri_decroissant(L) :
    n=len(L)                    
    i=0
    while i<n :
        j=i
        while j<n :
            if L[j]>=L[i] :                 #Il s'agit globalement de la même fonction que la précédent, le seul changement est qu'on ait remplacé le signe "<" par un symbole ">"
                a=L[i]                              
                L[i]=L[j]
                L[j]=a
                j=j+1
            else :
                j=j+1
        i=i+1
    print("Voici votre liste triée dans l'ordre décroissant : ",L,"\n---------------------")

def moyenne(L) :
    i=len(L)
    a=0
    for elements in L :
        a=a+elements
    result=a/i
    print("La moyenne de votre liste est de : ", result,"\n---------------------")
    menu_infos()
start() #Et enfin la dernière commande du programme est en fait celle qui démarre tout en appelant la fonction "start()" qui va demander a l'utilisateur d'entrer sa liste