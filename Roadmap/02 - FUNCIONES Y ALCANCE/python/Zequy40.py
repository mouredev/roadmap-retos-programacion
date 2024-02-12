'''
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 '''
# Función sin parámetros ni retorno
def funcion_sin_parametros_ni_retorno():
    print("Esta es una función sin parámetros ni retorno.")

# Función con uno o varios parámetros
def funcion_con_parametros(parametro1, parametro2):
    suma = parametro1 + parametro2
    print(f"La suma de {parametro1} y {parametro2} es: {suma}")

# Función con retorno
def funcion_con_retorno(a, b):
    multiplicacion = a * b
    return multiplicacion

# Función que contiene otra función
def funcion_con_funcion():
    def funcion_interna():
        print("Esta es una función interna dentro de otra función.")
    funcion_interna()

# Uso de funciones ya creadas en el lenguaje
def funcion_con_funcion_builtin():
    lista = [1, 2, 3, 4, 5]
    longitud = len(lista)
    print(f"La longitud de la lista es: {longitud}")

# Funciones integradas de Python

# Funciones para manejar listas
lista = [1, 2, 3, 4, 5]
print("Suma de la lista:", sum(lista))
print("Longitud de la lista:", len(lista))
print("Valor mínimo de la lista:", min(lista))
print("Valor máximo de la lista:", max(lista))

# Funciones para manejar cadenas de texto
cadena = "Hola, mundo!"
print("Longitud de la cadena:", len(cadena))
print("Cadena en mayúsculas:", cadena.upper())
print("Cadena en minúsculas:", cadena.lower())
print("Cadena en separados por los espacios:", cadena.split())
print("Cadena con las primeras letra en mayuscula:", cadena.capitalize())
print("Cadena con la primera letra en mayuscula:", cadena.title())
      
# Funciones matemáticas
numero = 3.14
print("Valor absoluto:", abs(numero))
print("Redondeo hacia arriba:", round(numero))
print("Redondeo hacia abajo:", round(numero, 1))

# Funciones de conversión de tipos
cadena_numero = "123"
numero_convertido = int(cadena_numero)
print("Número convertido a entero:", numero_convertido)

# Funciones de entrada/salida
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)

# Funciones para manejar archivos
archivo = open("ejemplo.txt", "w")
archivo.write("Hola, este es un ejemplo de archivo.")
archivo.close()

# Variables globales y locales
variable_global = 10  # Variable global

def funcion_con_variable_local():
    variable_local = 5  # Variable local
    suma = variable_global + variable_local
    print(f"Suma de variable global y local: {suma}")

# Ejecución de las funciones
funcion_sin_parametros_ni_retorno()

parametro1 = 3
parametro2 = 7
funcion_con_parametros(parametro1, parametro2)

resultado = funcion_con_retorno(parametro1, parametro2)
print(f"El resultado de la función con retorno es: {resultado}")

funcion_con_funcion()

funcion_con_funcion_builtin()

funcion_con_variable_local()
print(f"Variable global fuera de la función: {variable_global}")

# Generar un error al intentar imprimir la variable local fuera de su ámbito
# print(f"Variable local fuera de la función: {variable_local}")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''

def numeros_condicionales(cadena1, cadena2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(cadena1 + cadena2)
        elif numero % 3 == 0:
            print(cadena1)
        elif numero % 5 == 0:
            print(cadena2)
        else:
            print(numero)
            contador += 1

    return contador

# Ejemplo de uso
resultado = numeros_condicionales("C#", "Python")
print(f"Python fue {resultado} veces + popular que C#.")
# 😁😁

