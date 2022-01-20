#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE 5
#   ================================================
#

xAB = input(' Entrez abscisse du vecteur AB; xAB = ')
print ("xAB = ", xAB)
yAB = input(' Entrez ordonnée du vecteur AB; yAB = ')
print ("yAB = ", yAB)

xCD = input(' Entrez abscisse du vecteur CD; xCD = ')
print ("xCD = ", xCD)
yCD = input(' Entrez ordonnée du vecteur CD; yCD = ')
print ("yCD = ", yCD)

if xAB * yCD == xCD * yAB:
  print ("vrai")
else:
  print ("faux")
      
