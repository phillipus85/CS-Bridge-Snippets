"""
Este modulo es el codigo guia para los conceptos de diccionario de pylatino 2025.

RESUMEN DEL MÓDULO
    Este módulo introduce los diccionarios en Python e incluye:
        - PARTE 1: Retomando el concepto llave-valor, crear diccionarios.
        - PARTE 2: Propiedades del diccionario: keys, values, items.
        - PARTE 3: Iterar sobre diccionarios (keys, values, items).


NOTAS:
    - Un diccionario almacena pares (llave, valor).
    - Las llaves suelen ser strings o números (deben ser inmutables, es decir no cambiar).
    - Acceso y modificación son muy rápidas.
"""


# definicion de la funcion principal
def main():
    print("===== Introducción a diccionarios =====")

    # Datos base (mismos que en listas)
    # repisa = [
    #     "Rayuela, Julio Cortázar",
    #     "Ficciones, Jorge Luis Borges",
    #     "Aura, Carlos Fuentes",
    #     "Delirio, Laura Restrepo",
    # ]
    titulos = ["Rayuela", "Ficciones", "Aura", "Delirio"]
    autores = ["Julio Cortázar", "Jorge Luis Borges", "Carlos Fuentes", "Laura Restrepo"]
    anhos = [1963, 1944, 1962, 2004]
    paises = ["Argentina", "Argentina", "México", "Colombia"]

    # TODO PARTE 1: concepto de llave- valor, acceso directo
    print("\n--- PARTE 1: Llave-valor, acceso y modificación ---")

    # Diccionario simple: {titulo: autor}
    autores_por_titulo = {
        "Rayuela": "Julio Cortázar",
        "Ficciones": "Jorge Luis Borges",
        "Aura": "Carlos Fuentes",
        "Delirio": "Laura Restrepo",
    }
    print("* Diccionario (titulo: autor):")
    print("\tdict:", autores_por_titulo)

    # Acceso directo por llave (rápido)
    print("\tAutor de 'Rayuela':", autores_por_titulo["Rayuela"])

    # Agregar un nuevo par (si no existe) o modificar (si existe)
    autores_por_titulo["Rayuela"] = "Julio CORTÁZAR"  # modificar
    autores_por_titulo["El túnel"] = "Ernesto Sabato"  # agregar
    print("\n* Después de modificar y agregar:")
    print("\tdict", autores_por_titulo)

    # Verificar existencia antes de acceder para evitar errores
    llave = "Cien años de soledad"
    if llave in autores_por_titulo:
        print("Autor de", llave, ":", autores_por_titulo[llave])
    else:
        print("No existe la llave:", llave)

    # TODO PARTE 2: funciones basicas, get, update, setdefault, pop
    print("\n--- PARTE 2: Funciones básicas (get, update, setdefault, pop) ---")

    # get: acceso seguro (permite valor por defecto)
    print("\n* usando get()")
    print("\tget('Ficciones'):",
          autores_por_titulo.get("Ficciones"))
    print("get('Inexistente', 'Desconocido'):",
          autores_por_titulo.get("La Hojarasca", "Desconocido"))

    # update: fusionar/actualizar con otro diccionario
    print("\n* usando update()")
    nuevos = {"Aura": "C. Fuentes", "La hojarasca": "Gabriel García Márquez"}
    autores_por_titulo.update(nuevos)
    print("\tDespués de update:", autores_por_titulo)

    # setdefault: devolver valor si existe; si no, lo crea con un valor por defecto
    print("\n* usando setdefault()")
    valor = autores_por_titulo.setdefault("El amor en los tiempos del cólera", "G. G. Márquez")
    print("\tsetdefault() agregó si no existía:", valor)
    print("\tDiccionario ahora:", autores_por_titulo)

    # pop: eliminar por llave y devolver el valor (opcional: valor por defecto)
    print("\n* usando pop()")
    valor_eliminado = autores_por_titulo.pop("El túnel", "No Disponible")
    print("\tpop('El túnel'):", valor_eliminado)
    print("\tDiccionario después de pop:", autores_por_titulo)

    # TODO PARTE 3: Crear diccionarios a partir de listas
    print("\n--- PARTE 3: Crear diccionarios a partir de listas ---")

    # 3.1) A partir de dos listas paralelas con zip: dict
    autores_por_titulo_zip = dict(zip(titulos, autores))
    print("\tDict (título: autor) con zip:", autores_por_titulo_zip)

    # 3.2) Índice: título (con enumerate)
    indice_a_titulo = dict(enumerate(titulos))
    print("\tDict (índice: título) con enumerate:", indice_a_titulo)

    # 3.3) Título: año (zip de títulos y años)
    anhos_por_titulo = dict(zip(titulos, anhos))
    print("\tDict (título: año):", anhos_por_titulo)

    # 3.4) Agrupar títulos por país (ciclo simple)
    libros_por_pais = {}
    for titulo, pais in zip(titulos, paises):
        if pais not in libros_por_pais:
            libros_por_pais[pais] = []
        libros_por_pais[pais].append(titulo)
    print("\tDict (país: lista de títulos):", libros_por_pais)

    # TODO PARTE 4: Propiedades y vistas (len, keys, values, items)
    print("\n--- PARTE 4: Propiedades y vistas (len, keys, values, items) ---")
    print("\tlen de diccionario:", len(autores_por_titulo))
    # convertir a lista para imprimir
    print("\tllaves, keys():", list(autores_por_titulo.keys()))
    print("\tvalores, values():", list(autores_por_titulo.values()))
    print("\telementos, items():", list(autores_por_titulo.items()))

    # Diccionario de libros con detalles: {titulo: {autor, anho, pais}}
    print("\n* Diccionario de libro con detalles:")
    biblioteca = {
        t: {"autor": a, "anho": an, "pais": p}
        for t, a, an, p in zip(titulos, autores, anhos, paises)
    }
    print("\tbiblioteca:\n\t", biblioteca)

    # Acceso directo a un campo del detalle
    titulo = "Aura"
    print("\tPaís de:", titulo, "es", biblioteca[titulo]["pais"])

    # TODO PARTE 5: Iterar sobre diccionarios
    print("\n--- PARTE 5: Iterar sobre diccionarios ---")

    # Iterar sobre llaves (por defecto): for llave in dic
    print("* Recorriendo llaves (títulos):")
    for titulo, sinonimo in zip(biblioteca, biblioteca.keys()):
        print("\tllave (título)", titulo)
        print("\tllave (sinonimo)", sinonimo)
        print("\tiguales?:", titulo == sinonimo)

    # Iterar sobre valores
    print("\n* Recorriendo valores (detalles):")
    for detalle in biblioteca.values():
        print("\tvalor (detalle)", detalle)

    # TODO explicar tuplas antes de explicar .items()

    # Iterar sobre items (llave, valor)
    print("\n* Recorriendo items (titulo, detalle):")
    for titulo, detalle in biblioteca.items():
        texto = titulo + " - " + detalle["autor"] + " (" + str(detalle["anho"]) + ", " + detalle["pais"] + ")"
        print("\tlibro:", texto)

    # Ejemplo simple de actualización al iterar
    print("\n* Actualizar un campo al iterar (sumar 1 al año de 'Rayuela'):")
    if "Rayuela" in biblioteca:
        biblioteca["Rayuela"]["anho"] = biblioteca["Rayuela"]["anho"] + 1
    print("\tInfo actualizada:", biblioteca["Rayuela"])


if __name__ == "__main__":
    main()
    print("============================================================")
    print("Fin de la introducción a diccionarios.")
