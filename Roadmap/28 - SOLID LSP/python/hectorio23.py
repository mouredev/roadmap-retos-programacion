# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

''' 
- EJERCICIO:
Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

-  DIFICULTAD EXTRA:
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
cumplir el LSP.
Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.
'''

class Vehiculo:
    """
    Clase base abstracta para todos los vehículos. Define dos métodos abstractos
    que deben ser implementados por las subclases: acelerar y frenar.
    """
    def acelerar(self):
        """
        Método abstracto para acelerar. Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por una subclase.")
    
    def frenar(self):
        """
        Método abstracto para frenar. Debe ser implementado por las subclases.
        """
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

class Coche(Vehiculo):
    """
    Clase que representa un coche. Implementa los métodos acelerar y frenar
    de acuerdo a la interfaz definida por la clase base Vehiculo.
    """
    def acelerar(self):
        return "[+] - El coche está acelerando."
    
    def frenar(self):
        return "[+] - El coche está frenando."

class Bicicleta(Vehiculo):
    """
    Clase que representa una bicicleta. Implementa los métodos acelerar y frenar
    de acuerdo a la interfaz definida por la clase base Vehiculo.
    """
    def acelerar(self):
        return "[+] - La bicicleta está acelerando."
    
    def frenar(self):
        return "[+] - La bicicleta está frenando."

class Avion(Vehiculo):
    """
    Clase que representa un avión. Implementa los métodos acelerar y frenar
    de acuerdo a la interfaz definida por la clase base Vehiculo.
    """
    def acelerar(self):
        return "[+] - El avión está acelerando."
    
    def frenar(self):
        return "[+] - El avión está frenando."

def test_lsp(vehiculo: Vehiculo):
    """
    Función para probar el principio de sustitución de Liskov (LSP). 
    Toma un objeto Vehiculo y llama a sus métodos acelerar y frenar.
    
    Parámetros:
        vehiculo (Vehiculo): Una instancia de una subclase de Vehiculo.
    """
    print(vehiculo.acelerar())
    print(vehiculo.frenar())

# Lista por comprension de diferentes vehículos que cumplen con el LSP
vehiculos = [Coche(), Bicicleta(), Avion()]

# Probar cada vehículo para asegurar que cumplen con el LSP
for v in vehiculos:
    test_lsp(v)
