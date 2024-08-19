"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Correcto

class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

class Eagle(Bird):
    def fly(self):
        return "Eagle flying"

def make_bird_fly(bird: Bird):
    print(bird.fly())

# Uso correcto del principio de sustitución de Liskov
sparrow = Sparrow()
eagle = Eagle()

make_bird_fly(sparrow)  # Output: Sparrow flying
make_bird_fly(eagle)    # Output: Eagle flying


# Incorrecto

class Bird:
    def fly(self):
        return "Flying"

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

def make_bird_fly(bird: Bird):
    print(bird.fly())

# Uso incorrecto del principio de sustitución de Liskov
ostrich = Ostrich()

# make_bird_fly(ostrich)  # Esto lanzará una excepción: "Ostriches can't fly"


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
"""

class Vehiculo:
    def acelerar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def frenar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Coche(Vehiculo):
    def acelerar(self):
        return "El coche está acelerando"

    def frenar(self):
        return "El coche está frenando"

class Bicicleta(Vehiculo):
    def acelerar(self):
        return "La bicicleta está acelerando"

    def frenar(self):
        return "La bicicleta está frenando"

class Motocicleta(Vehiculo):
    def acelerar(self):
        return "La motocicleta está acelerando"

    def frenar(self):
        return "La motocicleta está frenando"

def probar_vehiculo(vehiculo: Vehiculo):
    print(vehiculo.acelerar())
    print(vehiculo.frenar())

# Crear instancias de cada subclase
coche = Coche()
bicicleta = Bicicleta()
motocicleta = Motocicleta()

# Probar cada vehículo
probar_vehiculo(coche)        # Output: El coche está acelerando, El coche está frenando
probar_vehiculo(bicicleta)    # Output: La bicicleta está acelerando, La bicicleta está frenando
probar_vehiculo(motocicleta)  # Output: La motocicleta está acelerando, La motocicleta está frenando
