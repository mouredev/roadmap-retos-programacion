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
"""
FUNCIONES SIN VALOR DE RETORNO
"""
print("FUNCIONES SIN VALOR DE RETORNO")

#Función sin parámetros ni valores de retorno
def empty_function():
    print("Esta es una función sin parámetros ni valores de retorno")

empty_function()

#Función con un parámetro pero sin valores de retorno
def one_parameter(number):
    print(number * 2)

one_parameter(3)

#Función con dos parámetros sin valores de retorno
def two_parameters(first_value, second_value):
    print(f"La suma de {first_value} y {second_value} es: {first_value + second_value}")

two_parameters(5,3)

"""
FUNCIONES CON VALOR DE RETORNO
"""
print("\n")
print("FUNCIONES CON VALOR DE RETORNO")

#Función con un parámetro y retorno
def one_parameter_and_return(one_value):
    return one_value * 2

print(f"La función one_parameter_and_return con el parámetro de entrada 4 devuelve: {one_parameter_and_return(4)}")

#Función con dos parámetros y retorno
def two_parameters_and_return(first_value,second_value):
    return first_value - second_value

print(f"La función two_parameters_and_return que recibe los parámetros de entrada 8 y 3 devuelve: {two_parameters_and_return(8,3)}")

"""
FUNCIONES DENTRO DE FUNCIONES
"""
print("\n")
print("FUNCIONES DENTRO DE FUNCIONES")

#Con Lambdas
def concat_strings():
    return lambda string_one,string_two: string_one + string_two
print(f"Los strings concatenados son: {concat_strings()("Hola ","soy Alex")}") #Esto es un closure

#Con otras funciones
def multiply_value(value):
    def add_five():
        return value + 5
    return add_five() * 2

print(f"La función multiply_value: {multiply_value(3)}") #Esto es otro closure

def sum_values(value_one,value_two):
    def mutliply(value_three):
        return (value_one + value_three) * value_two
    return mutliply

print(f"La función sum_values da: {sum_values(2,3)(5)}") #Y Esto es otro closure

#Funciones como argumentos

def sum_two(number):
    return number + 2

def sum_two_values(value_one, value_two,f):
    return f(value_one + value_two)

print(f"La función sum_two_values que tiene como argumento sum_two: {sum_two_values(5,4,sum_two)}")

"""
FUNCIONES DEl LENGUAJE
"""
print("\n")
print("FUNCIONES DEl LENGUAJE")

one_list = [5,20,17,63,54]
other_list = ["Alex","Sole","Martín","Valeria","Spock"]
my_int = 7
my_other_int = 4

print(f"La función len() nos devuelve la longitud de one_list, que es: {len(one_list)}")
print(f"Con slice() podemos coger un \"trozo\" del índice 2 al 4 de one_list: {one_list[slice(2,5)]}")
print(f"podemos pasar one_list a una tupla con tuple(): {tuple(one_list)}")
print(f"También pasar de nuevo esa tupla a lista con list(): {list(tuple(one_list))}")
print(f"Con enumerate() + list() creamos una lista de tuplas desde one_list: {list(enumerate(one_list))}")
print(f"O comprobar el tipo de one_list con la función type(): {type(one_list)}")
print(f"También podemos crear un diccionario con dict.fromkeys():\n {dict.fromkeys(other_list,"default")}")
print(f"Podemos pasar un my_int a float con la función float(): {float(my_int)}")
print(f"Y pasar ese float a int de nuevo con int(): {int(float(my_int))}")
print(f"Se puede calcular la potencia de un número con pow(): {pow(2,3)}")
print(f"Pasar un número a string con str(): {str(my_int)}")
print(f"Definir un rango con range(): {range(0,10)}")
print(f"Redondear el número 3.94162835 con round(): {round(3.94162835)}")
print(f"Hacer el sumatorio de los elementos de one_list con sum(): {sum(one_list)}")
print(f"O podemos darle la vuelta a one_list con reversed() + list(): {list(reversed(one_list))}")
print(f"También la one_list podemos ordenarla con sorted(): {sorted(one_list)}")
print(f"Podemos obtener el valor ordinal de un caracter con ord(): {ord("A")}")
print(f"Con hash() podemos codificar cualquier cosa, por ejemplo la cadena \"Hola Mundo\": {hash("Hola Mundo")}")
print(f"Con hex() podemos pasar un número (el 23 por ejemplo) a hexadecimal: {hex(23)}")

"""
VARIABLES GLOBALES Y LOCALES
"""
print("\n")
print("VARIABLES GLOBALES Y LOCALES")

my_global_string = "Esto es una variable global" #Una variable local será accesible en cualquier parte de nuestro programa
def training_function():
    my_local_string = "Esto es una variable local" #Las variables locales a una función solo se pueden usar dentro del alcance de la función
    print(my_local_string) #puedo utilizar la variable porque estoy dentro de la función
    print(my_global_string) #también puedo llamar a la variable global dentro de la función

training_function()
#print(my_local_string) esto da un error porque my_local_string no está declarada fuera de la función.

"""
DIFICULTAD EXTRA
"""
print("\n")
print("DIFICULTAD EXTRA")
def adhoc_fizzbuzz(text_one,text_two):
    numbers_count = 0
    for number in range(0,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_one+text_two)
        elif number % 3 == 0:
            print(text_one)
        elif number % 5 == 0:
            print (text_two)
        else:
            print(number)
            numbers_count += 1
    
    return numbers_count

string_one = input("Dime la primera cadena de texto: ")
string_two = input ("Ahora dime la segunda cadena de texto: ")

print(f"Los números se han impreso {adhoc_fizzbuzz(string_one,string_two)} veces")
