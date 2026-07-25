# Funciones en python

# Funcion sin retorno
def test():
    print("Hola mundo")
test()  # Llamada a la función

# Funcion con retorno
def return_test():
    return "Hola mundo"
print(return_test())  # Llamada a la función con retorno

#Funcion con parametros
def parameters(name, age):
    print(f"Hola {name}, tienes {age} años")
parameters("Pedro", 19)  # Llamada a la función con parámetros

#Funcion con parametros por defecto
def parameters_default(name="Pedro", age=19):
    print(f"Hola {name}, tienes {age} años")
parameters_default()  # Llamada a la función con parámetros por defecto
parameters_default("Juan", 25)  # Llamada a la función con parámetros personalizados    

#Funcion dentro de otra función
def funcion_externa():
    def funcion_interna():
        print("Hola desde la función interna")
    funcion_interna()  # Llamada a la función interna
funcion_externa()  # Llamada a la función externa
# funcion_interna()  # Error, la función interna no es accesible desde fuera de la función externa

#Funcion con varios retornos
def varios_retornos(num):
    if num > 0:
        return "Número positivo"
    elif num < 0:
        return "Número negativo"
    else:
        return "Número cero"
print(varios_retornos(5))  # Llamada a la función con número positivo
print(varios_retornos(-3))  # Llamada a la función con número negativo
print(varios_retornos(0))  # Llamada a la función con número cero

#Funcion con bucle for para distintos nombres
def nombres(nombres_list):
    for nombre in nombres_list:
        print(f"Hola {nombre}")
nombres(["Pedro", "Juan", "Maria"])  # Llamada a la función con una lista de nombres

#Funcion con claves y valores
def claves_valores(**names): # El ** indica que se pueden pasar un número indefinido de argumentos con clave-valor
    for clave, valor in names.items(): # El método items() devuelve una lista de tuplas con las claves y valores del diccionario
        print(f"{clave}: {valor}") # f sirve para formatear la cadena de texto, reemplazando las variables por su valor

claves_valores(
    Nombre = "Pedro",
    Edad = 19,
    Nacionalidad = "Argentino"
) # Llamada a la función con claves y valores

#Funciones built-in (definidas por el lenguaje)

print(len("Hola mundo"))  # Función len() para obtener la longitud de una cadena de texto en este caso devuelve 10
print(type(123))  # Función type() para obtener el tipo de dato de una variable en este caso devuelve <class 'int'>, si fuera 1.5 devolveria <class 'float'>, si fuera "Hola" devolvería <class 'str'>, etc
print("pedro-blasco".upper())  # Función upper() para convertir una cadena de texto a mayúsculas, en este caso devuelve "PEDRO-BLASCO"
print("PEDRO-BLASCO".lower())  # Función lower() para convertir una cadena de texto a minúsculas, en este caso devuelve "pedro-blasco"
print("Hola mundo".split())  # Función split() para dividir una cadena de texto en una lista de palabras, en este caso devuelve ["Hola", "mundo"] 

# Variables Locales y Globales

global_variable = "Hola"  # Variable global, se puede acceder desde cualquier parte del código

def local_variable():
    local_variable = "Python"  # Variable local, solo se puede acceder dentro de la función
    print(f"{global_variable}, {local_variable}")  # Imprime la variable local

print(global_variable)  # Imprime la variable global
local_variable()  # Llamada a la función que imprime la variable local
# print(local_variable) Da error, la variable local no es accesible desde fuera de la función

"""
DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 """
 
def multiples(text1, text2):
    count = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{text1} {text2}") # Formatear el texto es una buena practica por si text1 y text2 no son cadenas de texto, de esta manera se convierten a string y no da error
        elif num % 3 == 0:
            print(f"{text1}")
        elif num % 5 == 0:
            print(f"{text2}")
        else:
            print(num)
            count += 1
    return count # Retorna el número de veces que se ha impreso el número en lugar de los textos

print(multiples("Texto1", "Texto2"))  # Llamada a la función con los textos "Fizz" y "Buzz"

