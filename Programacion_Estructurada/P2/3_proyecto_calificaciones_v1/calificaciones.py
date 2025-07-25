calificaciones={}
#Lista=[
#       ["Ruben"= ],
#       ["Andres"= ],
# ] 

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\tOprima cualquier tecla para continuar. ")

def menuPrincipal():
    print(f"\n\t\t\t.:: Sistemas de Gestion de Calificaciones ::. \n\t1. ➕Agregar\
          \n\t2. 📈Mostrar\n\t3. 📱Calcular Promedio\n\t4. 🔎Buscar \n\t5. 🛹Salir")
    opcion=input(f"\n\t\t Elige una opcion (1 - 5): ")
    return opcion

# Case 1
def agregarCalificaciones(lista):
    borrarPantalla()
    print(f"\n\t.:: Agregar Calificaciones ::.\n")
    nombre=input(f"\n\t🤓Nombre del alumno: ").upper().strip()

    calificaciones=[]

    for i in range (1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\n\tCalificacion #{i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print(f"\n\tIngresa una calificacion valida (0 - 10). ")
            except ValueError:
                print(f"\n\tIngresa un valor numerico. ")

    lista.append([nombre]+calificaciones) # Nombre no es una lista, entonces se "trasnforma" con [].
    print(f"\n\t\tAccion realizada con exito ")

# Case 2
def mostrarCalificaciones(lista):
    borrarPantalla()
    print(f"\n\t.:: Mostrar las Calificaciones👀 ::.\n")
    if len(lista)>0:
        print(f"{'Nombre':<15} {'Calif. 1':<10} {'Calif. 2':<10} {'Calif. 3':<10}")
        print("-"*60)
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("-"*60)
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print(f"\n\tNo hay calificaciones en el sistema. ")

# Case 3
def calcularPromedios(lista):
    borrarPantalla()
    print("Promedio de los alumnos")
    if len(lista)>0:
        print(f"{'Nombre':<15} {'Calif. 1':<10} {'Calif. 2':<10} {'Calif. 3':<10}")
        print("-"*60)
        promedioGrupal=0
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("-"*60)
        promedioGrupal=promedioGrupal/len(lista)
        print(f"El promedio del grupo es:{promedioGrupal:.2f}")
    else:
        print(f"\n\tNo hay calificaciones en el sistema. ")

# Case 4
def buscarCalificaciones(lista):
    borrarPantalla()
    print(f"\n\t🔎 .:: Buscar Calificaciones ::. 🔎\n")
    
