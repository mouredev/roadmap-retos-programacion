# #07 PILAS Y COLAS

# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).

"""
LIFO: Last in, first out
Describe el orden en que los elementos procesados o eliminados de una estructura de datos.
Como una pila, el último elemento que se coloca es el primero en ser retirado
Hay dos métodos que se utilizan para interactuar con estos elementos:
- push / en python append(valor) (ingresa un elemento al final de la cola)
- pop() (retira el último elemento y devuelve su valor)
- se pueden manejar con listas o arrays
"""
print("LIFO")
pila = ['alpha','beta','gamma','delta','epsilon','zeta','eta','teta']
print(f"Lista inicial:\n{pila}")
pila.append('iota')
print(f"Método push, se inserta un último elemento:\n{pila}")
print(f"Método pop, se retira el último elemento (.pop()) y devuelve su valor:\n{pila.pop()}\n")


"""
FIFO: Last in, first out
Describe el orden en que los elementos procesados o eliminados de una estructura de datos.
Se refiere a una cola, como una cola de clientes, el primero en entrar es el primero en salir
Hay dos métodos que se utilizan para interactuar con estos elementos:
- push / en python append(valor) (ingresa un elemento al final de la cola)
- pop(0) (retira el primer elemento y devuelve su valor)
- se pueden manejar con listas o arrays
"""
print("FIFO")
pila = ['α','β','γ','δ','ε','ζ','η','θ']
print(f"Lista inicial:\n{pila}")
pila.append('ι')
print(f"Método append(valor), se inserta un último elemento:\n{pila}")
print(f"Método pop(0), se retira el primer elemento y devuelve su valor:\n{pila.pop(0)}\n")

#### FIFO y LIFO con arrays
import array

arreglo = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print(f"Arreglo (array) inicial:\n{arreglo}")

arreglo.append(9)
print(f"Arreglo con método append():\n{arreglo}\n")

# LIFO: Elimina el último elemento
print(f"LIFO con método pop():\n{arreglo.pop()}")
print(f"Arreglo después del LIFO:\n{arreglo}\n")

arreglo.append(9)

# FIFO: Elimina el primer elemento
print(f"FIFO con método pop(0):\n{arreglo.pop(0)}")
print(f"Arreglo después del FIFO:\n{arreglo}")

### Con la libreria queue

import queue

pila = queue.LifoQueue(3)
cola = queue.Queue(3)

pila.put(4)
pila.put(5)
pila.put(6)
cola.put(7)
cola.put(8)
cola.put(9)

print("Cola FIFO")
print(cola.get())
print(cola.get())
print(cola.get())
print("\nCola LIFO")
print(pila.get())
print(pila.get())
print(pila.get())


###################
""" 
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
 """

#### NAVEGADOR

hist_back = []
hist_ford = []

def navegar():
    x = input("Qué sitio desea visitar?")
    hist_back.append(x)
    hist_ford.clear()
    print(f"Visitaste {x}!!")


def avanzar():
    if hist_ford: # Verifica que la lista no esté vacía    
        y = hist_ford.pop()
        hist_back.append(y)
        print(f"Avanzaste a {y}!!")
    else:
        print("No hay páginas a las que avanzar x_x")

def retroceder():
    if hist_back:
        if len(hist_back) == 1:
            z = hist_back.pop()
            hist_ford.append(z)
            print("Estás en la página de inicio, no hay hacia dónde retroceder :/")
        else:
            z = hist_back.pop()
            hist_ford.append(z)
            print(f"Retrocediste a {hist_back[-1]}!!")
    else:
        print("No hay páginas a las que retroceder :(")

def historial():
    if hist_back:
        print("Historial:")
        for j,k in zip(hist_back,range(len(hist_back))):
            print(f"{k+1}. {j}")
    else:
        print(f"El historial está vacío")    


def browser():

    # Bucle que permite navegar continuamente
    while True:
        i = input("""
Ha ingresado Shin Navi, qué acción desea realizar:
            1. Nueva página
            2. Avanzar
            3. Retroceder
            4. Historial              
            5. Salir                                          
""")
        if i == "1":
            navegar()
        elif i == "2":
            avanzar()
        elif i == "3":
            retroceder()
        elif i == "4":
            historial()
        elif i == "5":
            print("Saliendo del navegador! Bye!")
            break
        else:
            print("Opción no válida. Inténtelo nuevamente c:")

# browser()        


#### Impresoras
"""
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""
class shared_printer:
    def __init__(self):
        self.cola = []

    def imprimir(self):
        if self.cola:
            printed = self.cola.pop(0)
            print(f"Ha impreso: {printed}")
        else:
            print("La cola de impresión está vacia")

    def cola_impresion(self):
        if self.cola:
            for i,j in zip(self.cola,range(len(self.cola))):
                print(f"{j+1}. {i}")
        else:
            print("La cola de impresión está vacia")   

    def agregar_documento(self, opcion):
        self.cola.append(opcion)
        print(f"Ha añadido {opcion} a la cola de impresión")

    def run(self):
        while True:
            opcion = input(
"""
Si desea imprimir, escriba: imprimir.
Si desea revisar la cola de impresión escriba: cola
De otra forma, ingrese el nombre de su documento.
Si desea salir, escriba: salir

""")            
            if len(self.cola) <= 3:

                if opcion.lower() == "imprimir":
                    self.imprimir()
                elif opcion.lower() == "cola":
                    self.cola_impresion()
                elif opcion.lower() == "salir":
                    print("Ha salido de la impresora")
                    break
                elif opcion == "":
                    print("No ha ingresado ningún valor")
                else:
                    self.agregar_documento(opcion)
            else:
                x = input(
"""
La cola está llena, debe imprimir un documento antes de continuar
Escriba imprimir para imprimir
Escriba cola para revisar la cola
Escriba salir para salir
""")
                if x.lower() == "imprimir":
                    self.imprimir()
                elif x.lower() == "cola":
                    self.cola_impresion()
                elif x.lower() == "salir":
                    print("Ha salido de la impresora")
                    break
                else:
                    print("Escoja alguna de las opciones anteriores")

impresora = shared_printer()
impresora.run()