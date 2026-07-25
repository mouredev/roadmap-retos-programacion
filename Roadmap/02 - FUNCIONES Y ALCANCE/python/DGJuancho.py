# Funciones sin parámetro ni retorno


def hola_mundo():
    print("Hola Mundo")


hola_mundo()


# Función con argumentos
def pares(a, b):
    print(f"Los números pares entre {a} y {b} son:")
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


pares(1, 20)


# Función con retorno
def potencia(x):
    print(f"El cuadrado de {x} es: ")
    return print(x**2)


a = 5

potencia(a)

# Funciones dentro de otras funciones


def area_circulo(radio):
    return 3.1416 * radio**2


def volumen_cilindro(radio, altura):
    areaBase = area_circulo(radio)
    return areaBase * altura


radio = 2.6
altura = 6.5
volumen = volumen_cilindro(radio, altura)
print(f"El volumen del cilindro es: {volumen}")

# Función del sistema "len" "type"
print(len("DGJuancho"))
print(type(120))

# Variables global y local

global_var = "Juancho"


def edad():
    local_var = 46
    print(f"Mi nombre es {global_var} y tengo {local_var} años")


print(global_var)
# print(local_var) La variable no está definida fuera de la función
edad()

"""
DIFICULTAD EXTRA
"""


def numeros(texto_1, texto_2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto_1 + texto_2)
        elif i % 3 == 0:
            print(texto_1)
        elif i % 5 == 0:
            print(texto_2)
        else:
            print(i)
            count += 1
    return count


print(numeros("TRES", "CINCO"))
