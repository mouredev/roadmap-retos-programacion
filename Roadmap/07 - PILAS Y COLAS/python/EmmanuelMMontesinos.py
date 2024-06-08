"""
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */
"""
print("---Ejercicio 07: Pilas y Colas---")
# Pilas, Ultimo en entrar primero en salir
pila = []
"""Añadiendo elementos a la pila"""
for n in range(1,11):
    pila.append(n)
    print(f"Añadido a pila: {n}")
"""Quitando elementos de la pila"""
for element in range(len(pila)):
    print(f"Quitado de pila: {pila.pop()}")

# Colas, Primero en entrar primero en salir
cola = []
"""Añadiendo elementos a la cola"""
for n in range(1,11):
    cola.append(n)
    print(f"Añadido a cola: {n}")
"""Quitando elementos de la cola"""
for element in range(len(cola)):
    print(f"Quitando de cola: {cola.pop(0)}")
    

"""
 * DIFICULTAD EXTRA (opcional):
 * x- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

# Navegador Pila
class Navegador:
    def __init__(self) -> None:
        self.paginas_visitadas = ["home"]
        self.puntero = -1
        self.pagina_actual = "home"
        
    def actual(self,puntero=-1):
        if puntero == - 1:
            self.puntero = puntero
            self.pagina_actual = self.paginas_visitadas[self.puntero]
        else:
            if puntero == 1:
                try:
                    self.puntero -= 1
                    self.pagina_actual = self.paginas_visitadas[self.puntero]
                except IndexError:
                    print("No hay paginas siguientes")
                
            elif puntero == 2:
                if self.puntero < 0:
                    try:
                        self.puntero += 1
                        self.pagina_actual = self.paginas_visitadas[self.puntero]
                    except IndexError:
                        print("No hay paginas anteriores")
                else:
                    print("No hay paginas anteriores")

    def mostrar_actual(self):
        print(f"Actual: {self.pagina_actual}")

    def siguiente(self,nueva_pagina="adelante"):
        if nueva_pagina.lower() != "adelante":
            if self.puntero == -1:
                self.paginas_visitadas.append(nueva_pagina)
                self.actual()
            else:
                self.paginas_visitadas = [n for n in self.paginas_visitadas[0:self.puntero + 1]]
                self.paginas_visitadas.append(nueva_pagina)
                self.actual()
            
        else:
            self.actual(2)
    
    def anterior(self):
        self.actual(1)

    def comando(self,comando):
        if comando.lower() == "atras":
            self.anterior()
            self.mostrar_actual()
        elif comando.lower() == "historial":
            print(f"Historial: {self.paginas_visitadas}")
        else:
            self.siguiente(comando)
            self.mostrar_actual()

# Pruebas
print("---Navegador---")
mi_navegador = Navegador()
mi_navegador.comando("pagina 1")
mi_navegador.comando("atras")
mi_navegador.comando("historial")
mi_navegador.comando("pagina 2")
mi_navegador.comando("historial")


# Impresora Cola

class Impresora:
    def __init__(self) -> None:
        self.cola = []
        self.paginas_pendientes = len(self.cola)
    
    def actualizar_pendientes(self):
        self.paginas_pendientes = len(self.cola)
        print(f"Paginas pendientes: {self.paginas_pendientes}\n{self.cola}")
        

    def agregar(self,documento):
        self.cola.append(documento)
        print(f"Agregado: {documento}")
    
    def imprimir(self):
        hoja_impresa = self.cola.pop(0)
        print(f"Documento impreso: {hoja_impresa}")
        self.actualizar_pendientes()
        
    def comando(self,comand):
        if comand.lower() == "imprimir":
            self.imprimir()
        else:
            self.agregar(comand)
            
# Pruebas
print("---Impresora---")
mi_impresora = Impresora()
mi_impresora.comando("Libro_mouredev.pdf")
mi_impresora.comando("Libro_minudev.pdf")
mi_impresora.comando("imprimir")
mi_impresora.comando("Libro_holamundo.pdf")
mi_impresora.comando("Libro_pildorasinformaticas.pdf")
mi_impresora.comando("imprimir")