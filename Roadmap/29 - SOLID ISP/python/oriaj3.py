"""
29 - SOLID ISP - Interface Segregation Principle
Autor de la solución: oriaj3    

El principio de segregación de interfaces (ISP) establece que una clase no debe ser forzada a implementar interfaces que no usará.
En otras palabras, una clase no debe depender de métodos que no necesita. En lugar de tener una interfaz grande que contenga
muchos métodos, es mejor tener varias interfaces más pequeñas que contengan solo los métodos necesarios. 

Un ejemplo sería una interfaz de impresión que contiene métodos para imprimir, escanear y enviar por fax. Si una clase solo necesita
el método de impresión, no debería verse obligada a implementar los métodos de escaneo y fax.

En Python no hay una forma directa de implementar interfaces, pero se pueden usar clases abstractas para lograr un comportamiento similar.
Se usa la librería abc (Abstract Base Classes) para definir clases abstractas.
"""

"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""

# Ejemplo incorrecto
from abc import ABC, abstractmethod

class PrinterInterface(ABC):
    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def escanear(self):
        pass

    @abstractmethod
    def fax(self):
        pass

class PrinterBW(PrinterInterface):
    def imprimir(self):
        return "Imprimiendo en blanco y negro"
    
    def escanear(self):
        raise Exception("Esta impresora no puede escanear")
    
    def fax(self):
        raise Exception("Esta impresora no puede enviar fax")

class PrinterScanner(PrinterInterface):
    def imprimir(self):
        return "Imprimiendo"
    
    def escanear(self):
        return "Escaneando"
    
    def fax(self):
        raise Exception("No puedo enviar fax")

# Ejemplo correcto

class Im

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */
"""

