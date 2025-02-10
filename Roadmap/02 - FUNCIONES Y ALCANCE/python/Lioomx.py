'''
Funciones en Python
'''

# Función simple con argumentos y retorno

def suma(a, b):
    return a + b
resultado = suma(2, 3)
print(f"El resultado de la suma es: {resultado}")

# Función sin parámetros

def saludar():
    print("Hola, Bienvienido al curso de Python")

saludar()

# Función con valores predeterminados

def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3)) # 3^2 = 9; usa el valor predeterminado
print(potencia(3, 3)) # 3^3 = 27; usa el valor proporcionado

# Función que devuelve multiples valores

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    división = a / b
    return suma, resta, multiplicación, división # Devuelve una tupla

resultados = operaciones(10, 5)
print(resultados)

# Función con argumentos variables

def sumar_todos(*numeros):
    return sum(numeros)

print(sumar_todos(1, 2, 3, 4, 5))

# Uso de argumentos con nombre (keyword arguments)

def mostrar_info(**kwargs):
    for key, value, in kwargs.items():
        print(f"{key}: {value}")

mostrar_info(Nombre="Lio", Edad=24, Ciudad="CDMX")

# Funciones anónimas (lambda)

doblar = lambda x: x*2 # Función que dobla el valor de x;
print(doblar(5))

# Recursividad

def factorial(n): # Calcula el factorial de un número
    if n == 0: # Caso base
        return 1 # 0! = 1
    return n * factorial(n-1) # Llamada recursiva

print(factorial(5)) # 5! = 120

# Funciones anidadas 

def exterior(x): # Función exterior
    def interior(y): # Función interior
        return y ** 2 # Eleva al cuadrado
    return interior(x) + 1 # Llama a la función interior y suma 1

print(exterior(5)) # 5^2 + 1 = 26

# Función como parámetro

def aplicar_operación(función, valor): # Recibe una función y un valor 
    return función(valor) # Aplica la función al valor

resultado = aplicar_operación(lambda x: x ** 2, 5) 
print(resultado) # 5^2 = 25

# Función generadora
def generador_pares(n): # Genera números pares del 0 al n
    for i in range(n): # Itera sobre el rango de 0 a n
        if i % 2 == 0: # Si el número es par
            yield i # yield: devuelve el valor

for i in generador_pares(10): 
    print(i) # Imprime los números pares del 0 al 8

# Decoradores

def decorador(función): # Recibe una función
    def envoltura(): # Función envoltura
        print("Antes de la función") 
        función() # Llama a la función
        print("Después de la función") 
    return envoltura # Devuelve la función envoltura 

@decorador  # Aplica el decorador a la función
def mi_función(): 
    print("Mi función") 

mi_función() # Llama a la función decorada

# Manejo de excepciones

def dividir(a, b): # Divide dos números
    try: # try: intenta ejecutar el bloque de código
        return a / b # Intenta dividir a entre b
    except ZeroDivisionError: # ZeroDivisionError: Error al dividir entre 0
        return "Error: No se puede dividir entre 0" # Maneja el error

print(dividir(10, 2)) 
print(dividir(10, 0))

'''
Funciones dentro de funciones
'''

def exterior(x): 
    def interior (y):
        return y ** 2 
    return interior(x) + 1

print(exterior(5)) # 5^2 + 1 = 26

'''
Funciones creadas en el lenguaje
'''

print(abs(-5))
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))
print(len("Bienvenido"))
print(type(36))
print(type("Hola"))

''''
Variables Locales y Globales
'''

# Variables Globales

x = 10 # Variable global

def mostrar_x():
    print(f"Valor de x: {x}") # Accediendo a la variable global

mostrar_x()

# Variables locales

def funcion():
    y = 20 # Variable local
    print(f"Valor de y: {y}")

funcion()

"""
EXTRA
"""

def print_nmb(text1, text2):
    contador = 0

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: # Múltiplo de 3 y 5
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1) # Múltiplo de 3
        elif i % 5 == 0:
            print(text2) # Múltiplo de 5
        else:
            print(i) # Imprime el número si no es multiplo de 3 ni de 5
            contador += 1 # Incrementa el contador cuando se imprime un número
    return contador # Retorna el contador

resultado = print_nmb("Fizz", "Buzz")
print(f"Números impresos en lugar de textos: {resultado}")












