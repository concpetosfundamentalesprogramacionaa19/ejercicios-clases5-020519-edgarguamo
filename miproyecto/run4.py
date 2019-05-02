"""
	File:run4.py
	autor:edgarguamo

Deseamos obtener el costo de una carrera universitaria. El valor promedio 
de cada ciclo es de $1200, el valor promedio del seguro educativo 
es de $100 si la edad del estudiante es meno o igual a 20, caso contrario
sera de $150. Si el estudiante tiene una modalidad a distancia el número 
de ciclos a seguir es de 10, caso contrario deberá seguir 8 ciclos.
Obtener la proyección del costo de la carrera de un estudiante   
	
"""
# Mensaje de Bienvenida y petición de datos 
print ("Bienvenido al generador de costo por carrera de La UTPL")
modalidad = input ("Por favor ingrese la modalidad que seguirá\n")
edad = input ("A continuación ingrese la edad\n")
# Conversion de la variable
edad = int (edad)

# Operación a seguir si la modalidad es presencial
if (modalidad =="Presencial"):
	modulos = 8 * 1200
	if (edad <= 20):
		seguro = 100 * 8
	else:
		seguro = 150 * 8 
else:
# Operación a seguir si la modalidad es a distancia 
	if (modalidad == "Distancia"):
		modulos = 10 *1200
		if (edad <=20):
			seguro = 100 * 8
		else:
			seguro = 150 * 8 

# suma de los valores 
total_matricula = seguro + modulos
# Impresión del resultado 
print("El valor total a pagar por su carrera es de: ", total_matricula)
