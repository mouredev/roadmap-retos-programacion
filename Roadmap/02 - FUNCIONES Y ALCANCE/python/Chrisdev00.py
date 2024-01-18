"""
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

# Declaring and Calling a Function

# def function_name ():
#     codes
#     codes

# function_name()

############## Function without Parameters 

def show_name ():
    first_name = 'Pepito'
    last_name = 'Perez'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
show_name ()

def sum_two_numbers ():
    number_one = 2
    number_two = 3
    total = number_one + number_two
    print(total)
sum_two_numbers()

############### Function Returning a Value

def show_name ():
    first_name = 'Pepito'
    last_name = 'Perez'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(show_name ())

def sum_two_numbers ():
    number_one = 2
    number_two = 3
    total = number_one + number_two
    return total
print(sum_two_numbers())


########### Function with Parameters

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def sum_value(num):
    ten = 2
    return num + ten
print(sum_value(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55


############# Function with 2 parameters

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Pepito','Perez'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(3, 6))


############ Function Passing Arguments with Key and Value

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2))


############# Function Returning a boolean

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    
    return False
print(is_even(10))
print(is_even(7))


############### Function Returning a list

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))


############### Function with Default Parameters

def full_name (first_name = 'Pepito', last_name = 'Perez'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(full_name())
print(full_name('David','Smith'))


############## Function with Arbitrary Number of Arguments

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     
    return total
print(sum_all_nums(2, 3, 5))

################ Function as a Parameter of Another Function

def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))


########   Dificultad Extra #########

def impre_num (text1, text2):
    
    cont = 0
    for i in range (1,101):
        
        if i % 3 == 0 and i % 5 == 0:
            print(f"{text1} {text2}")
            cont += 1
        elif i % 3 == 0:
            print(text1)
            cont += 1
        elif i % 5 == 0:
            print(text2)
            cont += 1        
        else:
            print(i)
    
    return (100 - cont)

resul = impre_num("Pepito", "Perez")
print(f"El numero de veces que se imprimieron los numeros es: {resul}")


