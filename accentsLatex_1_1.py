#!/usr/bin/python3.5


## Bastien THOUVEREZ
## accentsLatex.py version 1.1
## 
## Transforme les caractères avec accents en accents de type Latex 
##
## Utilisation dans un terminal
## 	python accentsLatex_1_1.py <file1.tex> <file2.tex> ...
##
## Fonctionnalités:
##   - transforme les caractères avec accents en accents de type Latex
##	 - peut lire plusieurs fichiers
##   - sauvegarde l'ancien fichier dans old-<nom_fichier>
##   - ne remplace pas dans les commentaires
##
## TODO
##

import sys
import os

data= {
	'à': '\`a',
	'é': "\\'e",
	'è': '\`e',
	'ë': '\\"e',
	'ê': '\^e',
	'ï': '\\"i',
	'î': '\^i',
	'ö': '\\"o',
	'ô': '\^o',
	'û': '\^u',
	'ù': '\`u',
	'ç': '\c c',
	'À': '\`A',
	'É': "\\'E"
}
if(len(sys.argv) == 1):
	print("Usage : python accentsLatex.py <file.tex> <file2.tex> ...")
	exit(1)

# Pour chaque input utilisateur
for ind_file in range(1, len(sys.argv)):
	# Ouvre le fichier en lecture
	with open(sys.argv[ind_file], 'r') as inputFile:
		# Crée un fichier en écriture
		with open("out-"+sys.argv[ind_file], 'w') as outputFile:
			line = inputFile.readline()
			while line != "":
				# Pour chaque ligne
				comment = False
				# Pour chaque caractère de la ligne
				for c in line:
					# Si pas dans un commentaire
					if not comment:
						# Vérifie si on entre en commentaire
						if c == "%":
							comment = True
					outputFile.write(data[c] if c in data.keys() and not comment else c)
				line = inputFile.readline()
			

	outputFile.close()
	inputFile.close()
	# swap les noms des deux fichiers, 
	# le fichier d'entrée contient la sortie
	# le fichier de travail fais une sauvegarde du contenu de départ
	os.rename(sys.argv[ind_file], "old-"+sys.argv[ind_file])
	os.rename("out-"+sys.argv[ind_file], sys.argv[ind_file])
	print(sys.argv[ind_file], "has been modified\nOld content has been put in", "old-"+sys.argv[ind_file])
