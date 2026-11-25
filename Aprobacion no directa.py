# ================================
# PARTE A ANALISIS DE ESTRUCTURA DE DATOS
# ================================

# SITUACION 1
# Se hace uso de estructuras de matriz porque al estar ordenadas de forma con filas y columnas, con una matriz respetando su estrcutra se obtiene de manera mas exacta su ubicacion


def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return


estanteria = inicializar_matriz(3, 4, "Libre") 

estanteria[0][1] = "Libro A"
estanteria[1][3] = "Libro B"
estanteria[2][0] = "Libro C"

for fila in estanteria:
    print(fila)


# SITUACION 2
# Se hace uso de Tuplas ya que pide que los datos se guarden y no se modifiquen, las tuplas son inmutables


libro_a = ("978-987-001", "Libro A", "Autor Ejemplo", 2020)
libro_b = ("978-987-002", "Libro B", "Otro Autor", 2022)

print("Datos del libro:", libro_a)
print("ISBN:", libro_a[0])
print("Titulo:", libro_a[1])
print("Autor:", libro_a[2])
print("Fecha de publicacion:", libro_a[3])


# SITUACION 3
# Se hace uso de set porque es la estructura adecuada para elementos inmutables y con el .add agrega elementos en el set


socios = set()


socios.add("Ana Perez")
socios.add("Luis Gomez")
socios.add("Ana Perez")


print("socios registrados:", socios)
print("Cantidad de socios unicos:", len(socios))


# SITUACION 4
# Se hace uso de diccionario porque  es la mejor forma de juntar y relacionar un ISBN con toda la informacion sin necesidad de usar listas


catalogo = {
    "978-987-001": ("978-987-001", "Libro A", "Autor Ejemplo", 2020),
    "978-987-002": ("978-987-002", "Libro B", "Otro Autor", 2022)
}

isbn_buscando = "978-987-001"


if isbn_buscando in catalogo:
    libro = catalogo[isbn_buscando]
    print("Libro encontrado:", libro)
    print("Titulo:", libro[1])
    print("Autor:", libro[2])
    print("Fecha de publicacion:", libro [3])
else:
    print("No se encontro un libro con ese ISBN.")


# SITUACION 5
# Se hace uso de un manejo de archivos(open, write, read) para conservar datos los datos cuando se cierra el programa, apoyandose en una lista para leerlos
# y procesarlos dentro del codigo


# Lista inicial de socios para guardar en el archivo
socios = ["Ana Perez", "Luis Gomez"]

# Abrimos el archivo en modo escritura ("w") y guardamos cada socio separado por coma
archivo = open("socios.txt", "w")
for socio in socios:
    archivo.write(socio + ",")
archivo.close()

# Lista vacia donde vamos a guardar los datos leidos desde el archivo
socios_guardados = []

# Abrimos el archivo en modo lectura ("r") y leemos lo que esta guardado
archivo = open("socios.txt", "r")
contenido = archivo.read()
archivo.close()

# Recorremos letra por letra y cada vez que aparece una coma guardamos el nombre en la lista
nombre_actual = ""
for letra in contenido:
    if letra == ",":
        if nombre_actual != "":
            socios_guardados = socios_guardados + [nombre_actual]
            nombre_actual = ""
    else:
        nombre_actual = nombre_actual + letra

# Si quedo algun nombre sin coma al final, tambien lo agregamos
if nombre_actual != "":
    socios_guardados = socios_guardados + [nombre_actual]

# Mostramos los socios recuperados desde la lista
print("Socios guardados en el archivo:")
for socio in socios_guardados:
    print(socio)



#========================================
# PARTE B RAZONAMIENTO
#========================================


#1 Explique por qué utilizar múltiples listas separadas para almacenar datos relacionados puede generar errores de consistencia
# R:Puede generar problemas porque al ser multiples listas separadas eso genera que los datos queden unidos
# unicamente por su posicion provocando un desfasaje de los indices tanto que si se quiere agregar o eliminar terminan
# mezclando los datos de dististos registros. Ademas, afecta a las actualizaciones que se quieran hacer dejandolas incompletas; cuenta
# con dificultades para ordenar listas.

#2 Explique qué ventajas aporta utilizar una estructura basada en clave-valor para buscar información. 
# R:La ventaja es que se pude acceder usando su clave-valor facilitando la busqueda, ademas de que asocia un identificador unico
# directamente con su valor, dando una busqueda mas rapida e eficiente, ademas de contar con claves unicas cada identificador asocia
# un unico valor.

#3 Explique por qué una estructura que no permite duplicados puede ser útil en sistemas reales. 
# R:Una estructura que no permite duplicados es util porque evita registros de errores repetidos, verifica si un elemento ya existe
# ademas de que facilita la operacion entre conjuntos.

#4 Explique las diferencias entre almacenar datos: 
# únicamente en memoria;  
# en archivos.  
# ¿En qué situaciones utilizaría cada alternativa?
# R:La diferencia entre almacemnar datos unicamente en memoria y en archivos es que; almacenar datos en archivos esque es mas lenta, requiere 
# requiere definir un formato (.csv, .json, etc), esta limitida por el espacio en disco, conserva los archivos aunque el programa se cierre o se 
# reinicie la computadora. En cambio en unicamente en memoria, tiene una velocidad mas rapida (ya que el cambiar variables en RAM es inmediato)
# tiene una capacidad limitada por la RAM disponible, cuenta con una complejidad mas simple de manipular mientras el programa esta corriendo.
# Por ende POR MEMORIA es temporal y rapida mientras que por ARCHIVOS es permanente pero mas lenta.
# 
# Para unicamente en memoria se usa para situaciones de datos temporales, cuando el nro de datos pequeño y no importa que de borre al terminar 
# la ejecucion.
# Para archivos se usa para situaciones que se necesite conservar la informacio entre ejecuciones y cuando se quiere cargar un estado inicial
# al abrir el programa y guardar los cambios.



#=============================================
# PARTE C ANALISIS DE CODIGO
#=============================================

# CASO 1 

libro = ("9789501234567", "Guido", 2025)
libro[1] = "Python avanzado"

# ¿El código funcionará? 
# R:No, el codigo no va a funcionar
# ¿Qué ocurrirá?  
# R:El codigo va a tirar error en la posicion [1]
# ¿Por qué?  
# R:Porque libro esta definido mediante parentesis como una tupla en Python las tuplas no pueden ser reasignadas ni modificadas
# sus elementos una vez creada
# ¿Qué característica de la estructura utilizada produce ese comportamiento?
# R:La caracteristica utilizada que produce este comportamiento es que las tuplas son inmutables, es decir, evitan que los datos sean
# modificados accidentalmente


# CASO 2

socios = {"Juan", "Ana", "Pedro", "Ana"}

print(socios)

# ¿Cuántos elementos contendrá la estructura?
# R: La estructura tendra 3 elementos
# ¿Por qué?  
# R: Porque socios esta definido con {} como un conjunto set, y en los conjunto set no se contienen
# elemnetos duplicados
# ¿Qué ventaja aporta este comportamiento? 
# La ventaja que contiene este comportamiento esque evita que se dupliquen los datos de forma automatica 
# y de paso, se corrobora si un elemento ya existe.


# CASO 3

libros = {
    "9789501234567": {
        "titulo": "Python",
        "autor": "Guido"
    }
}

# ¿Qué estructura de datos aparece en el ejemplo?  
# R: Las estructuras de dato que aparecen es un diccionario, y dentro de los corchetes hay otro diccionario anidado
# ¿Qué representa cada clave?  
# R: En el diccionario principal representa "libros", la clave "97.." representa el ISBN unico que identifica el libro,
# y en los diccionarios internos "titulo" y "autor" representan los campos de ese libro. 
# ¿Qué ventajas ofrece para realizar búsquedas? 
# Las ventajas que ofrece es la de acceder directamente a la informacion de un libro mediante su clave, haciendo la busqueda
# mas rapida, directa y legible.


# UN DESARROLLADOR AFIRMA "Podría resolver todos los problemas utilizando únicamente listas."
# 1) NO, porque si bien funcionaria, terminaria siendo un codigo poco esencial y a la mezclaria datos que podrian interpretados
# por otros, o repititivos.
# 2) Las ventajas que tiene de usar solo listas esque no se necesitarian otras estructuras, siendo solo una estructura simple, 
# permite agregar, quitar, modificar elementos facilmente, ademas las listas permiten representar matrices y estanterias
# con filas y columnas.
# Las desventajas de usar solo listas esque las busquedas pasan a ser menos directas y mas lentas, se repiten mismas validaciones
# son mutables, por lo que una lista puede modificarse ya que no se mantienen fijas, como no se usan los archivos, los datos pueden
# llegar a perderse si se cierra el programa, ya que se mantienen en la memoria RAM



# ============================================
# PREGUNTAS DE SELECCION MULTIPLE
# ============================================

# 1) Respecto a los diccionarios en Python: 
# A.Permiten almacenar información mediante pares clave-valor. 
# B.Las claves deben ser únicas. 
# D.Se puede acceder a un valor utilizando su clave
# F.Son útiles para representar entidades como alumnos, libros o productos. 

# 2)Respecto a las tuplas:
# C.Una vez creadas, sus elementos no pueden modificarse. 
# B.Permiten almacenar distintos tipos de datos. 
# D.Son adecuadas para representar información que no debería cambiar. 
# F.Admiten acceso mediante índices. 

# 3) Respecto a los conjuntos (set):
# C.No garantizan posiciones mediante índices. 
# E.Son adecuados para representar colecciones de elementos únicos. 
# B.Son útiles para eliminar elementos repetidos. 

# 4)Respecto a las matrices en Python:
# B.Generalmente se representan mediante listas anidadas. 
# F.Permiten acceder a una posición utilizando fila y columna. 
# E.Todos sus elementos deben ser del mismo tipo. 
# A.Generalmente se representan mediante listas anidadas. 

# 5)Respecto al manejo de archivos:
# A.Permite conservar información luego de finalizar la ejecución del programa.
# E.La instrucción with open(...) ayuda a gestionar correctamente el cierre del archivo. 
# B.El modo "r" se utiliza para lectura. 
# C.El modo "w" permite escribir en un archivo. 


# EJEMPLO DE ESTRUCTURA DE TUPLAS

