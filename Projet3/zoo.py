import csv

with open('zoo.csv', 'r', newline='') as csvfile:
    tableReader = csv.reader(csvfile, delimiter=';')
    tableReader.__next__()
    for row in tableReader:
        print(' - '.join(row))

# CONSIGNE : remplacer pass par les instructions attendues
# Les assertions vérifient certains résultats au fur et à mesure

# Une fonction qui peut servir
def affiche(table):
    """Fonction qui affiche les éléments d'une table, un élément par ligne,
    quelle que soit le type de cet élément"""
    for element in table:
        print(element)
    print()    # permet de séparer un peu les affichages


# I) a) Importation de la table et affichage
# écrire le code donné dans l'énoncé

csv_tuple=[]
with open('zoo.csv', 'r', newline='') as csvfile:
    tableReader = csv.reader(csvfile, delimiter=';')
    tableReader.__next__()
    for row in tableReader:
        x=row[0],row[1]
        csv_tuple.append(x)
    print(csv_tuple)

# I) b) Importation de la table et affectation d'une variable
def csv_tuple(nom_fichier):
    """Fonction qui importe un fichier csv sous la forme d'une liste de
    tuples en sautant la ligne d'entêtes"""
    zoo = []
    with open(nom_fichier, 'r', newline='') as csvfile:
        tableReader = csv.reader(csvfile, delimiter=';')
        tableReader.__next__()
        for row in tableReader:
            zoo.append((row[0], row[1]))
    return zoo
zoo = csv_tuple('zoo.csv')
assert zoo==[('mammifère', 'Lion'),
             ('mammifère', 'Kangourou'),
             ('mammifère', 'Panda'),
             ('poisson', 'Raie'),
             ('mammifère', 'Gorille'),
             ('mammifère', 'Girafe'),
             ('poisson', 'Requin'),
             ('oiseau', 'Perroquet'),
             ('mammifère', 'Girafe'),
             ('oiseau', 'Autruche'),
             ('mammifère', 'Panda'),
             ('reptile', 'Lézard'),
             ('amphibien', 'Crapaud')
             ]
affiche(zoo)

# II) a) Ajout d'un panda
zoo.append((('mammifère','Panda')))
print('On ajoute un panda')
assert zoo==[('mammifère', 'Lion'),
             ('mammifère', 'Kangourou'),
             ('mammifère', 'Panda'),
             ('poisson', 'Raie'),
             ('mammifère', 'Gorille'),
             ('mammifère', 'Girafe'),
             ('poisson', 'Requin'),
             ('oiseau', 'Perroquet'),
             ('mammifère', 'Girafe'),
             ('oiseau', 'Autruche'),
             ('mammifère', 'Panda'),
             ('reptile', 'Lézard'),
             ('amphibien', 'Crapaud'),
             ('mammifère','Panda')
             ]
affiche(zoo)


# II) b) Détection de doublons

def detecte_doublons(table):
    """Fonction qui renvoie True si au moins un doublon est détecté"""
    check_doublons = table #liste orginale
    b = set(check_doublons) #set suprimme tous les element en doublons dans une liste
    if len(check_doublons) != len(b): #si les deux liste on une longueur different, il y a des doublons
        return True
    else:
        return False
detecte_doublons(zoo)
assert detecte_doublons(zoo)
assert not detecte_doublons([('mammifère', 'Lion'),
                               ('poisson', 'Perche'),
                               ('mammifère', 'Panda')
                               ])


# II) c) Suppression de doublons
def supprime_doublons(table):
    """Fonction qui supprime les doublons d'une table"""
    for i in range(len(table)-1):
        for j in range(i+1,len(table)-1):
            if table[i]==table[j]:
                del table[j]
    return table

    #on obtien une liste sans doublons

supprime_doublons(zoo)
assert not detecte_doublons(zoo)
affiche(zoo)


# III) a) Importation de la table (listes) et affectation d'une variable

def csv_liste(nomFichier):
    """Fonction qui importe un fichier csv sous la forme d'une liste de
    listes en sautant la ligne d'entêtes"""
    zoo = []
    with open(nomFichier, 'r', newline='') as csvfile:
        tableReader = csv.reader(csvfile, delimiter=';')
        tableReader.__next__()
        for row in tableReader: #Pour tout élément dans TableReader
            zoo.append([row[0], row[1]]) #Ajout de Liste avec les element
    return zoo
zoo = csv_liste('zoo.csv')
print("res en liste : " ) #print du résultat obtenue
assert zoo==[['mammifère', 'Lion'],
             ['mammifère', 'Kangourou'],
             ['mammifère', 'Panda'],
             ['poisson', 'Raie'],
             ['mammifère', 'Gorille'],
             ['mammifère', 'Girafe'],
             ['poisson', 'Requin'],
             ['oiseau', 'Perroquet'],
             ['mammifère', 'Girafe'],
             ['oiseau', 'Autruche'],
             ['mammifère', 'Panda'],
             ['reptile', 'Lézard'],
             ['amphibien', 'Crapaud']
             ]
affiche(zoo)


# III) b) Nommage des animaux

def ajout_nom(table):
    """Fonction qui demande et ajoute 0un nom à chaque élément de la table"""
    position = 0
    for elem in table: #Pour tout element dans la table
            nom_animal = input(f"Quel est le nom de l'animal {elem} : ") #demande a l'utilisateur un nom
            table[position].append(nom_animal) #ajout du nom dans la table
            position = position+1 #change l'index de la table pour nommer chaque animal
ajout_nom(zoo)
affiche(zoo)


# IV) Tri de la table suivant un champ

def tri_table(table,i):
    """Fonction qui tri la table en fonction du champ d'indice i"""
    original_table = table #copie de la table
    def getIndice(elem):
        return elem[i]
    original_table.sort(key=getIndice)#Tri de la table en fonction de l'indice i
    return original_table #return la table trié

zoo = tri_table(zoo,int(input("Quelle est vorte critère\n 1.type\n2.espèce\n3.nom"))-1)
affiche(zoo)
