#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""

init_pile = 21
min_removed_pil = 1
max_removed_pil = 4


def name_of_player(player):
	"""Demande le nom d'un joueur."""
	while True:
		name = input(player).strip()
		if name:
			return name
		print("Invalide. Recommencez.")


def choice_player(p1, p2):
	"""Demande quel joueur commence (p1 ou p2).
	 	Renvoie le nom choisi."""
	player = f"Qui commence ? ({p1}/{p2}) : "
	while True:
		choice = input(player).strip()
		if choice == p1:
			return p1
		if choice == p2:
			return p2
		print(f"Invalide. Entrer exactement '{p1}' ou '{p2}'.")


def start_match(player, pile):
	"""Demande au joueur combien d'allumettes, il retire (1..4) et valide la valeur."""

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


def main():
	p1 = name_of_player("Nom du joueur 1 :")
	p2 = name_of_player("Nom du joueur 2 :")
	current_match = choice_player(p1, p2)

	pile = init_pile
	# boucle principale du jeu
	while pile > 0:
		k = start_match(current_match, pile)
		pile -= k
		# si on vient de prendre la dernière allumette,
		# le joueur qui a pris (perd)
		if pile == 0:
			print(f"{current_match} a pris la dernière allumette et a PERDU.")

			# l'autre joueur gagne
			winner = p1 if current_match == p2 else p2
			print(f"{winner} est le gagnant !")
			break
		# changer de joueur
		if current_match == p2:
			current_match = p1
		else:
			current_match = p1


if __name__ == "__main__":
	main()
