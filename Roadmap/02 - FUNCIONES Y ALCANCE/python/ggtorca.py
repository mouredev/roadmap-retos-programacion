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
print("Ejercicio #02 - Funciones y Alcance")
print("-----------------------------------")
print("")

#Funcion sin parámetros ni retorno

def holaMundo():
    print("Hola mundo!")

print("Funcion sin parámetros ni retorno")
print("")
holaMundo() #Llamada a la función, se imprime "Hola mundo!"
print("")

#Funcion con un parametro

def holaPersona(nombre):
    print("Hola " +nombre +"!")

print("Funcion con un parametro")
print("")
holaPersona("Pedro") #Llamada a la función, se imprime "Hola Pedro!"
print("")

#Funcion con varios parametros y retorno

def multiplicacion (val1, val2):
    return val1 * val2

print("Funcion con varios parametros")
print("")

val1 = int(input("Introduce el primer valor: "))

val2 = int(input("Introduce el segundo valor: "))


print(f"\nEl resultado de la multiplicación es: {multiplicacion (val1, val2)}") #Llamada a la función, se imprime el resultado de multiplicacion.

#¿Se pueden crear funciones dentro de funciones?

def funcionPrincipal(x, y):
    def funcionInterna(y):
        return y + y
    return funcionInterna(x) * y

x = int(input("Establece el valor de x: "))
y = int(input("Establece el valor de y: "))

resultadoOperacion = funcionPrincipal(x, y)

print(f"\n El resutlado final es: {resultadoOperacion}") #Llamada a la función, se imprime el resultado de x*(y+y)

#Funciones propias del lenguaje

#len()
palabra = "aerodromo"
longitud =len(palabra)

print(longitud) #Imprime la longitud de la palabra "aerodromo"

#type()
print(type(24)) #Imprime que es un int
print(type("reactor")) #Imprime que es un string

#range()
for i in range(4):
    print (i) # Imprime una lista del 0 al 3

#sum()
numeros = [10, 20, 30]
total = sum(numeros)
print(total) #Imprime el total de la suma de los numeros establecidos previamente

#Variables LOCALES y GLOBALES

#Variable LOCAL

def sumar (a, b):
    total = a + b #total es una variable local ya que unicamente es accesible dentro de la funcion sumar
    return total
print(sumar(1, 2))

#Variable GLOBAL
contador = 0 # La variable contador se declara fuera de una funcion
def incrementar():
    global contador # Se establece que se va a usar la variable global "contador"
    contador += 1

def imprimirContador():
    print(contador)

print(f"el contador esta a {contador}")
vecesIncrementar = int(input("Cuantas veces quieres incrementar el contador? "))
for i in range(vecesIncrementar):
    incrementar()
print(f"\n El contador ahora está a ", end="")

imprimirContador()

#Dificultad extra

def dificultadExtra(cadena1, cadena2):
    contarNumeros = 0

    for numero in range(1, 101):
        if numero % 3 == 0 & numero % 5 == 0:
            print(cadena1 + cadena2)
        elif numero % 3 == 0:
            print(cadena1)
        elif numero % 5 == 0:
            print(cadena2)
        else:
            print(numero)
            contarNumeros += 1

    return contarNumeros
cadena1 = "hey"
cadena2 = "ho"
resultado = dificultadExtra(cadena1, cadena2)

print(f"Se imprimio un numero {resultado} veces")