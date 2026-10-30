"""
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
"""

#Super clase
class Animal:

    def __init__(self, name:str):
        self.name=name

    def sound(self):
        print("Este animal emite un sonido de animal")

#Subclase

class Dog(Animal):

    def sound(self): #Sobrecargar la operación/Redefenir
            print(f"{self.name} es un perro y hace guau")

class Cat(Animal):

    def sound(self): #Sobrecargar la operación/Redefinir
            print(f"{self.name} es un gato y hace miau")

def print_sound(animal:Animal):
     animal.sound()



Animal01=Animal("Animal01")
Tom=Dog("Tom")
Pepa=Cat("Pepa")
Animal01.sound()
Tom.sound()
Pepa.sound()

print("Llamando a print_sound")
print_sound(Animal01)
print_sound(Tom)
print_sound(Pepa)

class empleado:

    def __init__(self,name:str,ID:int):
        self.name=name
        self.ID=ID
        self.empleados=[]

    def add(self, empleado):
     self.empleados.append(empleado)

    def print_empleado(self):
         for empleados in self.empleados:
              print(empleados.name)
    
     


class gerente(empleado):

     def coordinar_proyectos(self):
          print(f"{self.name} coordina los proyectos")

class gerente_proyectos(empleado):

     def __init__(self,name:str,ID:int,project:str):
        super().__init__(name,ID)
        self.project=project

     def coodonina_proyecto(self):
          print(f"{self.name} coordina un proyecto")

class programadores(empleado):

    def __init__(self,name:str,ID:int,language:str):
        super().__init__(name,ID)
        self.language=language

    def trabajar(self):
          print(f"{self.name} es el unico que trabaja en {self.language}")

    def add(self, empleados: empleado):
        print(f"un programador no manda en la empresa, solo hace caso, no es jefe de {empleados.name}")

jefe=gerente("Pedro",1)
jefecito01=gerente_proyectos("Pablo",2, "Proyecto 01")
jefecito02=gerente_proyectos("Jose",2, "Proyecto 02")
prog01=programadores("jeferson",9999,"lo que necesite el proyecto")
prog02=programadores("jason",9998,"lo que necesite la empresa")
prog03=programadores("jas",9997,"lo que necesite la empresa01")
prog04=programadores("son",9996,"lo que necesite la empresa02")

jefe.add(jefecito01)
jefe.add(jefecito02)
jefecito01.add(prog01)
jefecito01.add(prog02)
jefecito02.add(prog03)
jefecito02.add(prog04)

prog01.add(prog02)
jefe.coordinar_proyectos()
jefecito01.coodonina_proyecto()
prog01.trabajar()
jefe.print_empleado()
jefecito01.print_empleado()
jefecito02.print_empleado()
prog01.print_empleado()