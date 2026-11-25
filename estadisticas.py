def calcular_total(alumnos):
    return len(alumnos)


def calcular_promedio(alumnos):
    if len(alumnos) == 0:
        return 0

    suma = 0
    for alumno in alumnos:
        suma = suma + alumno["nota"]

    promedio = suma / len(alumnos)
    return int(promedio * 100) / 100


def obtener_mayor_nota(alumnos):
    if len(alumnos) == 0:
        return None

    mejor = alumnos[0]
    for alumno in alumnos:
        if alumno["nota"] > mejor["nota"]:
            mejor = alumno

    return mejor


def contar_aprobados(alumnos):
    aprobados = 0
    for alumno in alumnos:
        if alumno["nota"] >= 6:
            aprobados = aprobados + 1
    return aprobados


def contar_desaprobados(alumnos):
    desaprobados = 0
    for alumno in alumnos:
        if alumno["nota"] < 6:
            desaprobados = desaprobados + 1
    return desaprobados


def mostrar_estadisticas(alumnos):
    print()
    print("ESTADÍSTICAS")
    total = calcular_total(alumnos)
    print("Cantidad total de alumnos:", total)

    if total == 0:
        print("Promedio de notas: No hay alumnos")
        print("Alumno con mayor nota: No hay alumnos")
        print("Cantidad de aprobados: 0")
        print("Cantidad de desaprobados: 0")
        return

    promedio = calcular_promedio(alumnos)
    mayor = obtener_mayor_nota(alumnos)
    aprobados = contar_aprobados(alumnos)
    desaprobados = contar_desaprobados(alumnos)

    print("Promedio de notas:", promedio)
    print(
        "Alumno con mayor nota:",
        mayor["nombre"],
        mayor["apellido"],
        "- Nota:",
        mayor["nota"],
    )
    print("Cantidad de aprobados:", aprobados)
    print("Cantidad de desaprobados:", desaprobados)