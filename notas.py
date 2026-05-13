def agregar_nota(lista, texto):
    lista.append(texto)
    print("Nota añadida correctamente")


def mostrar_notas(lista):
    if not lista:
        print(" Sin notas guardadas.")
    else:
        print("\n" + "─" * 30)
        print(f"{'ID':<4} | {'CONTENIDO'}")
        print("─" * 30)
        for i, nota in enumerate(lista):
            print(f"{i + 1:<4} | {nota}")
        print("─" * 30)


def eliminar_nota(lista):
    if not lista:
        print("La lista está vacía, nada que eliminar.")
        return # Salir deg la función inmediatamente
    
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