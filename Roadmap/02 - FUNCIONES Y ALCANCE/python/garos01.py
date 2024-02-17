# Ejemplo 1: Función sin parámetros ni retorno
def saludar():
    print("¡Hola, mundo!")


saludar()


# Ejemplo 2: Función con un parámetro y retorno
def cuadrado(numero):
    return numero**2


resultado_cuadrado = cuadrado(5)
print("El cuadrado de 5 es:", resultado_cuadrado)


# Ejemplo 3: Función con varios parámetros y retorno
def suma(a, b):
    return a + b


resultado_suma = suma(3, 7)
print("La suma de 3 y 7 es:", resultado_suma)


# Ejemplo 4: Función dentro de otra función
def operacion_compleja(x, y):
    def multiplicar(a, b):
        return a * b

    resultado_multiplicacion = multiplicar(x, y)
    return resultado_multiplicacion + 10


resultado_operacion = operacion_compleja(2, 3)
print("El resultado de la operación compleja es:", resultado_operacion)

# Ejemplo 5: Variable local y global
variable_global = 10


def funcion_con_variables():
    variable_local = 5
    print("Variable local dentro de la función:", variable_local)
    print("Variable global dentro de la función:", variable_global)


funcion_con_variables()

# Intentar acceder a variable_local aquí daría un error, ya que es local a la función.
# print("Intento de acceder a variable_local fuera de la función:", variable_local)
print("Variable global fuera de la función:", variable_global)


# Ejercicio extra
def imprimir_numeros_y_contar_textos(texto1, texto2):
    contador_textos = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
            contador_textos += 1
        elif numero % 3 == 0:
            print(texto1)
            contador_textos += 1
        elif numero % 5 == 0:
            print(texto2)
            contador_textos += 1
        else:
            print(numero)

    return contador_textos


# Ejemplo de uso:
resultado = imprimir_numeros_y_contar_textos("Fizz", "Buzz")
print(f"Se imprimieron {resultado} textos en total.")
