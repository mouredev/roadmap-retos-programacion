# #09 HERENCIA Y POLIMORFISMO
#### Dificultad: Media | Publicación: 26/02/24 | Corrección: 04/03/24

## Ejercicio

'''  
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 '''

def main():
    # Nuestra super clase
    class animal():
        def __init__(self, name, sound):
            self.nombre = name
            self.sonido = sound

        # metodo para emitir sonido
        def emite_sonido(self):
            print(f"{self.nombre} dice {self.sonido}") # Accedemos a los parametros mediante las variables

    # sub clase
    class perro(animal):
        # Sus parametros
        def __init__(self, name):
            # Parametros heredados del padre o super clase
            super().__init__(name, "rrrr") # El name del padre hereda al hijo. Sound es "rrrr" por defecto
            
    # sub clase
    class gato(animal):
        # Sus parametros
        def __init__(self, name):
            # Parametros heredados del padre o super clase
            super().__init__(name, "miau miau") # El name del padre hereda al hijo. sound es "miau miau" por defecto
    
    # Llamo a la sub clase. Ingreso un argumento, el otro se hereda por defecto
    animal_domestico = gato("Mia Colucci")
    # Llamo a metodo para emitir sonido, recibe los argumentos de la funcion que acabo de llamar
    animal_domestico.emite_sonido()
    # Llamo a la sub clase. Ingreso un argumento, el otro se hereda por defecto
    animal_domestico = perro("Max")
    # Llamo a metodo para emitir sonido, recibe los argumentos de la funcion que acabo de llamar
    animal_domestico.emite_sonido()
    """
    En terminal se imprime: Max dice rrrr
    """

    print("///////")
    """ 
    * DIFICULTAD EXTRA (opcional):
    * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
    * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
    * Cada empleado tiene un identificador y un nombre.
    * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
    * actividad, y almacenan los empleados a su cargo.
    """

    class empleado:
        def __init__(self, identificador, nombre) -> None:
            self.identificacion = identificador
            self.nombre = nombre

#//////////////////////
    class gerente(empleado):
        def __init__(self, identificador, nombre, departamento):
            super().__init__(identificador, nombre)
            self.departamento = departamento

        def placa(self):
            print(f"Nombre: {self.nombre}, ID: {self.identificacion}, Departamento: {self.departamento}")
#//////////////////////
    class gerente_proyecto(empleado):
        def __init__(self, identificador, nombre, departamento, proyecto):
            super().__init__(identificador, nombre)
            self.departamento = departamento
            self.proyectos = proyecto

        def placa(self):
            print(f"Nombre: {self.nombre}, ID: {self.identificacion}, Departamento: {self.departamento}, Proyecto: {self.proyectos}")
#//////////////////////
    class programador(empleado):
        def __init__(self, identificador, nombre, departamento, proyecto, tarea):
            super().__init__(identificador, nombre)
            self.departamento = departamento
            self.proyectos = proyecto
            self.area_de_trabajo = tarea

        def placa(self):
            print(f"Nombre: {self.nombre}, ID: {self.identificacion}, Departamento: {self.departamento}, Proyecto: {self.proyectos}, Tarea: {self.area_de_trabajo}")
#//////////////////////

    var_gerente = gerente("01", "Daniel", "Gerencia")
    var_gerente_proyecto = gerente_proyecto("02", "Luis", "Gerente de proyecto", "Manhattan")
    var_programador = programador("03", "Gloria", "Programacion", "Manhattan", "Resolver bugs")

    var_gerente.placa()
    var_gerente_proyecto.placa()
    var_programador.placa()

if __name__=="__main__":
    main()



