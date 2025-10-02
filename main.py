"""
combat des montres par lars schougaard 406
"""
import random
import time

while True:
    nb_victoire_consecutive = 0
    victoire = 0
    defaite = 0
    nb_combat = 0
    vie = 20
    escaped = False
    monstre = True

    while True:
        force_monstre = random.randint(1, 12)
        if victoire > 0 and victoire % 3 == 0 and not escaped:
            escaped = False
            print("Vous tomber contre un boss.")
            force_monstre = random.randint(8, 12)
        print(f"vous tomber face a un adeversaire de difficulte :{force_monstre}")
        action = int(input("Que voulez-vous faire? \n 1-Combatre cet adversaire.\n 2-Contourner cet adversaire et "
                           "aller ouvrir une autre porte.(coute un point de vie) \n 3-Afficher les règles du jeu. "
                           "\n 4-quiter la partie \n Entrer votre choix: \n "))

        if action == 1:

            nb_combat += 1
            combat_status = False
            escaped = False
            if monstre == True:
                score_de1 = random.randint(1, 6)
                score_de2 = random.randint(1, 6)
                force_joueur = score_de1 + score_de2

            print(f"Lancer du premier dé : {score_de1}. \n")
            time.sleep(0.5)
            print(f"Lancer du deuxième dé : {score_de2}. \n")
            time.sleep(0.5)
            print(f"Votre attaque fait {force_joueur} de dégats. \n")
            time.sleep(0.5)
            print(f"Adversaire : {nb_combat}\n ")
            time.sleep(0.5)
            print(f"Force de l'adversaire : {force_monstre} \n")
            time.sleep(0.5)
            print(f"Niveau de vie de l'usager : {vie} \n")
            time.sleep(0.7)
            monstre = True

            if force_joueur > force_monstre:
                combat_status = True

            if combat_status:
                print(f"Dernier combat : victoire ")
                time.sleep(0.5)
                victoire += 1
                nb_victoire_consecutive += 1
                vie += force_monstre
                print(f"Niveau de vie : {vie}.")
                print(f"Nombre de victoire consecutive : {nb_victoire_consecutive}. \n ")
                print(f"Combat numéro {nb_combat} : {victoire} victoire(s) vs {defaite} défaite(s).\n")
                time.sleep(0.5)

            else:
                print(f"Dernier combat : defaite ")
                time.sleep(0.5)
                defaite += 1
                nb_victoire_consecutive = 0
                vie -= force_monstre
                print(f"Niveau de vie : {vie}.")
                print(f"Nombre de victoire consecutive : {nb_victoire_consecutive}. \n")
                print(f"Combat numéro {nb_combat} : {victoire} victoire(s) vs {defaite} défaite(s).\n")
                time.sleep(0.5)

        elif action == 2:
            escaped = True
            vie -= 1
            print(f" Vous contournée l'adversaire. \n Vous aver maintenant {vie} vie(s). \n ")
            time.sleep(0.7)

        elif action == 3:
            monstre = False
            print("Pour réussir un combat,il faut que la somme des deux dé lancé soit supérieure à la force de "
                  "l’adversaire.\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
                  "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de "
                  "l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
                  " \nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\n "
                  "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalite"
                  " de 1 point de vie. \n ")
            time.sleep(2)

        elif action == 4:
            print(" merci et aurevoire ... ")
            quit()

        if vie <= 0:
            print(f"La partie est terminé, vous avez vaincus {victoire} montre(s). \n ")
            rejouer = input("Vouler vous rejouer? Oui ou non.")

            if rejouer == "oui":
                break

            if rejouer == "non":
                print("Merci d'avoire jouer.")
                quit()
