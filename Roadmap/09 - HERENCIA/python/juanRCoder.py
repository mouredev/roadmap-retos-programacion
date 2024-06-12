# Herencia, simplemente una clase extensa o hija de una clase padre.
# Polimorfismo, se refiere a la coincidencias en los nombres de metodos en las clases pero tienen diferente funcionalidad.

# EXAMPLE:
class Padre:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
    
    def saludar(self): #metodo en la clase Padre
        return f"Hola {self.name} {self.lastName}"


class Hijo(Padre):
    def __init__(self, name, lastName, age):
        super().__init__(name, lastName)  # Hereda los atributos de la superclase 'Padre'
        self.age = age  # inicializando atributo de instancia Hijo
        
    def saludar(self): #metodo en la clase Hijo
        return f"Soy yo el hijo, {self.name} {self.lastName}, tengo {self.age} anios"
        
        
heber = Padre('heber', 'ramirez');
print(heber.saludar())
# Hola heber ramirez

juan = Hijo('juan', 'ramirez', 23);
print(juan.saludar())
# Soy yo el hijo, juan ramirez, tengo 23 anios

#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.
#  */

class Empleado:
    empleados = []
    
    def __init__(self, id, name, cargo):
        self.id = id
        self.name = name
        self.cargo = cargo
        
    def presentation(self):
        print(f'ID: {self.id} Nombre: {self.name} Cargo: {self.cargo}')
        Empleado.empleados.append({"id": self.id, "name": self.name, "cargo": self.cargo})
    
    def func_manager(self):
        return self.empleados
    
    def func_projectManager(self):
        return "Equipo asignado: Default"
    
    def func_programmer(self):
        return 'Programando en Default'

class Manager(Empleado):
    def func_manager(self):
        print('Listado de empleados:')
        return self.empleados

class ProjectManager(Empleado):
    def __init__(self, id, name, cargo, equipo):
        super().__init__(id, name, cargo)
        self.equipo = equipo

    def func_projectManager(self):
        return f'Equipo Asignado: {self.equipo}'

class Programmer(Empleado):
    def __init__(self, id, name, cargo, language):
        super().__init__(id, name, cargo)
        self.language = language
    
    def func_programmer(self):
        return f"Programando en {self.language}"
    
juan  = Programmer( 12, 'juan', 'web developer', 'python')
robert = ProjectManager( 124, 'robert', 'project manager', 'frontend')
moure = Manager( 495, 'moureDev', 'CEO')

juan.presentation()
print(juan.func_programmer())
# ID: 12 Nombre: juan Cargo: web developer
# Programando en python

robert.presentation()
print(robert.func_projectManager())
# ID: 124 Nombre: robert Cargo: project manager
# Equipo Asignado: frontend

moure.presentation()
print(moure.func_manager())
# Listado de empleados:
# [{'id': 12, 'name': 'juan', 'cargo': 'web developer'}, {'id': 124, 'name': 'robert', 'cargo': 'project manager'}, {'id': 495, 'name': 'moureDev', 'cargo': 'CEO'}]
