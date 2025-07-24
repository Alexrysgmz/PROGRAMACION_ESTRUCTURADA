import reservaciones

def main():
    datos = []
    opcion = True

    while opcion:
        reservaciones.borrarPantalla()
        opcion = reservaciones.menuPrincipal()

        match opcion:
            case "1":
                reservaciones.crearReservacion()
                reservaciones.espereTecla()
            case "2":
                reservaciones.mostrarReservaciones()
                reservaciones.espereTecla()
            case "3":
                reservaciones.buscarReservaciones()
                reservaciones.espereTecla()
            case "4":
                reservaciones.modificarReservaciones()
                reservaciones.espereTecla()
            case "5":
                reservaciones.borrarReservaciones()
                reservaciones.espereTecla()
            case "6":
                opcion = False
                reservaciones.borrarPantalla()
                print(f"\n\tTerminaste la ejecución del sistema... ¡Gracias!")
            case _:
                reservaciones.borrarPantalla()
                print("\tOpción inválida, vuelva a intentarlo.")
                reservaciones.espereTecla()

main()



