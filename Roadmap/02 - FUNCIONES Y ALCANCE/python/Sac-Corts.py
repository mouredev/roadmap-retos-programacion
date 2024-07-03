""" 
EJERCICIO
"""

# Función sin parámetros ni retorno
def saludar():
    print("Hola Isaac")

saludar()

# Función con uno o varios parámetros 
def saludarNombre(name):
    print("Hola " + name)

saludarNombre("Geovanni")

# Función con retorno 
def sumar(a, b):
    return a + b

print(sumar(1, 4))

# Función dentro de una función
def funcion_principal(name):
    def funcion_secundaria():
        print("Mi nombre es:", name)
    funcion_secundaria()


funcion_principal("Isaac")

# Función ya creada en python
lista = [10, 30, 50, 100]
print(max(lista))
print(min(lista))

# Variable global
x = 21

def variable_global():
    print("Mi variable x es: ", x)

variable_global()

# Variable local 
def variable_local():
    global j 
    j = 11

variable_local()

def mostrar_variable_local():
    print("Mi variable j es: ", j)

mostrar_variable_local()

"""
DIFICULTAD EXTRA
"""

def numeros(cadena1, cadena2):
    contador = 0

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(cadena1 + cadena2)
        elif num % 3 == 0:
            print(cadena1)
        elif num % 5 == 0:
            print(cadena2)
        else:
            print(num)
            contador += 1
    return contador
    
cadena1 = "Fall"
cadena2 = "out"
resultado = numeros(cadena1, cadena2)
print("Número de veces que se ha impreso un número:", resultado)