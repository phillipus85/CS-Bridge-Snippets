def main():
    print("\n===== EJEMPLOS DE LISTAS =====")
    # nombres de personas
    nombres = [
        "Ana",
        "Carlos",
        "María",
        "Pedro",
    ]
    print("Lista de nombres:", nombres)
    a = nombres.remove("Carlos")
    # print(a)

    persona = nombres[5]
    print("Nombre de persona:", persona)

    # numeros telefónico
    telefonos = [
        3001234567,
        3159876543,
        3104567890
    ]
    print("Lista de teléfonos:", telefonos)

    numero = telefonos[2]
    print("Número Telefónico:", numero)

    print("\n===== EJEMPLOS DE DICCIONARIOS =====")
    # contactos telefónico
    contactos = {
        "Ana": 3001234567,
        "Carlos": 3159876543,
        "María": 3104567890,
    }
    print("directorio de contactos:", contactos)

    nombre = "Maria"
    telefono = contactos[nombre]
    print("Nombre:", nombre, "Teléfono", contactos[nombre])


if __name__ == "__main__":
    main()
