#! /bin/bash

latex presentation_proarm.tex
dvipdf presentation_proarm.dvi
libreoffice --impress presentation_proarm.pdf