# Función sin parámetros ni retorno
def saludar():
    print("¡Hola, mundo!")

saludar()

# Función con un parámetro y retorno
def cuadrado(numero):
    return numero ** 2

resultado_cuadrado = cuadrado(5)
print("Cuadrado de 5:", resultado_cuadrado)

# Función con varios parámetros y retorno
def suma(a, b):
    return a + b

x = 3
y = 7
resultado_suma = suma(x, y)
print(f"Suma de {x} y {y}:", resultado_suma)

# Función dentro de una función
def operacion_matematica(x, y):
    def cuadruple(num):
        return num * 4

    resultado1 = cuadruple(x)
    resultado2 = cuadruple(y)

    return resultado1 + resultado2

resultado_operacion = operacion_matematica(2, 3)
print("Resultado de operación compleja:", resultado_operacion)

# Variable local y global
variable_global = 10

def funcion_con_variables():
    variable_local = 5
    print("Variable local dentro de la función:", variable_local)
    print("Variable global dentro de la función:", variable_global)

funcion_con_variables()
print("Variable global fuera de la función:", variable_global)

# DIFICULTAD EXTRA
def imprimir_numeros_con_texto(texto1, texto2):
    contador = 0

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            contador += 1

    return contador

veces_impreso = imprimir_numeros_con_texto("Fizz", "Buzz")
print("Número de veces impreso:", veces_impreso)
