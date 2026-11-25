#BIBLIOTECA NACIONAL
# Ejemplo de Tuplas
# .Una vez creadas, sus elementos no pueden modificarse. 
# .Permiten almacenar distintos tipos de datos. 
# .Son adecuadas para representar información que no debería cambiar. 
# .Admiten acceso mediante índices.

# Datos del libro guardados, no se pueden modificar, en una tupla: (isbn, titulo, autor, fecha)
libro = ("9789501234567", "Python", "Guido", 2025)

print("Ejemplo de tupla con datos de un libro.")
print("Una vez creadas, sus elementos no pueden modificarse.") #Una vez creadas, sus elementos no pueden modificarse.

# Empiezo en "SI" para entrar al bucle y cortar recien cuando escriba "NO"
seguir = "SI"

while seguir != "NO":
    print("MENU PARA VERIFICAR DATOS")
    print("0: ISBN")
    print("1: Titulo")
    print("2: Autor")
    print("3: Fecha")

    indice = input("Elegi el indice (0, 1, 2 o 3): ")

    # Serevisa que el indice exista en la tupla
    if indice == "0" or indice == "1" or indice == "2" or indice == "3":
        dato = input("dato a verificar: ")

        # Comparamos segun el indice elegido accediendo a cada posicion con corchetes <Admiten acceso mediante índices>
        if indice == "0":
            if dato == libro[0]:
                print("Ese dato si figura en ese indice.")
            else:
                print("Ese dato no figura.")
        elif indice == "1":
            if dato == libro[1]:
                print("Ese dato si figura en ese indice.")
            else:
                print("Ese dato no figura.")
        elif indice == "2":
            if dato == libro[2]:
                print("Ese dato si figura en ese indice.")
            else:
                print("Ese dato no figura.")
        elif indice == "3":
            # Convertimos libro[3] (2025, entero) a texto con str() para compararlo con el input <Permiten almacenar distintos tipos de datos>
            if dato == str(libro[3]):
                print("Ese dato si figura en ese indice.")
            else:
                print("Ese dato no figura.")
    else:
        # Si hay otro indice, se avisa que no esta en la tupla sin romper el programa
        print("Ese indice no figura en la tupla.")

    # Actualizamos la variable para decidir si se hace otra comprobacion o se termina
    seguir = input("Queres verificar otro dato? (SI / NO): ")

# Al salir del bucle (cuando seguir == "NO"), mostramos el mensaje de cierre
print("Comprobacion finalizada.")



