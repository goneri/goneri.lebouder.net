+++
title = "addimage.py"
date = 2005-06-26T05:22:00+00:00
+++

Jusque a présent, pour ajouter des photos sur mon blog, je n'ai qu'a appeller le fichier avec un script Perl qui se charge de l'uploader proprement sur le serveur.

Suite au prosélitisme de [Dukez](http://glibersat.linux62.org/), j'ai fini par vouloir tester le language [Python](http://www.python.org/), c'est ainsi que j'ai refais mon script dans ce language. Le script [addimage.py](addimage.py) est l'oeuvre d'un debutant, j'implore votre indulgence fasse a la qualité du code :|.

Le script se charge de généré une image miniature si l'on upload une image et qu'elle est superieur a une certaine taille. Il place les fichiers dans un dossier qui créé en fonction de la date. Par exemple 19810611 pour le 11 Juin 1981. Enfin, a la fin du processus, il affiche le code html qui ne reste plus qu'a copier-coller.