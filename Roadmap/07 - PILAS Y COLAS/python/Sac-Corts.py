"""
  EJERCICIO
"""

# Clase Stack (Pila)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

pila = Stack()
pila.push(1)
pila.push(3)
pila.push(6)

print(pila.size()) # 3
print(pila.pop()) # 6
print(pila.peek()) # 3
print(pila.is_empty()) # False


# Clase Queue (Cola)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

fila = Queue()
fila.enqueue(1)
fila.enqueue(5)
fila.enqueue(10)

print(fila.size()) # 3
print(fila.dequeue()) # 1
print(fila.peek()) # 5
print(fila.is_empty()) # False


"""
 DIFICULTAD EXTRA
"""

# Navegador Web

historial = []
adelante = []

def navegar_a(pagina):
    historial.append(pagina)
    adelante.clear()

def ir_atras():
    if len(historial) > 1:
        adelante.append(historial.pop())
        print(f"Página actual: {historial[-1]}  | {historial} | {adelante}")
    else:
        print("No hay más páginas atrás.")

def ir_adelante():
    if adelante:
        historial.append(adelante.pop())
        print(f"Página actual: {historial[-1]}  | {historial} | {adelante}")
    else:
        print("No hay más páginas adelante.")

while True:
    comando = input("Introduce una página o 'atrás'/'adelante': ")
    if comando == "atrás" or comando == "atras":
        ir_atras()
    elif comando == "adelante":
        ir_adelante()        
    elif comando == "salir":
        print("Saliendo del navegador...")
        break
    else:
        navegar_a(comando)
        print(f"Página actual: {comando} | {historial} | {adelante}")



# Impresora

documentos = []

def agregar_documento(documento):
    documentos.append(documento)

def imprimir_documento():
    if len(documentos) > 0:
        imprimir = documentos.pop(0)
        print(f"Imprimiendo {imprimir} | {documentos}")
    else:
        print("No hay impresiones por el momento")

while True:
    comando = input("Introduce un documento o 'imprimir': ")
    if comando == "imprimir":
        imprimir_documento()
    elif comando == "salir":
        print("Apagando impresora...")        
        break
    else:
        agregar_documento(comando)
        print("Fila de impresión:", documentos)