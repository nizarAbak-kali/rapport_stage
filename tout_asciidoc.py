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
             proc = subprocess.Popen([,''],)
