#Funciones 

#Funciones sin parametros
def sin_parametros():
    print("Funcion sin parametros")

sin_parametros()

#Funciones con parametros 
def con_parametros(mensaje):
    print("Imprimiendo funcion con", (mensaje))

con_parametros("parametro")

#Funcion con retorno
def con_retorno(numero):
    return numero

print("El numero es:", con_retorno(28))

#Funcion dentro de otra funcion
def funcion1():
    def funcion2():
        print("Funcion dentro de otra funcion")
    funcion2()

funcion1()

#Funciones propias del lenguaje

print(len("Python")) #Imprime cantidad de caracteres del string (6)
print(type(True)) #Imprime el tipo de dato (booleano)
print(bin(6)) #Imprime nunmero entero a binario
print(max(2, 8, 26, 76, 1, 0)) #Imprime numero mayor

#Variable global y local

variable_global = "Python"

def programar():
    variable_local = "Mouredev"
    print(variable_global, variable_local)

programar()
# print(variable_local) no se puede acceder a la variable fuera de la funcion 

"""DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

def funcion_extra(mensaje1, mensaje2):
    contador = 0
    for numero in range (1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(mensaje1, mensaje2)
        elif numero % 5 == 0:
            print(mensaje2)
        elif numero % 3 == 0:
            print(mensaje1)
        else:
            print(numero)
            numero += 1
    return contador

funcion_extra("Aprendo", "Python")