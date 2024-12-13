### Ejercicio ###

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        print("El animal hace un sonido")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau") 
    

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

perro = Perro("Junior", "10 años")
gato = Gato("Malvavisco", "3 años")
perro.hacer_sonido()
gato.hacer_sonido()


### Ejercicio Extra ###

class Empleado:
    def __init__(self, id, nombre):
        self.id = id    
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"


class Gerente(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.empleados_a_cargo = []

    def agregar_empleado_a_cargo(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def listar_empleados_a_cargo(self):
        return [str(empleado) for empleado in self.empleados_a_cargo]
    

class GerenteDeProyectos(Gerente): 
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
         self.proyectos.append(proyecto)

    def listar_proyectos(self):
        return self.proyectos
    

class Programador(Empleado):
    def __init__(self, id, nombre, habilidades):
        super().__init__(id, nombre)
        self.habilidades = habilidades

    def listar_habilidades(self):
        return self.habilidades
    

gerente = Gerente(11, "Geovanni")
programador1 = Programador(21, "Isaac", ["Python", "JavaScript"])
programador2 = Programador(22, "Karina", ["Python", "C#"])
gerente_proyectos = GerenteDeProyectos(31, "Jessica")

gerente.agregar_empleado_a_cargo(programador1)
gerente.agregar_empleado_a_cargo(programador2)
gerente_proyectos.agregar_proyecto("Proyecto X")

print(f"Gerente: {gerente}")
print("Empleados a cargo del gerente:")
for empleado in gerente.listar_empleados_a_cargo():
    print(f" - {empleado}")

print(f"\nGerente de Proyectos: {gerente_proyectos}")
print("Proyectos a cargo:")
for proyecto in gerente_proyectos.listar_proyectos():
    print(f" - {proyecto}")

print(f"\nProgramador: {programador1}")
print("Habilidades:")
for habilidad in programador1.listar_habilidades():
    print(f" - {habilidad}")

