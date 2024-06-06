'''
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
'''
#Creamos la superclase animal
class Animal :
    def __init__(self):
        pass
        
#Creamos la subclase Perro
class Perro(Animal): #Así se heredan los métodos en python
    def ladrar(self):
        print("Guau")

#Creamos la clase Gato
class Gato(Animal):
    def maullar(self):
        print("Miau")


mi_Gato=Gato()
mi_Perro= Perro()
mi_Perro.ladrar()
mi_Gato.maullar()

#Dificultad EXTRA

class Empleado:
    def __init__(self,id,nombre,equipo):
        self.id=id
        self.nombre=nombre
        self.equipo=equipo or []

class Programador(Empleado):
    def desarrollar(self):
        return f'{self.nombre} con ID {self.id} Está desarollando una aplicación móvil y lleva a cargo a {len(self.equipo)} personas'

class Gerente_proyecto(Empleado):
    def supervisar(self):
        return f'{self.nombre} con ID {self.id} Revisa que el código está libre de bugs y lleva a cargo a {len(self.equipo)} personas'

class Gerente(Empleado):
    def dirigir(self):
        return f'{self.nombre} con ID {self.id} Decide cual es la siguiente característica a añadir a la aplicación móvil y lleva a cargo a {len(self.equipo)} personas'
        
#Instanciamos a los empleados de la empresa
programador1=Programador('1','Alexdevrep',[])
programador2=Programador('2','Carlos',[])
gerente_proyecto1=Gerente_proyecto('3','Brais',[programador1,programador2])
gerente1=Gerente('4','MoureDev',[gerente_proyecto1])

#Obtenemos los datos
print(programador1.desarrollar())
print(programador2.desarrollar())
print(gerente_proyecto1.supervisar())
print(gerente1.dirigir())


    