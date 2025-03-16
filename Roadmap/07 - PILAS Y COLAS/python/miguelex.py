pila = []

pila.append(3)
pila.append(2)
pila.append(1)

print("Mostramos la pila")
print(pila)

pila.pop()

print("Mostramos la pila tras sacar el elemento en la parte superior")
print(pila)


cola = []

cola.append(1)
cola.append(2)
cola.append(3)

print("Mostramos la cola")
print(cola)

cola.pop(0)

print("Mostramos la cola tras sacar el elemento en la parte inferior")
print(cola)


# Extra

pila = []

while True:
    
    action = input(
        "Añade url/adelante/atras/salir: "
    )

    if action == "salir":
        print("Saliendo del navegador web.")
        break
    elif action == "adelante":
        pass
    elif action == "atras":
        if len(pila) > 0:
            pila.pop()
    else:
        pila.append(action)

    if len(pila) > 0:
        print(f"Has navegado a la web: {pila[len(pila) - 1]}.")
    else:
        print("Estás en la página de inicio.")


cola = []

while True:
        
        action = input("Nombre del documento/imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(cola) > 0:
                print(f"Imprimiendo: {cola.pop(0)}")
        else:
            cola.append(action)

        print(f"Cola de impresión: {cola}")