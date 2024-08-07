"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función. 
 */
"""
# Clases
print("---Clases en Python---")

class Bebida:
    bebidas = 0
    def __init__(self,nombre:str,precio:float,es_alcohol:bool) -> None:
        self.nombre = nombre
        self.precio = precio
        self.es_alcohol = es_alcohol
        Bebida.bebidas += 1
        self.n_bebida = Bebida.bebidas
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Es Alcohol: {self.es_alcohol}")
        print(f"Numero de Bebida: {self.n_bebida}")
        print(f"Numero de Bebidas Totales: {Bebida.bebidas}")
        print("------")
        

cocacola = Bebida("cocacola",2.5,False)
cafe = Bebida("cafe",1.5,False)
cerveza = Bebida("cerveza",2,True)

cocacola.imprimir()
cafe.imprimir()
cerveza.imprimir()

cocacola.nombre = "Cocacola Ligth"
cafe.precio = 1.2
cerveza.es_alcohol = False

cocacola.imprimir()
cafe.imprimir()
cerveza.imprimir()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""
# Pila
class Alumnos:
    
    def __init__(self) -> None:
        self.elementos = []
    
    def añadir(self,entrada):
        self.elementos.append(entrada)
        
    def eliminar(self):
        antiguo = self.elementos.pop()
        print(f"{antiguo} ha sido eliminado")
        
    def listado(self):
        print(f"Numero de Alumnos: {len(self.elementos)}")
        
    def imprimir(self):
        print(f"{self.elementos}")
        print("------")

clase_1a = Alumnos()
clase_1a.añadir("Juan")
clase_1a.añadir("Sergio")
clase_1a.añadir("Emmanuel")

clase_1a.listado()
clase_1a.imprimir()

clase_1a.eliminar()
clase_1a.listado()
clase_1a.imprimir()


# Cola

class Restaurante:
    clientes_consumiendo = 0
    def __init__(self,n_personas) -> None:
        Restaurante.clientes_consumiendo += 1
        self.grupos = []
        self.añadir(n_personas)

    def añadir(self,n_personas):
        self.grupos.append(n_personas)
        
    def eliminar(self):
        if len(self.grupos) > 0:
            self.grupos.pop(0)
        else:
            print("No hay grupos para eliminar")
        
    def listar(self):
        print(f"Numeros de grupos: {len(self.grupos)}")
        
    def imprimir(self):
        print(f"Grupos activos: {self.grupos}")
        
bar_pepito = Restaurante("4")
bar_pepito.listar()
bar_pepito.imprimir()

bar_pepito.añadir("6")
bar_pepito.añadir("9")
bar_pepito.listar()
bar_pepito.imprimir()

bar_pepito.eliminar()
bar_pepito.listar()
bar_pepito.imprimir()