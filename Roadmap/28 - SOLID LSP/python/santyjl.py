#28 SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
"""

'''
La L de SOLID alude al apellido de quien lo creó, Barbara Liskov, y dice que “las clases derivadas
deben poder sustituirse por sus clases base”.
'''

#Mal uso
class Ave:
    def volar(self):
        return "El ave está volando"

class Pinguino(Ave):
    def volar(self):
        # Los pingüinos no pueden volar, pero al ser una subclase de Ave,
        # nos vemos obligados a implementar este método de una forma ilógica.
        raise Exception("Los pingüinos no pueden volar")

# Función que espera cualquier ave
def mover_ave(ave: Ave):
    return ave.volar()

# Creamos un objeto de la clase Pinguino
pinguino = Pinguino()

# Intentamos volar con el pingüino, pero causa un error
print(mover_ave(pinguino))  # Error: Los pingüinos no pueden volar

#Buen uso
class Ave:
    def mover(self):
        return "El ave se está moviendo"

class AveVoladora(Ave):
    def volar(self):
        return "El ave está volando"

class Pinguino(Ave):
    def mover(self):
        return "El pingüino está nadando"

class Aguila(AveVoladora):
    def volar(self):
        return "El águila está volando alto"

# Función que puede aceptar cualquier tipo de ave para moverse
def mover_ave(ave: Ave):
    return ave.mover()

# Función específica para aves voladoras
def volar_ave(ave: AveVoladora):
    return ave.volar()

# Creamos un pingüino y un águila
pinguino = Pinguino()
aguila = Aguila()

# Llamamos a la función mover para ambas aves
print(mover_ave(pinguino))  # Salida: El pingüino está nadando
print(mover_ave(aguila))    # Salida: El ave se está moviendo

# Llamamos a la función volar solo para aves voladoras
print(volar_ave(aguila))    # Salida: El águila está volando alto

#Extra
class Vehiculo:
    def acelerar():
        return f"El Vehiculo esta Acelerando"

    def frenar():
        return f"El vehiculo esta Frenando"

class Moto(Vehiculo):
    def acelerar():
        return f"La Moto esta Acelerando"

    def frenar():
        return f"La Moto esta Frenando"

class Carro(Vehiculo):
    def acelerar():
        return f"El Carro esta Acelerando"

    def frenar():
        return f"El Carro esta Frenando"

class Bus(Vehiculo):
    def acelerar():
        return f"El Bus esta Acelerando"

    def frenar():
        return f"El Bus esta Frenando"

moto = Moto
carro = Carro
bus = Bus

print(moto.acelerar())
print(moto.frenar())

print(carro.acelerar())
print(carro.frenar())

print(bus.acelerar())
print(bus.frenar())