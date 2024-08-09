"""
Pilas y colas
"""

# Pila/Stack (LIFO/Ultimo en entrar, primero en salir)
items_pila = []


def apilar(item):
    items_pila.append(item)


def desapilar():
    if len(items_pila) > 0:
        items_pila.pop()
    else:
        print('La pila esta vacia.')


def pila_vacia():
    return len(items_pila) == 0


def tamaño_pila():
    return len(items_pila)


apilar(1)
apilar(2)
apilar(3)
print(f'Items de la pila al apilar: {items_pila}')
desapilar()
print(f'Items de la pila al desapilar: {items_pila}')
print(f'La pila esta vacia: {pila_vacia()}')
print(f'Tamaño de la pila: {tamaño_pila()}')
print()


# Cola/Queue (FIFO/Primero en entrar, primero en salir)
items_cola = []


def agregar_a_la_cola(item):
    items_cola.insert(0, item)


def quitar_de_la_cola():
    if len(items_cola) > 0:
        items_cola.pop()
    else:
        print('La cola esta vacia.')


def cola_vacia():
    return len(items_cola) == 0


def tamaño_cola():
    return len(items_cola)


agregar_a_la_cola(1)
agregar_a_la_cola(2)
agregar_a_la_cola(3)
print(f'Items de la cola despues de agregar a la cola: : {items_cola}')
quitar_de_la_cola()
print(f'Items de la cola despues de quitar de la cola: : {items_cola}')
print(f'Items de la cola: : {items_cola}')
print(f'La cola esta vacia: {cola_vacia()}')
print(f'Tamaño de la cola: : {tamaño_cola()}')
print()

"""
EXTRA
"""


def navegador():
    paginas = []
    ultima_pagina = ''

    while True:
        accion = input(
            'Ingrese una pagina o interactue con las palabras atras/adelante/salir: '
        ).lower()

        match accion:
            case 'atras':
                if len(paginas) > 0:
                    ultima_pagina = paginas.pop()
            case 'adelante':
                if ultima_pagina != '':
                    paginas.append(ultima_pagina)
            case 'salir':
                break
            case _:
                paginas.append(accion)

        if len(paginas) > 0:
            print(f'Esta en la página: {paginas[-1]}')
        else:
            print('Esta en la paina de inicio.')


navegador()


def impresora():
    documentos = []

    while True:
        accion = input('Ingrese un documento o interactue con las palabras imprimir/listar/salir: ')

        match accion:
            case 'imprimir':
                if len(documentos) > 0:
                    documento_impreso = documentos.pop()
                    print(f'Se ha impreso el documento: {documento_impreso}')
            case 'salir':
                break
            case 'listar':
                if len(documentos) > 0:
                    for documento in documentos:
                        print(documento)
            case _:
                documentos.insert(0, accion)
                print(f'Ha agregado a la cola de impresión el documento: {accion}')

        if len(documentos) == 0:
            print('No hay documentos en cola de impresión.')


impresora()
