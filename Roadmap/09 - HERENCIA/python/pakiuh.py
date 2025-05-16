'''EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.'''

class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def sonido_emiten(self):
        pass

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def sonido_emiten(self):
        return "Guau, Guau"

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    def sonido_emiten(self):
        return "Miau, Miau"

pirata = Gato("Pirata")
print(f"{pirata.nombre} hace {pirata.sonido_emiten()}")

toby = Perro("Toby")
print(f"{toby.nombre} hace {toby.sonido_emiten()}")

'''DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.'''

class Empleado:
    def __init__(self,id, nombre):
        self.id = id
        self.nombre = nombre

class Gerente(Empleado):
    def __init__(self, id, nombre, departamento, numero_subordinados):
        super().__init__(id, nombre)
        self.departamento = departamento
        self.numero_subordinados = numero_subordinados
    
    def contratar(self, contratado):
        return f"Has contratado un nuevo empleado que se llama {contratado}"
    
    def despedir(self, despedido):
        return f"Has despedido a {despedido}"

class Gerente_proyecto(Empleado):
    def __init__(self, id, nombre, proyecto, numero_subordinados):
        super().__init__(id, nombre)
        self.proyecto = proyecto
        self.numero_subordinados = numero_subordinados
    
    def set_plazos(self, fecha):
        return f"la fecha de finalización del {self.proyecto} es {fecha}"
    
    def get_numero_empleados(self):
        return self.numero_subordinados
    

class Programador(Empleado):
    def __init__(self, id, nombre, gerente_proyecto):
        super().__init__(id, nombre, gerente_proyecto)
    
    def set_proyecto(self,proyecto):
        self.proyecto = proyecto
    
    def get_proyecto(self):
        return self.proyecto
    

