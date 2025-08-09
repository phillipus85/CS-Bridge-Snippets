"""
Este modulo es el codigo guia para los conceptos de lista de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo es una introducción a las listas en Python e incluye:
        - ESCENA 1: Definir listas, vacias y con elementos.
        - ESCENA 2: Acceder a elementos de una lista.
        - ESCENA 3: Agregar y eliminar elementos de una lista.
        - ESCENA 4: Modificar elementos de una lista.
        - ESCENA 5: Relacionar con otros comandos python.
        - ESCENA 6: Recorrer elementos de una lista.
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
    print("===== Introducción a listas =====")

    # TODO ESCENA 1: Definir listas, vacias y con elementos.
    # definir lista vacia
    print("--- Definición de listas ---\n")
    repisa = []
    sinonimo = list()
    # verificar que ambos tipos de creacion son equivalentes
    print("son listas? ->", repisa == sinonimo)
    # pero no son la misma variable
    print("son la misma variable? ->", repisa is sinonimo, "\n")

    repisa = [
        "Rayuela, Julio Cortázar",
        "Ficciones, Jorge Luis Borges",
        "Aura, Carlos Fuentes",
        "Delirio, Laura Restrepo",
    ]

    sinonimo = list(repisa)
    print("son listas? ->", repisa == sinonimo)
    print("son la misma variable? ->", repisa is sinonimo, "\n")

    # # lista con solo titulos
    # titulos = [
    #     "Rayuela",
    #     "Ficciones",
    #     "Aura",
    #     "Delirio",
    # ]

    # # lista con solo autores
    # autores = [
    #     "Julio Cortázar",
    #     "Jorge Luis Borges",
    #     "Carlos Fuentes",
    #     "Laura Restrepo",
    # ]

    # TODO ESCENA 2: Acceder a elementos de una lista.
    print("--- Acceder a elementos de una lista ---")
    # acceso a elementos segun su posicion
    # primer elemento
    primer_libro = repisa[0]
    print("Primer libro:", primer_libro)
    # último elemento
    # opción 1
    ultimo_libro = repisa[-1]
    print("Último libro (opción 1):", ultimo_libro)
    # opción 2, sinonimo con len
    ultimo_libro = repisa[len(repisa) - 1]
    print("Último libro (opción 2):", ultimo_libro, "\n")

    # TODO ESCENA 3: Agregar y eliminar elementos de una lista.
    print("--- Agregar y eliminar elementos de una lista ---")

    # agregar un libro
    # opción 1, append, última posición
    nuevo_libro = "El túnel, Ernesto Sabato"
    repisa.append(nuevo_libro)
    repisa.append(nuevo_libro)
    print("Después de agregar un libro:\n", repisa)

    # opción 2, insert, posición específica
    nuevo_libro = "La hojarasca, Gabriel García Márquez"
    indice = 1
    repisa.insert(indice, nuevo_libro)
    print("Después de agregar un libro en posición", indice, ":\n", repisa)

    # eliminar un libro
    # opción 1, pop, última posición
    libro = repisa.pop()
    print("Después de eliminar un libro:\n", repisa)
    print("Libro eliminado:", libro)

    # opción 2, remove, por valor
    # eliminar un libro por su nombre
    titulo = "Ficciones, Jorge Luis Borges"
    # que pasa si no es exactamente igual
    # libro = "ficciones, Jorge Luis Borges"
    libro = repisa.remove(titulo)
    print("Después de eliminar un libro:\n", repisa)
    print("Libro eliminado:", titulo, "\n")

    # TODO ESCENA 4: relacionar con otros comandos python
    # uso de condicionales
    # revisar si un elemento esta en la lista con in
    libro = "Delirio, Laura Restrepo"
    esta = (libro in repisa)
    # utilizar condicionales if/else
    # alternativas codigo
    # if libro in repisa:
    # if esta is True:
    # if esta is not False:
    # if libro in repisa is True:
    # if libro in repisa is not False
    if esta:
        print("El libro ", libro, "está en la repisa.")
    else:
        print("El libro no está en la repisa.")

    # TODO ESCENA 5: Modificar elementos de una lista.
    print("\n--- Modificar elementos de una lista ---")
    libro_viejo = repisa[0]
    libro_nuevo = "Cien años de soledad, Gabriel García Márquez"
    repisa[0] = libro_nuevo

    print(libro_viejo, "ha sido reemplazado por", libro_nuevo)
    print(libro_viejo in repisa)
    print(repisa)

    # TODO ESCENA 6: Recorrer elementos de una lista.
    print("--- Recorrer elementos de una lista ---")
    # opción 1, usando el iterador for
    print("\nRecorriendo con iterador for (opción 1):")
    for libro in repisa:
        print("\tEn la repisa está:", libro)

    # opción 2, usando el índice
    print("\nRecorriendo con índice (opción 2):")
    for i in range(len(repisa)):
        print("\tEn la repisa está:", repisa[i])

    # opción 3, usando enumerate
    print("\nRecorriendo con enumerate (opción 3):")
    for i, libro in enumerate(repisa):
        print("\tEn la repisa está:", libro, "(índice", i, ")")

    # opción 4, while
    i = 0
    print("\nRecorriendo con while (opción 4):")
    while i < len(repisa):
        print("\tEn la repisa está:", repisa[i])
        i += 1

    # bono recorerlo al revez
    print("\nRecorriendo al revés con indice (opción 5):")
    for i in range(len(repisa) - 1, -1, -1):
        print("\tEn la repisa está:", repisa[i])
        i -= 1

    # bono recorerlo al revez con iterador
    print("\nRecorriendo al revés con iterador (opción 6):")
    for libro in reversed(repisa):
        print("\tEn la repisa está:", libro)

    # bono recorrerlo al revez con while
    print("\nRecorriendo al revés con while (opción 7):")
    i = len(repisa) - 1
    while i >= 0:
        print("\tEn la repisa está:", repisa[i])
        i -= 1

    # repisa.append("Ficciones, Jorge Luis Borges")
    # repisa.append("Rayuela, Julio Cortázar")
    # repisa.append("Delirio, Laura Restrepo")
    # repisa.append("Delirio, Laura Restrepo")
    # # libro = "Delirio, Laura Restrepo"
    # libro = "Rayuela, Julio Cortázar"
    # conteo = contar_libros(repisa, libro)


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
