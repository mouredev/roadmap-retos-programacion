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
 */

'''

#definimos una variable global
esto_es_una_variable_global="Variable_local"

#funcion sin parametros
def funcion_sin_parametros():
    print("Esto es una funcion sin parámetros")

#Funcion que recibe un parámetro
def funcion_con_parametros(nombre):
    print(f"Esto es un saludo para => {nombre}")

#funcion con un parámetro y el tipo de dato definido
def funcion_con_tipo_de_datos_definido(ciudad : str):
    print(f"Quiero viajar a {ciudad}")

#funcion con parametros definidos y tipos de datos
def funcion_con_parametros_definidos_suma(a:int = 2, b: int = 0):
    print(f"El resultaod es {a+b}")

#funcion con retorno y parámetro definido
def funcion_con_retorno(comida:str):
    return f"Quisier probar {comida} algún día"

def funcion_mostrando_variable_global():
    print(f"{esto_es_una_variable_global}")

#funcion que mustra las tablas de multiplcar segun una variable local (que solo existe dentro de la funcion)
def funcion_con_variable_local():
    tabla_de_multiplicar=input("Escribe una tabla de multiplicar => ")

    for i in range (0,12):
        print(f"{tabla_de_multiplicar} * {i} = {tabla_de_multiplicar*i}")


# Llamada a las funciones
funcion_sin_parametros()
funcion_con_parametros("Juan")
funcion_con_tipo_de_datos_definido("Managua")
funcion_con_parametros_definidos_suma(3, 5)

resultado_retorno = funcion_con_retorno("Gallo pinto")
print(resultado_retorno)

funcion_mostrando_variable_global()
funcion_con_variable_local()
#Extra

"""
DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def extra(texto_1:str, text_2:str):
    contador=0
    #mostramos los numeros del 1 al 100
    for i in range (0,100):
        if i % 3 :
            print(texto_1)
        elif i % 5:
            print(text_2)
        elif i%3 and i%5:
            print(f"{texto_1} {text_2}")
        else:
            #si las condiciones anteriores no se cumplen se mostrarpa en pantalla el numero
            print(i)
            contador+=1

    return contador



print(extra("primer texto", "segundo texto"))