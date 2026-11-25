from archivos import guardar_alumnos
from validaciones import (
    dni_existe,
    edad_valida,
    es_entero_valido,
    es_numero_valido,
    nota_valida,
)


def buscar_indice_alumno(alumnos, dni):
    for i in range(len(alumnos)):
        if alumnos[i]["dni"] == dni:
            return i
    return -1


def crear_alumno(dni, nombre, apellido, edad, nota):
    alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota,
    }
    return alumno


def mostrar_un_alumno(alumno):
    print("DNI:", alumno["dni"])
    print("Nombre:", alumno["nombre"])
    print("Apellido:", alumno["apellido"])
    print("Edad:", alumno["edad"])
    print("Nota:", alumno["nota"])


def pedir_edad_valida(mensaje, permitir_vacio):
    texto = input(mensaje)

    if permitir_vacio and texto == "":
        return True, None

    if not es_entero_valido(texto):
        print("La edad debe ser un número entero válido.")
        return False, None

    edad = int(texto)
    if not edad_valida(edad):
        print("La edad no puede ser negativa.")
        return False, None

    return True, edad


def pedir_nota_valida(mensaje, permitir_vacio):
    texto = input(mensaje)

    if permitir_vacio and texto == "":
        return True, None

    if not es_numero_valido(texto):
        print("La nota debe ser un número válido.")
        return False, None

    nota = float(texto)
    if not nota_valida(nota):
        print("La nota debe estar entre 0 y 10.")
        return False, None

    return True, nota


def cargar_alumno(alumnos):
    print()
    print("CARGAR ALUMNO")
    dni = input("DNI: ")

    if dni == "":
        print("El DNI no puede estar vacío.")
        return alumnos

    if dni_existe(alumnos, dni):
        print("Ya existe un alumno con ese DNI.")
        return alumnos

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    if nombre == "" or apellido == "":
        print("Nombre y apellido son obligatorios.")
        return alumnos

    ok_edad, edad = pedir_edad_valida("Edad: ", False)
    if not ok_edad:
        return alumnos

    ok_nota, nota = pedir_nota_valida(
        "Nota final (0 a 10, usar punto si tiene decimales): ", False
    )
    if not ok_nota:
        return alumnos

    nuevo = crear_alumno(dni, nombre, apellido, edad, nota)
    alumnos = alumnos + [nuevo]
    guardar_alumnos(alumnos)
    print("Alumno cargado con éxito.")
    return alumnos


def listar_alumnos(alumnos):
    print()
    print("LISTADO DE ALUMNOS")
    if len(alumnos) == 0:
        print("No hay alumnos cargados.")
        return

    for alumno in alumnos:
        mostrar_un_alumno(alumno)
        print("-" * 20)


def buscar_alumno(alumnos):
    print()
    print("BUSCAR ALUMNO")
    dni = input("Ingrese el DNI a buscar: ")
    indice = buscar_indice_alumno(alumnos, dni)

    if indice == -1:
        print("No se encontró un alumno con ese DNI.")
        return

    print()
    print("Alumno encontrado:")
    mostrar_un_alumno(alumnos[indice])


def modificar_alumno(alumnos):
    print()
    print("MODIFICAR ALUMNO")
    dni = input("Ingrese el DNI del alumno a modificar: ")
    indice = buscar_indice_alumno(alumnos, dni)

    if indice == -1:
        print("No se encontró un alumno con ese DNI.")
        return

    alumno = alumnos[indice]
    print()
    print("Datos actuales:")
    mostrar_un_alumno(alumno)
    print()
    print("(Deje vacío y presione Enter si no quiere cambiar un dato)")

    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_apellido = input("Nuevo apellido: ")

    ok_edad, nueva_edad = pedir_edad_valida("Nueva edad: ", True)
    if not ok_edad:
        print("No se guardaron cambios.")
        return

    ok_nota, nueva_nota = pedir_nota_valida(
        "Nueva nota (0 a 10, usar punto si tiene decimales): ", True
    )
    if not ok_nota:
        print("No se guardaron cambios.")
        return

    if nuevo_nombre != "":
        alumno["nombre"] = nuevo_nombre
    if nuevo_apellido != "":
        alumno["apellido"] = nuevo_apellido
    if nueva_edad is not None:
        alumno["edad"] = nueva_edad
    if nueva_nota is not None:
        alumno["nota"] = nueva_nota

    guardar_alumnos(alumnos)
    print("Alumno modificado con éxito.")


def eliminar_alumno(alumnos):
    print()
    print("ELIMINAR ALUMNO")
    dni = input("Ingrese el DNI del alumno a eliminar: ")
    indice = buscar_indice_alumno(alumnos, dni)

    if indice == -1:
        print("No se encontró un alumno con ese DNI.")
        return

    del alumnos[indice]
    guardar_alumnos(alumnos)
    print("Alumno eliminado con éxito.")