# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝

# ----------------------------------------
# Pilas(stack - LIFO):
# ----------------------------------------
# - Es una estructura de datos. 
# - Sigue el principio LIFO (last in, first out), significa que
#   el último elemento añadido, es el primero en ser retirado.
# Implementar:
class stack:
    def __init__(self):
        self.elements = []
    
    def __len__(self): # total elementos.
        return len(self.elements)

    def is_empty(self): # es vacia.
        return len(self) == 0
    
    def push(self, item): # Agregar elemento.
        self.elements.append(item)
    
    def push_batch(self, items): # Agregar multiples.
        # use <history.push_batch(["1", "2", "3"])">
        self.elements.extend(items)
    
    def pop_get(self): # Eliminar y obtener.
        if not self.is_empty():
            return self.elements.pop()
        else: 
            return None
    
    def get_top(self): # Obtener sin eliminar.
        if not self.is_empty():
            return self.elements[-1]
        else: 
            return None
    
    def get_tuple(self): # retornar pila como tupla.
        return tuple(reversed(self.elements))
    
    def clear(self): # vaciar pila.
        self.elements.clear()
# ____________________________________________
# Ejercicio usando la implementación de pilas:
"""
Simula el mecanismo adelante/atrás de un navegador web.
- Crea un programa en el que puedas navegar a una página o indicarle que te quieres 
  desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
- Las palabras "adelante", "atrás" desencadenan esta acción, el resto 
  se interpreta como el nombre de una nueva web.
"""

msg_nav = """
Historial de navegación:
-------------------------------------------------
Usar: "<" para página anterior.
      ">" para página adelante.
      "h" Ver historial completo.
      "x" para salir. 
Escribir web para agregar:
-------------------------------------------------"""
def nav_history(history, back_history, forward_history):
    def web(url):
        print(f"({len(back_history)}) <- Atras <-[Actual: {url}]-> Delante -> ({len(forward_history)})")

    def back():
        if not back_history.is_empty():
            forward_history.push(history.get_top()) # Obtener sin eliminar.
            history.push(back_history.pop_get())    # Eliminar y obtener.
            web(history.get_top()) 
        else:
            print("No hay página previa.")

        select()

    def forward():
        if not forward_history.is_empty():
            back_history.push(history.get_top())
            history.push(forward_history.pop_get())
            web(history.get_top())
        else:
            print("No hay página siguiente.")

        select()

    def new_web(url):
        back_history.push(history.get_top())
        forward_history.clear()
        history.push(url)
        web(history.get_top())
        select()

    def the_history():
        if not history.is_empty():
            for item in history.get_tuple():
                print(item)
        else:
            print("Historial vacío.")

        select()

    def select():
        print("____________")
        action = input("acción: ")
        if len(action) > 0:
            match action:
                case "<": back()
                case ">": forward()
                case "x": main()
                case "h": the_history()
                case _:   new_web(action)
        else:
            print("Eres muy gracioso xD.")
            select()

    print(msg_nav)
    web(history.get_top())
    select()

# -----------------------------------------
# Colas (Queue - FIFO):
# -----------------------------------------
# - Estructura de datos que sigue el principio FIFO(First In, First Out)
# - El primer elemento que se inserta es el primero en ser retirado.
# Implementar:
from collections import deque
class queue:
    def __init__(self):
        self.elements = deque()

    def __len__(self): # total elementos.
        return len(self.elements)

    def is_empty(self): # es vacia.
        return len(self) == 0
    
    def enqueue(self, item): # agregar
        self.elements.append(item)

    def enqueue_all(self, items): # Agregar multiples.
        self.elements.extend(items)

    def dequeue(self): # Eliminar y devolver
        if not self.is_empty():
            return self.elements.popleft()
        else:
            return None
    
    def peek(self): # Obtener sin eliminar.
        if not self.is_empty():
            return self.elements[-1]
        else: 
            return None
    
    def get_tuple(self): # retornar cola como tupla.
        return tuple(self.elements)

    def clear(self): # vaciar cola.
        self.elements.clear()

# ____________________________________________
# Ejercicio usando la implementación de Colas:
"""
Simula el mecanismo de una impresora compartida.
- recibe documentos y los imprime cuando así se le indica.
- La palabra "imprimir" imprime un elemento de la cola.
- El resto de palabras se interpretan como nombres de documentos.
"""

msg_printer = """
------------------------------------------------
Usar: "p" Imprimir.
      "l" Ver documentos pendientes.
      "x" para salir.
Escribir nombre de documento para enviar a cola: 
------------------------------------------------"""
def queue_printer(doc_queue):
    def print_doc():
        if not doc_queue.is_empty():
            print(f"{doc_queue.dequeue()} -> ha sido impreso.")
            print(f"{len(doc_queue)} -> archivos faltantes")
        else:
            print("No hay archivos.")
        select()

    def queue_pending():
        if not doc_queue.is_empty():
            for doc in doc_queue.get_tuple():
                print(doc)
        else:
            print("No hay archivos.")

        select()

    def send_doc(doc):
        doc_queue.enqueue(doc)
        print("Archivo agregado a cola de impresión.")
        select()

    def select():
        print("____________")
        action = input("acción: ")
        if len(action) > 0:
            match action:
                case "p": print_doc()
                case "l": queue_pending()
                case "x": main()
                case _:   send_doc(action)
        else:
            print("Eres muy gracioso xD.")
            select()

    print(msg_printer)
    select()
#__________________________________________________________
#__________________________________________________________
msg_home = """
----------------------------------
Usar: "1" para simulador_navegador.
      "2" para simulador_impresora.
      "Otra tecla" para salir.
----------------------------------
"""
def main():
    def case_nav():
        back_history = stack()
        forward_history = stack()
        history = stack()
        history.push("Inicio")
        nav_history(history, back_history, forward_history)
    
    def case_printer():
        doc_queue = queue()
        doc_queue.enqueue_all(["a.pdf", "b.txt", "c.docx"])
        queue_printer(doc_queue)

    print(msg_home)
    select = input("seleccionar: ")
    match select:
        case "1": case_nav()          
        case "2": case_printer()
        case _: print("Bye")

if __name__ == "__main__":
    main()
