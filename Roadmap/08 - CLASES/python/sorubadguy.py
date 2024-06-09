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

class Raza(Perro):#!Las clases pueden heredar tambien 2 o mas clases base

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

"""
!Extra
"""
"""
*Clase Pila
"""
class Pila:

    def __init__(self, pila = []) -> None:
        self.pila = []
        if len(pila) == 0:
            self.pila = []
        else:
            for i in range(0, len(pila)):
                self.pila.append(pila[i])


    def tamano_pila(self):
        print(f"La pila posee {len(self.pila)} elementos")

    def anadir_elemento(self):
        self.pila.append(input("Ingrese el valor a agregar: "))
    
    def quitar_elemento(self):
        self.pila.pop()
    
    def mostrar_contenido(self):
        elemento = self.pila.pop()
        print(elemento)
        if(len(self.pila) > 0):
            self.mostrar_contenido()
        self.pila.append(elemento)


pila = Pila([1,2,3,4,5,6,7,8,9])
pila.tamano_pila()
pila.mostrar_contenido()
#pila.anadir_elemento()
pila.tamano_pila()
pila.mostrar_contenido()
pila.quitar_elemento()
pila.mostrar_contenido()

"""
*Clase Cola
"""

class Cola:

    def __init__(self, cola = []) -> None:
        self.cola = []
        if len(cola) == 0:
            self.cola = []
        else:
            for i in range(0, len(cola)):
                self.cola.append(cola[i])

    def tamano_cola(self):
        print(f"La cola posee {len(self.cola)} elementos")

    def anadir_elento(self):
        self.cola.append(input("Ingrese el valor a agregar: "))

    def quitar_elemento(self):
        self.cola.pop(0)

    def mostrar_contenido(self):
        for i in range(0, len(self.cola)):
            print(self.cola[i])


cola = Cola([1,2,3,4,5,6,7,8,9])
cola.anadir_elento()
cola.tamano_cola()
cola.quitar_elemento()
cola.tamano_cola()
cola.mostrar_contenido()