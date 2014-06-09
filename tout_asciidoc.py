#! /usr/bin/python

import glob 
import os.path 
# contient les fonctions systeme 
import sys
# permet d'utliser des sous processus 
import subprocess

# fonctions  qui va parcours un dossier , appliquer le asscidoc sur les fichier 
#et le faire de maniere recurssive 
def ascils (path):
    for root , dir , files in os.walk(path):
        #decoupage du nom du fichier courant de son chemin absolue
        filepath_root,filename_root = os.path.split(root)
        #boucle sur les fichier dans le dossier 
        #chaque fichier va se faire asciidoc 
        for i in files :
            nom_fichier_complet = root + i
            print "on traite le fichier :" + nom_fichier_complet 
            proc = subprocess.Popen([sys.executable,'~/./asciidoci ',nom_fichier_complet],stdout=subprocess.PIPE)

        for j in dir:
            print "on traite le fichier :" + nom_fichier_complet 
            ascils(j)


if __name__ == "__main__" :
    if len(sys.argv) > 1:
        print "pas le bon nombre d'argument"
        print "pas encore la fonctionnalite ... (-_-)' "
    else :
        path = "."
        ascils(path)
