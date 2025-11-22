def main():
    print("\n===== EJEMPLOS DE LISTAS =====")
    # nombres de personas
    nombres = [
        "Ana",      # índice 0
        "Carlos",   # índice 1
        "María",    # índice 2
        "Pedro",    # índice 3
        "Luisa"     # índice 4
    ]

    print("\n----- FUNCIONES DE LISTAS -----")
    # probando pop, append, index
    print("Lista de nombres inicial:", nombres)

    # eliminar un elemento existente por índice
    print("\n\tEliminar elemento por índice con pop()")
    print("\tTamaño:", len(nombres), "Lista de nombres:", nombres)
    persona = nombres.pop(2)
    print("\tEliminó:", persona)

    # agregar un elemento al final
    print("\n\tAgregar elemento con append()")
    nombres.append("Sofía")
    print("\tTamaño:", len(nombres), "Lista de nombres:", nombres)

    # buscar el índice de un elemento
    print("\n\tBuscar índice de un elemento con index()")
    persona = nombres[-2]   # penúltimo elemento
    print("\tNombre de persona:", persona, "En indice:", nombres.index(persona))

    print("\nLista de nombres final:", nombres)

    print("\n----- Probando otras funciones de listas -----")
    # numeros telefónico
    telefonos = [
        3001234567,     # índice 0
        3159876543,     # índice 1
        3104567890,     # índice 2
        3206547890,     # índice 3, numero a eliminar y luego reinsertar
        3309871234,     # índice 4
    ]

    print("Lista de telefonos inicial:", telefonos)
    # probando remove, insert, sort
    print("\n\tEliminar elemento por valor con remove()")
    print("\tTamaño:", len(telefonos), "Lista de teléfonos:", telefonos)

    # eliminar un elemento por valor
    numero_a_eliminar = 3206547890
    telefonos.remove(numero_a_eliminar)
    print("\tTamaño:", len(telefonos), "Lista de teléfonos:", telefonos)

    # agregar un elemento en una posición específica
    print("\n\tAgregar elemento en posición específica con insert()")
    telefonos.insert(1, numero_a_eliminar)
    print("\tTamaño:", len(telefonos), "Lista de teléfonos:", telefonos)

    # ordenar la lista
    print("\n\tOrdenar lista con sort()")
    telefonos.sort()
    print("\tTamaño:", len(telefonos), "Lista de teléfonos:", telefonos)
    # invertir el orden de la lista
    print("\n\tInvertir lista con sort(reverse=True)")
    telefonos.sort(reverse=True)
    print("\tTamaño:", len(telefonos), "Lista de teléfonos:", telefonos)

    print("\nLista de teléfonos final:", telefonos)

    print("\n===== EJEMPLOS DE DICCIONARIOS =====")
    # contactos telefónico
    contactos = {
        "Ana": 3001234567,
        "Carlos": 3159876543,
        "María": 3104567890,
    }

    print("Tamaño:", len(contactos),
          "directorio de contactos inicial:", contactos)

    print("\n----- FUNCIONES DE DICCIONARIOS -----")

    # busqueda por llave
    print("\n\tBuscar número telefónico por nombre (llave)")
    nombre = "María"    # María con tilde
    # telefono = contactos[nombre]
    telefono = contactos.get(nombre, "Contacto no encontrado")
    print("\tNombre:", nombre, "Teléfono:", telefono)
    
    
    
    print("Teléfono:", telefono)

    # agregar un nuevo contacto
    print("\n\tAgregar nuevo contacto")
    contactos["Pedro"] = 3201234567
    print("directorio de contactos actualizado:", contactos)

    # actualizar diccionario con otro diccionario
    otros_contactos = {
        "Luisa": 3309876543,
        "Sofía": 3401237890,
    }
    contactos.update(otros_contactos)
    print("\tTamaño:", len(contactos),
          "directorio de contactos actualizado:", contactos)

    # eliminar un contacto
    print("\n\tEliminar contacto por nombre (pop)")
    nombre_a_eliminar = "Pedro"
    telefono_eliminado = contactos.pop(nombre_a_eliminar, "Contacto no encontrado")
    print("\n\tEliminó:", nombre_a_eliminar, "Teléfono:", telefono_eliminado)
    print("\tTamaño:", len(contactos),
          "directorio de contactos actualizado:", contactos)

    # para evitar error usamos el método get
    # telefono = contactos[nombre]
    telefono = contactos.get(nombre, "Contacto no encontrado")
    print("Teléfono:", telefono)
    print("Nombre:", nombre, "Teléfono", telefono)
    
    

    print("\n----- BÚSQUEDA POR VALOR EN DICCIONARIOS -----")
    for nom, tel in contactos.items():
        if tel == telefono:
            print("¡Contacto encontrado!")
            print("Nombre:", nom, "Teléfono", tel)


if __name__ == "__main__":
    main()
