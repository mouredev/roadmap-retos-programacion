'''
* EJERCICIO:
* Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
* y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
'''
# Correcto

class Empleado:
    def puesto (self):
        return "Trabaja"

class Jefe(Empleado):
    def puesto (self):
        return "Cobra"

Juan = Empleado()
Pedro = Jefe()
print(Juan.puesto())
print(Pedro.puesto())
#Aquí intercambiamos y la funcionalidad debería ser compatible
Juan = Jefe()
Pedro = Empleado()
print(Juan.puesto())
print(Pedro.puesto())

# Incorrecto
class Empleado:
    def puesto (self):
        return "Trabaja, no manda"

class Jefe(Empleado):
    def puesto (self):
        return "Sólo manda, no trabaja"

Juan = Empleado()
Pedro = Jefe()
print(Juan.puesto())
print(Pedro.puesto())
#Aquí intercambiamos y la funcionalidad debería ser compatible
Juan = Jefe()
Pedro = Empleado()
print(Juan.puesto())
print(Pedro.puesto())
#Pero en el resultado se observa la contradicción. No hay una especialización sino funciones incompatibles 

'''
* DIFICULTAD EXTRA (opcional):
* Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
* cumplir el LSP.
* Instrucciones:
* 1. Crea la clase Vehículo.
* 2. Añade tres subclases de Vehículo.
* 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
* 4. Desarrolla un código que compruebe que se cumple el LSP.
'''

class Vehiculo:
    def __init__(self, velocidad = 1):
        self.velocidad = velocidad    

    def acelerar (self):
        self.velocidad += 1

    def frenar (self):
        self.velocidad -= 1

class Coche(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass

class Moto(Vehiculo):    
    pass

Renault = Coche()
BH = Bicicleta()
BMV = Moto()


BH = Coche()
BH.frenar()
print(BH.velocidad)
Renault.acelerar()
print(Renault.velocidad)
Renault.frenar()
print(Renault.velocidad)
BH.acelerar()
print(BH.velocidad)
print(Renault.velocidad)
Renault = Bicicleta()
Renault.acelerar()
print(Renault.velocidad)
print(BH.velocidad)
BH = Bicicleta()
print(BH.velocidad)
#A pesar de las sustituciones la identidad de los objetos se conserva junto con su velocidad y la identidad
#queda guardada con el nombe de la variable objeto y arrastra a sus propiedades heredadas, en este caso: velocidad
