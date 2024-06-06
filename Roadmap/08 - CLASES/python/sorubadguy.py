"""
*Clases
"""

#?Ejemplo de definicion de clase
class Ejemplo:

    #?atributo de clase
    numero = 32

    #?Inicializador de la clase
    def __init__(self) -> None:
        pass

    #?Funcion propia de la clase
    def mostrar_ejemplo(self):
        print("Hola Soy una clase")

print(Ejemplo.numero)

#!Instancia de una clase
x = Ejemplo()
x.mostrar_ejemplo()
y = Ejemplo()
x.mostrar_ejemplo()
