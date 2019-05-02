"""
	File:run2.py
	autor:edgarguamo
"""

from misvariables import *

#uso de condicional simple
nota = input("Ingrese la primera nota: ")
nota2 = input("Ingrese la segunda nota: ")

nota = int(nota)
nota2 = int(nota2)


if nota >= 18:
	print ("%s con la calificacón de %d" % (mensaje, nota))
else:
	print ("%s con la calificacón de %d" % (mensaje2, nota))

if nota2 >=18:
	print ("%s con la calificacón de %d" % (mensaje, nota2))
else:
	print ("%s con la calificación de %d" % (mensaje2, nota2))
