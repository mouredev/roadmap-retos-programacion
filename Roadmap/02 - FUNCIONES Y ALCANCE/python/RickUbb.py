# Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
# Sin parámetros ni retorno
import math

def hola():
    hola = "Hola, Rick Ubb!"

print(hola)

# Con uno o varios parámetros
def hola(saludo1, saludo2):
    saludo = f"{saludo1}, {saludo2}!"
    print(saludo)

print(hola("hi", "Rick Ubb"))

# Con retorno
def holas():
    return "Hola, Rick Ubb!"

print(holas)

# Comprueba si puedes crear funciones dentro de funciones.
def hoya():
    def mundo():
        return "Mundo"
    saludo = mundo()
    return saludo

# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
print(hoya())
saludo = len(hoya())
print(saludo)
print(math.sqrt(9))

# Pon a prueba el concepto de variable LOCAL y GLOBAL.
variable_global = "Soy una variable global"

def saludar():
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)

print(saludar())
print(variable_global)
#print(variable_local) da error por que la variable solo existe detro de la funcion

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""


def funcion_extra(cadena1, cadena2):
    numero = 0
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print(f"{cadena1}, {cadena2} {i}")
        elif (i % 5 == 0):
            print(f"{cadena2}, {i}")
        elif (i % 3 == 0):
            print(f"{cadena1}, {i}")
        else:
            numero += 1
            print(f"{i}, {numero}")

    return numero
print(funcion_extra("Rick", "Sanchez"))