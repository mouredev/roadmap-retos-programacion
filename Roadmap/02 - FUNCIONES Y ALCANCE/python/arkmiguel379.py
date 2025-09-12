# Funcion sin valor de retorno y sin parametros

def saludar():
    print("Hola Logan")

saludar()

# Funcion con retorno sin parametros

def obtener_numero():
    return 379

print(obtener_numero())

# Funcion sin valor de retorno con parametros

def mensaje(str1, str2):
    print(f"{str1} {str2}")

mensaje("Hola", "Mundo")

# Funcion con retorno y parametros

def suma(value1, value2):
    return value1 + value2

print(suma(5,8))

# Funcion con paremetros opcionales o predeterminados

def informacion(nombre, apellido, edad, categoria = 0):
    print(f"Nombre: {nombre} Apellido: {apellido} Edad: {edad} Categoria: {categoria}")

informacion("Miguel", "Moreno", 28, 3)

# Funcion con múltiples valores de retorno

def division(dividendo, divisor):
    cociente = dividendo / divisor
    resto = dividendo % divisor
    return cociente, resto

resultado_cociente, resultado_resto = division(10,2)

print(resultado_cociente)
print(resultado_resto)

# ======================= FUNCIONES DENTRO DE FUNCIONES ============================

def funcion_externa():
    print("Inicio de la funcion externa")

    def funcion_interna():
        print("Ejecucion de la funcion interna")

    funcion_interna()

    print("Finalizacion de la funcion externa")

funcion_externa()

# ======================= FUNCIONES DEL SISTEMA ===================================

lista = [1, 2, 3, 4, 5]
longitud_lista = len(lista) # <-- LEN: Permite saber cual es la longitud de la coleccion a la que se aplica
print(longitud_lista)

tipo = type(lista) # <-- TYPE: Permite saber de que tipo es la variable que se le pasa
print(tipo)

entero = int("379") # <-- INT: Permite convertir a tipo INT el valor que se le pasa
cadena = str(257379) # <-- STR: Permite convertir a tipo STR el valor que se le pasa
flotante = float("3.14") # <-- FLOAT: Permite convertir a tipo FLOAT el valor que se le pasa

# nombre = input("Ingrese su nombre") # <-- INPUT: Lee una entrada del usuario desde la consola

secuencia = range(1, 10, 2) # <-- Secuencia de numeros del 1 al 10 que va de 2 en 2

coleccion = [10, 2, 3, 8, 13, 33, 25]
minimo = min(coleccion) # <-- Devuelve el valor minimo de una coleccion
maximo = max(coleccion) # <-- Devuelve el valor maximo de una coleccion
print(minimo)
print(maximo)

lista_desordenada = [10, 2, 3, 8, 13, 33, 25]
lista_ordenada = sorted(lista_desordenada)
print(lista_ordenada)

redondeado = round(3.14159) # <-- Dedondea al numero entero mas cercano

#============================== EXTRA =============================

def funcionE(str1, str2):

    contador = 0

    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{str1} + {str2}")

        elif i % 3 == 0:
            print(str1)

        elif i % 5 == 0:
            print(str2)
            
        else:
            print(i)
            contador += 1

    return contador

funcionE("Primer cadena", "Segunda cadena")