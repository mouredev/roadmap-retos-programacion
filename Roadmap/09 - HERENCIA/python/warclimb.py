#09 HERENCIA
#### Dificultad: Media | Publicación: 26/02/24 | Corrección: 04/03/24

## Ejercicio


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

class Animal:
    def __init__(self, nombre, sonido):
        self._nombre = nombre
        self._sonido = sonido

    # getters y setters
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def sonido(self):
        return self._sonido
    
    @sonido.setter
    def sonido(self, sonido):
        self._sonido = sonido

    def emitir_sonido(self):
        return self._sonido

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "AWUUUFFF!")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Mmmmmmeeeeeoooowww!")

# Creo un perro y un gato
perro = Perro("Sora")
gato = Gato("Doña Tecla")

# Muestro el sonido que emiten
print(f"Hola soy {perro._nombre} escucha esto: {perro.emitir_sonido()}")
print(f"Hola soy {gato._nombre} escucha esto: {gato.emitir_sonido()}")


# DIFICULTAD EXTRA
class Empleado:
    """
    Clase padre que representa a los empleados
    args:
    - id (int): identificador del empleado
    - nombre (str): nombre del empleado
    """
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    # getters y setters
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"Empleado: {self._nombre}"

class Gerente(Empleado):
    """
    Clase que representa a un gerente
    args:
    - id (int): identificador del empleado
    - nombre (str): nombre del empleado

    methods:
    - contratar(empleado): contrata un empleado
    - despedir(empleado): despide un empleado
    - mostrar_empleados(): muestra los empleados a cargo
    """

    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        print("Gerente creado")
        self._empleados = []

    def contratar(self, empleado):
        self._empleados.append(empleado)
    
    def despedir(self, empleado):
        self._empleados.remove(empleado)
    
    def mostrar_empleados(self):
        return self._empleados

    def __str__(self):
        return f"Gerente: {self._nombre}"
    
class GerenteProyecto(Empleado):
    """
    Clase que representa a un gerente de proyecto
    args:
    - id (int): identificador del empleado
    - nombre (str): nombre del empleado

    methods:
    - asignar_proyecto(proyecto): asigna un proyecto
    - mostrar_proyectos(): muestra los proyectos asignados
    """

    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        print("Gerente de Proyecto creado")
        self._proyectos = []

    # getters y setters
    @property
    def proyectos(self):
        return self._proyectos

    @proyectos.setter
    def proyectos(self, proyectos):
        self._proyectos = proyectos
    
    # metodos
    def asignar_proyecto(self, proyecto):
        """
        Asigna un proyecto al gerente de proyecto
        args:
        - proyecto (str): proyecto a asignar
        """
        self._proyectos.append(proyecto)
    
    def mostrar_proyectos(self):
        """
        Muestra los proyectos asignados al gerente de proyecto
        """
        return self._proyectos
    
    def __str__(self):
        return f"Gerente de Proyecto: {self._nombre}"

class Programador(Empleado):
    """
    Clase que representa a un programador
    args:
    - id (int): identificador del empleado
    - nombre (str): nombre del empleado

    methods:
    - asignar_especialidades(especialidad): asigna una especialidad
    - mostrar_especialidades(): muestra las especialidades asignadas
    """

    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        print("Programador creado")
        self._especialidades = []

    # getters y setters
    @property
    def especialidades(self):
        return self._especialidades
    
    @especialidades.setter
    def especialidades(self, especialidades):
        self._especialidades = especialidades
    
    # métodos
    def asignar_especialidades(self,especialidad):
        """
        Asigna una especialidad al programador
        args:
        - especialidad (str): especialidad a asignar
        """
        self._especialidades.append(especialidad)
        
        
    def mostrar_especialidades(self):
        """
        Muestra las especialidades asignadas al programador
        """
        return self._especialidades
    
    def __str__(self):
        return f"Programador: {self._nombre}, especialista en {self._especialidades}"

# Creamos empleados de diferentes tipos
gerente = Gerente(1, "Juan")
gerente_proyecto = GerenteProyecto(2, "Pedro")
programador_cobol = Programador(3, "Eutimio")

# Contratamos empleados
gerente.contratar(gerente_proyecto)
gerente_proyecto.asignar_proyecto("TPV Bancos")

# asignamos especialidades al programador
programador_cobol.asignar_especialidades("Cobol")

# Mostramos los empleados a cargo del gerente
print(f"{gerente} tiene a cargo a: {gerente.mostrar_empleados()}")
print(f"{gerente_proyecto} tiene asignado el proyecto: {gerente_proyecto.mostrar_proyectos()}")
print(f"{programador_cobol} tiene asignadas las especialidades: {programador_cobol.mostrar_especialidades()}")
    
