"""
Pilas y colas
"""


class Pila:
    def __init__(self):
        self.items = []

    def aplilar(self, item):
        self.items.append(item)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError('La pila esta vacia')

    def es_vacia(self):
        return len(self.items) == 0

    def tamaño_pila(self):
        return len(self.items)


pila = Pila()
pila.aplilar(1)
pila.aplilar(2)
pila.aplilar(2)
pila.desapilar()
print(f'Items de la pila: {pila.items}')
print(f'La pila esta vacia: {pila.es_vacia()}')
print(f'Tamaño de la pila: {pila.tamaño_pila()}')
print()


class Cola:
    def __init__(self):
        self.items = []

    def poner_en_cola(self, item):
        self.items.insert(0, item)

    def quitar_de_la_cola(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError('La cola esta vacia')

    def es_vacia(self):
        return len(self.items) == 0

    def tamaño_cola(self):
        return len(self.items)


cola = Cola()
cola.poner_en_cola(1)
cola.poner_en_cola(2)
cola.poner_en_cola(3)
cola.poner_en_cola(4)
cola.quitar_de_la_cola()
print(f'Items de la cola: : {cola.items}')
print(f'La cola esta vacia: {cola.es_vacia()}')
print(f'Tamaño de la cola: : {cola.tamaño_cola()}')
print()

"""
EXTRA
"""


def navegador():
    paginas = []

    while True:
        accion = input(
            'Ingrese una pagina o interactue con las palabras atras/adelante/salir: '
        ).lower()

        match accion:
            case 'atras':
                if len(paginas) > 0:
                    paginas.pop()
            case 'adelante':
                pass
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
