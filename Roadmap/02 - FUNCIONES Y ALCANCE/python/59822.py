'''EJERCICIO:
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
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.'''
 
#Función simple
#Función sin parametros

def hablar():
    print("Hola, soy una función")

print(hablar()) #Aqui imprime none porque no tiene una funcion return
hablar() #Aqui imprime el print de la función

#Función sin parametros ni retorno
def hablar2():
    pass

#Función con varios parametros
def hablar3(nombre, apellido):
    print("Hola, soy", nombre, apellido)

hablar3("Laura", "Gonzalez")

#Funcion con un parametro y retorno
def hablar(nombre):
    return "Hola, soy " + nombre
print(hablar("Laura")) #Aqui imprime el return de la función

#Funciones con parametros por defecto

def estudio(universidad = "Universidad Nacional"):
    print("Estudio en la", universidad)
estudio()

#Funcion con retorno sin parametros

def casa():
    casa = "verde"
    return f"Mi casa es {casa}"
print(casa())

#Funcion lambda es una función anónima que se puede usar para hacer una función en una sola linea
#Funcion lambda con un parametro
suma = lambda x: x + 10
print(suma(5))

#Funcion lambda con varios parametros
nombre_completo = lambda nombre, apellido: f"{nombre} {apellido}"
print(nombre_completo("Laura", "Gonzalez"))

#Funcion lambda con varios parametros y operaciones
resta = lambda x,y,z,w: x - y + z / w
print(resta(10,2,3,2))

#Funcion recursiva es una función que se llama a si misma
def factorial(numero = 4):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial())

#Funcion con argumentos es una función que recibe un número indeterminado de argumentos
def suma_con_args(*args):
    return sum(args)

print(suma_con_args(1,2,3,4,5))