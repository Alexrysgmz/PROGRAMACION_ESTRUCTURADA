"""
pelicula={
    "Nombre":"",
    "Categoria":"",
    "Clasificacion":"",
    "Genero":"",
    "Idioma":""
}
"""

pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\tOprima cualquier tecla para continuar. ")

# Case 1
def crearPeliculas():    
    borrarPantalla()
    print("\n\t.:: Agregar peliculas ::.\n")

    pelicula.update({"Nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"Categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"Clasificacion":input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"Genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"Idioma":input("Ingresa el idioma: ").upper().strip()})

    print(f"\n\t\tLa operacion se realizo con exito")

# Case 2
def mostrarPeliculas():
    borrarPantalla()
    print(f"\n\t.:: Mostrar peliculas ::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}: {pelicula[i]}")
    else:
        print(f"No hay peliculas registradas en este momento...")

# Case 3
def borrarPeliculas():    
    borrarPantalla()
    print(f"\n\t.:: Borrar peliculas ::.\n")
    if len(pelicula)>0:
        resp=input(f"¿Deseas borrar o quitar la pelicula? (SI/NO): ").upper().strip()
        if resp=="SI":
            pelicula.clear()
    else:
        print(f"No hay peliculas registradas en este momento...")

# Case 4
def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print(f"\n\t.:: Agregar una caracteristicas de peliculas ::.")
    atributo=input(f"Ingrese el nombre de la nueva caracteristica: ").capitalize().strip()
    valor_atributo=input(f"Ingresa el valor de la nueva caracteristica que agregar: ").capitalize().strip()
    pelicula[atributo]=valor_atributo
    print(f"\n\t\tLa operacion se realizo con exito")

# Case 5
def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print(f"\n\t.:: Modificar una caracteristica de pelicula ::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}: {pelicula[i]}")
            resp=input(f"Deseas modificar este atributo? (SI/NO) ").upper().strip()
            if resp=="SI":
                pelicula.update({i:input(f"¿Cual es el nuevo atributo? ").upper().strip()})
                print(f"\n\t\tLa operacion se realizo con exito")
                espereTecla()
    else:
        print(f"No hay peliculas registradas en este momento... ")

#Case 6
def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print(f"\n\t.:: Borrar una caracteristica de pelicula ::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}: {pelicula[i]}")
        resp=input(f"¿Deseas eliminar alguna de las siguientes caracteristicas? (SI/NO) ").upper().strip()
        if resp=="SI":
            valor=input(f"¿Cual de las caracteristicas desea eliminar? ").capitalize().strip()
            pelicula.pop(valor)
        else:
            input(f"No se ha eliminado ninguna caracteristica. ")
    else:
        print(f"No hay peliculas registradas en este momento... ")


 