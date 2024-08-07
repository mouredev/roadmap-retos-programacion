# #07 PILAS Y COLAS
#### Dificultad: Media | Publicación: 12/02/24 | Corrección: 19/02/24

## Ejercicio

#
# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).
#
# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.
# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#   interpretan como nombres de documentos.
#

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        return self.items.pop()

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        return self.items.pop(0)

# Ejemplo de uso de la pila
pila = Pila()
pila.agregar(1)
pila.agregar(2)
pila.agregar(3)

print("Elementos en la pila:")
while not pila.esta_vacia():
    print(pila.eliminar())

# Ejemplo de uso de la cola
cola = Cola()
cola.agregar('a')
cola.agregar('b')
cola.agregar('c')

print("\nElementos en la cola:")
while not cola.esta_vacia():
    print(cola.eliminar())
    
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        return self.items.pop()


class NavegadorWeb:
    def __init__(self):
        self.historial_atras = Pila()
        self.historial_adelante = Pila()
        self.pagina_actual = ""

    def navegar(self, url):
        if self.pagina_actual:
            self.historial_atras.agregar(self.pagina_actual)
            self.historial_adelante = Pila()  # Limpiar historial adelante cuando navegamos a una nueva página
        self.pagina_actual = url
        print("Navegando a:", url)

    def retroceder(self):
        if not self.historial_atras.esta_vacia():
            pagina_anterior = self.historial_atras.eliminar()
            self.historial_adelante.agregar(self.pagina_actual)
            self.pagina_actual = pagina_anterior
            print("Navegando hacia atrás a:", pagina_anterior)
        else:
            print("No hay páginas disponibles para retroceder.")

    def avanzar(self):
        if not self.historial_adelante.esta_vacia():
            pagina_siguiente = self.historial_adelante.eliminar()
            self.historial_atras.agregar(self.pagina_actual)
            self.pagina_actual = pagina_siguiente
            print("Navegando hacia adelante a:", pagina_siguiente)
        else:
            print("No hay páginas disponibles para avanzar.")

    def mostrar_pagina_actual(self):
        print("Página actual:", self.pagina_actual)


# EXTRA: SIMULA MECANISMO ADELANTE O ATRAS DE UN PAGINA WEB
if __name__ == "__main__":
    navegador = NavegadorWeb()

    while True:
        entrada = input("Introduce una URL o 'adelante'/'atras' para navegar (o 'salir' para salir): ")

        if entrada.lower() == "salir":
            print("Saliendo del navegador.")
            break
        elif entrada.lower() == "adelante":
            navegador.avanzar()
        elif entrada.lower() == "atras":
            navegador.retroceder()
        else:
            navegador.navegar(entrada)

        navegador.mostrar_pagina_actual()
    

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None


class ImpresoraCompartida:
    def __init__(self):
        self.cola_impresion = Cola()

    def recibir_documento(self, documento):
        self.cola_impresion.agregar(documento)
        print("Documento recibido:", documento)

    def imprimir_documento(self):
        documento = self.cola_impresion.eliminar()
        if documento:
            print("Imprimiendo:", documento)
        else:
            print("No hay documentos en la cola de impresión.")

    def mostrar_cola(self):
        if self.cola_impresion.esta_vacia():
            print("Cola de impresión vacía.")
        else:
            print("Cola de impresión:", self.cola_impresion.items)

# EXTRA: SIMULA EL MECANISMO DE UNA IMPRESORA
if __name__ == "__main__":
    impresora = ImpresoraCompartida()

    while True:
        entrada = input("Introduce un documento para imprimir o 'imprimir' para imprimir un documento (o 'salir' para salir): ")

        if entrada.lower() == "salir":
            print("Saliendo del programa.")
            break
        elif entrada.lower() == "imprimir":
            impresora.imprimir_documento()
        else:
            impresora.recibir_documento(entrada)

        impresora.mostrar_cola()
