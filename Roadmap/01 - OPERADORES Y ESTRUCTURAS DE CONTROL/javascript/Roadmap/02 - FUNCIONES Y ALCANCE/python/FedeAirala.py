# Reto #02 FUNCIONES Y ALCANCE

""" * EJERCICIO:
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
 
# Una función en Python es un bloque de líneas de código o un conjunto de instrucciones 
# que se utilizan para realizar una tarea específica. Puede reutilizarse cuando se lo requiera. 
# Las funciones nos ayudan a que el código sea más fácil de leer y entender.

# Creando funciones: para ello se utiliza la palabra reservada def seguido del nombre que desee utilizar.

# Función sin parámetros ni retorno.

def funcion():
    print ("Esto es una función")   # Esta función realiza un print por terminal.
funcion()                           # Llamada de la función para su ejecución.

# Función con un parámtero

def parametro (texto1):
    print (texto1)
parametro("Función con parámetro")

# Función con varios parámetros

def suma (a,b):
    print (f"La suma es:{a+b}") 
suma(10,5)

def concatenar(texto1,texto2):
    print (texto1 + texto2)
concatenar ("Hola", " Python")

# Función con retorno

def retorno(a,b):
    suma = a+b
    return suma 
print (retorno (5,6))

# Funciones dentro de funciones

def funcion1():
    def funcion2():
        print ("Función 2 dentro de otra función 1")
    funcion2()
funcion1()    

# Funciones creadas por el lenguaje

print (f"La función len devuelve el tamaño de una cadena. Tamaño de Hola Python!: {len('Hola Python!')}")

# Variable Local

var_local = "Variable local fuera de la función"
def var():
    var_local = "Variable Local dentro de la función"
    print (var_local)
print (var_local)
var()

# Variable Global

var_global = "Variable global fuera de la función"
def var_g():
    global var_global
    var_global = "Variable global dentro de la función cambia la exterior"
    print (var_global)
print (var_global)
var_g()
        
# Dificultad extra

def dificultad_extra (texto1,texto2):
    num_veces=0
    
    for i in range (1,101):

        if i%3 == 0 and i%5== 0:
            print  (f"Textos concatenados en posición {i}: {texto1+texto2}")
        elif i%3 == 0 :
            print (f"Posición {i}: {texto1}")
        elif i%5 == 0:
            print (f"Posición {i}: {texto2}")
        else:
            print (f"A este número no le corresponde texto: {i}")
            num_veces += 1
    return print (f" El número de veces que no se ecribió un texto fue: {num_veces}")

dificultad_extra("Hola"," Python")