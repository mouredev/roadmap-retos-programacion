print("""
Clases
""")


class Phone:
    reference = '000'

    def __init__(self, marca: str, serie: str, anio: int):
        self.marca = marca
        self.anio = anio
        self.serie = serie

    def imprimir(self):
        print(f'Celular marca {self.marca}, serie {self.serie}, referencia {self.reference} del año {self.anio}')


class_phone = Phone(marca='Xiaomi', serie='Note 10 Pro', anio=2024)
class_phone.imprimir()
class_phone.marca = 'Poco'
class_phone.imprimir()
print()

print("""
EXTRA
""")

print('Pila:')


class Stack:
    def __init__(self):
        self.stack_items = []

    def push_item(self, item):
        self.stack_items.append(item)

    def pop_item(self):
        if len(self.stack_items) > 0:
            self.stack_items.pop()

    def count_items(self):
        print(len(self.stack_items))

    def get_items(self):
        print(self.stack_items)


stack = Stack()
stack.push_item(1)
stack.push_item(2)
stack.push_item(3)
stack.get_items()
stack.pop_item()
stack.pop_item()
stack.get_items()
stack.count_items()
print()


print('Cola:')


class Cola:
    def __init__(self):
        self.cola_items = []

    def push_item(self, item):
        self.cola_items.insert(0, item)

    def pop_item(self):
        if len(self.cola_items) > 0:
            self.cola_items.pop()

    def get_items(self):
        print(self.cola_items)

    def count_items(self):
        print(len(self.cola_items))


cola = Cola()
cola.push_item(1)
cola.push_item(2)
cola.push_item(3)
cola.push_item(4)
cola.get_items()
cola.pop_item()
cola.pop_item()
cola.get_items()
cola.count_items()
