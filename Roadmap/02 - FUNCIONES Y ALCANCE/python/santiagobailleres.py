#02 FUNCIONES Y ALCANCE

'''
/*
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
'''

# 1- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
#    Sin parámetros ni retorno, con uno o varios parámetros, con retorno.

# Función sin parámetros ni retorno
def funcion1():
    print("Función sin parámetros ni retorno")

funcion1()

# Función sin parámetros y con retorno
def funcion2():
    return "Función sin parámetros y con retorno"

print(funcion2())

# Función con un parámetro predeterminado y sin retorno
def funcion3(parametro = "Hola"):
    print("Función con un parámetro predeterminado y sin retorno:", parametro)

funcion3()

# Función con un parámetro y sin retorno
def funcion4(parametro):
    print("Función con un parámetro y sin retorno:", parametro)
    
funcion4("Hola")

# Funcion con varios parámetros y con retorno
def funcion5(parametro1, parametro2):
    return parametro1 + parametro2

a = funcion5(2, 3)
print(a)

# Función con retorno de varios valores
def funcion6(parametro1, parametro2):
    return parametro1, parametro2

a, b = funcion6(2, 3)
print(a)
print(b)

# Función con numero variable de argumentos
def funcion7(*args):
    for arg in args:
        print(arg)

funcion7(1, 2, 3, 4, 5)

# Función con numero variable de argumentos y argumentos con nombre
def funcion11(**kwargs): # kwargs = keyword arguments
    for key, value in kwargs.items():
        print(key, value)

funcion11(a = 1, b = 2, c = 3)

# 2- Comprueba si puedes crear funciones dentro de funciones.
def funcion8():
    def funcion9():
        print("Función dentro de función")
    funcion9()

funcion8()

# 3- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
def funcion10():
    print("Función que utiliza una función ya creada en el lenguaje")
    print("Ejemplo de función que ya existe en Python: len([1, 2, 3]) =", len([1, 2, 3]))

funcion10()

# 4- Pon a prueba el concepto de variable LOCAL y GLOBAL.
variable_global = 5

def funcion12():
    variable_local = 3
    print("Variable local:", variable_local)
    print("Variable global:", variable_global)

print("Variable global:", variable_global)
# print("Variable local:", variable_local) # Error: variable_local no está definida

funcion12()

# EXTRA - Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#         La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#         - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#         - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#         - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#         - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def funcionExtra(text1, text2):
    cont = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            cont += 1
    return cont

print("Número de veces que se ha impreso el número:", funcionExtra("multi3", "multi5"))