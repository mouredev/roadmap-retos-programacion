'''
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
'''

'''
Basic
'''

# Ejemplo Incorrecto
class Bird:
    def fly(self):
        return "Flying"

class Chicken(Bird):
    def fly(self):
        raise Exception("Los pollos no vuelan")
    
# bird = Bird()
# print(bird.fly())
# chicken = Chicken()
# print(chicken.fly())

# Correcto
class Bird:
    def move(self) -> str:
        return "Moving"
    
class Chicken(Bird):
    def move(self) -> str:
        return "Walking"
    
bird = Bird()
print(bird.move())
chicken = Chicken()
print(chicken.move())

'''
Extra
'''

