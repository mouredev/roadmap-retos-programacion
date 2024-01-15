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

# Función sin parámetros y sin retorno
def saludo_01():
    print("¡¡Hola, buenos días!!")
    
saludo_01()

# Función con  parámetros y sin retorno
def saludo_02(nombre, apellido):
    print(f"Hola, {nombre} {apellido}.\n¿Cómo estás?")

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")

saludo_02(nombre,apellido)

# Función con parámetros y retorno
numero_01 = float(input("Escriba el primer número: "))
numero_02 = float(input("Escriba el segundo número: "))

def sumar(numero_01,numero_02):
    resultado = numero_01 + numero_02
    return resultado 

resultado_suma = sumar(numero_01,numero_02)
print(f"El resultado de sumar {numero_01} + {numero_02} = {resultado_suma}")

# Función dentro de otro función

def suma_resta(numero_01,numero_02):
    
    resta = numero_01 - numero_02
    suma =sumar(numero_01, numero_02)
    
    return  resta, suma

resultado_resta, resultado_suma = suma_resta(numero_01,numero_02)

print(f"El resultdao de la resta es {resultado_resta} y el de la suma es {resultado_suma}")

# Funciones integradas de Python

x = int("123") #conversión de string a entero
print(x)
y = float("3.14") #conversión de string a float
print(y)
z = str(42) #conversión de entero a string
print(z)
is_true = bool(1) #conversión de entero a booleano
print(is_true)

# Variables locales y globales

saludo = "Hola" #variable global

def saludar():
    nombre = input("¿Cómo te llamas: ") #variable local
    print(saludo, nombre)
    
saludar()


#EXTRA

multiplo_3 = "Es múltiplo de 3"
multiplo_5 = "Es múltiplo de 5"

def multiplos(parametro_1, parametro_2):
    contador = 0
    for i in range(1,101,1):
        if i % 3 == 0 and i % 5 == 0:
            print(parametro_1 + parametro_2)
        elif i % 3 == 0:
            print(parametro_1)
        elif i % 5 == 0:
            print(parametro_2)
        else:
            print(i)
            contador += 1
            
    print(f"Se han impreso {contador} números")
            
multiplos(multiplo_3, multiplo_5)
        
    