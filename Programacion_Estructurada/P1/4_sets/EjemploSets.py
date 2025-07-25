#Ejemplo: Crear un programa que solicite los email de los alumnos de la UTD, \n\t
# almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

import os
os.system('cls')

resp="si"
emails=[]
while resp=="si":
    emails.append(input("Introduzca su email: "))
    resp=input("Quiere agregar otro email?: ")

emails_set=set(emails)

