# Author: Héctor Adán 
# GitHub: https://github.com/hectorio23

##########################################
############ CLASE WEBPAGE ###############
##########################################

class WebPage:
    def __init__(self, title, index):
        self.title = title
        self.index = index

    def get_info(self):
        print(f"<Object WebPage - {self.title} at {hex(id(self))}>")

##########################################
############ CLASE STACK #################
##########################################

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    @property
    def size(self):
        return len(self.items)

##########################################
############ CLASE QUEUE #################
##########################################

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    @property
    def size(self):
        return len(self.items)

##########################################
############# FUNCIONES ##################
##########################################

def imprimir_menu(counter):
    stack = Stack()
    back_stack = Stack()
    index = WebPage("index", counter)
    stack.push(index)

    while True:
        print("\n=======================================================")
        print(f"          Bienvenido a la página No. {stack.size}")
        print("=======================================================")
        print("Atras (presiona 'a' | 'A')           Siguiente (presiona 's' | 'S')")
        choose = input("Opción del usuario> ")

        if len(choose) > 1:
            temporal = WebPage(choose, counter)
            stack.push(temporal)

        elif (choose.lower() == 'a') and (stack.size > 1):
            otro_temporal = stack.pop()
            otro_temporal.get_info()
            stack.items[-1].get_info()
            back_stack.push(otro_temporal)
            print("Mostrando página anterior...")

        elif (choose.lower() == 's') and (back_stack.size > 0):
            atras_temporal = back_stack.pop()
            atras_temporal.get_info()
            stack.items[-1].get_info()
            stack.push(atras_temporal)
            print("Mostrando siguiente página...")

        else:
            print("Opción no disponible. Por favor, crea una página web.")

##########################################
########### PROGRAMA PRINCIPAL ###########
##########################################

if __name__ == "__main__":
    q1 = Queue()
    s1 = Stack()
    counter = 1

    ##########################################
    ####### USO DE UN STACK DINÁMICO #########
    ##########################################

    print("\n************ USO DE UN STACK DINÁMICO ************")

    w1 = WebPage("Index", 2)
    w2 = WebPage("Account", 5)
    w3 = WebPage("Login", 6)

    print(f"\nCantidad de elementos de Stack antes de agregarlos: {s1.size} elementos")
    s1.push(w1)
    s1.push(w2)
    s1.push(w3)
    print(f"Cantidad de elementos de Stack después de agregarlos: {s1.size} elementos")

    s1.pop()
    s1.pop()
    s1.pop()
    print(f"Cantidad de elementos de Stack después de eliminarlos: {s1.size} elementos")

    ##########################################
    ####### USO DE UN QUEUE DINÁMICO #########
    ##########################################

    print("\n************ USO DE UN QUEUE DINÁMICO ************")

    print(f"\nCantidad de elementos de Queue antes de agregarlos: {q1.size} elementos")
    q1.push(w1)
    q1.push(w2)
    q1.push(w3)
    print(f"Cantidad de elementos de Queue después de agregarlos: {q1.size} elementos")

    q1.pop()
    q1.pop()
    q1.pop()
    print(f"Cantidad de elementos de Queue después de eliminarlos: {q1.size} elementos")

    ##########################################
    ############### MENU PRINCIPAL ############
    ##########################################

    imprimir_menu(counter)
