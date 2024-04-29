# #02 FUNCIONES Y ALCANCE
#### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

## Ejercicio

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


#Funciones sin parametros

def my_function():
    print("mi primera función")

my_function()
#Funciones sin parametros con retorno
def my_function():
    return print("función con retorno")

my_function()

#Funciones con parametros
def my_function(numero1,numero2):
    print(numero1+numero2)


my_function(5,5)

def my_strings(text1,text2):
    print(f"{text2}{text1}")

my_strings("hola","adios")

#Función dentro de otra función con lambda y sin lambda
def my_function(numero1, numero2):
    resultado = lambda numeroL1, numeroL2: numero1 + numero2 + numeroL1 * numeroL2
    return resultado
print("ejecutamos función con lambda dentro ",my_function(5,5)(2,2))

def my_function(numero1, numero2):
    def resultado(numeroL1, numeroL2): 
        return numero1 + numero2 + numeroL1 * numeroL2
    return resultado

print("Resultado de una función dentro de otra: ",my_function(5,5)(2,2))

# Uso de la función principal
resultado_adicional = my_function(5, 5)(2, 2)
print("metemos la función en una variable ",resultado_adicional)


#Funciones creadas por el sistema 

miMombre=input()
print("Mi nombre es... ",miMombre)

def imprimirMayusculas(*texts):
    for text in texts:
        print(text.upper())

imprimirMayusculas("hola","adios","hasta luego")


#Dificulta Extra :
numeros=range(1,101)

def dificultaExtra (parametro1,parametro2):
    contador=0
    for numero in numeros:
      
        if numero%3==0 and numero%5==0:
            print(parametro1,parametro2)
        elif numero%3==0:
            print(parametro1)
        elif numero%5==0:
            print(parametro2)
        else:
            print(numero)
            contador+=1


    return contador

print(dificultaExtra("multiplo de 3 ","multiplo de 5"))