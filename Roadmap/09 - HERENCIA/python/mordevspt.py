"""
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

""" 
SOLO HERENCIA 
"""

# Clase Padre
class Animalsh:
    # Declaramos las funciones en la calse padre y no hacemo nada en las clases hija
    def soundAnimal(self,sound):
        return print(sound)

# Clases hijas o subclases
class Dogsh(Animalsh):
    pass

class Catsh(Animalsh):
    pass

# Probando el código
perro = Dogsh()
perro.soundAnimal("¡Guau!")

gato = Catsh()
gato.soundAnimal("¡Miau!")

"""
HERENCIA CON POLIMORFISMO

El polimorfismo es una técnica en programación que permite a objetos de diferentes 
clases responder a los mismos mensajes (métodos)
"""

# Clase Padre
class Animal:
    # Declaramos el método en la clase padere, pero no lo desarrollamos
    def soundAnimal(self):
        pass

# Clases hijas o subclases
class Dog(Animal):
    # Sobrecargamos el método, lo especializamos
    def soundAnimal(self):
        print("¡Guau!")

class Cat(Animal):
    # Sobrecargamos el método, lo especializamos
    def soundAnimal(self):
        print("¡Miau!")

# En vez de llamar a cada función de un animal cualquiera,
# podemos llamar a una función que las llame
def petSound(animal: Animal):
    animal.soundAnimal()
    
# Probando el código
perro = Dog()
#perro.soundAnimal()
petSound(perro)

gato = Cat()
#gato.soundAnimal()
petSound(gato)

"""
DIFICULTAD EXTRA (opcional):
 Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 Cada empleado tiene un identificador y un nombre.
 Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 actividad, y almacenan los empleados a su cargo.
"""

class Employee():
    # Contador de instancias
    instance_count = 0 

    # Incrementamos el contador por instancia
    @classmethod
    def increaseInstanceCount(cls):
        cls.instance_count += 1
    # Obtenemos el contador, la cantidad de instancias correspondientes
    @classmethod
    def getInstanceCount(cls):
        return cls.instance_count
        
    def __init__(self,id:int,name:str):
        self.increaseInstanceCount() # Aumentamos el contador cada vez que se instancie
        self.name = name
        self.id = id
        self.employees = [] #Lista donde guardaremos a los empleados que agregamos a los cargos
    
    # Agregado de empleados
    def addEmployee(self,employee):
        self.employees.append(employee)
        
    # Obtener los empleados a su cargo
    def getEmployees(self):
        # Recorremos la lista
        for employee in self.employees:
            print(employee.name)
        
class Manager(Employee):
    # MÉTODOS
    def strategy(self):
        print(f"{self.name} está definiendo la estrategia empresarial")
    def decision(self):
        print(f"{self.name} toma decisiones clave en la empresa")
    def manage(self):
        print(f"{self.name} administra los recursos y presupuestos de la empresa")

class Projectmanager(Employee):
    # Inicializador propio
    def __init__(self, id:int, name:str, proyect:str):
        super().__init__(id,name) # Lo que necesitamos de la clase padre (Super)
        self.proyect = proyect # Propiedad propia de la clase
        
    # MÉTODOS
    def plan_manage_project(self):
        print(f"{self.name} está planificando y gestionando sus proyectos")
    def budgets(self):
        print(f"{self.name} define presupuestos para el proyecto")
    def schedule(self):
        print(f"{self.name} define los cronogramas del proyecto")
    def meeting(self):
        print(f"{self.name} liderar las reuniones del proyecto")

class Programmer(Employee):        
    # Inicializador propio
    def __init__(self, id:int, name:str, language:str):
        super().__init__(id,name) # Lo que necesitamos de la clase padre (Super)
        self.language = language # Propiedad propia de la clase
    
    # Los progamadores no pueden tener empleados, sobre-escribimos
    def addEmployee(self, employee):
        pass
    
    # MÉTODOS
    def code(self):
        print(f"{self.name} está programando código en el lenguaje {self.language}")
    def test(self):
        print(f"{self.name} está testeando el software")
    def debugging(self):
        print(f"{self.name} está depurando el código en el lenguaje {self.language}")
    def delivery(self):
        print(f"{self.name} está entrangando el software")

# Manager
manager = Manager(1,"Sauron")
print(f"El Manager de la empresa se llama {manager.name} y tiene como identificador el número {manager.id}")
manager.strategy()

# Proyect Manager
pmanager1 = Projectmanager(5,"Bilbo","Proyect1")
print(f"El Project Manager de la empresa se llama {pmanager1.name} y tiene como identificador el número {pmanager1.id}")
pmanager1.budgets()

pmanager2 = Projectmanager(7,"Bolson","Proyect2")
print(f"El Project Manager de la empresa se llama {pmanager2.name} y tiene como identificador el número {pmanager2.id}")
pmanager2.schedule()

# Programmer
programer1 = Programmer(11,"Perry","Python")
programer2 = Programmer(12,"Merry","JavaScript")
print(f"Tienen dos programadores llamados {programer1.name} y {programer2.name}")
programer1.code()
programer2.test()

# Número de instancias Totales
print(f"Instancias totales: {Manager.getInstanceCount() + Projectmanager.getInstanceCount() + Programmer.getInstanceCount()}")

# Añanir empleados
manager.addEmployee(pmanager1)
manager.addEmployee(pmanager2)
pmanager1.addEmployee(programer1)
pmanager2.addEmployee(programer2)

# Mostramos los empleados
print(f"El Manager {manager.name} tiene como emepleados a los Project Manager:")
manager.getEmployees()
print(f"El Project Manager {pmanager1.name} tiene como emepleados a los Programmers:")
pmanager1.getEmployees()
print(f"El Project Manager {pmanager2.name} tiene como emepleados a los Programmers:")
pmanager2.getEmployees()