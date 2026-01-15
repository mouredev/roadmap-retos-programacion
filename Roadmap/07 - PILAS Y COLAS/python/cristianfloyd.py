"""* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
*"""

# pila/Stack (LIFO)
print("=" * 80)
print("PILA/STACK (LIFO)")
print("=" * 80)

stack = []
# push
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack luego de agregar elementos: {stack}")
# pop
item_extraido = stack.pop()
print(f"Stack luego de eliminar el último elemento: {stack}")
print(f"Elemento extraído de la pila: {item_extraido}")

stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(f"Elemento extraído de la pila: {stack_item}")
print(f"Stack luego de eliminar el último elemento: {stack}")

# cola/Queue (FIFO)
print("=" * 80)
print("COLA/QUEUE (FIFO)")
print("=" * 80)

queue = []
# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(f"Queue luego de agregar elementos: {queue}")

# dequeue
item_extraido_cola = queue.pop(0)
print(f"Queue luego de eliminar el primer elemento: {queue}")
print(f"Elemento extraído de la cola: {item_extraido_cola}")


class Pila:
    def __init__(self, lista: list = []) -> None:
        self.items = lista

    def esta_vacia(self) -> bool:
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def apilar(self, valor) -> None:
        """Añade un elemento al tope de la pila."""
        self.items.append(valor)

    def desapilar(self):
        """Elimina y retorna el elemento del tope de la pila."""
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def buscar(self, valor):
        """Busca un elemento en la pila."""
        return valor in self.items

    def ver_tope(self):
        """Retorna el elemento del tope de la pila sin eliminarlo."""
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")

    def ver(self):
        """Retorna todos los elementos de la pila."""
        return self.items
    
    def limpiar(self) -> None:
        """Limpia todos los elementos de la pila."""
        self.items = []

    def __len__(self):
        """Retorna el número de elementos en la pila."""
        return len(self.items)


# Ejemplo de uso de la clase Pila
print("=" * 80)
print("Ejemplo de uso de la clase Pila:")
print("=" * 80)
objeto_pila = Pila([1, 2, 3])
print(f"Elementos en la pila: {objeto_pila.ver()}")

objeto_pila.apilar(4)
print(f"Elementos en la pila después de apilar 4: {objeto_pila.ver()}")

item_extraido = objeto_pila.desapilar()
print(f"Elementos en la pila después de desapilar: {objeto_pila.ver()}")
print(f"Elemento extraído de la pila: {item_extraido}")

print(f"¿Está vacía la pila? {objeto_pila.esta_vacia()}")

print(f"Elemento en el tope de la pila: {objeto_pila.ver_tope()}")

print(f"¿El valor 2 está en la pila? {objeto_pila.buscar(2)}")

print(f"Número de elementos en la pila: {len(objeto_pila)}")


class Cola:
    def __init__(self, items: list = []) -> None:
        self.items = items

    def esta_vacia(self) -> bool:
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def encolar(self, valor) -> None:
        """Añade un elemento al final de la cola."""
        self.items.append(valor)

    def desencolar(self):
        """Elimina y retorna el elemento al frente de la cola."""
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def buscar(self, valor) -> bool:
        """Busca un elemento en la cola."""
        return valor in self.items

    def ver_frente(self):
        """Retorna el elemento al frente de la cola sin eliminarlo."""
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")

    def ver(self) -> list:
        """Retorna todos los elementos de la cola."""
        return self.items

    def __len__(self) -> int:
        """Retorna el número de elementos en la cola."""
        return len(self.items)

    def __add__(self, valor):
        """Permite usar el operador + para encolar un elemento."""
        self.encolar(valor)
        return self


# Ejemplo de uso de la clase Cola
print("=" * 80)
print("Ejemplo de uso de la clase Cola:")
print("=" * 80)
objeto_cola = Cola([1, 2, 3])
print(f"Elementos en la cola: {objeto_cola.ver()}")

objeto_cola.encolar(4)
print(f"Elementos en la cola después de encolar 4: {objeto_cola.ver()}")
objeto_cola + 5
print(f"Elementos en la cola después de encolar 5 usando '+': {objeto_cola.ver()}")

print(f"Elemento en el frente de la cola: {objeto_cola.ver_frente()}")
item_extraido = objeto_cola.desencolar()
print(f"Elementos en la cola después de desencolar: {objeto_cola.ver()}")
print(f"Elemento extraído de la cola: {item_extraido}")

print(f"¿Está vacía la cola? {objeto_cola.esta_vacia()}")

print(f"¿El valor 2 está en la cola? {objeto_cola.buscar(2)}")

print(f"Número de elementos en la cola: {len(objeto_cola)}")



"""  * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 *    """

class NavegadorWeb:
    """
    Simula un navegador web con funcionalidad adelante/atrás utilizando una pila.
    """
    def __init__(self):
        self.historial = Pila()
        self.adelante_stack = Pila()
        self.pagina_actual = None

    def navegar_a(self, url: str):
        if self.pagina_actual:
            self.historial.apilar(self.pagina_actual)
        self.pagina_actual = url # se establece la nueva página actual
        self.adelante_stack.limpiar()  # limpiar el stack de adelante al navegar a una nueva página
        print(f"Navegando a: {self.pagina_actual}")

    def atras(self):
        if not self.historial.esta_vacia(): # verificar historial no vacio
            self.adelante_stack.apilar(self.pagina_actual)
            self.pagina_actual = self.historial.desapilar()
            print(f"Regresando a: {self.pagina_actual}")
        else:
            print("No hay páginas en el historial.")
        
    def añadir_pagina(self, url: str):
        if self.pagina_actual:
            self.historial.apilar(self.pagina_actual)
        self.pagina_actual = url
        print(f"Navegando a: {self.pagina_actual}")

    def adelante(self):
        if not self.adelante_stack.esta_vacia():
            self.historial.apilar(self.pagina_actual)
            self.pagina_actual = self.adelante_stack.desapilar()
            print(f"Avanzando a: {self.pagina_actual}")
        else:
            print("No hay páginas adelante.")

    def obtener_pagina_actual(self):
        return self.pagina_actual

def simulacion_navegador():
    firefox = NavegadorWeb()
    while True:
        accion = input("Ingresa una URL, 'atras', 'adelante' o 'salir': ")
        if accion == "salir":
            print("Saliendo del navegador.")
            break
        elif accion == "atras":
            firefox.atras()
        elif accion == "adelante":
            firefox.adelante()
        else:
            firefox.navegar_a(accion)
        print(f"Página actual: {firefox.obtener_pagina_actual()}")


simulacion_navegador()


#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se

class impresoraCompartida:
    """
    Simula una impresora compartida utilizando una cola.
    """
    def __init__(self):
        self.cola_impresion = Cola()

    def agregar_documento(self, documento: str):
        self.cola_impresion.encolar(documento)
        print(f"Documento '{documento}' agregado a la cola de impresión.")

    def imprimir(self):
        if not self.cola_impresion.esta_vacia():
            documento_a_imprimir = self.cola_impresion.desencolar()
            print(f"Imprimiendo documento: {documento_a_imprimir}")
        else:
            print("No hay documentos en la cola de impresión.")

def simulacion_impresora():
    epson_lx300 = impresoraCompartida()
    while True:
        accion = input("Ingresa el nombre del documento para agregar a la cola, 'imprimir' o 'salir': ")
        match accion:
            case "salir":
                print("Saliendo de la impresora.")
                break
            case "imprimir":
                epson_lx300.imprimir()
            case _:
                epson_lx300.agregar_documento(accion)

simulacion_impresora()