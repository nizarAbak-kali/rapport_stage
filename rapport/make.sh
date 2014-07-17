#!/bin/bash


./clean

pdflatex rapport_finale.tex

mupdf rapport_finale.pdf &

cat plan1 
