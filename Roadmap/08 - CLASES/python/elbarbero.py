"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 """

from collections import deque

class MiClase:
    def __init__(self):
        self.n_reto = 8
        self.nombre_reto = "Clases"
        self.url_web_retos = "https://retosdeprogramacion.com/roadmap/"
        self.url_github = "https://github.com/mouredev/roadmap-retos-programacion/tree/main/Roadmap/08%20-%20CLASES"
    
    def print(self):
        print(f"""
              "-----------------DATOS del RETO-----------------
              "Número del reto: {self.n_reto}
              "Nombre del reto: {self.nombre_reto}
              "Web de los retos: {self.url_web_retos}
              "Github del reto: {self.url_github}
              """)

class Pila(list):
    def __init__(self, *args):
        self.__count = len(*args)
        super().__init__(item for item in args)
    
    def add(self, element):
        super().append(element)
        self.__count += 1
    
    def delLIFO(self):
        super().pop()
        self.__count -= 1
    
    def delete(self, index):
        try:
            del self[0][index]
            self.__count -= 1
        except IndexError as ex:
            print("No existe ese indice en la colección")
       
    @property        
    def count(self):
        return self.__count
    
    def print(self):
        print(f"Tiene un total de {self.__count} elementos -> {self}")


class Cola():
    def __init__(self, *args):
        self.cola = deque(*args)
    
    def add(self, element):
        self.cola.append(element)
    
    def delFIFO(self):
        print(f"El elemento borrado es: {self.cola.popleft()}")
    
    def delete(self, index):
        try:
            del self.cola[index]
        except IndexError as ex:
            print("No existe ese indice en la colección")
            
    def count(self):
        return len(self.cola)
    
    def print(self):
        print(f"Tiene un total de {self.count()} elementos -> {self.cola}")

if __name__ == "__main__":

    print("----------------------CLASE----------------------------")
    miclase = MiClase()
    miclase.print()
    
    print("----------------------PILAS----------------------------")
    webs = Pila(["https://es.wikipedia.org/wiki/Wikipedia:Portada", "https://es.wikipedia.org/wiki/Gran_Premio_de_Abu_Dabi", "https://es.wikipedia.org/wiki/Lewis_Hamilton", "https://es.wikipedia.org/wiki/Fernando_Alonso", "https://es.wikipedia.org/wiki/Asturias"])
    print(webs)
    webs.add("www.google.es")
    print(webs)
    webs.delLIFO()
    print(webs)
    webs.delete(3)
    webs.print()
    
    print("----------------------COLAS----------------------------")
    numbers = Cola([1, 2, 3, 4, 5, 6])
    numbers.print()
    print(numbers.cola)
    numbers.delFIFO()
    numbers.print()
    numbers.delete(2)
    numbers.print()

