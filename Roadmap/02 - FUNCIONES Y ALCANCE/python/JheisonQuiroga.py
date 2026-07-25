# Funciones

# 1. Funciones sin parámetros

def add_two_numbers():
    n1 = 10
    n2 = 12
    print("El resultado de la suma es: ", n1 + n2)

add_two_numbers()

# 1.1 Con uno, dos y varios parametros

def square_number(num):
    square = num * num
    print(square)

square_number(10)

def mult(n1, n2):
    result = n1 * n2
    print(result)

# 1.2 Retornando un valor

def hello_world():
    return f"Hello, World"

hello = hello_world() # Se guarda el valor de retorno (string) en una variable
print(hello)

# 1.3 Retornando varios valores

def love_number():
    first_n = 6
    second_n = 9
    return first_n, second_n

print(love_number()) # (6, 9)
first_n, second_n = love_number()
print(str(first_n) + str(second_n))

# 1.4 Numero variable o arbitrario de parámetros

def square_numbers(*numbers): # argumentos posicionales
    lst_numbers = [num ** 2 for num in numbers]
    return lst_numbers

print(square_numbers(2, 4, 6, 8, 10))

# Keywords argument
# Numero variable de argumentos por palabras clave
def unpaking(**names):
    for key, value in names.items():
        print(key, value)

unpaking(
    name = "Duban",
    last_name = "Quiroga",
    skills = ["Python", "Git"],
    age = 25
)

# 2. Funciones dentro de funciones

def out_function():
    def inner_function():
        print("Hola Mundito")
    inner_function()

out_function()

"""
 3. Funciones integradas del sistema (built - in)

"""

my_string = "Hello world"
print(len(my_string)) # Se obtiene el largo de mi cadena (11 carácteres)

#Funcion type()
print(type(my_string)) # <class 'str'>


fv_fruits = ["banana", "pineaple", "watermelon", "strawberry"]

for i, fruit in enumerate(fv_fruits): # Funcion enumerate: Se obtiene una lista indexada de indice-valor
    print(i + 1, fruit)

"""
4. Prueba de scope global y local
"""

gravity = 9.8

def object_weight():
    global gravity

    mass = 70
    gravity = 10
    weight = mass * gravity
    print(weight)

object_weight()
print(gravity) # Sin la palabra reservada GLOBAL, deberia ser 9.8

"""
Extra
"""

#Funcion que recibe dos cadenas de texto y retorne un numero

def fizzbuzz(n1, n2) -> int:
    count = 0
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(n1 + n2)
        elif n % 3 == 0:
            print(n1)
        elif n % 5 == 0:
            print(n2)
        else:
            count += 1
            print(n)
    return count

number = fizzbuzz("Fizz", "Buzz")
print(number)