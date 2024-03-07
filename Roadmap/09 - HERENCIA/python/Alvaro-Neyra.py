#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.

# Superclase Animal:
class Animal:
    def __init__(self, name, especie, edad):
        self.name = name
        self.especie = especie
        self.edad = edad
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.sleep} is sleeping.")
    def make_sound(self):
        pass # Dejamos este metodo sin implementar, ya que los animales hacen sonidos distintos para comunicarse
    def description(self):
        print(f"Soy un animal del tipo: {type(self).__name__}")
    def datos(self):
        print(f"Mi nombre es {self.name}")
        print(f"Tengo {self.edad} años de edad!")

# Subclase de Animal para Perro:
class Perro(Animal):
    def __init__(self, name, edad, breed = "No especificado"):
        super().__init__(name, "Perro", edad)
        self.breed = breed
    def make_sound(self):
        print("Woof!!")
    
# Subclase de Animal para Gato:
class Gato(Animal):
    def __init__(self, name, edad, breed = "No especificado"):
        super().__init__(name, "Gato", edad)
        self.breed = breed
    def make_sound(self):
        print("Miau!!")

## Probando las clases:
mi_perro = Perro("Luke", 2)
un_gato = Gato("Michi", 8)
un_gato_de_raza = Gato("Bigotes", 2, "Persa")
un_perro_de_raza = Perro("Bobi", 1, "Cane Corso")

# Usamos make_sound en la clase perro:
mi_perro.make_sound()
# Imprimimos en consola la raza no especificada de mi perro:
raza_de_mi_perro = mi_perro.breed
print(raza_de_mi_perro)
# Cambiamos la raza de mi perro
mi_perro.breed = "Mestizo"
raza_de_mi_perro = mi_perro.breed
print(raza_de_mi_perro)
# Usamos make_sound() de un gato:
un_gato.make_sound()
# Usamos description de la clase padre
un_perro_de_raza.description()
# Usamos description de la clase padre con una subclase de gato:
un_gato_de_raza.description()
# Usamos el metodo datos de la superclase Animal en una subclase (mi_perro):
mi_perro.datos()
# un_gato.datos():
un_gato.datos()

#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.

# Superclase Empleado:
class Empleado:
    def __init__(self, nombre, id_de_empleado):
        self.nombre = nombre
        self.id = id_de_empleado
    def __str__(self):
        return "El id del empleado %s es %s" % (self.nombre, self.id)
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Id del empleado: {self.id}")
        print(f"Cargo: {type(self).__name__}")
    def cargo(self):
        print(f"Cargo: {type(self).__name__}")

# Subclase Gerente:
class Gerente(Empleado):
    def __init__(self, nombre, id_de_empleado):
        super().__init__(nombre, id_de_empleado)
        self.empleados_a_monitorear = []
    def agregar_empleados(self, empleado):
        if not empleado in self.empleados_a_monitorear:
            self.empleados_a_monitorear.append(empleado)
        else:
            print(f"Ya esta en la lista de empleados a cargo!")
    def despedir_empleado(self, empleado):
        if empleado in self.empleados_a_monitorear:
            self.empleados_a_monitorear.remove(empleado)
        else:
            print(f"El gerente: {self.nombre} no esta a cargo del empleado: {empleado}")
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Empleados a monitorear: ")
        for indice, empleado in enumerate(self.empleados_a_monitorear):
            print(f"{indice + 1}: {empleado}")

# Subclase Gerente de Proyectos:
class GerenteDeProyectos(Empleado):
    def __init__(self, nombre, id_de_empleado):
        super().__init__(nombre, id_de_empleado)
        self.proyectos_a_cargo = []
    def agregar_proyectos(self, proyecto):
        if not proyecto in self.proyectos_a_cargo:
            self.proyectos_a_cargo.append(proyecto)
        else:
            print(f"{proyecto} ya esta en la lista de proyectos a cargo del gerente de proyectos {self.nombre}")
    def eliminar_proyectos(self, proyecto):
        if proyecto in self.proyectos_a_cargo:
            self.proyectos_a_cargo.remove(proyecto)
        else:
            print(f"El Gerente de Proyectos: {self.nombre} no esta a cargo del proyecto: {proyecto}")
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Proyectos a cargo:")
        for indice, proyecto in enumerate(self.proyectos_a_cargo):
            print(f"{indice + 1}: {proyecto}")

# Subclase Programador:
class Programador(Empleado):
    def __init__(self, nombre, id_de_empleado):
        super().__init__(nombre, id_de_empleado)
        self.lenguages = []
    def anadir_lenguage(self, lenguaje):
        if lenguaje not in self.lenguages:
            self.lenguages.append(lenguaje)
        else:
            print(f"{lenguaje} ya esta en la lista de lenguajes del programador: {self.nombre}")
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguajes aprendidos por el programador: {self.nombre}")
        for lenguaje in self.lenguages:
            print("- %s" % lenguaje)


## GERENTE:
## Usando las subclases de la superclase Empleado:
gerente_principal = Gerente("Alvaro", 143)
gerente_principal_de_proyectos = GerenteDeProyectos("Juan", 120)
programador_junior = Programador("Carlos", 902)
programador_midlevel = Programador("Coder", 101)
el_mejor_programador_del_mundo = Programador("Brais Moure", 404)
lider_del_proyecto = Programador("SuperCoder", 1902)

# Agregando empleados como gerente
gerente_principal.agregar_empleados(programador_junior)
gerente_principal.agregar_empleados(programador_midlevel)
gerente_principal.agregar_empleados(el_mejor_programador_del_mundo)
# Mostrando informacion del gerente principal
gerente_principal.mostrar_informacion()
# Eliminando un empleado (despedir):
gerente_principal.despedir_empleado(programador_junior)
gerente_principal.mostrar_informacion()
# Eliminando un empleado que no esta en la lista de empleados del gerente principal:
gerente_principal.despedir_empleado(lider_del_proyecto)
# Usando el metodo .cargo() de la superclase Empleado:
gerente_principal.cargo()

## GERENTE DE PROYECTOS:
gerente_principal_de_proyectos = GerenteDeProyectos("Alvaro Neyra", 1293)
# Agregando proyectos:
gerente_principal_de_proyectos.agregar_proyectos("Clon de Spotify")
gerente_principal_de_proyectos.agregar_proyectos("PassVault")
gerente_principal_de_proyectos.agregar_proyectos("E-Commerce")
# Conseguiendo la informacion del gerente de proyectos:
gerente_principal_de_proyectos.mostrar_informacion()
# Eliminando un proyecto
gerente_principal_de_proyectos.eliminar_proyectos("Clon de Spotify")
gerente_principal_de_proyectos.mostrar_informacion()

## PROGRAMADOR:
# Anadiendo lenguajes al lider del proyecto
lider_del_proyecto.anadir_lenguage("Java")
lider_del_proyecto.anadir_lenguage("Python")
lider_del_proyecto.anadir_lenguage("JavaScript")
lider_del_proyecto.anadir_lenguage("Rust")
# Repetiendo un lenguaje:
lider_del_proyecto.anadir_lenguage("Python")
# Mostrando informacion
lider_del_proyecto.mostrar_informacion()

