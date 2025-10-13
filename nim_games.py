#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""

init_match = 21
min_removed_pil = 1
max_removed_pil = 4


def name_of_player(player):
	while True:
		name = input("Entrez votre nom: ").strip()
		if name:
			return name
		print("Invalide. Recommencez.")


def choice_name(p1, p2):
	while True:
		choice = input(f"Qui commence ? ({p1}/{p2}) : ")
		if choice == p1:
			return p1
		elif choice == p2:
			return p2
		print(f"Invalide. Entrer exactement '{p1}' ou '{p2}'.")


def start_match(player, pile):
	while True:
		try:
			k = int(input(
				f"{player}, il reste {pile} allumettes. Combien enlevez-vous ({min_removed_pil}-{max_removed_pil}): ) ? "))
		except ValueError:
			print("Entrez un entier.")
			continue
		if k < min_removed_pil or k > max_removed_pil:
			print(f"Choix invalide, entrez un nombre entre {min_removed_pil} et {max_removed_pil}.")
			continue
		if k > pile:
			print(f"Il reste que {pile} d'allumettes!")
			continue
	return k

