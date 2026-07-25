# 02 FUNCIONES Y ALCANCE

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
"""

# Funcion sin parámetros ni retorno
def sin_parametros():
    print("Hola, bienvenido a Python!")

# Funcion con un parámetro
def con_parametro(nombre):
    print(f"Hola, {nombre}!")

# Funcion con varios parámetros
def con_varios_parametros(nombre, edad):
    print(f"Hola, {nombre}, tienes {edad} años.")

# Funcion con retorno
def suma(a, b):
    return a + b

# Funcion dentro de otra función
def operacion_compuesta(x, y):
    def elevar_al_cuadrado(n):
        return n * n
    suma = x + y
    print(f"El cuadrado de la suma entre", x, "y", y, f"es {elevar_al_cuadrado(suma)}")

# Función que utiliza variables globales y locales | con funciones del lenguaje
contador_global = 0
def funcion_con_variable_global():
    global contador_global
    contador_local = 0
    for i in range(0, 5):
        contador_local += 1
        contador_global = contador_local * 2  # Modifica la variable global
    print(f"Contador local: {contador_local}, Contador global: {contador_global}")

sin_parametros()  # Llamada a la función sin parámetros
con_parametro("Alejandro")  # Llamada a la función con un parámetro
con_varios_parametros("Alejandro", 30)  # Llamada a la función con varios parámetros
resultado = suma(10, 5)  # Llamada a la función con retorno
print(f"La suma de 10 y 5 es: {resultado}")  # Imprime el resultado de la suma
operacion_compuesta(3, 4)  # Llamada a la función con operación compuesta
funcion_con_variable_global()  # Llamada a la función que utiliza variables globales
print(f"la variable global es: {contador_global}")  # Esto funcionará porque contador_global es global 

# DIFICULTAD EXTRA
def imprimir_numeros(param1, param2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1 + param2)
            contador += 1
        elif i % 3 == 0:
            print(param1)
            contador += 1
        elif i % 5 == 0:
            print(param2)
            contador += 1
        else:
            print(i)
    return contador

# Llamada a la función de dificultad extra
resultado_extra = imprimir_numeros("Fizz", "Buzz")
print(f"Números impresos en lugar de textos: {resultado_extra}")

