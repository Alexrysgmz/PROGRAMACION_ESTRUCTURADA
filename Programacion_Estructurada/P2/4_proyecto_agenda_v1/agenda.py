#agenda={}

# contactos = {
#           "Ruben": {"6181234567","ruben@gmail.com"}
#           "Andres": {"6187654321","andres@gmail.com"}
#  }

# Borrar Pantalla
def borrarPantalla():
    import os
    os.system("cls")

# Espere tecla
def espereTecla():
    input("\n\t⏰ Oprima cualquier tecla para continuar. ")

# Menú principal mostrado en la terminal
def menuPrincipal():
    print(f"\n\t\t\t👥 .:: Sistemas de Gestion de Agenda de Contactos ::. 👥 \n\n\t  Agregar Contacto\n\t  Mostrar todos los contactos\n\t  Buscar contacto por nombre\n\t  Eliminar contactos\n\t  Modificar contactos\n\t  Salir\n\t")
    opcion=input(f"\t\t🔢 Elige una opcion (1 - 6): ")
    return opcion

# Funcion para agregar contactos en la agenda
def agregarContactos(agenda):
    borrarPantalla()
    print(f"\n\t👥 .:: Agregar Contactos ::. 👥\n")

    nombre=input(f"🎷 Nombre: ").upper().strip()

    if nombre in agenda:
        print(f"❌ Este contacto ya existe, intentelo de nuevo. ")
    else:
        tel=input(f"\n📱 Telefono: ").upper().strip()
        email=input(f"\n📨 E-mail: ").lower().strip()
        agenda[nombre]=[tel, email]
        print(f"\n✅ Accion realizada con exito. \n")

# Funcion para mostrar los contactos de la agenda
def mostrarContactos(agenda):
    borrarPantalla()
    print(f"\n\t👁  .:: Mostrar Contactos ::.  👁\n")

    if not agenda:
        print(f"❌ No hay contactos registrados en la agenda. ")
    else:
        print(f"{'Nombre':<15} {'# Telefono':<15} {'E-mail':<10}")
        print(f"-"*60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<10}")
        print(f"-"*60)

# Funcion para buscar contactos en la agenda
def buscarContactos(agenda):
    borrarPantalla()
    print(f"\n\t🔎  .:: Buscar Contactos ::.  🔎\n")

    if not agenda:
        print(f"❌ No hay contactos registrados en la agenda. ")
    else:
        nombre=input(f"🔎 Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'Nombre':<15} {'# Telefono':<15} {'E-mail':<10}")
            print(f"-"*60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<10}") # De esta manera puedes imprimir los valores de un usuario en una lista.
            print(f"-"*60)
        else:
            print(f"❌ Este contacto no existe. ")

# Funcion para eliminar contactos de la agenda
def eliminarContactos(agenda):
    borrarPantalla()
    print(f"\n\t❌ .:: Eliminar Contactos ::. ❌\n")

    contacto=input(f"👁  ¿Que contacto deseas eliminar? ").upper().strip()
    if contacto in agenda:
        print(f"\n🎷 Nombre: {contacto:<15}\n📱 Telefono: {agenda[contacto][0]:<15}\n📨 E-mail: {agenda[contacto][1]:<10}")
        resp=input(f"\n👁  ¿Deseas eliminar el contacto? (SI/NO) ").upper().strip()
        if resp=="SI":
            agenda.pop(contacto)
            print(f"\n✅ Operacion realizada con exito. ")
        else:
            print(f"\n❌ No se realizo ninguna accion, intente nuevamente. ")
    else:
        print(f"\n❌ No se ha detectado ningun contacto con ese nombre, intentelo de nuevo. ")

# Funcion para editar contactos de la agenda
def editarContactos(agenda):
    borrarPantalla()
    print(f"\n\t✍  .:: Modificar Contactos ::.  ✍\n")

    if not agenda:
        print(f"❌ No hay contactos registrados en la agenda. \n")
    else:
        nombre=input(f"✍  Nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print(f"\n🔎 Valores actuales: ")
            print(f"\n🎷 Nombre: {nombre:<15}\n📱 Telefono: {agenda[nombre][0]:<15}\n📨 E-mail: {agenda[nombre][1]:<10}")
            resp=input(f"\n👁  ¿Deseas modificar los valores? (SI/NO) ").upper().strip()
            if resp=="SI":
                tel=input(f"\n📱 Telefono: ").upper().strip()
                email=input(f"\n📨 E-mail: ").lower().strip()
                agenda[nombre]=[tel, email]
                print(f"\n✅ Accion realizada con exito. \n")
            else:
                print(f"\n❌ No se realizo ninguna accion, intente nuevamente. ")
        else:
            print(f"❌ Este contacto no existe. ")


