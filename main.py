"""
combat des montres par lars schougaard 406
"""
import random

vie = 20



while True:
    nb_victoire_consecutive = 0
    victoire = 0
    defaite = 0
    nb_combat = 0
    force_monstre = random.randint(1, 5)
    print(f"vous tomber face a un adeversaire de difficulte :{force_monstre}")
    action = int(input("Que voulez-vous faire? \n 1-Combatre cet adversaire.\n 2-Contourner cet adversaire et aller ouvrir une autre porte.(coute un point de vie) \n 3-Afficher les règles du jeu. \n 4-quiter la partie \n Entrer votre choix:"))

    if action == 1 :
        nb_combat += 1
        combat_status = False
        score_de = random.randint(2, 12)
        print(f"Adversaire : ")
        print(f"Force de l'adversaire : {force_monstre}")
        print(f"Niveau de vie de l'usager : {vie}")
        print(f"Combat numéro {nb_combat} : {victoire} vs {defaite}.")
        print(f"Lancer du dé : {score_de}.")
        if score_de > force_monstre :
            combat_status = True

        if combat_status == True:
            print(f"Dernier combat : victoire ")
            victoire += 1
            nb_victoire_consecutive += 1
            vie += force_monstre
            print(f"Niveau de vie : {vie}.")
            print(f"Nombre de victoire consecutive : {nb_victoire_consecutive}.")

        elif combat_status == False :
            print(f"Dernier combat : defaite ")
            defaite += 1
            nb_victoire_consecutive = 0
            vie -= force_monstre
            print(f"Niveau de vie : {vie}.")
            print(f"Nombre de victoire consecutive : {nb_victoire_consecutive}.")

            if vie <= 0 :
                print(f"La partie est terminé, vous avez vaincus {victoire} montre(s).")
                break

    if action == 2 :
        break

    if action == 3 :
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
        print("Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        print("La partie se termine lorsque les points de vie de l’usager tombent sous 0.")
        print("L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

    if action == 4 :
        print(" merci et aurevoire ... ")
        break



