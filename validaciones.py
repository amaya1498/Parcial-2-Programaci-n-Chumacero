DIGITOS = "0123456789"
CARACTERES_NOTA = "0123456789."


def dni_existe(alumnos, dni):
    for alumno in alumnos:
        if alumno["dni"] == dni:
            return True
    return False


def es_entero_valido(texto):
    if texto == "":
        return False

    for caracter in texto:
        if caracter not in DIGITOS:
            return False

    return True


def edad_valida(edad):
    if edad < 0:
        return False
    return True


def es_numero_valido(texto):
    if texto == "" or texto == ".":
        return False

    cantidad_puntos = 0
    for caracter in texto:
        if caracter not in CARACTERES_NOTA:
            return False
        if caracter == ".":
            cantidad_puntos = cantidad_puntos + 1

    if cantidad_puntos > 1:
        return False

    return True


def nota_valida(nota):
    if nota < 0 or nota > 10:
        return False
    return True