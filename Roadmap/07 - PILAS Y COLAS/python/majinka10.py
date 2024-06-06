lista = [3, 2]
print(f"Tratamiento de una lista: {lista} como pila")
lista.append(4)
print(f"Añadiendo al final de la pila: {lista}")
lista.pop()
print(f"Eliminando el último elemento que entró: {lista}")

print(f"Tratamiento de una lista: {lista} como cola")
lista.append(6)
print(f"Añadiendo al final de la cola: {lista}")
lista.pop(0)
print(f"Eliminando el primer elemento de la cola: {lista}")

# Ejercicio EXTRA
print("\nEjercicio de navegación en la web.\n")
def navegacion():
    webs = []
    index = 0
    while True:
        accion = input('Qué acción quieres relizar: \n - "Adelante" para avanzar \n - "Atras" para retroceder \n - Nombre de la web a la que quieres acceder \n - Salir para finalizar la navegación \n').lower()
        match accion:
            case 'adelante':
                if index < len(webs):
                    index += 1
                    print(f"Estás en {webs[index-1]}")
                else:
                    print("No hay nada más adelante.")
            case 'atras':
                if index > 1:
                    index -= 1
                    print(f"Estás en {webs[index-1]}")
                else:
                    print("No hay nada más atras.")
            case 'salir':
                print("Adiós.")
                break
            case _:
                webs.append(accion)
                index = len(webs)
                print(f"Estás en {accion}")

navegacion()
            
print("\nEjercicio de la impresora\n")

def imprimir():
    lista = []
    while True:
        accion = input("Qué quieres realizar: \n - 'Imprimir' para retirar el primer elemento de la cola. \n - Agrega un documento escribiendo su nombre. \n - 'Terminar' para salir. \n").lower()
        match accion:
            case 'imprimir':
                if len(lista) < 1:
                    print("No hay elementos para imprimir.")
                else:
                    elemento = lista.pop(0)
                    print(f"Se ha impreso el documento {elemento}")
            case 'terminar':
                break
            case _:
                lista.append(accion)

imprimir()