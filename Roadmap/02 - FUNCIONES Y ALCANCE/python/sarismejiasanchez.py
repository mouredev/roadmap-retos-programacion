# #02 FUNCIONES Y ALCANCE

# Función sin argumentos ni retorno
print("Función sin argumentos ni retorno")

def saludo():
    print("Hola mundo!")

# Ejecutar la funcion
saludo()

# Función con un argumentos y retorno
print(f"\nFunción con un argumentos y retorno")
numero = 5

def cuadrado(numero):
    return numero ** 2

resultado = cuadrado(numero)
print(f"Cuadrado de {numero}: {resultado}")

# Funcion con argumentos predeterminados
print(f"\nFuncion con argumentos predeterminados")

def default_arg_greet(name="Python"):
    print(f"Hola, {name}")

default_arg_greet("Sara")
default_arg_greet()

# Llamar la funcion indicando los argumentos
def greet(greet, name):
    print(f"{greet}, {name}")

greet("Hola", "Python")
greet(name="Python", greet="Hi")

# Función con argumentos y retorno de multiples valores
print(f"\nFunción con argumentos y retorno de multiples valores")

def suma_producto(num1, num2):
    print(f"Parámetros de la función: num1 = {num1}, num2 = {num2}")
    suma = num1 + num2
    producto = num1 * num2
    return suma, producto

suma, producto = suma_producto(5, 4)
print(f"Suma: {suma}")
print(f"Producto: {producto}")

# Función con un numero variable de argumentos
print(f"\nFunción con un numero variable de argumentos")

def variable_arg_greet(*names): # Argumentos separados por coma
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Python", "Sara", "MoureDev", "Comunidad")

# Función con un numero variable de argumentos con palabra clave
print(f"\nFunción con un numero variable de argumentos con palabra clave")

def variable_key_arg_greet(**names): # Cada argumento estará formado por una clave y un valor
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language = "Python",
    name="Sara",
    alias = "sarismejiasanchez",
    age = 31
    )


"""
Función dentro de función
"""
print(f"\nFunción dentro de función")

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python!")
    inner_function()

outer_function()

"""
En esta función, se define una función interna llamada cuadruplicar. 
La función principal toma un parámetro x, multiplica este parámetro por 4 utilizando 
la función interna cuadruplicar, y luego devuelve el resultado.
"""

def funcion_principal(x):
    def cuadruplicar(num):
        return num * 4
    resultado = cuadruplicar(x)
    return resultado

resultado_final = funcion_principal(5)
print("Resultado de función dentro de función:", resultado_final)


"""
Funciones del lenguaje (built-in)
https://docs.python.org/3/library/functions.html
"""

print(f"\nFunciones del lenguaje (built-in)")

"""
len()
Retorna el tamaño (el número de elementos) de un objeto. 
El argumento puede ser una secuencia (como una cadena, un objeto byte, una tupla, lista o rango) 
o una colección (como un diccionario, un set o un frozen set).
"""
print(f"\nlen():")
longitud_lista = len([1, 2, 3, 4, 5])
print(f"La longitud de la lista es: {longitud_lista}")

"""
enumerate(iterable, start=0)
Retorna un objeto enumerador. iterable tiene que ser una secuencia, un iterator, 
o algún otro objeto que soporte la iteración. El método __next__() del iterador 
retornado por la función enumerate() retorna una tupla que contiene un contador 
(desde start, cuyo valor por defecto es 0) y los valores obtenidos al iterar sobre iterable.
"""
print(f"\nenumerate(iterable, start=0)")
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(f"Lista: {seasons}")
print(f"Lista con enumerate: {list(enumerate(seasons))}")

"""
filter(function, iterable)
function	A Function to be run for each item in the iterable
iterable	The iterable to be filtered

Filter the array, and return a new array with only the values equal to or above 18:
"""
print(f"\nfilter(function, iterable):")
ages = [5, 12, 17, 18, 24, 32]
print(f"Lista ages: {ages}")

def is_adult(age):
    if age < 18:
        return False
    else:
        return True

adults = filter(is_adult, ages)

for age in adults:
    print(age)


"""
Variables Globales y Locales
Global: Se definen por fuera del ámbito de la función
Local: Funcioan dentro del ambito de la función
"""

print(f"\nVariables Globales y Locales")
global_var = "Python"
print(f"global_var: {global_var}")

def hello_python():
    local_var = "Hello"
    print(f"local_var: {local_var}")
    print(f"{local_var}, {global_var}!")

hello_python()

# Variable global
variable_global = 10

# Función que utiliza variable global
def incrementar_variable():
    global variable_global
    variable_global += 1

# Uso de variable global
print(f"\nVariable global antes de incrementar:", variable_global)
incrementar_variable()
print("Variable global después de incrementar:", variable_global)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
print(f"\nDIFICULTAD EXTRA")
def return_numbers(text1, text2):
    count = 0
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 == 0):
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else:
            print(number)
            count += 1
    return count
    
# Ejecucion
text1 = "Fizz"
text2 = "Buzz" 
resultado = return_numbers(text1, text2)
print(f"Se realizaron {resultado} impresiones de números")