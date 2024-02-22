#08 CLASES
"""
/*
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
 */
"""


class Iphone:
    def __init__(self) :
        self.nombre = "iPhone15"
        self.camara = "12MP"
        self.almacenamiento = "265GB"
        self.ram = "8GB"

    def presentacion(self):
        return f"""
    Nombre: {self.nombre}
    Camara: {self.camara}
    Almacenamiento: {self.almacenamiento}
    Ram: {self.ram}
    """

class Telefono:
    def __init__(self , nombre :str , camara : str , almacenamiento : str , ram : str ) -> str:
        self.nombre = nombre
        self.camara = camara
        self.almacenamiento = almacenamiento
        self.ram = ram

    def presentacion(self):
        return f"""
    Nombre: {self.nombre}
    Camara: {self.camara}
    Almacenamiento: {self.almacenamiento}
    Ram: {self.ram}
    """

iphone15 = Iphone()
print(iphone15.presentacion())

Sansung_S23 = Telefono("Sansung S23", "200MP" ,"256GB" , "8GB" )
print(Sansung_S23.presentacion())

### Extra
class Pila:
    def __init__(self):
        self.pila : list = []

    def añadir (self , elemento_a_añadir):
        self.pila.append(elemento_a_añadir)

    def eliminar(self):
        del self.pila[-1]

    def ultimo_elemento(self):
        print(self.pila[-1])

    def pila_actual(self):
        print(self.pila)


class Cola:
    def __init__(self) :
        self.cola : list = []

    def añadir(self , elemento_a_añadir):
        self.cola.append(elemento_a_añadir)
        print("se añadio el elemento")

    def eliminar(self):
        del self.cola[0]
        print("se elimino el elemento")

    def primer_elemento(self):
        print(self.cola[0])

    def cola_actual(self):
        print(self.cola)

cola = Cola()
pila = Pila()

while True :
    pila_cola = int(input("que vas a usar? , colas(1) , pilas(2) o salir(3) : "))

    if pila_cola == 1 :

        while True :
            print("""
                1.añadir
                2.eliminar
                3.primer_elemento
                4.cola_actual
                5.salir
                """)
            try:
                decicion = int(input("eliga segun el indice : "))
            except Exception as error:
                print(" ha habido un error que es : " , error)


            if decicion == 1:
                elemento = input("elemento a añadir : ")
                cola.añadir(elemento)

            elif decicion == 2:
                cola.eliminar()

            elif decicion == 3:
                cola.primer_elemento()

            elif decicion == 4:
                cola.cola_actual()

            elif decicion == 5 :
                break

            else :
                print("opcion no existente")


    elif pila_cola == 2:
        while True:
            print("""
                1.añadir
                2.eliminar
                3.ultimo_elemento
                4.pila_actual
                5.salir
                """)
            try:
                decicion = int(input("eliga segun el indice : "))
            except Exception as error:
                print("ha habido un error el cual es : " , error)


            if decicion == 1:
                elemento = input("elemento a añadir : ")
                pila.añadir(elemento)

            elif decicion == 2:
                pila.eliminar()

            elif decicion == 3:
                pila.ultimo_elemento()

            elif decicion == 4:
                pila.pila_actual()

            elif decicion == 5 :
                break

            else :
                print("opcion no existente")

    elif pila_cola == 3:
        break

    else :
        print("opcion no correcta")