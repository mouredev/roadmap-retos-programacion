###################################### HERENCIA ########################################
'''
La herencia es un mecanismo de la programación orientada a objetos que sirve para crear clases nuevas a partir de clases preexistentes. Se toman (heredan) atributos y métodos de las clases bases y se los modifica para modelar una nueva situación.

La clase desde la que se hereda se llama clase base y la que se construye a partir de ella es una clase derivada.

Si nuestra clase base es la clase punto que hemos visto antes, puedo crear una nueva clase de la siguiente manera:
'''

from math import sqrt

class Punto():
    
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__x = x # Definición de atributo privado (encapsulación)
        self.__y = y

    @property
    def x(self) -> int:
        print('Imprimiendo coordenada X:')
        return self.__x
    
    @property
    def y(self) -> int:
        print('Imprimiendo coordenada y:')
        return self.__y
    
    @x.setter
    def x(self, x: int = 0) -> None:
        print('Cambio x')
        self.__x = x
        
    @y.setter
    def y(self, y: int = 0) -> None:
        print('Cambio y')
        self.__y = y
        
    def mostrar(self) -> None:
        return str(self.__x) + ":" + str(self.__y)
    
    def distancia(self, point) -> None:
        dx = self.__x - point.x
        dy = self.__y - point.y
        
        return sqrt((dx*dy + dy*dy)** 0.5)
    
class Punto3D(Punto):
    
    def __init__(self, x:int = 0, y:int = 0, z:int = 0):
        super().__init__(x, y) # Llamada al constructor de la clase base
        self.__z = z # Atributo propio de la clase derivada
        
    @property
    def z(self) -> None:
        print('Imprimiendo coordenada Z:')
        return self.__z
    
    @z.setter
    def z(self, z) -> None:
        print('Cambio coordenada Z')
        self.__z = z
    
    # Sobreescritura de métdos
    def mostrar(self) -> None:
        return super().mostrar() + ":" + str(self.__z)
    
    def distancia(self, npoint) -> None:
        '''
        Devuelve la distancia entre ambos puntos 3D
        '''
        
        dx = self.__x - npoint.x
        dy = self.__y - npoint.y
        dz = self.__z - npoint.z
        
        return (dx*dx + dy*dy + dz*dz) ** 0.5 


class Animal():
    
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age
        
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @name.setter
    def name(self, name: str) -> None:
        print('Cambiando nombre')
        self.__name = name
    
    @age.setter
    def age(self, age: int) -> None:
        print('Cambiando nombre')
        self.__age = age
        
# EJERCICIO PRINCIPAL
      
class Dog(Animal):
    
    def __init__(self, name: str, age: int, race: str) -> None:
        super().__init__(name, age)
        self.__race = race
        
    @property
    def race(self) -> None:
        return self.__race
    
    @race.setter
    def race(self, race: str) -> None:
        print('Estableciendo raza.')
        self.__race = race
        
    def talk(self) -> None:
        print('Woof Woof!!!')

class Cat(Animal):
    
    def __init__(self, name: str, age: int, race: str) -> None:
        super().__init__(name, age)
        self.__race = race
        
    @property
    def race(self) -> None:
        return self.__race
    
    @race.setter
    def race(self, race: str) -> None:
        print('Estableciendo raza.')
        self.__race = race
        
    def talk(self) -> None:
        print('Miau Miau!!!') 
        

pet1 = Dog(name="Coco", age=5, race="Golden Retriever")
pet2 = Cat(name="Perla", age=7, race="Romano")

print(pet1.name)
print(pet1.age)
print(pet1.talk())
print(pet2.name)
print(pet2.age)
print(pet2.talk())

# FIN EJERCICIO PRINCIPAL

# DIFICULTAD EXTRA

class Employee():
    def __init__(self, id: str, name: str) -> None:
        self.__id = id
        self.__name = name
    
    @property
    def id(self) -> str:
        return self.__id
    
    @id.setter
    def id(self, id: str) -> None:
        self.__id = id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
class Programmer(Employee):
    
    def __init__(self, id, name, languages: list = []):
        super().__init__(id, name)
        self.__languages = languages
        
    @property
    def languages(self) -> list:
        return self.__languages
    
    @languages.setter
    def languages(self, languages: list) -> None:
        self.__languages = languages
    
    def work(self) -> None:
        print('Coding...')

class ProyectManager(Employee):
    
    def __init__(self, id, name, programmers: list = []):
        super().__init__(id, name)
        self.__programmers = programmers
    
    @property
    def programmers(self) -> list:
        return self.__programmers
    
    @programmers.setter
    def programmers(self, programmers: list) -> None:
        self.__programmers = programmers
        
    def work(self) -> None:
        print('Managing projects...')
        
class Manager(Employee):
    
    def __init__(self, id, name, employees: list = []):
        super().__init__(id, name)
        self.__employees = employees
    
    @property
    def employees(self) -> list:
        return self.__employees
    
    @employees.setter
    def employees(self, employees: list) -> None:
        self.__employees = employees
        
    def work(self) -> None:
        print('Managing...')
        
        
p1 = Programmer(id="1", name="Juan", languages=["Python", "Java"])
p2 = Programmer(id="2", name="Maria", languages=["C++", "C#"])
p3 = Programmer(id="3", name="Pedro", languages=["JavaScript", "PHP"])
p4 = Programmer(id="4", name="Ana", languages=["Ruby", "Swift"])
p5 = Programmer(id="5", name="Luis", languages=["Go", "Kotlin"])

pm1 = ProyectManager(id="6", name="Carlos", programmers=[p1, p2])
pm2 = ProyectManager(id="7", name="Laura", programmers=[p3, p4])
pm3 = ProyectManager(id="8", name="Sofia", programmers=[p5])

m1 = Manager(id="9", name="Javier", employees=[pm1, pm2, pm3])
m1.work()
pm1.work()
p1.work()
p2.work()
p3.work()
p4.work()
p5.work()

# Listar todos los programdores asignados a un ProjectManager
for p in pm1.programmers:
    print(p.name)

# FIN DIFICULTAD EXTRA
       
###################################### FIN HERENCIA ########################################