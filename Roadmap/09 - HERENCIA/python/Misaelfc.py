"""
Ejercicio
"""
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
        
    def sound(self):
        pass
        
# Subclases

class Perro(Animal):
        
    def sound(self):
            print("Guau!")
        

class Gato(Animal):
    

    def sound(self):
        print("Miau!")
        
def print_sound(animal: Animal):
    animal.sound()
        

mi_animal = Animal("Animal")
print_sound(mi_animal)
mi_perro = Perro("Flaco")
print_sound(mi_perro)
mi_gato = Gato("Guero")
print_sound(mi_gato)

"""
Extra
"""

class Empleado:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.empleados = []
        
    def add(self, empleado):
        self.empleados.append(empleado)
        
    def print_empleados(self):
        for empleado in self.empleados:
            print(f"Empleado: {empleado.nombre} (ID: {empleado.id})")
        

class Manager(Empleado):
    
    def coordinar_proyectos(self):
        print(f"{self.nombre} está coordinando proyectos de la empresa.")
        
    
class ProjectManager(Empleado):
    def __init__(self, id: int, nombre: str, proyecto: str):
            super().__init__(id, nombre)
            self.proyecto = proyecto

    def coordinar_proyecto(self):
            print(f"{self.nombre} está coordinando sus proyectos.")
    
class Developer(Empleado):
    def __init__(self, id: int, nombre: str, lenguaje: str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje
    
    def escribir_codigo(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")
        
    def add(self, empleado):
            print(f"{self.nombre} no puede agregar empleados, {empleado.nombre} no se añadirá.")
            
            
mi_manager = Manager(1, "Abrahamdev")
mi_project_manager = ProjectManager(2, "Misaelfc", "Proyecto de IA")
mi_project_manager2 = ProjectManager(3, "Juanito", "Proyecto de Web")
mi_developer = Developer(4, "Carlos", "Python")
mi_developer2 = Developer(5, "Ana", "JavaScript")
mi_developer3 = Developer(6, "Luis", "Java")
mi_developer4 = Developer(7, "Maria", "Python")

mi_manager.add(mi_project_manager)
mi_manager.add(mi_project_manager2)

mi_project_manager.add(mi_developer)
mi_project_manager2.add(mi_developer2)
mi_project_manager2.add(mi_developer3)
mi_project_manager2.add(mi_developer4)

mi_developer.add(mi_developer2)  # Esto no debería permitir agregar empleados
mi_developer.escribir_codigo()
mi_project_manager.coordinar_proyecto()
mi_manager.coordinar_proyectos()
mi_manager.print_empleados()
mi_project_manager.print_empleados()
mi_project_manager2.print_empleados()
mi_developer.print_empleados()  # Esto no debería mostrar empleados, ya que no puede agregarlos