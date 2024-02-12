"""
EJERCICIO:
- Crea ejemplos de funciones basicas que representen las diferentes
posibilidades del lenguaje:
Sin parametros ni retorno, con uno o vario parametros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algun ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el cocepto de variable LOCAL Y GOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer mas o menos 
posibilidades)

DIFICULTAD EXTRA (opcional):
- Crea una funcion que reciba dos parametros de tipo cadena de texto,
y retorne un numero.
- La funcion imprime todos los numeros del 1 al 100. Teniendo en
cuenta que:
- Si el numero es multiplo de 3, muestra la cadena de texto del 
primer parametro.
- Si el numero es multiplo de 5, muestra la cadena de texto del 
segundo parametro 
- Si el numero es multiplo de 3 y de 5, muestra las dos cadenas de 
texto concatenadas.
- La funcion retorna el numero de veces que se ha impreso el numero
en lugar de los texto.

- Presta especial atención a la sintaxis que debes utilizar en cada 
uno de los casos.
- Cada lenguaje sigue una convenciones que debes de respetar para que 
el código se entienda.

by adra-dev.
"""

"""
Funciones: Las funciones son pequeños programas, con una entrada de 
datos sobre la cual se generara una salida. Tradicionalmente 
denominadas <<Subrutinas>>.
"""

# Funcion sin parametros ni retorno

def my_function():
    pass

print(my_function())

# Funcion con uno o varios parametros

def bigger_than(a, b):
    if a > b:
        pass
    pass

print(bigger_than(9, 8))

# Funcion con retorno

def less_than(a, b):
    if a < b:
        return a
    return b 

print(less_than(5,9))

"""
Anidacion: 
    La anidacion hace referncia tanto a la declaracion de una funcion
    dentro del cuerpo de otra, como a la llamada a una funcion a
    partir de los resultados de otra.

    La usaremos cuando definir una funcion fuera de otra no tiene 
    sentido, es decir, cuando la funcion interna solo va a ser 
    utilizada por la funcion externa. Una funcion interna solo es 
    visible en el ambito de la funcion que la aloja.
"""

def check_items(items):

    def dump(item):
        print('The item', item, 'is nots valid')
    
    for i,x in enumerate(items):
        if x > 100:
            dump(i)

check_items([96, 98, 102, 99])

"""
Built-in functions o funciones predefinidas del lenguaje:
    Son funciones ya creadas dentro del lenguaje y que siempre estan 
    disponibles cuando las necesitemos, puedes checarlas todas en la
    url: (https://docs.python.org/3/library/functions.html).
"""
a = [1, 2, 3, 4, 5, 6]
print(sum(a)) # la funcion sum, suma los elementos dentro un iterable.

"""
Ambito o Scope:
    El ambito de una variagle es el contexto en el cual la variable
    es conocida. Las varaibles que se definen en el cuerpo de una 
    funcion son variables locales, mientrasque las que se definen a
    lo largo del programa son variables globales.
"""

# Scope
animal = 'leon' # Variable Global -> Funciones, condiciones, ciclos

def imprimir_animal():
    animal = 'Ballena' # Variable Local

    print(animal)
    print(id(animal))


imprimir_animal()

print(animal)
print(id(animal))


"""
Extra
"""

def fizz_buzz(str1 ="fizz", str2 ="buzz"):
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0 :
            print(str1 + " " + str2)
        elif number % 3 == 0:
            print(str1)
        elif number % 5 == 0:
            print(str2)
        else:
            print(number)
            count += 1
    return print("El numero total de veces que se ha impreso el numero es:", count)

fizz_buzz('Hello', 'there')