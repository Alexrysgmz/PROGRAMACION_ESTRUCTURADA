import mysql.connector
from mysql.connector import Error

reservaciones={}
nueva=[]

# Función para borrar pantalla.
def borrarPantalla():
    import os
    os.system('cls')

# Función para esperar tecla.
def espereTecla():
    input(f"\n🚀 ... Oprima ENTER para continuar ... 🚀 ")

# Función de conexion.
def conectar():
    try:
        conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_yourself_music"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None 

# Función para nuestro menu principal.
def menuPrincipal():
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    print(f"\n\t\t\t.:: Sistema de Gestión de Reservaciones ::. \n\n\t1. Agendar 📖\
          \n\t2. Mostrar 👀\n\t3. Buscar 🔎\n\t4. Salir 🛹")
    opcion=input(f"\n\t\t 🔢 Elige una opcion (1 - 4): ")

    return opcion

# Función para agregar reservaciones al sistema.
def crearReservacion():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
        print("\n\t\t\t\t.:: Agendar reservacion ::.\n")

        Nombre=input("Nombre del Artista/Banda: ")
        Genero=input("Genero Musical: ")
        Sala=input(f"\n🎷 ¿Cuál sala quieres reservar?\n\n\t1. 🟦 Azul\n\t2. 🟥 Roja\n\t3. 🟧 Naranja\n\t4. ⬜ Blanca\n\t")
        opciona = input(f"\t\t 🔢 Elige una opción (1 - 4): ")
        match opciona:
            case "1": ["🎷 Sala"] = "AZUL"; opciona=False
            case "2": ["🎷 Sala"] = "ROJA"; opciona=False
            case "3": ["🎷 Sala"] = "NARANJA"; opciona=False
            case "4": ["🎷 Sala"] = "BLANCA"; opciona=False
            case _: 
                borrarPantalla()
                print("\t❌ Opción inválida, vuelva a intentarlo.")
                espereTecla()
        Fecha=input("Fecha de la reservacion (Ejemplo: 21/07/25 7pm-9pm: )")
        cursor=conexionBD.cursor()

        sql="insert into reservaciones ( Nombre, Genero, Sala, Fecha ) values (%s, %s, %s, %s)"
        val=(Nombre, Genero, Sala, Fecha)
        print(f"{'ID':>10}{'Nombre':>15}{'Genero':>15}{'Sala':>15}{'Fecha':>15}")

        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")

# Función para mostrar las reservaciones del sistema.
def mostrarReservaciones():
    borrarPantalla()
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        sql="select * from reservaciones"
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("\n\t .:: Mostrar Películas ::.\n")
        if registros:
            print(f"\n\tMostrar las Peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Genero':<15}{'Sala':<15}{'Fecha':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print(f"-"*80)  
    else:
        print("\n\t .:: Esta reservacion no existe :/ ::. ") 

# Función para buscar las reservaciones del sistema.
def buscarReservaciones():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Ingrese nombre del artista: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from reservaciones where Nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"\n\tMostrar Artistas")
            print(f"{'ID':<10}{'Nombre':<15}{'Genero':<15}{'Sala':<15}{'Fecha':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print(f"-"*80)  
    else:
        print("\n\t .:: Esta reservacion no existe :/ ::. ")

# Función para borrar reservaciones.
def borrarReservaciones():
    borrarPantalla()
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    conexionBD=conectar()
    if conexionBD!=None:
        nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"\n\tMostrar Artistas")
            print(f"{'ID':<10}{'Nombre':<15}{'Genero':<15}{'Sala':<15}{'Fecha':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
                print(f"-"*80) 
                resp=input(f"¿Deseas borrar la reservacion {nombre}? (Si/No): " ).lower().strip()
                if resp=="si":
                    sql="delete from reservaciones where nombre=%s"
                    val=(nombre,)
                    cursor.execute(sql,val)
                    conexionBD.commit()
                    print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
        else:
            print("\n\t .:: Esta reservacion no existe :/ ::. ") 

# Funcion para modificar reservaciones.
def modificarReservaciones():
    borrarPantalla()
    print("\n\t\t\t\t.:: YOURSELF MUSIC STUDIO ::.")
    conexionBD=conectar()
    if conexionBD!=None:
        nombre1=input("Nombre del artista/banda: ").upper().strip()
        cursor=conexionBD.cursor()
        sql="select * from reservaciones where nombre=%s"
        val=(nombre1,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
          print(f"\n\tMostrar Reservaciones")
          print(f"{'ID':<10}{'Nombre':<15}{'Genero':<15}{'Sala':<15}{'Fecha':<15}")
          print(f"-"*80)
          for fila in registros:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80) 
            resp=input(f"¿Deseas modificar la pelicula {nombre1}? (Si/No): " ).lower().strip()
            if resp=="si":
                reservaciones.update({"Nombre":input("Nombre del artista/banda: ").upper().strip()})
                reservaciones.update({"Genero":input("Genero Musical: ").upper().strip()})
                reservaciones.update({"Sala":input("En que sala le gustaría reservar?: ").upper().strip()})
                reservaciones.update({"Fecha":input("Ingrese Fecha y hora (Ejemplo: 21/07/2025 7:00pm-9:00pm) : ").upper().strip()})
                sql="update reservaciones set Nombre=%s, Genero=%s, Sala=%s, Fecha=%s, where Nombre=%s"
                val=(reservaciones["Arstista/Banda"],reservaciones["Genero"],reservaciones["Sala"],reservaciones["Fecha"],nombre1)
                cursor.execute(sql,val)
                conexionBD.commit()
                print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
        else:
          print("\n\t .:: Esta reservacion no existe :/ ::. ")

