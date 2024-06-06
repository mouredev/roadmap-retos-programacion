import os
os.system('clear') #MAC/LINUX
os.system('cls') #WINDOWS

"""
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal."""

class Animal():#Declaramos la clase principal Animal
    
    def __init__(self,sonido, animal):#Definimos el método init que recibirá 2 parámetros
        self.sonido = sonido #Declaramos las variables con self
        self.animal = animal# para guardar los 2 parámetros recibidos
    def print(self):#Definimos una función que imprima en base a los argumentos recibidos
        print(self.animal, self.sonido)# en los 2 parámetros


class Especie(Animal):#Declaramos la clase Especie y entre paréntesis le indicamos de qué clase heredará
    articulo ="El"#Declaramos un artículo definido masculino por defecto 
    def print(self):#Declaramos una función llamada igual que la heredada de la clase padre (no obligatorio)
        if self.animal.endswith("a"):#Condicionamos para los las especies que se nombran con artículo femenino
            self.articulo="La"# , en español habitualmente las especies que acaban en "a"  
        print(self.articulo, self.animal, self.sonido)# Llamamos a la función heredada (2 parámetros) y propia
    # (3 parámetros) en un ejemplo de polimorfismo, en los casos de herencia prevalece la función que se encuentre en la
    # subclase, si es herencia múltiple también pero se establece una jerarquía según el orden en el que heredemos las clases
    # de izquierda a derecha como vemos en la clase Programador del ejercicio de abajo

mi_perro = Especie("ladra", "perro")
mi_gato = Especie("maulla", "gato")
mi_vaca = Especie("muge", "vaca")
mi_tigre = Especie("ruge", "tigre")
mi_perro.print()
mi_gato.print()
mi_vaca.print()
mi_tigre.print()
print("\n\n")


"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Empleado():
 
    def __init__(self):
       self.finanzas = "NO"
       self.compras = "NO"
       self.proyectos = "NO"
       self.organizacion = "NO"
       self.programacion = "NO"
       self.despliegue = "NO"
   
    def print_propiedades(self, cargo, id , nombre):
          self.cargo = cargo
          self.id = id
          self.nombre = nombre
         
          print ("\nid:", self.id, "\nNombre:",self.nombre,"\nCargo:", self.cargo,"\n¿Hace finanzas? =", 
               self.finanzas,"\n¿Hace compras? =", self.compras, "\n¿Planifica proyectos? =", self.proyectos,
               "\n¿Organiza el trabajo? =", self.organizacion, "\n¿Pica código? =", self.programacion,
               "\n¿Despliega programas? =",self.despliegue)
      
    def print_empleados(self,list_empleados):
        print ("Empleados a su cargo:", end=' ')
        print(' , '.join(list_empleados))
        print("")
     
class Gerente(Empleado):
      
      def es_gerente(self, id, nombre,lista_g):
        self.finanzas="SI"
        self.compras="SI"
        self.print_propiedades("Gerente", id ,nombre)
        self.print_empleados(lista_g)

 
class Gerente_proyecto(Gerente,Empleado):
         
      def es_gerente_proyecto(self, id, nombre,lista_p):
        self.organizacion="SI"
        self.proyectos="SI"
        self.print_propiedades("Gerente de proyecto", id ,nombre)
        self.print_empleados(lista_p)

class Programador (Gerente_proyecto,Gerente,Empleado):
      
      def es_programador(self, id, nombre):
        self.programacion="SI"
        self.despliegue="SI"     
        self.print_propiedades("Programador", id ,nombre)
        

gerente = Gerente()
gerente_proyecto = Gerente_proyecto()
programador = Programador()

dict_empleados = {
1: "Miguel",
2: "Sandra",
3: "Carlos",
4: "Rocío",
5: "Pedro",
6: "Lucía",
7: "Steven",
8: "Sara",
9: "Guillermo",
10: "Leire"
}
list_empleados = []
list_proyectos = []
for k,v in dict_empleados.items():
      if  k>2 and k<6:
          list_empleados.append(v)
      if k>= 6:
          list_empleados.append(v)
          list_proyectos.append(v)

for k,v in dict_empleados.items():

   if k<=2:
        gerente.es_gerente(k,v,list_empleados)
        
   elif k>2 and k<6:
        gerente_proyecto.es_gerente_proyecto(k,v,list_proyectos)
        
   else:
        programador.es_programador(k,v)