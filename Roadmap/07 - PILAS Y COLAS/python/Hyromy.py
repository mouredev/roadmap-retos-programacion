pila = []

print(pila) #[]

pila.append("Item 1")
pila.append("Item 2")
pila.append("Item 3")
pila.append("Item 4")
pila.append("Item 5")

print(pila) #[1, 2, 3, 4, 5]

pila.pop()
print(pila) #[1, 2, 3, 4]

for i in range(len(pila)):
    print(f"Item eliminado: {pila.pop()}")
else:
    print(pila)

""" ---------------- """

from collections import deque

cola = deque()

print(cola) #[]

cola.append("Elemento 1")
cola.append("Elemento 2")
cola.append("Elemento 3")
cola.append("Elemento 4")
cola.append("Elemento 5")

print(cola) #[1, 2, 3, 4, 5]

cola.popleft()
print(cola) #[2, 3, 4, 5]

for i in range(len(cola)):
    print(f"Elemento eliminado: {cola.popleft()}")
else:
    print(cola) #[]


# ---- DIFICULTAD EXTRA ----

nav = [0]
def navegador() -> None:    
    print(" ---- NAVEGADOR WEB ----")
    print("Selecciona una opción del navegador")
    while True:
        print("( B ) Buscar \n" +
              "( <- ) Regresar\n" +
              "( -> ) Avanzar\n" +
              "( X ) Salir")
        opt = input("=> ")

        if opt.casefold() == "b":
            buscar(nav)

        elif opt == "<-" or opt.casefold() in "regresar":
            regresar()

        elif opt == "->" or opt.casefold() in "avanzar":
            avanzar()

        elif opt.casefold() == "x":
            break

        else:
            print("\n(!) OPCION NO VALIDA\n")


def buscar(nav:list):
    print("\nEscribe el sitio que quieras buscar")
    busqueda = input("=> ")

    if nav[0] != len(nav) -1:
        i = nav[0] + 1
        copy = nav[:i] 
        nav.clear()

        for i in copy:
            nav.append(i)

    nav.append(busqueda)
    nav[0] += 1

    current()

def regresar():
    if nav[0] -1 <= 0:
        print("\n(!) NO PUEDES RERESAR MAS\n")
    else:
        nav[0] -= 1

    current()

def avanzar():
    if nav[0] +1 >= len(nav):
        print("\n(!) NO PUEDES AVANZAR MAS\n")
    else:
        nav[0] += 1

    current()

def current():
    index = nav[0]
    print(f"\nESTAS NAVEGANDO EN {nav[index]}\n")

navegador()