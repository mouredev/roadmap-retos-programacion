'''
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
'''

class animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
class perro(animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def guau(self):
        print(f'{self.nombre}: Guau!')

class gato(animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    def miau(self):
        print(f'{self.nombre}: Miau!')

pity = perro('Pity', 15, 'Oscuro')
croqueta = gato('Croqueta', 9, 'Naranja')

pity.guau()
croqueta.miau()

'''
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
# 
'''

class empresa:
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa

#Clase base de todos los objetos, la de empresa de momento no tiene mucho que aportar mas que el nombre    
class empleado(empresa):
    def __init__(self, nombre_empresa, id, nombre, ):
        super().__init__(nombre_empresa)
        self.id = id
        self.nombre = nombre

#GERENTE
class Gerente(empleado):
    autorizacion_nvl = 3 #Autorizacion para interactuar con otros objetos, como puertas o acciones dentro de la empresa
    def __init__(self, nombre_empresa, id, nombre,):
        super().__init__(nombre_empresa, id, nombre) #Se heredan parametros de "empleado"

    def pagar_remuneracion(): #Simple mensaje por pantalla
        print('El gerente a pagado la remuneracion mensual!')

#Gerente proyectos
class gerente_de_proyecto(empleado):
    autorizacion_nvl = 2
    def __init__(self, nombre_empresa, id, nombre,):
        super().__init__(nombre_empresa, id, nombre)
    
    def Incentivo():
        print('El gerente de proyectos ha dado un bono al que termine primero como incentivo!')

#Programador
class programador(empleado):
    autorizacion_nvl = 1
    def __init__(self, nombre_empresa, id, nombre,):
        super().__init__(nombre_empresa, id, nombre)
    
    def trabajar():
        print('El programador esta trabajando muy duro!')

###########################################################.-.-.-.-  Instanciar clases para crear los 3 primeros objetos


junior1 = programador('Google', '000000000000000001', 'Adan') #se que el id deberia ser numerico, pero me gusta como se ven los "000000" en adan xD
senior1 = gerente_de_proyecto('Google', 255, 'Jesus')
jefe = Gerente('Google', 0, 'Dios')

###########################################################.-.-.-.-  Haciendo clara referencia a la jerarquia de una empresa, pero con dios xd



