# Una función te permite definir un bloque de código reutilizable que se puede ejecutar muchas veces dentro de tu programa.

# función simple
def funcion_simple():
    print('Soy una función simple')

funcion_simple()

# función con parámetro
def funcion_parametro(lenguaje):
    print(f'Estoy programando con {lenguaje}')

funcion_parametro('Python')

# función con varios parámetros
def funcion_parametro(nombre, lenguaje):
    print(f'Hola, me llamo {nombre} y estoy programando con {lenguaje}')

funcion_parametro('Alex','Python')

# función con parámetros por defecto
def funcion_parametros_defecto(coche = 'Ferrari', color = 'rojo'):
    print(f'El {coche} es {color}')

funcion_parametros_defecto() # devuelve el print con los valores por defecto si no se le indica lo contrario
funcion_parametros_defecto('Lambo') # devuelve el print: El lambo es rojo (hemos cambiado el primer valor, el segundo sigue por defecto)

# función con retorno sin parámetros
def funcion_retorno():
    mensaje = 'Bienvenidos'
    return mensaje

print(funcion_retorno())

# función con retorno con parámetros
def funcion_retorno_parametros(a, b):
    resultado = a + b
    return resultado

print(funcion_retorno_parametros(20,7))

# función anónima o Lambda
suma = lambda x, y: x + y
print(suma(2,3))

# función recursiva
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial(7))

# función con argumentos
def suma_con_args(*args):
    return sum(args)

resultado = suma_con_args(1, 2, 3, 4)
print(resultado)  # devuelve: 10


# Funciones dentro de funciones
def funcion_externa(a):
    def funcion_interna_multiplicacion(b):
        return b * 5
    
    resultado = funcion_interna_multiplicacion(a)

    return resultado

print(funcion_externa(5))


# Funciones ya creadas en el lenguaje

# max() --> Devuelve el elemento más grande en un iterable o el más grande de dos o más argumentos
lista = [2,5,27,3,45]
print(max(lista))

# len() --> Este método devuelve la longitud (el número de elementos) de un objeto. Toma un argumento x
palabra = 'Esternocleidomastoideo'
print(len(palabra))


# Variables locales: Son aquellas que se definen dentro de una función y solo son accesibles dentro de esa función
def funcion_local():
    variable_local = 10
    print(variable_local)

funcion_local()
# print(variable_local) --> da un error porque desde fuera la variable no es accesible

# Variables globales: Son aquellas que se definen fuera de cualquier función o bloque de código y son accesibles en todo el programa
# Pueden ser utilizadas tanto dentro como fuera de las funciones
# Se declaran con la palabra clave global dentro de una función si se desea modificar su valor
variable_global = 50

def funcion_global():
    print(variable_global)

funcion_global()
print(variable_global) # no da error porque es accesible desde cualquier parte del código

def modificar_global():
    global variable_global
    variable_global = 20

modificar_global()
print(variable_global)

""" * EJERCICIO:
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion_extra(texto1, texto2):
    veces_impreso = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(texto1 + '' + texto2)
        elif num % 3 == 0:
            print(texto1)
        elif num % 5 == 0:
            print(texto2)
        else:
            print(num)
            veces_impreso += 1

    return f'El numero de veces quue se a impreso el numero son: {veces_impreso}'

print(funcion_extra('Hola','Adios'))