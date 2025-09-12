'''

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


'''

class Pokemon:

    def __init__(self, nombre:str, tipo:str, ataque:str, ataque_especial:str, vida:int, cp:int):
        self.nombre=nombre
        self.tipo=tipo       
        self.ataque=ataque
        self.ataque_especial=ataque_especial
        self.vida=vida
        self.cp=cp
    
    def atacar(self):
        print(self.nombre +" usó " + self.ataque + " para atacar \ny causó " + str(self.cp/4) + " puntos de daño al inimigo!")
        return self.ataque
    def atacar_especial(self):
        print(self.nombre +" usó " + self.ataque_especial + " para atacar \ny causó " + str(self.cp*1.5) + " puntos de daño al inimigo!")
        return self.ataque_especial

squirtle=Pokemon("Squirtle","agua","chorro de agua","cañon de agua",82,105)
print(squirtle)
squirtle.atacar()
squirtle.atacar_especial()


#EXTRA

class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, item):
        self.elementos.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return "La pila está vacía"
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def numero_de_elementos(self):
        return len(self.elementos)
    
    def imprimir_contenido(self):
        print("Contenido de la pila:", self.elementos)

# Ejemplo de uso de la clase Pila
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.imprimir_contenido()
print("Desapilando:", pila.desapilar())
pila.imprimir_contenido()
print("Número de elementos en la pila:", pila.numero_de_elementos())

class Cola:
    def __init__(self):
        self.elementos = []
    
    def encolar(self, item):
        self.elementos.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            return "La cola está vacía"
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def numero_de_elementos(self):
        return len(self.elementos)
    
    def imprimir_contenido(self):
        print("Contenido de la cola:", self.elementos)

# Ejemplo de uso de la clase Cola
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.imprimir_contenido()
print("Desencolando:", cola.desencolar())
cola.imprimir_contenido()
print("Número de elementos en la cola:", cola.numero_de_elementos())


