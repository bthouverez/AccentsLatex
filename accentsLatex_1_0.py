#!/usr/bin/python3.5


## Bastien THOUVEREZ
## accentsLatex.py version 1.0
## 
## Transforme les caractères avec accents en accents de type Latex 
##
## Utilisation dans un terminal
## 	python accentsLatex_1_0.py <file1.tex> <file2.tex> ...
##
## Fonctionnalités:
##   - transforme les caractères avec accents en accents de type Latex
##	 - peut lire plusieurs fichiers
##   - sauvegarde l'ancien fichier dans old-<nom_fichier>	
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
	print("Usage : python accentsLatex.py <file.tex>")
else:
	# Pour chaque input utilisateur
	for i in range(len(sys.argv)-1):
		cpt = i+1
		# Ouvre le fichier en lecture
		with open(sys.argv[cpt], 'r') as inputFile:
			# Crée un fichier en écriture
			with open("out-"+sys.argv[cpt], 'w') as outputFile:
				while True:
					c = inputFile.read(1)
					outputFile.write(data[c] if c in data.keys() else c)
					if not c:
						break

		outputFile.close()
		inputFile.close()
		# swap les noms des deux fichiers, 
		# le fichier d'entrée contient la sortie
		# le fichier de travail fais une sauvegarde du contenu de départ
		os.rename(sys.argv[cpt], "old-"+sys.argv[cpt])
		os.rename("out-"+sys.argv[cpt], sys.argv[cpt])
		print(sys.argv[cpt], "has been modified\nOld content has been put in", "old-"+sys.argv[cpt])
