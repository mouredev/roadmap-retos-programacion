# @Roni
"""
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos utilizando su función.
"""
class Iguana:
    def __init__(self,genero="",endemico="", especie="") -> None:
        self.genero=genero
        self.endemico=endemico
        self.especie=especie
    def imprimir(self):
        print(f"Genero: {self.genero}\nEndemico: {self.endemico} \nEspecie:{self.especie}")

ig1=Iguana() # --> Instanciamos/Incicalizamos la clase
print("****IGUANA****")
"""Le asignamos los valores"""
ig1.genero="Macho"
ig1.endemico="Sudamerica"
ig1.especie="Iguana"
ig1.imprimir() # --> Llamamos al método que nos devolvera los valores
"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola
(estudiadas en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""
class Pila:
    def __init__(self,datos=None) -> None:
        self.datos=list()
    def añadir(self,dato):
        self.datos.append(dato)
    def eliminar(self):
        if len(self.datos)>0:
            self.datos.pop()
        else:
            print("La pila esta vacía")
    def numeroDeElementos(self) -> int:
        return len(self.datos)
    def imprimir(self):
        i=0
        for dato in self.datos:
            i=i+1
            print(f"Dato {i}= {dato}")
print("****PILA****")
pila =Pila() # --> Instanciamos/Incicalizamos la clase
"""Le asignamos los valores"""
pila.añadir(1)
pila.añadir(2)
pila.añadir(3)
print(f"El número de elementos es: {pila.numeroDeElementos()}"); # --> Imprimimos números de elementos
print("Su contenido es:") # --> Imprimimos todos los datos
pila.imprimir()
pila.eliminar() # --> Eliminamos elemento de arriba de la pila
print(f"El número de elementos después de pila.elminarDatos(): {pila.numeroDeElementos()}"); # --> Imprimimos números de elementos
print("Su contenido después de pila.elminarDatos():") # --> Imprimimos todos los datos
pila.imprimir()
pila.eliminar()
pila.eliminar()
pila.eliminar() # --> Salta el aviso

class Cola:
    def __init__(self,datos=None) -> None:
        self.datos=list()
    def añadir(self,dato):
        self.datos.append(dato)
    def eliminar(self):
        if len(self.datos)>0:
            self.datos.pop(0)
        else:
            print("La cola esta vacía")
    def numeroDeElementos(self) -> int:
        return len(self.datos)
    def imprimir(self):
        i=0
        for dato in self.datos:
            i = i+1
            print(f"Cola {i}= {dato}")
print("****COLA****")
cola =Cola() # --> Instanciamos/Incicalizamos la clase
"""Le asignamos los valores"""
cola.añadir("Elemento 0")
cola.añadir("Elemento 1")
cola.añadir("Elemento 2")
print(f"El número de elementos es: {cola.numeroDeElementos()}"); # --> Imprimimos números de elementos
print("Su contenido es:") # --> Imprimimos todos los datos
cola.imprimir()
cola.eliminar() # --> Eliminamos el primer elemento de de la cola
print(f"El número de elementos después de cola.elminarDatos(): {cola.numeroDeElementos()}"); # --> Imprimimos números de elementos
print("Su contenido después de cola.elminarDatos():") # --> Imprimimos todos los datos
cola.imprimir()
cola.eliminar()
cola.eliminar()
cola.eliminar() # --> Salta el aviso
