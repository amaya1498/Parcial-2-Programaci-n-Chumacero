import json

NOMBRE_ARCHIVO = "alumnos.json"


def preparar_archivo_inicial():
    guardar_alumnos([])


def cargar_alumnos():
    archivo = open(NOMBRE_ARCHIVO, "r")
    contenido = archivo.read()
    archivo.close()

    if contenido == "":
        preparar_archivo_inicial()
        return []

    alumnos = json.loads(contenido)
    return alumnos


def guardar_alumnos(alumnos):
    archivo = open(NOMBRE_ARCHIVO, "w")
    json.dump(alumnos, archivo, indent=4)
    archivo.close()