"""
-------------------
FUNCIONES Y ALCANCE
-------------------
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
# Ejercicio

def funBasica():
    print("Esto es una función básica")

funBasica()

def funArgumento(name):
    print("Mi nombre es: " + name)
    
funArgumento("Sergio")

def funMult(parametro, parametroDos):
    print(parametro * parametroDos)
    
funMult(5, 10)

def funRetorno():
    return "Función con retorno"
    
print(funRetorno())

my_list = [1, 2, 3, 4]
def funSum():
    return max(my_list) + 5

print(funSum())

myGlobal_variable = 6

def my_fun():
    myLocal_variable = myGlobal_variable + 5
    return myLocal_variable
    
#print(myLocal_variable) # undefined
print(my_fun())

# Ejercicio Extra

print("Ejercicio extra:")

def my_ejercicio(str_one, str_two):
    count = 0
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(str_one, str_two)
        if n % 3 == 0:
            print(str_one)
        elif n % 5 == 0:
            print(str_two)
        else:
            print(n)
            count += 1
    print(f"Se han impreso: {count} números")
    
my_ejercicio("fizz", "buzz")