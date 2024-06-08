import time
"""
*Clases
"""

#?Ejemplo de definicion de clase
class Perro:

    #?Atributo general de la clase
    
    
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

#?Herencia, raza tiene las mismas caracteristicas de perro, ademas de las suyas propias

class Raza(Perro):

    def __init__(self, nombre: str, color_pelo: str, tipo_pelo: str, altura: float, raza = "puro perro"):
        super().__init__(nombre)
        self.raza = raza
        self.color_pelo = color_pelo
        self.tipo_pelo = tipo_pelo
        self.altura = altura

    def mostrar_raza(self):
        print(f"Raza: {self.raza}\nTipo de Pelo: {self.tipo_pelo}\nColor del Pelo: {self.color_pelo}\nAltura: {self.altura} mt(s)")

perro3 = Raza("pancho", "marron", "corto", 1.2)
perro3.agregar_truco("Hacerce el muertito")
perro3.mostrar_raza()
print(perro3.trucos) #?caracteristica de la clase perro, heredada por raza