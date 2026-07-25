#29 SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
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
from abc import ABC, abstractmethod


# Interfaces pequeñas y específicas para cada tipo de vehículo
class VehiculoTerrestre(ABC):
    @abstractmethod
    def conducir(self):
        pass

class VehiculoAereo(ABC):
    @abstractmethod
    def volar(self):
        pass

class VehiculoAcuatico(ABC):
    @abstractmethod
    def navegar(self):
        pass

# Clase Coche que solo necesita implementar la interfaz de Vehículo Terrestre
class Coche(VehiculoTerrestre):
    def conducir(self):
        print("El coche está conduciendo.")

# Clase Avión que solo implementa la interfaz de Vehículo Aéreo
class Avion(VehiculoAereo):
    def volar(self):
        print("El avión está volando.")

# Clase Barco que solo implementa la interfaz de Vehículo Acuático
class Barco(VehiculoAcuatico):
    def navegar(self):
        print("El barco está navegando.")

# Crear instancias de los vehículos
coche = Coche()
avion = Avion()
barco = Barco()

# Usar los métodos según las interfaces implementadas
coche.conducir()  # Salida: El coche está conduciendo.
avion.volar()     # Salida: El avión está volando.
barco.navegar()   # Salida: El barco está navegando.

#mal uso
# Interfaz general que agrupa todas las funcionalidades para vehículos
class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def navegar(self):
        pass

# Clase Coche que no necesita volar ni navegar, pero debe implementar los métodos
class Coche(Vehiculo):
    def conducir(self):
        print("El coche está conduciendo.")

    def volar(self):
        raise NotImplementedError("El coche no puede volar.")  # Error

    def navegar(self):
        raise NotImplementedError("El coche no puede navegar.")  # Error

# Clase Avión que no necesita conducir ni navegar, pero debe implementar los métodos
class Avion(Vehiculo):
    def conducir(self):
        raise NotImplementedError("El avión no puede conducir.")  # Error

    def volar(self):
        print("El avión está volando.")

    def navegar(self):
        raise NotImplementedError("El avión no puede navegar.")  # Error

# Clase Barco que no necesita conducir ni volar, pero debe implementar los métodos
class Barco(Vehiculo):
    def conducir(self):
        raise NotImplementedError("El barco no puede conducir.")  # Error

    def volar(self):
        raise NotImplementedError("El barco no puede volar.")  # Error

    def navegar(self):
        print("El barco está navegando.")

coche = Coche()
avion = Avion()
barco = Barco()

# Usar los métodos según la interfaz grande
coche.conducir()      # Funciona correctamente: "El coche está conduciendo."
coche.volar()         # Error: El coche no puede volar.
coche.navegar()       # Error: El coche no puede navegar.

avion.volar()         # Funciona correctamente: "El avión está volando."
avion.conducir()      # Error: El avión no puede conducir.
avion.navegar()       # Error: El avión no puede navegar.

barco.navegar()       # Funciona correctamente: "El barco está navegando."
barco.volar()         # Error: El barco no puede volar.
barco.conducir()      # Error: El barco no puede conducir.

""" !!!EXTRA¡¡¡ """

# Interfaces (Clases Abstractas)
class ImpresoraBlancoNegroInterfaz(ABC):
    @abstractmethod
    def impresion_en_blanco_y_negro(self):
        pass

class ImpresoraColorInterfaz(ABC):
    @abstractmethod
    def impresion_a_color(self):
        pass

class EscanerInterfaz(ABC):
    @abstractmethod
    def escanear(self):
        pass

class EnviarFaxInterfaz(ABC):
    @abstractmethod
    def enviar_fax(self):
        pass

# Clases concretas
class ImpresoraBlancoNegro(ImpresoraBlancoNegroInterfaz):
    def impresion_en_blanco_y_negro(self):
        print("Se está imprimiendo el documento en blanco y negro")

class ImpresoraColor(ImpresoraColorInterfaz):
    def impresion_a_color(self):
        print("Se está imprimiendo el documento a color")

class ImpresoraMultifuncional(ImpresoraColorInterfaz, ImpresoraBlancoNegroInterfaz,
                              EscanerInterfaz, EnviarFaxInterfaz):

    def impresion_a_color(self):
        print("Se está imprimiendo el documento a color")

    def impresion_en_blanco_y_negro(self):
        print("Se está imprimiendo el documento en blanco y negro")

    def enviar_fax(self):
        print("La impresora está enviando un Fax")

    def escanear(self):
        print("La impresora está escaneando para sacarle copia al documento")

# Crear instancias de las clases
impresora_blanco_y_negro = ImpresoraBlancoNegro()
impresora_color = ImpresoraColor()
impresora_multifuncional = ImpresoraMultifuncional()

# Ejecución del código
print("\nImpresora a color e impresora en blanco y negro:")
impresora_blanco_y_negro.impresion_en_blanco_y_negro()
impresora_color.impresion_a_color()

print("\nImpresora Multifuncional:")
impresora_multifuncional.impresion_a_color()
impresora_multifuncional.impresion_en_blanco_y_negro()
impresora_multifuncional.enviar_fax()
impresora_multifuncional.escanear()
