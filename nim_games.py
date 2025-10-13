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
		name = input("Enter your name: ").strip()
		if name:
			return name
		print("Sorry, try again.")


