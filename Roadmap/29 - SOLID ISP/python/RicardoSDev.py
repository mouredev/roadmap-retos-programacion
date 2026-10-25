'''
Explora el "Principio SOLID de Segregación de Interfaces
* (Interface Segregation Principle, ISP)", y crea un ejemplo
* simple donde se muestre su funcionamiento de forma correcta e incorrecta.
'''

#Incorrecto

class Person:
   
    def estudiando():
        pass
    def dando_clase():
        pass

class Profesor(Person):
    def estudiando():
        print ("Los profes estudian")
    def dando_clase():
        print ("Por ser profe doy clase")

class Estudiante(Person):
    def estudiando():
        print ("Es mi obligación")
    def dando_clase(): #Totalmente superfluo pero obligatorio. Caulquier implementación distinta de pass
        # conduciría a error sino es un Eroor en sí ya provocado
        pass
    
Juan = Profesor
Juan.dando_clase()
Luis = Estudiante
Luis.estudiando()
Luis.dando_clase() # Esta sentencia no hace nada y puede infundir a error

#Correcto

from abc import ABC, abstractmethod

class Clase(ABC):
    @abstractmethod
    def dando_clase():
        pass

class Estudio(ABC):
    @abstractmethod
    def estudiando():
        pass

class Profesor(Clase, Estudio):
    def estudiando():
        return "Los profes estudian"
    def dando_clase():
        return "Por ser profe doy clase"

class Estudiante(Estudio):
    def estudiando():
        return "Es mi obligación"
#Ya no sería obligatorio incluir el método dando_clase()    

Juan = Profesor
print(Juan.dando_clase())
print(Juan.estudiando())
Luis = Estudiante
print(Luis.estudiando())

'''
* DIFICULTAD EXTRA (opcional):
* Crea un gestor de impresoras.
* Requisitos:
* 1. Algunas impresoras sólo imprimen en blanco y negro.
* 2. Otras sólo a color.
* 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
* Instrucciones:
* 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
*  2. Aplica el ISP a la implementación.
*  3. Desarrolla un código que compruebe que se cumple el principio.
'''

class blanco_negro():
    def imprimir_b_n (self, documento):
        pass        
class color():
    def imprimir_color (self, documento):
        pass
class multifuncion():
    def imprimir(self, documento):
        pass
    def escanear(self, documento):
        pass
    def enviar_fax(self, documento):
        pass
        

class impresora_b_n(blanco_negro):
    def imprimir_b_n(self, documento):
        print(f"Imprimiendo en blanco y negro {documento}") 
class impresora_color(color):
    def imprimir_color(self, documento):
        print(f"Imprimiendo en color {documento}")
class impresora_multifuncion(multifuncion):        
    def imprimir (self, documento):
            print(f"Imprimiendo b/n y color {documento}")
    def escanear (self, documento) -> str:
            print (f"Escaneando {documento}")
    def enviar_fax (self, documento):
        print (f"Enviando {documento}")     
# Test

def test_impresora():
    printer = impresora_b_n()
    color_printer = impresora_color()
    multi_printer = impresora_multifuncion()

    printer.imprimir_b_n("Doc.doc")
    color_printer.imprimir_color("Doc.doc")
    multi_printer.imprimir("Doc.doc")
    multi_printer.escanear("Doc.doc")
    multi_printer.enviar_fax("Doc.doc")
test_impresora()    

