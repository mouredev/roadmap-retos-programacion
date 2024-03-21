
# /*
#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  */

# << DUCK TYPING >>
# Si existe Herencia estariamos hablando de Polimorfismo.
# Incluso en lenguajes que no soportan el concepto de Duck Typing, es decir que son de tipado estático,gracias al poliformismo podemos conseguir algo parecido al Duck Typing.

"""
#TIPOS POLIFORMISMO:
# --> Subtipos

En python tenemos que tener muy en cuenta el DUCK TYPING: If is walks like a duck and it quacks like a duck then it must be a duck.

En python lo más importante importa si existe el método el tipo de dato!!


1.Poliformismo de "subtipos" (tiene lugar en tiempo de EJECUCIÓN). Existen dos vertientes del mismo:
    -Single Dispatch -> Es el más utilizado, lo que quiere decir es que mientras el programa se esta ejecutando se decide que versión del método se va a invocar basándose en el tipo de la referencia del objeto
    -Multiple Dispatch -> Consiste en utilizar/despachar el método correcto según el ORDEN,TIPO y NÚMERO de parámetros o argumentos del método/función.

    Ejemplo: Si tenemos los siguientes métodos homónimos:
                                                A) métodoCualquiera(String a, Integer b, Boolean c),
                                                B) métodoCualquiera(),
                                                C) métodoCualquiera(String x, String y, String z)
    El compilador o interprete decidirá el método correcto basándose en el ORDEN, NÚMERO y TIPO de datos.
                                                Si tengo este método: métodoCualquiera("Hola", "Hello", "Ciao") --> Invocaremos el método A

    CARACTERÍSTICAS:
        1. Poliformimso dinámico 


2.Poliformismo "paramétrico" = Genéricos en JAVA
    CARACTERÍSTICAS:
        1. Poliformimso estático y se realiza en tiempo de EJECUCIÓN
        2. Pueden utilizar técnicas de mejoramiento del desempeño que aplica el compilador
        3. Menos flexibilidad
        4. El programador puede crear programas de forma más general y abstracta. Siempre y cuando se usen lenguajes de tipado estático como Java


3.Poliformismo "ad hoc" (tiene lugar en tiempo de COMPILACIÓN)-> Capacidad que tiene un método o función para arrojar un resultado para diferentes tipos de datos que recibe como argumentos
        CARACTERÍSTICAS:
        1. Poliformimso estático y se realiza en tiempo de EJECUCIÓN
        2. Pueden utilizar técnicas de mejoramiento del desempeño que aplica el compilador
        3. Menos flexibilidad
        4. El programador puede crear programas de forma más general y abstracta. Siempre y cuando se usen lenguajes de tipado estático como Java

        Ejemplo: Si tengo un función de multiplicar que me devuelve un resultado independientemente de los tipos de datos que le paso como argumentos INT, FLOAT etc.
        Tengo un función polimórfica AD HOC

"""
class Animal():
    def __init__(self,name: str,age: int):
        self.name = name
        self.age = age

    def sound(self):
        print("Soy un sonido genérico")


class Perro(Animal):

    def __init__(self, breed):
        self.breed = breed

    # Poliformismo en compilacuón
    def sound(self):
        print("GUAU!")


class Gato(Animal):

    def __init__(self, breed):
        self.breed = breed

    def sound(self):
        print("MIAU!")


# Función para demostrar el poliformismo de tipo AD HOC o OVERLOAD(Sobrecarga)
def saludo_polimorfico(animal: Animal):
    animal.sound()

# CASOS DE USO: Poliformismo en tiempo de compilación.
animal = Animal("Ani1",4)
animal.sound()


perro = Perro("Bull Terrier")
perro.sound()

gato = Gato("British")
gato.sound()


saludo_polimorfico(animal)
saludo_polimorfico(perro)
saludo_polimorfico(gato)



#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.

class Employee():
    # Atributo de clase que heredara cualquier clase hija
    human = True

    def __init__(self,id: int,name: str):
        # Atributos de instancia
        self.id = id
        self.name = name
        print(f"Creando una instancia de Employee: [ID: {self.id} | NAME: {self.name}]")


class Manager(Employee):
    #Atributo de Clase
    fav_color = "blue"

    def __init__(self, id: int, name: str, age: int):
        # Heredamos del constructor de la super clase ID y NAME
        super().__init__(id, name)
        # Añadimos un atributo específico de los Manager
        self.age = age


    def coordinate1(self):
        return f"{self.name} tiene {self.age} y está coordinando un proyecto."


class ProjectManager(Employee):
    #Atributo de Clase
    fav_color = "red"

    def __init__(self, id: int, name: str, username: str):
        # Heredamos del constructor de la super clase ID y NAME
        super().__init__(id, name)
        # Añadimos un atributo específico de los Manager
        self.username = username


    def coordinate2(self):
        return f"El color favorito de {self.name} {self.username} es el {ProjectManager.fav_color.upper()} y está coordinando varios proyectos."


class Programmer(Employee):
    #Atributo de Clase
    fav_color = "green"

    def __init__(self, id: int, name: str, language: str):
        # Heredamos del constructor de la super clase ID y NAME
        super().__init__(id, name)
        # Añadimos un atributo específico de los Manager
        self.language = language


    def code(self):
        return f"El color favorito de {self.name} es el {Programmer.fav_color.upper()} y le encanta picar código {self.language}."


#CASOS DE USO
empleado1 = Employee(1234,"Roberto")
#print(Employee.human) # CURIOSIDAD -> Puedo imprimir por pantalla cualquier atributo de clase sin necesidad de crear una instancia/objeto de la clase

manager1 = Manager(6789,"Berta",32)
print(manager1.coordinate1())
#print(Manager.human) # CURIOSIDAD -> Como es hija de Employee hereda su atributo de clase
#print(Manager.fav_color) # Y tiene un atributo de clase extra

projectManager1 = ProjectManager(5333,"Juan","López")
print(projectManager1.coordinate2())

programmer1 = Programmer(222,"Night","Python")
print(programmer1.code())