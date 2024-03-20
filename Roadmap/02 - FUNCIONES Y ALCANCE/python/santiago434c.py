"""
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

"""
# Funcion Sin parametros ni retorno retorno
def funcion_simple():
    a = 5
    a += a
    print(a)

# Funcion con un parametro
def funcion_parametro(num):
    num += 1
    print(num)

# Funcion con varios parametros
def funcion_varios_parametros(palabra, num):
    str(palabra)
    int(num)
    print("Esta es tu palabra: ",palabra, "y este es tu numero: ",num)

#Funcion con arguemntos predeterminados
def predetermindos(name="Python"):
     print(f"Hola, {name}")

# Funcion con retorno
def funcion_retorno(num1, num2):
    num1 *=2
    num2 %=5
    result = num2 + num1
    return result

#Funcion con retorno de varios argumentos
def retorno_multiple():
    return "Hola", "python"

#Asignacion del return para imprimir
greet, name = retorno_multiple()

#Funcion con numero variable de argumentos
def funcion_arg_multiples(*names):
    for name in names:
        print(f"Hola, {name}")

#Funcion con un numero variable de arguemtos con palabra clave - Similar al diccionario
def funcion_multi_palabra_clave(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

#Funciones dentro de funciones?
def externa():
    def interna():
        print("Funcion interna: Sapo perro")
    interna()

#Funciones del leguaje (built-in)
#Logitud
print(len("Hola"))
print(type(36))   
print("Hola".upper())

#Variable Local y Global
"""
-Una funcion puede acceder varibles globales.
-Pero no se pueden acceder a variables locales desde fuera de la funcion.
-Si existe una variable local y global en la funcion se tomará la local
 y afuera la global.

"""
a = 5
text = "perro"
def funcion_local_global():
    a = 8
    print(f"Este es el numero local: , {a}, y el texto global es: {text}")

#EXTRA
def funcion_reto(texto1, texto2):
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 | number % 5 == 0:
            concat = texto1+texto2
            print(f"{number}, - {concat}")
        elif number % 3 == 0:
            print(f"{number}, - {texto1}")
        elif number % 5 == 0:
            print(f"{number}, - {texto2}")
        else:
             count += 1
             print(f"{number}")
    return count
    
funcion_simple()
funcion_parametro(2)
funcion_varios_parametros("Nuevo", 2024)
res = funcion_retorno(12, 25)
print("Este es el resultado del return: ", res)
print(greet)
print(name)
externa()
funcion_arg_multiples("Gato", "Toby", "Ahmed")
funcion_multi_palabra_clave(laguage="Python",
                            name="Santiago",
                            age="16")
print("Este es el numero global:", a)
funcion_local_global()
    
res = funcion_reto("fizz", "buzz")
print(res)

