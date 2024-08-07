"""
    Una pila se puede inplementar en python utilizando una lista como estructura
    de datos base. Las operaciones de apilar y desapilar se pueden realizar utilizando
    los metodos append() y pop de la lista
"""

pila = []


def apilar(elemento):
    pila.append(elemento)


def desapilar():
    return pila.pop()


def esta_vacia():
    return len(pila) == 0


def tamanio():
    return len(pila)


apilar(1)
apilar(2)
apilar(3)

print(desapilar())  # 3
print(desapilar())  # 2
print(desapilar())  # 1


"""
Colas
"""
cola = []


def agregar(elemento):
    cola.append(elemento)


def quitar():
    return cola.pop(0)


def empty():
    return len(cola) == 0


def lenght():
    return len(cola)


agregar(1)
agregar(2)
agregar(3)

print(quitar())  # 1
print(quitar())  # 2
print(quitar())  # 3


# Dificultad extra: Implementar pilas y cadenas de texto y simular navegar entre webs
pila = ['www.spider.com', 'www.wolverine.es', 'www.flash.mx']


def w_new(elemento):
    global pila
    pila.append(elemento)
    return str(elemento)


def atras():
    global pila
    aux = pila.pop()
    if len(pila) > 0:
        pila.insert(0, aux)
        return pila[-1]
    else:
        return "No existe web"


def siguiente():
    global pila
    if len(pila) > 0:
        aux = pila.pop(0)
        pila.append(aux)
        actual = pila[-1]
        return actual
    else:
        return "No hay web"


def navegar(direccion):
    global pila
    if direccion.lower() == "adelante":
        print(f"Estas navegando en: {siguiente()}")
    elif direccion.lower() == "atras":
        print(f"Estas navegando en: {atras()}")
    elif (direccion.startswith('www.')):
        # Se agrega la nueva página a la pila y se muestra
        pila.append(direccion)
        print(f"Mostrando página: {direccion}")
    else:
        print("Web invalida")


# Bucle principal de navegación
while True:

    direccion = input(
        "Introduce una dirección web ('salir' o 'adelante' o 'atras'): ")
    if direccion.lower() == 'salir':
        break
    navegar(direccion)

"""
    Utilizando colas y cadenas de texto, simular el mecanismo de impresora
"""

cola = ['Doc1', 'Doc2', 'Doc3', 'Doc4']


def imprimir():
    global cola
    print(f"El documento que se imprime es: {cola.pop(0)}")


def nuevo(doc):
    cola.append(doc)
    return doc


def imprime(doc):
    global pila
    if doc.lower() == "imprimir":
        imprimir()
    else:
        print(f"Añadir documento: {nuevo(doc)}")


while True:
    print("Documentos a imprimir: ")
    for docs in cola:
        print(docs)
    doc = input("Introduce si quieres imprimir o añadir documento o salir: ")
    if doc.lower() == 'salir':
        break
    imprime(doc)
