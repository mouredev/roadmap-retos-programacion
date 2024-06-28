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








