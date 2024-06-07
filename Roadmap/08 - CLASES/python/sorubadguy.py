import time
"""
*Clases
"""

#?Ejemplo de definicion de clase
class Perro:

    #?Atributo general de la clase
    tipo = "Perro"
    
    #?Inicializador de la clase
    def __init__(self, nombre: str):
        self.nombre = nombre #?Atributo unico para cada instancia
        self.trucos = [] #?Si la lista estuviese como atributo general, todas las instancias de esta clase compartirian la misma lista

    def agregar_truco(self, truco):
        self.trucos.append(truco)

perro1 = Perro("Gero")
perro2 = Perro("Mily")

perro1.agregar_truco("saltar")
perro1.agregar_truco("voltereta")
perro2.agregar_truco("dar la pata")

print(f"{perro1.nombre} puede hacer los siguientes trucos: {perro1.trucos}")
print(f"{perro2.nombre} puede hacer los siguientes trucos: {perro2.trucos}")
