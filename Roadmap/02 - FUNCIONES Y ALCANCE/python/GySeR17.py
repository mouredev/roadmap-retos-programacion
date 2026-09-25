"""
Lista de funciones posibles
1. Funciones built-in
2. Funciones definidas por el usuario
3. Funciones dentro de funciones (HOF - Funciones de Orden Superior)
4. Funciones anonimas(funciones lambda)
5. Funciones de modulos
6. Funciones de objetos (Metodos)
7. Funciones recursivas
8. Funciones generadoras
9. Funciones decoradoras
"""


"""
1. Funciones integradas (Built-in Functions)
"""

#Algunas de las mas usadas pueden ser:
print("Hola")   #Muestra informacion en pantalla
len("Python")   #Retorna la longitud de un objeto
type(5)         #Muestra el tipo de dato
type("Hello!")
int("10")       #Convierte a entero
float("2.3")    #Convierte a decimal
str(1234)       #Convierte a texto  
#input("Introduzca su nombre:\n")    #Recibe datos del usuario
sum(range(5), 2)                    #Suma elementos
max(1, 2, 5, 9, 4, 8, 3, 6, 36)     #Retorna el maximo
max(-6, 2, 5, 9, 4, 8, 3, 6, 36)    #Retorna el minimo
range(2, 15)                        #Genera secuencias de numeros

"""
2. Funciones definidas por el usuario
"""
# simple

def saludo():
    print("Hola, Python!")

saludo()

#Con recepcion de parametros:
print("\nCon 1 parametro")

def cuadrado(num):
    print(num ** 2)

cuadrado(3)


print("\nCon varios parametros")

def sumar(a, b, c):
    return a + b + c

total = sumar(2, 5, 9)
print(total)

def mult(a, b, c):
    return a * b * c

total_2 = mult(2, 5, 9)
print(total_2)

"""
3.Funciones dentro de funciones (HOF - Funciones de Orden Superior)
"""

#Cualquier funcion que este definida por el usuario

def aplicar(funcion, valor):
    return funcion(valor)

def cubo(x):
    return x ** 3
print(aplicar(cubo, 5))

"""
4. Funciones anonimas(funciones lambda)
"""

#Son funciones pequeñas sin nombre, usadas para operaciones simples
suma = lambda a, b: a + b
print(suma(3, 4))

# Se usan mucho con map o sorted:
numeros = [1, 2, 3, 4]
doble = list(map(lambda x: x * 2, numeros)) #crear una lista, que con la funcion de map esta funcion lambda itera por cada numero de la lista:
print(doble)

"""
5. Funciones de modulos
"""
#Se deben importar para poder ser usados:

import math
print(math.sqrt(16))

import random
print(random.randint(1, 15))

"""
6. Funciones de objetos (Metodos)
"""
texto_1 = "Hola Sergio!"
print(texto_1.upper())

numeros = [1, 2, 3, 4]
numeros.append(5)
print(numeros)


"""
7. Funciones recursivas
"""

#Son funciones que se llaman a si mismas

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

"""
8. Funciones generadoras
"""

#Usan yield para generar valores uno por uno, sin almacenar toda la lista en memoria.
def contar():
    for i in range(5):
        yield i 
for numero in contar():
    print(numero)

"""
9. Funciones decoradoras
"""
#Son funciones que modifican el comportamiento de otras funciones
def decorador(func):
    def nueva_funcion():
        print("Antes de ejecutar")
        func()
        print("despues de ejecutar")
    return nueva_funcion

@decorador
def saludo():
    print("Hola!")

saludo()

"""
Dificultad extra:
"""
print("=================================")
print("      Dificultad extra:")
print("=================================")

def numeros():
 pass

#Siguiendo el video de brais:

#Sin parametros:

print("Sin parametos:")
def saludar_1():
    print("Hola Gyser17!")

saludar_1()

#con parametro:
print("\nCon 1 parametro:")
def saludar_2(name_2):
    print(f"Hola, {name_2}")

saludar_2("Sergio!")

#Con varios parametros:
print("\nCon varios parametros:")
def saludar_3(saludo_3, name_3):
    print(f"{saludo_3}, {name_3}")

saludar_3("Buenos dias!","Sergio")

#Con parametros por defecto:
print("\nCon parametros por defecto:")

def saludar_4(name_4 = "Gyser"):
    print(f"Hola!, {name_4}!\nComo te va??")

saludar_4()
saludar_4("Sergio")