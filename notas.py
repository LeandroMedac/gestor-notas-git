def agregar_nota(lista, texto):
    lista.append(texto)
    print("Nota añadida correctamente")


def mostrar_notas(lista):
    if len(lista) == 0:
        print("No hay notas guardadas")
    else:
        print("\nLISTA DE NOTAS")
        for i, nota in enumerate(lista):
            print(f"{i + 1}. {nota}")


def eliminar_nota(lista):
        mostrar_notas(lista)
        if len(lista) > 0:
            try:
                indice = int(input("Número de nota a eliminar: ")) - 1
                if 0 <= indice < len(lista):
                    lista.pop(indice)
                    print("Nota eliminada con éxito.")
                else:
                    print("Error: El número no existe en la lista.")
            except ValueError:
                print("Error: Debes introducir un número válido.")

def vaciar_notas(lista):
        lista.clear()
        print("Todas las notas han sido eliminadas.")