#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim – variante simple (et base pour Marienbad)

Ce programme arbitre une partie du jeu de Nim entre deux joueurs humains
ou entre un joueur humain et l'ordinateur (IA).

Règles :
- On part de 21 allumettes.
- Chaque joueur enlève entre 1 et 4 allumettes.
- Celui qui prend la dernière allumette perd.
- En mode IA, l'ordinateur applique une stratégie gagnante simple :
  - Si possible, il retire un nombre d’allumettes qui ramène le total
    à un multiple de 5 (21, 16, 11, 6, 1).
"""

import os
import random
import time
from colorama import init
from termcolor import colored

# Initialisation des constantes du jeu
init_pile = 21          # Nombre d’allumettes au départ
min_removed_pil = 1     # Minimum d’allumettes qu’un joueur peut retirer
max_removed_pil = 4     # Maximum d’allumettes qu’un joueur peut retirer


def name_of_player(player):
    """
    Demande et valide le nom d’un joueur.

    Args:
        player (str): Message d’invite affiché à l’utilisateur.

    Returns:
        str: Nom du joueur saisi et validé.
    """
    while True:
        name = input(player).strip()
        if name:
            return name
        print("Invalide. Recommencez.")


def choice_player(p1, p2):
    """
    Demande quel joueur commence la partie.

    Args:
        p1 (str): Nom du joueur 1.
        p2 (str): Nom du joueur 2.

    Returns:
        str: Nom du joueur qui commence.
    """
    msg = f"Qui commence ? ({p1}/{p2}) : "
    while True:
        choice = input(msg).strip().upper()
        if choice == p1:
            return p1
        if choice == p2:
            return p2
        print(f"Invalide. Entrez exactement '{p1}' ou '{p2}'.")


def start_match(player, pile):
    """
    Demande combien d’allumettes un joueur retire et vérifie la validité.

    Args:
        player (str): Nom du joueur qui joue.
        pile (int): Nombre d’allumettes restantes.

    Returns:
        int: Nombre d’allumettes à retirer.
    """
    while True:
        try:
            k = int(input(
                f"{player}, il reste {pile} allumettes. "
                f"Combien enlevez-vous ({min_removed_pil}-{max_removed_pil}) ? "
            ))
        except ValueError:
            print("Erreur : entrez un entier valide.")
            continue
        # Vérification des bornes et cohérence du choix
        if k < min_removed_pil or k > max_removed_pil:
            print(f"Choix invalide : entre {min_removed_pil} et {max_removed_pil}.")
            continue
        if k > pile:
            print(f"Il ne reste que {pile} allumette(s) !")
            continue
        return k


def switch_player(current, p1, p2):
    """
    Renvoie le joueur suivant.

    Args:
        current (str): Joueur actuel.
        p1 (str): Joueur 1.
        p2 (str): Joueur 2.

    Returns:
        str: Le joueur qui joue au prochain tour.
    """
    return p2 if current == p1 else p1


def computer_move(pile):
    """
    Calcule le nombre d’allumettes à retirer pour l’IA.

    Stratégie : si possible, laisser un multiple de 5 à l’adversaire.

    Args:
        pile (int): Nombre d’allumettes restantes.

    Returns:
        int: Nombre d’allumettes retirées par l’IA.
    """
    remainder = pile % 5
    if remainder == 0:
        # Aucun multiple de 5 possible → choix aléatoire
        return random.randint(min_removed_pil, max_removed_pil)
    else:
        return remainder


def clear_screen():
    """
    Efface le contenu de la console pour un affichage fluide et propre.
    Compatible Windows (cls) et Linux/Mac (clear).
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_matches(pile, removed=0):
    """
    Affiche les allumettes restantes, avec effet visuel.

    Args:
        pile (int): Nombre d’allumettes restantes.
        removed (int): Nombre d’allumettes retirées au dernier tour (pour animation).
    """
    clear_screen()
    print("\nPile d'allumettes :\n")

    # Animation : les allumettes disparaissent une par une
    if removed > 0:
        for step in range(removed):
            print("|" * (pile + removed - step))
            time.sleep(0.15)
            print("\nPile d'allumettes :\n")

    # Affichage final
    print("\n" + "|" * pile)
    print(f"({pile} allumette{'s' if pile > 1 else ''} restantes)\n")


def prGreen(s):
    """Affiche un texte coloré en vert (utilise le module colorama)."""
    print("\033[92m {}\033[00m".format(s))


def main():
    """
    Fonction principale : gère le déroulement complet d’une partie.
    """
    mode = input("Choisissez le mode (1 : 2 joueurs, 2 : contre l'IA) : ").strip().upper()

    # Initialisation des joueurs
    p1 = name_of_player("Nom du joueur 1 : ")
    p2 = "IA" if mode == "2" else name_of_player("Nom du joueur 2 : ")

    current_match = choice_player(p1, p2)
    pile = init_pile

    # Boucle principale : la partie continue tant qu’il reste des allumettes
    while pile > 0:
        if current_match == "IA":
            time.sleep(1)
            k = computer_move(pile)
            print(f"L'IA retire {k} allumette(s).")
        else:
            k = start_match(current_match, pile)

        pile -= k
        show_matches(pile)

        # Vérifie si la partie est terminée
        if pile == 0:
            print(f"{current_match} a pris la dernière allumette et a PERDU.")
            text_colored = colored(f"{switch_player(current_match, p1, p2)} GAGNE !")
            prGreen(text_colored)
            break

        # Changement de joueur
        current_match = switch_player(current_match, p1, p2)
        print(f"\nIl reste {pile} allumettes. À {current_match} de jouer !\n")


# Point d’entrée du programme
if __name__ == "__main__":
    main()
