# En este archivo trabajaremos con funciones
# La forma basica de definir una funcione es:
def nombre_funcion(parametro1):
    #hacer funcion
    return None #Retornar un valor

# Funcion si parametros
def saludar():
    return "Hola, como estas?"

# Funcion con un parametro
def saludo_personalizado(nombre:str):
    return f"Hola {nombre.capitalize()}, como estas?"

print(saludo_personalizado('Jhon'))

def saludo_edad(nombre:str, edad:int):
    return f"Hola, mi nombres {nombre}, tengo {edad} años"

# Se pueden usar funciones dentro de funciones?
def funcion_externa(a:float, b:float):
    def funcion_interna(c:float):
        return c ** 2
    return a * funcion_interna(b)

print(funcion_externa(2,2))

# Tambien es aplicable para hacer recursividad, sin embargo este concepto trata de que usamos la misma funcion para obtener algun rasultado, sin necesidad de una funcion interna

#factorial
def factorial(n:int):
    if n > 0:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)
    else:
        return None
    
print(factorial(5))

#Funciones integradas en python:
length = len('Hola como estas?')
# funciones para hacer casting float(), list(), int(), str()
max(12,4,1)
min(12,51,1)
#Existen muchas...

# Scope de las funciones    
variable_global = 10
def operacion():
    variable_local = 5
    return variable_global - variable_local

# Ejercicio opcional
def FizzBuzz(a='Fizz', b='Buzz'):
    contador = 0
    for i in range(0,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - {a}{b}")
        elif i % 3 == 0:
            print(f"{i} - {a}")
        elif i%5 == 0:
            f"{i} - {b}"
        else:
            contador += 1
    return contador

print(FizzBuzz())