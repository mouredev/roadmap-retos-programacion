"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""

# Funciones

print("\n *******Funciones******* \n")

# Función sin parámetros ni retorno

print("\n *******Función sin parámetros ni retorno******* \n")

def saludar():
    print("Hola Mundo!")

saludar()

# Función con parámetros

print("\n *******Función con parámetros******* \n")

def saludar(nombre):
    print(f"Hola {nombre}!")

saludar("Eduardo")

# Función con retorno

print("\n *******Función con retorno******* \n")

def sumar(a, b):
    return a + b

resultado = sumar(5, 5)
print(f"Resultado de la suma: {resultado}")

# Función dentro de función

print("\n *******Función dentro de función******* \n")

def saludar(nombre):
    def mensaje():
        return "Hola"
    return f"{mensaje()} {nombre}!"

print(saludar("Eduardo"))

# Funciones ya creadas

print("\n *******Funciones ya creadas******* \n")

print("Función print(): Devuelve un mensaje por consola")
print("Función input(): Devuelve un mensaje por consola y recoge la entrada del usuario")
print("Función len(): Devuelve la longitud de un objeto")
print("Función range(): Devuelve una secuencia de números")
print("Función type(): Devuelve el tipo de un objeto")
print("Función int(): Devuelve un número entero")
print("Función str(): Devuelve una cadena de texto")
print("Función float(): Devuelve un número decimal")
print("Función list(): Devuelve una lista")
print("Función dict(): Devuelve un diccionario")
print("Función tuple(): Devuelve una tupla")
print("Función set(): Devuelve un conjunto")
print("Función bool(): Devuelve un valor booleano")

# Variable LOCAL y GLOBAL

print("\n *******Variable LOCAL y GLOBAL******* \n")

variable_global = "Soy una variable global"

def mostrar_variable():
    variable_local = "Soy una variable local"
    print(variable_local)

mostrar_variable()

# Dificultad extra

print("\n *******Dificultad extra******* \n")

def hola_mundo(param1, param2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("HolaMundo")
        elif i % 3 == 0:
            print("Hola")
        elif i % 5 == 0:
            print("Mundo")
        else:
            print(i)
        contador += 1
    return contador

print(hola_mundo("Hola", "Mundo"))



