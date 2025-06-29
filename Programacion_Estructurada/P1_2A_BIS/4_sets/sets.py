"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system('cls')


paises={"México","Brasil","España","Canada","Canada"}
print(paises)

varios={True,"UTD",33,3.14}
print(varios)

#Funciones u Operaciones
paises.add("Mexico")
print(paises)

paises.pop()
print(paises)

paises.remove("Mexico")

os.system('cls')
#Ejemplo: Crear un programa que solicite los email de los alumnos de la UTD, \n\t
# almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

c=input("Ingrese correo institucional: ")

correos=[c]
print(c)
