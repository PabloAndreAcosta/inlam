# Konstruera en modul, area, som innehåller funktioner för att beräkna areor av rektanglar, cirklar och trianglar. 

import math

def rektangel(b,h):
  area = b*h
  return area

def cirkel(r):
  area = math.pi * r**2 
  return area

def triangel(b,h):
  area = (b * h)/2
  return area

resultat =triangel(10,20)
print(resultat)

