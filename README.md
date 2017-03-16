# AccentsLatex
Conversion des caractères spécifiques à la langue française en code pour LaTeX

Un codage propre des caractères accentués dans un document LaTeX nécessite de diviser l'écriture du caractère en spécifiant l'accent à placer, puis le caractère sur lequel placer l'accent.

Par exemple, le mot "écolière" devrait être écrit "\'ecoli\`ere" en LaTeX.

### But du projet
AccentsLatex se résume à un script Python qui permet de convertir les caractères accentués en code pour LaTeX.
Il est alors possible d'écrire librement du texte sans se soucier des accents, puis donner le fichier.tex à manger au script Python. Ainsi le fichier.tex verra ses caractères accentués convertis et le contenu de départ est sauvegardé dans un fichier-old.tex.

### Mises à jour
Version 1.1:
* Ne tient plus compte des caractères des commentaires

Version 1.0:
* Modifie les caractères accentués les plus courants de la langue française
* Possibilité de donner plusieurs fichiers à lire au script
