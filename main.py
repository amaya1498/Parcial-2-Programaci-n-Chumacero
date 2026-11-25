from alumnos import (
    buscar_alumno,
    cargar_alumno,
    eliminar_alumno,
    listar_alumnos,
    modificar_alumno,
)
from archivos import cargar_alumnos
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print() 
    print("GESTIÓN DE ALUMNOS")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadísticas")
    print("7. Salir")


def ejecutar_opcion(opcion, alumnos):
    match opcion:
        case "1":
            alumnos = cargar_alumno(alumnos)
        case "2":
            listar_alumnos(alumnos)
        case "3":
            buscar_alumno(alumnos)
        case "4":
            modificar_alumno(alumnos)
        case "5":
            eliminar_alumno(alumnos)
        case "6":
            mostrar_estadisticas(alumnos)
        case "7":
            print("Saliendo del programa...")
        case _:
            print("Opción no válida. Intente de nuevo.")
    return alumnos


def main():
    alumnos = cargar_alumnos()
    opcion = ""

    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        alumnos = ejecutar_opcion(opcion, alumnos)


main()
