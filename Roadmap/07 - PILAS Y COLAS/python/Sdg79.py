
pila = []
pila.append("Sergio")
pila.append("Laura")
pila.append("Mica")
print(pila)

del pila[-1]
# pila.pop() funcion del sitema para desapilar
print(pila)


cola = []
cola.append("Sergio")
cola.append("Laura")
cola.append("Mica")
print(cola)

del cola[0]
# cola.pop(0) funcion del sistema para eliminar el elemento 0
print(cola)


# DIFICULTAD EXTRA:

cola = []

def web():
    index = -1
    while True:
        seleccion = input("Ingrese una web o use las palabras adelante, atras, salir: ")
        if seleccion == "adelante":
            if len(cola)-1 == index:
                print("no hay mas paginas web")
                print(cola[index])
            else:
                index += 1
                print(cola[index])
            
        elif seleccion == "atras":
            if (index + 1) == 0:
                print("No ha cargado ninguna pagina web")
            elif index == 0:
                print("Es la primer pagina web")
                print(cola[index])
            else:
                index -= 1
                print(cola[index])
            
        elif seleccion == "salir":
            print(cola)
            break
        else:
            cola.append(seleccion)
            index += 1
            print(cola[index])
            
web()

"""
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """

cola = []

def impresora():
    while True:
        documento = input("Ingrese un documento o use las palabras imprimir o salir: ")
        if documento == "imprimir":
            if len(cola) == 0:
                print("no hay archivos para imprimir")
            else:
                print(f"Imprimiendo: {cola[0]}")
                cola.pop(0)

            
        elif documento == "salir":
            print(cola)
            break
        else:
            cola.append(documento)
            print(cola)
            
impresora()