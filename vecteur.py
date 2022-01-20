#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE Vecteurs
#   ================================================
#
from os import system

# This is just to clear the screen. Only works on Windows ( on Unix should be clear instead of cls )

_ = system('cls')

# This is the real program

xAB =  int(input(' Entrez abscisse du vecteur AB; xAB = '))
print ("xAB = ", xAB)
yAB = int(input(' Entrez ordonnée du vecteur AB; yAB = '))
print ("yAB = ", yAB)

xCD =  int(input(' Entrez abscisse du vecteur CD; xCD = '))
print ("xCD = ", xCD)
yCD = int(input(' Entrez ordonnée du vecteur CD; yCD = ')) 
print ("yCD = ", yCD)

if xAB * yCD == xCD * yAB:
  print ("vrai")
else:
  print ("faux")
      
