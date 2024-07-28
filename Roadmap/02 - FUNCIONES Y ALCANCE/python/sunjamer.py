# funciones

# funcion sin parametros

def pinta_texto():
    print ("esta función pinta este texto")

pinta_texto()

# funcion que retorna un valor

def sumador():
    a = 9
    b = 5
    return (a + b)

print (sumador())

# función con parametros

def multiplicador_por2 (numero):
    return (numero * 2)

print(multiplicador_por2(25))

# función con dos parámetros

def multiplicar_por_valor(numero, multiplicador):
    return (numero * multiplicador)

print(multiplicar_por_valor(796,344))

# funcion con key y valor

def multiplicar_por_valor2 (numero, multiplicador):
    return (numero * multiplicador) 

print (multiplicar_por_valor2 (multiplicador=2, numero=500))

# función que retorna un string

def junta_palabras(palabra1, palabra2):
    espacio = ' '
    palabra_total = palabra1 + espacio + palabra2
    return (palabra_total)

print (junta_palabras("tonto", "quienlolea"))

# funcion con parámetro por defecto

def calcular_edad (año_nacimiento=2000, año_actual=2024):
    return (año_actual - año_nacimiento)

print(calcular_edad(1977, 2014))

# funcion con numero indeterminado de argumentos

def multiplicar_numeros(*numeros):
    total = 1
    for nums in numeros:
        total *= nums 
    return total

print(multiplicar_numeros(3, 5, 10, 2, 24))







"""
extra
"""


def funcion_extra (cadena1, cadena2) -> int:
    contador = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print (cadena1 + ' y ' + cadena2)
        elif num % 3 == 0:
            print(cadena1)
        elif num % 5 == 0:
            print (cadena2)
        else:
            print (num)
            contador += 1
    return contador

veces = funcion_extra("multiplo de 3","multiplo de 5")
print(veces)
    

# funcion dentro de función

def suma_numeros (num1, num2, num3):
    def suma_num1_num2 (num1, num2):
        return num1 + num2
    suma_parcial = suma_num1_num2(num1, num2)
    return num3 + suma_parcial

print(suma_numeros (20, 400, 80))








