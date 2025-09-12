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

# Funciones básicas
def funcion_basica():
    print("Función básica sin parámetros ni retorno.")

def funcio_con_parametro(nombre, apellido):
    print(f"Función con parámetros: param1 = {nombre}, param2 = {apellido}.")

def funcion_con_retorno():
    return "Devuelve un valor."

def funcion_con_parametros_retorno(number1, number2):
    return number1 * number2

def funcion_parametros_opcional(nombre, apellido, apodo = "'Sin apodoo'"):
    print(f"Función con parámetros opcionales: param1 = {nombre}, param2 = {apellido}, param3 = {apodo}.")


# Funciones dentro de funciones
def funcion_padre():
    def funcion_Hijo():
        print("Función hija.")
    print("Función padre.")
    funcion_Hijo()

# Variable LOCAL y GLOBAL
var_global = "Soy una variable global."

def funcio_global_local():
    var_local = "Soy una variable local."
    print(var_global)
    print(var_local)
#print(var_local); # Da error porque la variable no está definida en este áambito.

funcion_basica()
funcio_con_parametro("Alejandro", "Abascal")
print(funcion_con_retorno())
print(funcion_con_parametros_retorno(23, 10))
funcion_parametros_opcional("Alejandro", "Abascal")
funcion_padre()
funcio_global_local()


# DIFICULTAD EXTRA

def dificultad_extra(texto1, texto2):
    contador = 0
    for i in range(1, 100):
        if(i % 3 == 0 and i % 5 == 0):
            print(f"{texto1} {texto2}")
        elif (i%3 == 0):
            print(texto1)
        elif (i%5 == 0):
            print(texto2)
        else:
            print(i)
            contador += 1
    return f"\nSe ha impreso el número {contador} veces."

print(dificultad_extra("Alejandro", "Abascal"))