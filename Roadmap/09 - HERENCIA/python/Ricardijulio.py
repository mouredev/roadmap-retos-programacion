#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.

class Animal:
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad
    
    def comunicar(self):
        pass
    
class Perro(Animal):
    def comunicar(self):
        print('Wof! wof!')
        
class Gato(Animal):
    def comunicar(self):
        print('Miau! miau!')
        
perro = Perro('Mamifero','2 años')
gato = Gato('Mamifero','9 meses')

perro.comunicar()
gato.comunicar()

# DIFICULTAD EXTRA:

class Empleado:
    def __init__(self,nombre,identificador):
        self.nombre = nombre
        self.identificador = identificador
    
    def mostrar_info(self):
        print(f'Mi nombre es {self.nombre} y mi identificador es {self.identificador}')
        
class Gerente(Empleado):
    def __init__(self,nombre,identificador):
        super().__init__(nombre,identificador)
    
    equipo = []    
    
    def asignar(self,persona):
        self.equipo.append(persona)
        print (f'Se ha añadido a {persona} al equipo de {self.nombre}')

class Gerente_proyectos(Gerente):
    def __init__(self,nombre,identificador):
        super().__init__(nombre,identificador)
    proyectos = []
    tareas = {}
    
    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        print (f'Se ha añadido {proyecto} a la lista de proyectos de {self.nombre}')
        
    def asignar_tarea(self, tarea, persona):
        self.tareas[tarea]=persona
        print(f'Se le ha asignado {tarea} a {persona}')
           

class Programador(Empleado):
    
    def __init__(self,nombre,identificador,nivel):
        super().__init__(nombre,identificador)
        self.nivel = nivel
    lenguajes = []
    
    def usar_lenguaje(self,lenguaje):
        self.lenguajes.append(lenguaje)
        print(f'{self.nombre} puede usar {lenguaje}')
        
    def escribir_codigo(self,lenguaje):
        for i in self.lenguajes:
            if lenguaje == i:
                print(f'{self.nombre} esta escribiendo codigo en {lenguaje}')
            else:
                print(f'{self.nombre} no maneja {lenguaje}')
        
g = Gerente('Daniel','1002')
g.asignar('Pedro')
g.asignar('Sofia')
g.asignar('Federico')

gp = Gerente_proyectos('Pedro','1030')
gp.asignar_proyecto('San juan')
gp.asignar_tarea('Ruta de acceso','Angel')

p = Programador('Angel','1023','Senior')
p.usar_lenguaje('python')
p.escribir_codigo('python')

g.mostrar_info()
gp.mostrar_info()
p.mostrar_info()
