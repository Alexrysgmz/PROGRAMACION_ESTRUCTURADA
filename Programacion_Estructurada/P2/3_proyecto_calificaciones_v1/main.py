import calificaciones

def main():

    datos = []

    opcion=True

    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menuPrincipal()

        match opcion:
            case "1":
                calificaciones.agregarCalificaciones(datos)
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrarCalificaciones(datos)
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcularPromedios(datos)
                calificaciones.espereTecla()
            case "4":
                opcion=False
                calificaciones.buscarCalificaciones(datos)
                calificaciones.espereTecla()
            case "5":
                opcion=False
                calificaciones.borrarPantalla()
                print(f"\n\tTerminaste la ejecucion del sistema... Gracias! ...")
            case _:
                calificaciones.borrarPantalla()
                print("\tOpcion invalida, vuelva a intentarlo.")
                calificaciones.espereTecla()
                opcion=True
main()

