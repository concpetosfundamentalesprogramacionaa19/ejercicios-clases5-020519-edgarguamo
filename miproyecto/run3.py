"""
	File:run3.py
	autor:edgarguamo

	"nota mayor o igual a 18: sobresaliente"
	nota mayor o igual a 16 y menor 
	a 18 muy buena
	nota mayor o igual a 13 y menor a 16 buena
	nota menor a 13: insuficiente
"""
from misvariables import *

#uso de condicional simple
nota = input("Ingrese la primera nota: ")

nota = int(nota)

if nota >= 18:
	print ("Usta esta aprobacon con %d, que es %s" % (nota, "Excelente"))
else: 
	if (nota >=16) and (nota<18):
		print ("Usta esta aprobacon con %d, que es %s" % (nota, "Muy Buena"))
	else: 
		if (nota >=13) and (nota<16):
			print ("Usta esta aprobacon con %d, que es %s" % (nota, "Buena"))
		else:
			print ("Usta esta reprobado con %d, que es %s" % (nota, "insuficiente"))

	

