#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).

# Pilas (Stack):
class Pila:
    """Representa una pila con operaciones de apilar, desapilar y verificar. Usamos una lista. Esta estructura de datos es de comportamiento LIFO (Last In First Out). Esto quiere decir que el ultimo en ser anadido a la lista es el primero en salir."""
    def __init__(self):
        self.items = []
    def ver(self):
        return self.items
    def apilar(self, valor):
        self.items.append(valor)
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    def es_vacia(self):
            return self.items == []
    

# Colas (Queue):
class Cola:
    """Representa una cola con operaciones de apilcar, desapilar, y verificar. Usamos una lista. Esta estructura de datos es de comportamiento FIFO (First In First Out). Esto quiere decir que el ultimo en ser anadido va a ser el primero en irse."""
    def __init__(self):
        self.items = []
    def ver(self):
        return self.items
    def anadir_a_la_cola(self, valor):
        # Anadiendo el valor al inicio de la lista y moviendo los demas elementos a un indice mas.
        self.items.insert(0, valor)
    def sacar_de_la_cola(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La cola esta vacia")
    def es_vacia(self):
        return self.items == []
    
# Usando las pilas y colas:
    
# Generando una pila
pila1 = Pila()
print(f"Generando una pila:")
print(pila1.ver())
# Anadiendo elementos:
print(f"Anadiendo elementos...")
pila1.apilar("Primer Elemento")
pila1.apilar("Segundo Elemento")
pila1.apilar(3)
pila1.apilar(400)
print(pila1.ver())
# Sacar el ultimo elemento de la estructura
print(f"Sacando el ultimo elemento de la estructura")
ultimo_valor = pila1.desapilar()
print(pila1.ver())
print(f"Este era el ultimo elemento de la pila: {ultimo_valor}")
# Verificando si esta vacia:
print(f"Verificando si la pila esta vacia: {pila1.es_vacia()}")

# Generando una cola
cola1 = Cola()
print(f"Generando una cola:")
print(cola1.ver())
# Anadiendo elementos a la cola:
print(f"Anadiendo elementos a la cola:")
cola1.anadir_a_la_cola("Primer Elemento")
cola1.anadir_a_la_cola("Segundo Elemento")
cola1.anadir_a_la_cola(3)
cola1.anadir_a_la_cola(400)
print(cola1.ver())
# Sacar al primer elemento de la cola:
print(f"Sacando al primer elemento de la estructura")
ultimo_valor_de_la_cola = cola1.sacar_de_la_cola()
print(cola1.ver())
print(f"Este era el ultimo elemento de la cola: {ultimo_valor_de_la_cola}")
# Verificando si la cola esta vacia:
print(f"Verficando si la cola esta vacia: {cola1.es_vacia()}")

#  * DIFICULTAD EXTRA (opcional):

# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.

class Navegador:
    def __init__(self):
        self.items = []
        self.indice_actual = - 1
    def historial(self):
        return self.items
    def anadir_pagina(self, url):
        if isinstance(url, str):
            self.items.append(url)
        else:
            print("Solo se permiten anadir URLs")
    def avanzar(self):
        if self.indice_actual < len(self.items) - 1 and self.indice_actual != -1:
            pagina = self.items[self.indice_actual + 1]
            self.indice_actual =+ self.items.index(pagina)
            print(f"Pagina Actual: {pagina}")
        else:
            print("No hay mas paginas para avanzar")
    def retroceder(self):
        if self.indice_actual != 0:
            pagina = self.items[self.indice_actual - 1]
            self.indice_actual = self.items.index(pagina)
            print(f"Pagina Actual: {pagina}")
        else:
            print("No se puede retroceder mas")
    def eliminar_ultima_pagina_del_historial(self):
        return self.items.pop()
    
print("Creando el historial del navegador...")
chrome = Navegador()
# Viendo el historial del navegador:
print(f"Historial actual del navegador: {chrome.historial()}")

while True:
    accion = input("Que quieres hacer dentro del navegador?: Escribe (Historial, Anadir, Avanzar, Retroceder, Eliminar) o si quieres cerrar la ejecucion escribe (Cerrar):").lower()
    if accion == "historial":
        print(f"Este es el historial actual del navegador: {chrome.historial()}")
    elif accion == "anadir":
        url = input("Que pagina deseas anadir? Colocar URL completo:").lower()
        chrome.anadir_pagina(url)
    elif accion == "avanzar":
        chrome.avanzar()
    elif accion == "retroceder":
        chrome.retroceder()
    elif accion == "eliminar":
        chrome.eliminar_ultima_pagina_del_historial()
    elif accion == "cerrar":
        break

# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.

class Impresora:
    def __init__(self):
        self.items = []
    def anadir_documento(self, valor):
        if (isinstance(valor, str)):
            print(f"Anadiendo elemento: {valor}")
            self.items.insert(0, valor)
        else:
            print("El nombre del documento tiene que ser de valor str")
    def imprimir(self):
        if self.items != []:
            documento_impreso = self.items.pop()
            print(f"Imprimiendo documento....")
            print(f"Impreso: {documento_impreso}")
        else:
            print("No hay mas documentos que imprimir!")
    def cola_de_impresion(self):
        return self.items

print("Comprando impresora...")
impresora_nueva = Impresora()
print("Impresora habilitada!!")

while True:
    action = input("Que deseas hacer con la impresora? Escribe si: (Ver, Anadir, Imprimir o Apagar)").lower()
    if action == "anadir":
        documento = input("Escribe el nombre de documento a imprimir: ")
        impresora_nueva.anadir_documento(documento)
        print(f"Documento anadido: {documento}")
    if action == "imprimir":
        print(f"Imprimiendo..")
        impresora_nueva.imprimir()
    if action == "ver":
        cola_de_impresion = impresora_nueva.cola_de_impresion()
        print(cola_de_impresion)
    if action == "apagar":
        break