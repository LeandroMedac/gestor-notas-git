from notas import agregar_nota, mostrar_notas, eliminar_nota

notas = []

while True:
    print("\n--- Gestión ---")
    print("1. Añadir")
    print("2. Mostrar")
    print("3. Eliminar")
    print("4. Salir")

    opcion = input("¿Opción?: ")

    if opcion == "1":
        texto = input("Introduce la nota: ")
        agregar_nota(notas, texto)

    elif opcion == "2":
        mostrar_notas(notas)

    elif opcion == "3":
        eliminar_nota(notas)

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("Opción incorrecta")