"""
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
"""

# Superclase
class Animal:
    def __init__(self, nombre:str):
        self.nombre = nombre        
    
    def sonido(self):
        pass

#Subclase Perro, lo que se incluye entre los paréntesis es el nombre de la superclase
class Perro(Animal): 
    
    def sonido(self):
        return "Guauuu!!"

#Subclase Gato, lo que se incluye entre los paréntesis es el nombre de la superclase        
class Gato(Animal):
    
    def sonido(self):
        return "Miauuuu!!"

# Instancia de subclase tipo Perro, hereda de Animal la propiedad nombre y sobreescribe el método sonido
perro = Perro("Fido")
print(f'Una de mis mascotas se llama {perro.nombre} y su sonido es {perro.sonido()}')

# Instancia de subclase tipo Gato, hereda de Animal la propiedad nombre y sobreescribe el método sonido
gato = Gato("Micifú")
print(f'Una de mis mascotas se llama {gato.nombre} y su sonido es {gato.sonido()}')

# Polimorfismo en tiempo de ejecución, recibe un objeto de tipo Animal (superclase), y dependiendo de la instancia de superclase o subclase que reciba, imprimirá una u otra cosa
def sonidoAnimal(animal:Animal):
    print(f'El animal {animal.nombre} hace {animal.sonido()}')

sonidoAnimal(perro) # Imprime la info de perro
sonidoAnimal(gato) # Imprime la info de gato

# EXTRA

class Empleado:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados = []
        self.proyectos = []
        self.lenguajes = []
        
    def addEmpleado(self, empleado):
        self.empleados.append(empleado)
        
    def addProyecto(self, proyecto):
        self.proyectos.append(proyecto)
        
    def addLenguaje(self, lenguajes):
        self.lenguajes.append(lenguajes)
        
class Gerente(Empleado):
    def __init__(self, identificador, nombre):
        super().__init__(identificador, nombre)
        
    def coordinar(self):
        return f'El gerente {self.nombre} coordina a {len(self.empleados)} empleados {self.empleados}'

    def addProyecto(self, empleado):
        print("Un gerente no gestiona proyectos")
    
    def addLenguaje(self, lenguajes):
        print("Un gerente no desarrolla")


class GerenteProyecto(Empleado):
    def __init__(self, identificador:int, nombre:str):
        super().__init__(identificador, nombre)        
    
    def gestionar(self):
        return f'El gerente de proyecto {self.nombre} gestiona {len(self.proyectos)} proyecto/s {self.proyectos}'
    
    def addEmpleado(self, empleado):
        print("Un gerente de proyectos no puede tener empleados")
        
    def addLenguaje(self, lenguajes):
        print("Un gerente de proyectos no desarrolla")

class Programador(Empleado):
    def __init__(self, identificador, nombre):
        super().__init__(identificador, nombre)        
        
    def  programar(self):
        return f'El programador {self.nombre} programa en {len(self.lenguajes)} lenguaje/s {self.lenguajes}'
    
    def addProyecto(self, empleado):
        print("Un programador no gestiona proyectos")
    
    def addEmpleado(self, empleado):
        print("Un programador no puede tener empleados")

# PRUEBAS
gerente = Gerente(1, 'Pepe')
gerente.addEmpleado('Luis')
gerente.addEmpleado('Antonio')
print(gerente.coordinar())

gerenteProyecto = GerenteProyecto(2, 'Luis')
gerenteProyecto.addProyecto('Proyecto 1')
gerenteProyecto.addProyecto('Proyecto 2')
print(gerenteProyecto.gestionar())

programador = Programador(3, 'Antonio')
programador.addLenguaje('Java')
programador.addLenguaje('JavaScript')
programador.addLenguaje('Python')
programador.addLenguaje('PHP')
print(programador.programar())

# Un gerente puede tener un objeto de tipo empleado
gerente.addEmpleado(programador)
print(gerente.coordinar())

# Control de añadido de funciones según su categoría

# Un gerente no desarrolla
gerente.addLenguaje('Cobol')
# Un gerente no gestiona proyectos
gerente.addProyecto('Proyecto 3')

# Un Gerente de Proyectos no gestiona personal
gerenteProyecto.addEmpleado('Juan')
gerenteProyecto.addEmpleado(programador)
# Un Gerente de Proyectos no desarrolla
gerenteProyecto.addLenguaje('Ruby')

# Un programador no gestiona proyectos
programador.addProyecto('Proyecto 4')
# Un programador no puede tener empleados
programador.addEmpleado('José')
programador.addEmpleado(programador)