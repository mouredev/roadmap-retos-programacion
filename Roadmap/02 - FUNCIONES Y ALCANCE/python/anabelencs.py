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

# FUNCIONES DEFINIDAS POR EL USUARIO


# FUNCIÓN SIMPLE

def funcion_1():
    print("¡Hola, soy la función 1!")

funcion_1()


# FUNCIÓN CON RETORNO

def funcion_2():
    return"¿Qué tal? Soy la función 2." # No necesita los paréntesis con el print

respuesta = funcion_2()
print(respuesta)

# Devuelve un "None" si no se usa la función bien.

print() # Se puede imprimir una línea en blanco sin poner las comillas de str.

def funcion_3():
    print("¡Hola, soy la función 3!")

funcion_3() # Esto sí imprime porque la función contiene la indicación de imprimir

def funcion_4():
    return"¡Hola, soy la función 4!"

funcion_4() # Esto no imprime porque la función es return, no imprimir... hay que mandarle a imprimir después.

print(funcion_4())

print()


# FUNCIÓN CON UN ARGUMENTO

def funcion_5(nombre):
    print("Hola desde la función 5,",nombre)

funcion_5("Belén")

print()


# FUNCIÓN CON MÁS DE UN ARGUMENTO

def funcion_6(saludo, nombre):
    print("¡",saludo,nombre,"!")

funcion_6("Hola desde la función 6,","Belén")
funcion_6(nombre = "Belén", saludo = "Hola desde la función 6 reordenada,")

print()


# FUNCIÓN CON UN ARGUMENTO PREDETERMINADO

def funcion_7 (nombre = "Sin nombre asignado"):
    print(f"¡Hola desde la función 7, {nombre}!")

funcion_7() # Usa el valor dado a la variable por defecto
funcion_7("Belén") # Usa el valorque se le da en este momento

# Entonces, defino la función y si tiene print, luego simplemente la acciono.
# Si es return, sí debo luego indicar la impresión.

print()


# FUNCIÓN CON ARGUMENTOS Y RETORNO

def funcion_8(saludo, nombre):
    return f"¡{saludo}, {nombre}!"

print(funcion_8("Hola desde la función 8", "Belén"))

print()


# FUNCIÓN CON RETORNO DE VARIOS VALORES

def funcion_9():
    return "Hola desde la funcion_9", "Belén"

saludo, nombre = funcion_9()
print(saludo)
print(nombre)

print()


# FUNCIÓN CON UN NÚMERO VARIABLE DE ARGUMENTOS
# No tan habitual en otros lenguajes

def funcion_10(*nombres): # El asterisco quiere decir que le podemos dar más de un nombre, separados por comas.
    for nombre in nombres:
        print(f"Hola desde la función 10, {nombre}!")

funcion_10("Python", "Belén", "Antonio", "colegas")

print()


# FUNCIÓN CON UN NÚMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE
# No tan habitual en otros lenguajes

def funcion_11(**valores): # En este caso lleva dos asteriscos, para que cada argumento lleve una palabra clave.
    for clave, valor in valores.items():
        print(f"Hola desde la función 11, {valor} ({clave})!")

funcion_11(lenguaje="Python", nombre="Belén", alias="anabelencs", comunidad="ComunidadDeMoureDev", año=2026)

'''
También se puede poner así:
funcion_11(
    lenguaje="Python", 
    nombre="Belén", 
    alias="anabelencs", 
    comunidad="ComunidadDeMoureDev", 
    año=2026
)
'''

print()


# FUNCIONES DENTRO DE FUNCIONES

def funcion_12():
    def funcion_13():
        print("Hola desde la función 13, Python!")
    funcion_13()
funcion_12()

# Python sí puede crear funciones dentro de funciones.

print()


# FUNCIONES DEL LENGUAJE (BUILT-IN FUNCTIONS)

print("Conteo de elementos:",len("anabelencs"))
print("Tipo de variable:",type("anabelencs")) 
print("Tipo de variable:",type(95))
print(f"Tipo de variable: {type(95)}") # Lo mismo pero repasando la escritura
print("Mayúsculas cerradas:", "anabelencs".upper())

# Recordar revisar más funciones que se pueden usar en el lenguaje que estamos estudiando.

print()


# VARIABLES LOCALES Y GLOBALES

# ámbito... scope

global_var = "Python"

def funcion_14():
    print(f"Hola desde la función 14, {global_var}")
funcion_14()

print()

def funcion_15():
    local_var = "Variable que sólo funciona dentro de la función 15 "
    print(f"Hola, {local_var}")
    print("Prueba de impresión de una variable local:", local_var)
funcion_15()

print("Prueba de impresión de una variable global:", global_var)
# print("Prueba de impresión de una variable local:", local_var) # Si dejo esto en el código, es un fallo porque esa variable sólo funciona dentro de la función donde se le creó.

# Buena práctica en la programación: tratar de restringir siempre que se pueda el ámbito de nuestro código.

print()


# PROBLEMA EXTRA

'''
NOOOOOOO
def funcion_extra(**valores):
    for n, t1, t2 in valores.items():
        for n in range (1,101):
            if n % 3 == 0:
                print(t1)
            elif n % 5 == 0:
                print(t2)
            elif n % 3 == 0 and n % 5 == 0:
                print(t1, t2)
            else:
                print(n.count)
                #print(len{n})
    return...
'''

def funcion_extra(t1, t2):
    contador = 0
    for n in range (1,101):
        if n % 3 == 0 and n % 5 == 0:
            print(t1, t2)  
        elif n % 3 == 0:
            print(t1)
        elif n % 5 == 0:
            print(t2)
        else:
            print(n)
            contador += 1
    return contador

print(f"Contador: {funcion_extra("Texto 1", "Texto 2")}")

# funcion_extra("Fizz", "Buzz") # ejercicio típico en programación

print()