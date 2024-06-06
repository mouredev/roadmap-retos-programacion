import time
"""
*Clases
"""

#?Ejemplo de definicion de clase
class Ejemplo:

    #?atributo de clase
    
    #?Inicializador de la clase
    def __init__(self) -> None:
        self.hora = time.time_ns()

    #?Funcion propia de la clase
    def mostrar_ejemplo(self):
        print("Hola Soy una clase")

    def mostrar_hora(self):
        print(self.hora)

#!Instancia de una clase
#?Inicializo la instancia
x = Ejemplo()
x.mostrar_hora()
x.mostrar_ejemplo