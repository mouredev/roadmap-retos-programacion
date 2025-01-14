"""
Ejemplos de funciones básicas:
    Sin parámetros ni retorno
    Con uno o varios parámetros
    Con retorno...
"""
# Suma sin parámetro ni retorno
def suma():
    print(1+2)

# Resta sin parámetro, pero con retorno
def resta():
    return 2 - 1
# Multiplicación con parámetro y retorno
def multi(a,b):
    return a * b

"""
Funciones dentro de funciones
"""
# Función que contiene otra función
def saludo(nombre):
    def complemento(nombre):
        complemento = "Hola, estimando"
        saludo = "{} {}".format(complemento,nombre)
        return saludo
    saludo = complemento(nombre)
    return saludo

"""
Variable LOCAL y GLOBAL.
"""

def ver():
    # Esto es una variable locañ de la función ver()
    palabra1 = "Nuevo"
    # Esto ya es una variable global
    global palabra2
    palabra2 = "Auntiguo"
    return palabra1, palabra2

# <palabra1> no puede ser llamado aquí para usarlo, en cambio <palabra2> sí

"""
A continuación, imprimimos todas las funciones, utilizando la función print() de python
"""

print("Esto es la función sin parámetro: {}".format(suma()), "Función con retorno, pero sin parámetro: {}".format(resta()), "Función con parámetro y retorno: {}".format(multi(1,3)), "Función dentro de otra función: {}".format(saludo("Santos")), sep="\n")
print("Esto es variable local de la función ver(): {}".format(ver()[0]), "Y esto es la variable global de ver(): {}".format(ver()[1]), sep="\n")

"""
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion(texto1, texto2):
    for i in range(1,101):
        numero = 0
        if i % 3 == 0 and i % 5 == 0:
            print(texto1+texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else: numero+=1
    return numero

print(funcion("texto1","texto2"))