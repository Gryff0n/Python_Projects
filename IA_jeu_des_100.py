# coding: utf-8

import random
import time

# Zone de déclaration des variables
current_score = 0
turn = 0
tmp_score = 0
# Zone de déclération des fonctions


def core(current_score):
    stages = [4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100]
    next_stage = 0
    for i in range(0, len(stages)):
        if stages[i] > current_score:
            next_stage = stages[i]
            break
    tmp_score = next_stage - current_score
    if tmp_score <= 7:
        return tmp_score
    else:
        return random.randint(1, 7)

# Début du programme


print("""Bienvenu dans le jeu des 100 !
Le principe est simple. Vous devez entrer un nombre entre 1 et 7 qui va s'ajouter à un score global.
La partie commence à 0 et le premier joueur à atteindre 100 l'emporte !
Bien entendu, le score global est commun aux deux joueurs.
Saurez-vous user de stratégie pour battre la machine ?
""")

print("On détermine alétoirement qui commence...")
turn = random.randint(0, 1)
if turn == 0:
    print("Vous commencez !")
else:
    print("La machine commence !")

while current_score != 100:
    if turn % 2 == 0:
        while 1:
            tmp_score = input("Entrez un nombre > ")
            if str(tmp_score).isdigit():
                tmp_score = int(tmp_score)
                if int(tmp_score) >= 1 and int(tmp_score) <= 7:
                    break
                else:
                    print("INPUT_ERROR: La donnée saisie est incorrecte !")
            else:
                print("INPUT_ERROR: La donnée saisie est incorrecte !")
        current_score += tmp_score
        print("Score actuel :", current_score)
    else:
        tmp_score = core(current_score)
        time.sleep(0.5)
        print("\nLa machine a choisi", tmp_score)
        current_score += tmp_score
        print("Score actuel :", current_score)

    if current_score > 100:
        current_score = 0
        print("DOMMAGE ! VOUS AVEZ DÉPASSÉ 100 !")
        print("J'ai donc remis le score à 0 :)")
        print("Score actuel :", current_score)
    turn += 1

if turn % 2 == 1:
    print("Vous... Vous avez gagné ???")
    time.sleep(1.5)
    print("Comment avez-vous battu mon algorythme :(")
    time.sleep(2)
    print("Je suppose que je dois vous félicier...")
    time.sleep(4)
else:
    print("La machine a gagné !")
    time.sleep(1.5)
    print("Comme toujours :)")
    time.sleep(4)

