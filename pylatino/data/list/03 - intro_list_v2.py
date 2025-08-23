"""
Este modulo es el codigo guia para los conceptos de lista de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo es una introducción a las listas en Python e incluye:
        - PARTE 1: Definir listas, vacias y con elementos.
        - PARTE 2: Acceder a elementos de una lista.
        - PARTE 3: Agregar elementos de una lista.
        - PARTE 4: Eliminar elementos de una lista.
        - PARTE 5: Modificar elementos de una lista.

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
    print("========== Introducción a listas ==========")

    # TODO PARTE 1: Definir listas, vacias y con elementos.
    # definir lista vacia
    print("\n--- PARTE 1: Definiendo listas ---")
    # creando lista vacia con []
    repisa = []
    # creando lista vacia con list()
    sinonimo = list()
    print("\n+ Definiendo listas vacías: +")
    print("\trepisa:", repisa, "sinonimo:", sinonimo)

    # verificar que ambas formas de crear listas son equivalentes
    # ambas son listas vacias
    if repisa == sinonimo:
        print("\tAmbas listas son iguales y vacias", sinonimo, repisa)
    # ambas son de tipo lista
    if type(repisa) is type(sinonimo):
        print("\tAmbas listas son del mismo tipo:", type(repisa))

    # pero no son la misma variable
    if repisa is sinonimo:
        print("\t'repisa' y 'sinonimo' son la misma variable")
    else:
        print("\t'repisa' y 'sinonimo' son diferentes variables")

    # verificar si repisa es la misma variable
    if repisa is repisa:
        print("\t'repisa' y 'repisa' son la misma variable")

    # creando una lista con elementos, repisa con libros!
    print("\n + Definiendo listas con elementos: +")
    repisa = [
        "Rayuela, Julio Cortázar",
        "Ficciones, Jorge Luis Borges",
        "Aura, Carlos Fuentes",
        "Delirio, Laura Restrepo",
    ]

    print("\t'repisa':", repisa, "'sinonimo':", sinonimo)
    print("\tSon listas iguales y con elementos?", repisa == sinonimo)
    print("\tSon la misma variable?", repisa is sinonimo)

    # creando lista con elementos con list()
    sinonimo = list(repisa)

    # verificar que ambas listas son iguales
    print("\trepisa':", repisa, "'sinonimo':", sinonimo)
    print("\tSon listas iguales y con elementos?", repisa == sinonimo)
    print("\tSon la misma variable?", repisa is sinonimo)

    # TODO PARTE 2: Acceder a elementos de una lista.
    print("\n--- PARTE 2: Acceder a elementos de las listas ---")
    print("\t'repisa':", repisa)

    # acceso a elementos segun su posicion
    # primer elemento
    primer_libro = repisa[0]
    print("\tPrimer libro:", primer_libro)

    # último elemento
    # opción 1
    ultimo_libro = repisa[-1]
    print("\tÚltimo libro (opción 1):", ultimo_libro)

    # opción 2, sinonimo con len
    ultimo_libro = repisa[len(repisa) - 1]
    print("\tÚltimo libro (opción 2):", ultimo_libro)

    # TODO PARTE 3: Agregar elementos de una lista.
    print("\n--- PARTE 3: Agregar elementos de una lista ---")
    print("\t'repisa':", repisa)

    # agregar un libro
    # opción 1, append, última posición
    print("\n+ Utilizando .append(elm) (Opción 1): +")
    print("\tRepisa:", repisa)
    nuevo_libro = "El túnel, Ernesto Sabato"
    repisa.append(nuevo_libro)
    print("\tRepisa después de agregar un libro:", repisa)
    repisa.append(nuevo_libro)
    print("\tRepisa después de agregar otro libro:", repisa)

    # opción 2, insert, posición específica
    print("\n+ Utilizando .insert(i, elm) (Opción 2): +")
    print("\tRepisa:", repisa)

    # nuevo libro + indice
    nuevo_libro = "La hojarasca, Gabriel García Márquez"
    indice = 1
    repisa.insert(indice, nuevo_libro)
    print("\tRepisa después de agregar un libro en la posición:", indice)
    print("\tRepisa:", repisa)

    # TODO PARTE 4: Eliminar elementos de una lista.
    print("\n--- PARTE 4: Eliminar elementos de una lista ---")
    print("\t'repisa':", repisa)

    # eliminar un libro
    # opcion 1, pop, última posición
    print("\n+ Utilizando .pop() (Opción 1): +")
    # opción 1, pop, última posición
    libro = repisa.pop()
    print("\tLibro eliminado:", libro)
    print("\tRepisa después de eliminar un libro:", repisa)

    # opción 2, pop con índice
    print("\n+ Utilizando .pop(idx): +")
    print("\tRepisa:", repisa)
    libro = repisa.pop(3)
    # coincide con: Aura, Carlos Fuentes
    print("\tLibro eliminado:", libro)
    print("\tRepisa después de eliminar un libro:", repisa)

    # opción 3, remove, por valor
    print("\n+ Utilizando .remove(val) (Opción 3): +")
    # eliminar un libro por su nombre
    titulo = "Ficciones, Jorge Luis Borges"
    # que pasa si no es exactamente igual
    libro = repisa.remove(titulo)
    print("Después de eliminar un libro:\n", repisa)
    print("Libro eliminado:", titulo, "\n")

    # TODO PARTE 5: Modificar elementos de una lista.
    print("\n--- Modificar elementos de una lista ---")
    print("\tRepisa:", repisa)

    # modificar un libro
    libro_viejo = repisa[0]
    libro_nuevo = "Cien años de soledad, Gabriel García Márquez"
    repisa[0] = libro_nuevo
    print("\tLibro viejo:", libro_viejo)
    print("\tLibro nuevo:", libro_nuevo)
    print("\tRemplazo el 'libro viejo'??", repisa[0] == libro_nuevo)
    print("\tRepisa después de modificar un libro:", repisa)


if __name__ == '__main__':
    """main es la funcion principal del programa
    """
    main()
    print("============================================================")
    print("Fin de la introducción a listas.")
