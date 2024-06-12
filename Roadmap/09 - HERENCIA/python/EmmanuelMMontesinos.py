"""
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
"""

# Herencia
'''Super Clase / Clase Padre'''
class Animal:
    # Inicializo con todos los parametros comunes para todos los animales
    def __init__(self,nombre,categoria,sonido="") -> None:
        self.nombre = nombre
        self.categoria = categoria
        self.sonido = sonido
    
    # Utilizo el metodo
    def __str__(self) -> str:
        return "Animal"
    
    # Funciones comunes para todos los animales: Mostrar los datos y emitir sonidos
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}\n")
        
    def emitir_sonido(self):
        print(f"{self.nombre.title()} hace:",end=" ")
        print(self.sonido + "\n")
        

'''Clases que heredan de Animal'''
class Perro(Animal):
    def __init__(self, nombre, categoria) -> None:
        super().__init__(nombre, categoria,sonido="Guau!")
    
    def __str__(self) -> str:
        return "Perro"
    
    # Función propia de Perro
    def rastrar(self):
        print(f"El {self} esta rastreando\n")
        
class Gato(Animal):
    def __init__(self, nombre, categoria) -> None:
        super().__init__(nombre, categoria,sonido="Miau!")
        
    def __str__(self) -> str:
        return "Gato"
    
    # Función propia de Gato
    def ronronear(self):
        print(f"El {self} esta ronroneando: Grrrrr\n")


# Pruebas
perro = Perro("Ojala","Grande")
perro.imprimir_datos()
perro.emitir_sonido()
perro.rastrar()

gato = Gato("Salomon","Pequeño")
gato.imprimir_datos()
gato.emitir_sonido()
gato.ronronear()



"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""


class Empleados:
    
    def __init__(self,nombre,puesto) -> None:
        Empleados.n_empleados += 1
        self.id = Empleados.n_empleados
        self.nombre = nombre
        self.puesto = puesto

    def imprimir_datos(self):
        print("Información del trabajador:")
        print(f"Nombre: {self.nombre}")
        print(f"Id: {self.id}\n")
    
    n_empleados = 0
    lista_empleados = []
    
        
class Programadores(Empleados):
    
    def __init__(self, nombre, puesto,lider) -> None:
        super().__init__(nombre, puesto)
        self.tarea = ""
        self.lider = lider
        self.objetivo = ""
        Empleados.lista_empleados.append(self)
        print(f"{self.nombre} ha sido añadido al grupo de {self.lider}\n")
            
class Lider(Empleados):
    
    def __init__(self, nombre, puesto) -> None:
        super().__init__(nombre, puesto)
        print(f"{self.nombre} es ahora Lider de Equipo!\n")
        
    def asignar_tarea(self,tarea):
        empleados = self.ver_empleados()
        for empleado in empleados:
            empleado.tarea = tarea
            print(f"{self.nombre} ha asignado una tarea a {empleado.nombre}: {empleado.tarea}\n")
            
    def ver_empleados(self):
        lista = [empleado for empleado in Empleados.lista_empleados if empleado.lider == self.nombre]
        return lista
    
    def imprimir_empleados(self):
        lista = self.ver_empleados()
        print(f"Equipo de {self.nombre}:")
        for empleado in lista:
            print(f"{empleado.nombre} ---> {empleado.puesto}")
        print()
    
class Jefe(Empleados):
    
    def __init__(self, nombre, puesto) -> None:
        super().__init__(nombre, puesto)
        print(f"{self.nombre} ha comprado la Empresa\n")
        
    def asignar_objetivo(self,lider,objetivo):
        lider.objetivo = objetivo
        print(f"{self.nombre} ha asignado el objetivo de '{objetivo}' a {lider.nombre}\n")


# Pruebas
    
lider = Lider("MoureDev","Jefe de Proyecto")
empleado_1 = Programadores("Emmanuel","Junior","MoureDev")
jefe = Jefe("Elon Musk","CEO")

lider.imprimir_datos()
lider.imprimir_empleados()

lider.asignar_tarea("Haz este Ejercicio!")
jefe.asignar_objetivo(lider,"destruir Twitter")
