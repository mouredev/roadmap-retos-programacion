"""
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
 """

# Función sin parámetros y sin retorno:
def get_name1():
    print("Mariano")

get_name1()

# Función sin parámetros y con retorno:
def get_name2():
    name = "Pablo"
    return print(name)

get_name2()

# Función con parámetros y sin retorno:
def get_name3(name):
    print(name)

get_name3("Adrián")

# Función con parámetros y con retorno:
def get_name4(name, surname):
    return print(name + " " + surname)

get_name4("Manolo", "García")

# Función dentro de otra función:
def rest_tax(profit): # profit es una variable local que solo es accesible dentro de la función rest_tax
    def irpf_calculate(quantity):
        if quantity < 1500:
            tax = 10
        elif quantity > 1500:
            tax = 15
        return float(tax)
    total = profit  - ((irpf_calculate(profit)/100) * profit)
    return total

entrada = int (input("Introduzca su sueldo bruto mensual: "))
salary = rest_tax(entrada) # salary es una variable global y puede ser utilizada en cualquier parte del código
print(salary)

# Función ya creada en el lenguaje:

list1 = [5,10,7,15,45,3]

print(list(filter(lambda number: number >= 7, list1)))

"""
DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def return_num(word1, word2):
    counter = 0
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            counter += 1
            print(word1 + " " + word2)
        elif i % 3 == 0:
            counter += 1
            print(word1)
        elif i % 5 == 0:
            counter += 1
            print(word2)
        else:
            print(i)
    return counter

print(return_num("Hola", "Que tal")) 