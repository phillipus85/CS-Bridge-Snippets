"""
Este modulo es el codigo guia para conceptos avanzados de listas de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo cubre funciones y técnicas avanzadas para trabajar con listas en Python:
        - PARTE 1: Funciones de alto nivel (zip, map, filter).
        - PARTE 2: Funciones de verificación (any, all).
        - PARTE 3: Comprensión de listas.
        - PARTE 4: Listas bidimensionales (matrices).
        - PARTE 5: Ordenamiento y búsqueda.
        - PARTE 6: Copias de listas y referencia.
NOTAS:
    - Este módulo extiende los conceptos básicos presentados en "01 - intro_list.py"
    - Se continúa usando el ejemplo de libros latinoamericanos
"""

# importaciones necesarias
from copy import deepcopy

# definicion de funciones especificas


def busqueda_binaria(lista, elemento):
    """Implementa búsqueda binaria en una lista ordenada"""
    inicio = 0
    fin = len(lista)

    while inicio < fin - 1:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  # Elemento no encontrado


# definicion de la funcion principal

def main():
    """Función principal del programa"""
    print("===== Funciones Avanzadas para Listas =====")

    # Datos iniciales - usando los títulos y autores proporcionados
    print("--- Definición de listas ---")

    # lista con libros
    repisa = [
        "Rayuela, Julio Cortázar",
        "Ficciones, Jorge Luis Borges",
        "Aura, Carlos Fuentes",
        "Delirio, Laura Restrepo",
    ]
    print("Lista de libros:", repisa)

    # lista con solo titulos
    titulos = [
        "Rayuela",
        "Ficciones",
        "Aura",
        "Delirio",
    ]

    # lista con solo autores
    autores = [
        "Julio Cortázar",
        "Jorge Luis Borges",
        "Carlos Fuentes",
        "Laura Restrepo",
    ]

    # Datos adicionales para los ejemplos
    anhos = [1963, 1944, 1962, 2004]

    paises = [
        "Argentina",
        "Argentina",
        "México",
        "Colombia"
    ]

    # TODO PARTE 1: Funciones de alto nivel para listas
    # zip() - combinar varias listas
    print("\n--- PARTE 1: Usando zip() para combinar listas: ---")
    print("Biblioteca completa:")
    # for titulo, autor in zip(titulos, autores):
    for titulo, autor, an, pais in zip(titulos, autores, anhos, paises):
        texto = titulo + " por " + autor + " (" + str(an) + ", " + pais + ")"
        print("\t", texto)
        # print(f"  '{titulo}' por {autor} ({an}, {pais})")
        # print(f"  '{titulo}' por {autor})")

    # map() - mapear/relacionar elementos de una lista a otra
    print("\n--- Usando map() para transformar elementos: ---")

    # Paso 1: definir una función que combina título y autor
    def combinar_titulo_autor(titulo, autor):
        """Función que combina un título y un autor"""
        texto = titulo + ", " + autor
        return texto
        # return f"{titulo}, {autor}"

    # Paso 2: map() aplica la función a elementos de titulos y autores
    libros_completos = list(map(combinar_titulo_autor, titulos, autores))

    # Paso 3: imprimir cada libro de la lista resultante
    for libro in libros_completos:
        print("\tTítulo y autor:", libro)

    # filter() - filtrar elementos según una condición
    print("\n--- Usando filter() para filtrar elementos: ---")

    # Paso 1: Crear tuplas combinando título, autor y país
    libros_completos = list(zip(titulos, autores, paises))
    print("Libros completos (título, autor, país):")
    for libro in libros_completos:
        print("\tlibro:", libro)
    # libros_completos = [(t, a, p) for t, a, p in zip(titulos, autores, paises)]

    # Paso 2: Definir función para verificar si un libro es de Argentina
    def es_de_argentina(libro_tupla):
        """Devuelve True si el libro es de Argentina, False en caso contrario"""
        # libro_tupla es una tupla del estilo (titulo, autor, pais)
        # Desempaquetar la tupla
        titulo, autor, pais = libro_tupla
        return pais == "Argentina"

    # Paso 3: Usar filter() para obtener solo los libros de Argentina
    # filter() devuelve un iterador con elementos que cumplen la condición
    libros_argentina = list(filter(es_de_argentina, libros_completos))
    print("\nLibros filtrados (solo de Argentina):")
    for libro in libros_argentina:
        print("\tlibro", libro)
        # print(f"  {libro}")

    # Paso 4: Extraer solo los títulos y autores de los libros filtrados
    titulos_argentina = []
    autores_argentina = []

    # for titulo, autor, _ in libros_argentina:
    for titulo, autor, pais in libros_argentina:
        titulos_argentina.append(titulo)
        autores_argentina.append(autor)

    # titulos_argentina = [titulo for titulo, autor, pais in libros_argentina]
    # autores_argentina = [autor for titulo, autor, pais in libros_argentina]

    print(f"\nTítulos de Argentina: {titulos_argentina}")
    print(f"Autores de Argentina: {autores_argentina}")

    # TODO PARTE 2: Funciones de verificación
    print("\n--- PARTE 2: Funciones de verificación ---")
    limite = 2000
    libros_recientes = []
    for an in anhos:
        if an > limite:
            libros_recientes.append(True)
        else:
            libros_recientes.append(False)

    # any() - verifica si al menos un elemento cumple una condición
    # equivalente a muchos OR en logica
    print("\n* Usando any() para verificar condiciones:")
    hay_libro_reciente = any(libros_recientes)
    texto = "¿Hay algún libro publicado después del:"
    texto += str(limite) + "?:"
    texto += str(hay_libro_reciente)
    print("\t", texto)

    print("\n* Usando all() para verificar condiciones:")
    # all() - verifica si todos los elementos cumplen una condición
    # equivalente a muchos AND en logica
    todos_siglo_xx = all(libros_recientes)
    texto = "¿Todos los libros son del siglo XX?"
    texto += str(todos_siglo_xx)
    print("\t", texto)

    # TODO PARTE 3: Comprensión de listas
    print("\n--- PARTE 3: Comprensión de listas ---")

    # Comprensión básica
    print("* Comprensión básica de listas:")
    titulos_mayusculas = [titulo.upper() for titulo in titulos]
    print("\tTítulos en mayúsculas:", titulos_mayusculas)

    # Comprensión con condición
    print("\n* Comprensión con condición:")
    libros_largos = [titulo for titulo in titulos if len(titulo) > 6]
    print("\tTítulos con más de 6 caracteres:", libros_largos)

    # Comprensión con múltiples condiciones
    # Usando una comprensión de listas para verificar
    hay_libro_reciente = any([an > limite for an in anhos])
    # imprimiendo el resultado
    texto = "¿Hay algún libro publicado después del:"
    texto += str(limite) + "?:"
    texto += str(hay_libro_reciente)
    print("\t", texto)

    # Usando una comprensión de listas para verificar
    todos_siglo_xx = all(an > limite for an in anhos)
    print("\t¿Todos los libros son del siglo XX?:", todos_siglo_xx)

    # TODO PARTE 4: Listas bidimensionales (matrices)
    print("\n--- PARTE 4: Listas bidimensionales (matrices) ---")

    # Matriz donde cada fila es un libro: [título, autor, año, país]
    matriz_libros = [[t, a, an, p] for t, a, an, p in zip(titulos, autores, anhos, paises)]

    # Mostrar la matriz (fila por fila)
    for fila in matriz_libros:
        print("\t-fila:", fila)

    # Acceso sencillo a elementos
    print("\n* Acceso a elementos específicos de la matriz:")
    print("\tPrimer título:", matriz_libros[0][0])          # fila 0, col 0
    print("\tAutor del 2º libro:", matriz_libros[1][1])     # fila 1, col 1

    # Recorrer toda la matriz con doble for
    print("\n* Recorriendo celda por celda:")
    for i in range(len(matriz_libros)):
        for j in range(len(matriz_libros[i])):
            posicion = "[" + str(i) + "][" + str(j) + "]"
            informacion = str(matriz_libros[i][j])
            print("\tCelda:", posicion + " = " + informacion)
            # print(f"    [{i}][{j}] = {matriz_libros[i][j]}")

    # TODO PARTE 5: Ordenamiento y búsqueda
    print("\n--- PARTE 5: Ordenamiento (sort y sorted) ---")

    # 1) sorted() -> crea una copia ordenada (no modifica la original)
    titulos_ordenados = sorted(titulos)  # alfabético ascendente
    print("* Creando listas ordenadas:")
    print("\tTítulos (copia ordenada):", titulos_ordenados)
    print("\tTítulos (original sin cambios):", titulos)  # comprobación

    # 2) list.sort() -> ordena EN EL LUGAR la lista
    # (modifica la lista original)
    print("\n* Ordenando listas existentes (in-place):")
    autores.sort()  # alfabético in-place
    print("\tAutores ordenados (in-place):", autores)

    # 3) Números: ascendente y descendente con sorted
    print("\tAños ascendentes:", sorted(anhos))
    print("\tAños descendentes:", sorted(anhos, reverse=True))

    # 4) Ordenar pares sin funciones complejas (tuplas se ordenan por el 1er campo)
    # (año, título) -> queda ordenado por año automáticamente
    print("\n* Ordenando por año y título:")
    libros_por_año = sorted(zip(anhos, titulos))
    for an, titulo in libros_por_año:
        texto = str(an) + ": " + titulo
        print("\t", texto)

    # # 5) Orden por país y luego por título (orden natural de tuplas)
    # por_pais_titulo = sorted(zip(paises, titulos))
    # print("\tPor país y título:")
    # for pais, titulo in por_pais_titulo:
    #     texto = titulo + " (" + pais + ")"
    #     print("\t", texto)

    # Búsqueda binaria
    # FIXME no transcribir
    print("\n* Búsqueda binaria en listas ordenadas:")
    titulo_buscar = "Ficciones"
    # Primero debemos ordenar la lista
    titulos_ordenados = sorted(titulos)
    indice = busqueda_binaria(titulos_ordenados, titulo_buscar)

    if indice != -1:
        print(
            f"  '{titulo_buscar}' encontrado en la posición {indice} de la lista ordenada.")
    else:
        print(f"  '{titulo_buscar}' no encontrado en la lista.")
    # END del FIXME

    # PARTE 6: Copias de listas y referencia
    print("\n--- PARTE 6: Copias de listas y referencia ---")

    # Copia superficial vs profunda
    print("\n* Copia superficial vs profunda:")

    # Lista original
    biblioteca = [
        ["Rayuela", "Julio Cortázar", 1963],
        ["Ficciones", "Jorge Luis Borges", 1944],
        ["Aura", "Carlos Fuentes", 1962],
        ["Delirio", "Laura Restrepo", 2004]
    ]

    # Copia por referencia (comparten la misma memoria)
    biblioteca_ref = biblioteca

    # Copia superficial (shallow copy)
    biblioteca_shallow = biblioteca.copy()

    # Copia profunda (deep copy)
    biblioteca_deep = deepcopy(biblioteca)

    # Modificar la lista original
    biblioteca[0][2] = 1964  # Cambiar el año de Rayuela

    print("\tLista original después de la modificación:")
    print("\tdato:", biblioteca[0])

    print("\n\tCopia por referencia (comparten memoria):")
    print("\treferencia:", biblioteca_ref[0])

    print("\n\tCopia superficial (shallow copy):")
    print("\tcopia (superficial):",
          biblioteca_shallow[0],
          " # ¡El año también cambió!")

    print("\n\tCopia profunda (deep copy):")
    print("\tcopia (profunda):",
          biblioteca_deep[0],
          " # ¡¡¡El año NO cambió!!!")

    print("\n* Comparación de identidad y valores:")
    # true
    print("\tReferencia es igual: ", biblioteca is biblioteca_ref)
    # False
    print("\tCopia superficial es igual: ", biblioteca is biblioteca_shallow)
    # True
    print("\tValores de copia superficial son iguales: ", biblioteca == biblioteca_shallow)
    # False
    print("\tValores de copia profunda son iguales: ", biblioteca == biblioteca_deep)


if __name__ == '__main__':
    main()
    print("============================================================")
    print("Fin del módulo de funciones avanzadas para listas.")
