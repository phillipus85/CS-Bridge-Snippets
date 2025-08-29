"""
Este modulo es el codigo guia para los recorridos de lista de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo es una introducción a las listas en Python e incluye:
        - PARTE 1: Definir listas con elementos.
        - PARTE 2: Relacionar con otros comandos python.
        - PARTE 3: Recorrer elementos de una lista.
        - PARTE 4: Funciones con listas.
NOTAS:
    - No hay elementos duplicados en una lista.
    - Las listas son mutables, lo que significa que se pueden modificar después de su creación.
    - Las listas pueden contener elementos de diferentes tipos.
    - Ejemplo basado en libros latinoamericanos.
"""

# importaciones necesarias


# definicion de funciones especificas


# definicion de la funcion principal

def main():
    """main es la funcion principal del programa
    """
    print("========== Recorridos de listas ==========")

    # TODO PARTE 1: Definir lista con elementos.
    print("\n--- PARTE 1: Definiendo listas con elementos. ---")
    # creando una lista con elementos, repisa con libros!
    repisa = [
        "Rayuela, Julio Cortázar",
        "Ficciones, Jorge Luis Borges",
        # "Cien años de soledad, Gabriel García Márquez",
        "Aura, Carlos Fuentes",
        "Delirio, Laura Restrepo",
        "El túnel, Ernesto Sabato",
        "La hojarasca, Gabriel García Márquez",
    ]

    # creando lista con elementos con list()
    sinonimo = list(repisa)
    # verificar que ambas listas son iguales
    print("\t'repisa':", repisa, "'sinonimo':", sinonimo)
    print("\tSon listas iguales y con elementos?", repisa == sinonimo)
    print("\tSon la misma variable?", repisa is sinonimo)

    # TODO PARTE 2: relacionar con otros comandos python
    print("\n--- PARTE 2: Relacionar con otros comandos python ---")
    # uso de condicionales
    print("\tRepisa:", repisa)

    # revisar si un elemento esta en la lista con in
    libro = "Delirio, Laura Restrepo"
    esta = (libro in repisa)
    # utilizar condicionales if/else
    # alternativas codigo
    # if libro in repisa:
    # if esta is True:
    # if esta is not False:
    # if libro in repisa is True:
    # if libro in repisa is not False:
    if esta:
        print("\n\tEl libro ", libro, "está en la repisa.")
    else:
        print("\n\tEl libro ", libro, "no está en la repisa.")

    # libro que no esta
    otro_libro = "Cien años de soledad, Gabriel García Márquez"
    # esta = (otro_libro in repisa)
    if otro_libro in repisa is True:
        print("\tEl libro ", otro_libro, "está en la repisa.")
    else:
        print("\tEl libro ", otro_libro, "no está en la repisa.")

    # TODO PARTE 3: Recorrer elementos de una lista.
    print("\n--- PARTE 3: Recorrer elementos de una lista ---")
    print("\tRepisa:", repisa)

    # opción 1, usando el iterador for
    print("\n\tRecorriendo con iterador for (opción 1):")
    for libro in repisa:
        print("\t\tEn la repisa está:", libro)

    # opción 2, usando el índice
    print("\n\tRecorriendo con índice (opción 2):")
    for i in range(len(repisa)):
        print("\t\tEn la repisa está:", repisa[i])

    # opción 2, utilizando el indice para modificar datos
    print("\n\tModificando con índice (opción 2):")
    for i in range(len(repisa)):
        print("\t\tEn la repisa está:", repisa[i])
        # modificar el libro a mayúsculas
        libro = repisa[i]
        libro = libro.upper()
        repisa[i] = libro
        # # alternativa 1
        # libro = repisa[i]
        # repisa[i] = libro.upper()
        # # alternativa 2
        # repisa[i] = repisa[i].upper()

    # revisar cambios
    print("\n\tRepisa:", repisa)

    # reseteando cambios
    repisa = list(sinonimo)

    # opción 3, while con contador
    i = 0
    print("\nRecorriendo con while (opción 3):")
    while i < len(repisa):
        print("\t\tEn la repisa está:", repisa[i])
        i += 1

    # opcion 3, cambiar con while y condicional.
    # libro importante y prestado
    libro_importante = "Delirio, Laura Restrepo"
    libro_prestar = "Cien años de soledad, Gabriel García Márquez"

    i = 0
    prestado = False
    while i < len(repisa) and prestado is False:
        if repisa[i] == libro_importante:
            repisa[i] = repisa[i].upper()
        if repisa[i] == libro_prestar:
            libro_prestado = repisa[i]
            print("\t\tLibro prestado:", libro_prestado)
            repisa.pop(i)
            prestado = True
        i += 1
    print("\n\tcontador i:", i, "largo repisa:", len(repisa))

    # revisar cambios
    print("\n\tRepisa:", repisa)


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
    repisa = []
    print(repisa)
