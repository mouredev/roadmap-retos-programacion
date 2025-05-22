# HERENCIA EN PYTHON

class Animal():
    
    def __init__(self, nombre : str, raza : str):
        self.nombre = nombre
        self.raza = raza
        
    def emitir_sonido(self):
        print("Mi mascota saluda diciendo...")
        

class Perro(Animal):
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Guau Guau!")
        
class Gato(Animal):
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau Miau!")
        
        
mi_perro = Perro("Firulais", "Pastor Aleman")
print(f"Mi perro se llama {mi_perro.nombre} y es un {mi_perro.raza}")
mi_perro.emitir_sonido()
print("--------------------------------------------")
mi_gato = Gato("Pancho", "Siames")
print(f"Mi gato se llama {mi_gato.nombre} y es un {mi_gato.raza}")
mi_gato.emitir_sonido()

print("----------------------------------------------------------------------")


#Ejercicio extra


class Empleado:
    def __init__(self, id : int, name : str, cargo : str):
        self.id = id
        self.name = name
        self.cargo = cargo
        self.empleado = []
        
    
    def añadir_empleados(self, empleado ):
        self.empleado.append(empleado)
        
    def empleados_a_cargo(self):
        print("Empleados a cargo: ")
        for empleado in self.empleado:
            print(empleado.name)


class Gerente(Empleado):
    def __init__(self, id, name, cargo):
        super().__init__(id, name, cargo)
        

class GerenteProyecto(Empleado):
    def __init__(self, id, name, cargo, proyecto):
        super().__init__(id, name, cargo)
        self.proyecto = proyecto

class Developer(Empleado):
    def __init__(self, id, name, cargo, language):
        super().__init__(id, name, cargo)
        self.language = language
    
    def realizar_proyecto(self):
        print(f"Realizando proyecto en: {self.language}")
        
    def añadir_empleados(self, empleado : Empleado):
        print(f"El programador no tiene empleados a cargo; {empleado.name} no se añadio")
        
        
#ASIGNACION DE ROLES       
gerente = Gerente(1, "Jose", "Gerente de Area")

gerente_proyecto1 = GerenteProyecto(2, "Pablo", "Gerente de Proyecto 1", "Proyecto web")
gerente_proyecto2 = GerenteProyecto(3, "Juanito", "Gerente de Proyecto 2", "Proyecto de escritorio")
gerente_proyecto3 = GerenteProyecto(4, "Pedro", "Gerente de Proyecto 3", "Proyecto Movil")

dev1 = Developer(5, "Paco", "Junior Developer", "JavaScript")
dev2 = Developer(6, "Raul", "Semi Senior Developer", "C#")
dev3 = Developer(7, "Carlos", "Senior Developer", "Java")

#JERARQUIA 

gerente.añadir_empleados(gerente_proyecto1)
gerente.añadir_empleados(gerente_proyecto2)
gerente.añadir_empleados(gerente_proyecto3)
gerente.empleados_a_cargo()

gerente_proyecto1.añadir_empleados(dev1)
gerente_proyecto2.añadir_empleados(dev2)
gerente_proyecto3.añadir_empleados(dev3)
gerente_proyecto1.empleados_a_cargo()
gerente_proyecto3.empleados_a_cargo()
gerente_proyecto2.empleados_a_cargo()

dev1.añadir_empleados(dev2)
