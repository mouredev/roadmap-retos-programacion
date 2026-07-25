## Ejercicio

""""
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
# Función sin parámetros ni retorno
def saludar():
    print("¡Hola, bienvenido!")
saludar()
# Función con parámetros y sin retorno
def sumar(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")
sumar(2, 8)
# Función con parámetros y con retorno
num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))
def multiplicar(num1, num2):
    return num1 * num2
resultado=multiplicar(num1, num2)
print("El resultado de la multiplicación es: " + str(resultado))

def saludo(mensaje, nombre):
    print(f"{mensaje}, {nombre}")
saludo(nombre="Victor", mensaje="Hola")

def saludo_con_retorno():
    return "Hola", "Victor"
mensaje, nombre = saludo_con_retorno()
print(mensaje)
print(nombre)
# Función dentro de otra función
def funcion_externa():
    def funcion_interna():
        print("Esta es una función interna.")
    funcion_interna()
funcion_externa()
# Funciones incorporadas
mensaje=input("Escribe un mensaje: ")
print("La longitud del mensaje escrito es de: " + str(len(mensaje)) + " caracteres.")
def saludos(*nombres):
    for nombre in nombres:
        print("Hola, " + nombre)
saludos("Ana", "Luis", "Carlos", "Marta", "Sofía")
 # Utiliza la función incorporada len()
valor=float(input("Introduce un número decimal: "))
print("El tipo de dato ingresado es un: " + str(type(valor)))
# Variable global y local
variable_global="Soy una variable global"
def mostrar_variables():
    variable_local="Soy una variable local"
    print(variable_global)
    print(variable_local)
mostrar_variables()
def variable_local():
    tipo_variable="local"
    print("Esto es una variable: " + tipo_variable)
variable_local()
# Dificultad extra
def cadena_texto(cadena1, cadena2):
    contador=0
    for numeros in range(1, 101):
        if numeros % 3 == 0 and numeros % 5 == 0:
            print(cadena1 + cadena2)
        elif numeros % 3 == 0:
            print(cadena1)
        elif numeros % 5 == 0:
            print(cadena2)
        else:
            print(numeros)
            contador+=1
    return contador
resultado=cadena_texto("Fizz", "Buzz")
print("El número de veces que se imprimió un número en lugar de los textos es: " + str(resultado))






