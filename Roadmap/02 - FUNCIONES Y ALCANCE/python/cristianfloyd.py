print("Funciones en Python")


# * - Crea ejemplos de funciones básicas que representen las diferentes
# *   posibilidades del lenguaje:
# *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

# Función sin parámetros y sin valor de retorno
def saludo():
    print("Hola, bienvenido a las funciones en Python")

saludo()

# Función con un parámetro y sin valor de retorno
def imprimir_cuadrado(numero):
    print(f"El cuadrado de {numero} es {numero ** 2}")

imprimir_cuadrado(4)

print("="*80)
print("Función con varios parámetros y sin valor de retorno")
def imprimir_suma(a, b):
    suma = a + b
    print(f"La suma de {a} y {b} es {suma}")

imprimir_suma(3, 5)

print("="*80)
print("Función con un parámetro y con valor de retorno")
def calcular_cuadrado(numero):
    return numero ** 2

resultado_cuadrado = calcular_cuadrado(6)
print(f"El cuadrado de 6 es {resultado_cuadrado}")

print("="*80)
print("Función con varios parámetros y con valor de retorno")
def calcular_potencia(base, exponente):
    return base ** exponente

resultado_potencia = calcular_potencia(2, 3)
print(f"2 elevado a la potencia 3 es {resultado_potencia}")

# funcion con multiples parametros y 1 retorno
print("="*80)
print("Función con múltiples parámetros y un valor de retorno")
def multiples_parametros(*args):
    return sum(args)

multiples_parametros_resultado = multiples_parametros(1, 2, 3, 4, 5)
print(f"La suma de los parámetros es {multiples_parametros_resultado}")

# * - Comprueba si puedes crear funciones dentro de funciones.

print("="*80)
print("Funciones dentro de funciones")
def funcion_externa(x):
    # creo una funcion interna
    def duplicar(y):
        return y * 2
    return duplicar(x) + 3

resultado_funcion_interna = funcion_externa(5)
print(f"El resultado de la función externa es {resultado_funcion_interna}")

# * - Pon a prueba el concepto de variable LOCAL y GLOBAL.

print("="*80)
print("Variables LOCAL y GLOBAL")

variable_global = "Soy una variable global"
def mostrar_variables():
    variable_local = "Soy una variable local"
    print(variable_local)  # Accediendo a la variable local
    print(variable_global)  # Accediendo a la variable global

mostrar_variables()

# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

print("="*80)
print("Uso de funciones integradas de Python")
numeros = [5, 2, 9, 1, 5, 6]
print(f"Números originales: {numeros}")
numeros_ordenados = sorted(numeros)
print(f"Números ordenados: {numeros_ordenados}")

longitud = len(numeros)
print(f"La longitud de la lista es {longitud}")
mayor_numero = max(numeros)
print(f"El número mayor es {mayor_numero}")
menor_numero = min(numeros)
print(f"El número menor es {menor_numero}")

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
print("="*80)

print("Función FizzBuzz personalizada")
def mi_fizzbuzz(texto1: str, texto2: str) -> int:
    contador = 0
    for index in range(1, 101):
        if index % 15 == 0:
            print(texto1 + texto2, end="")
        elif index % 3 == 0:
            print(texto1, end="")
        elif index % 5 == 0:
            print(texto2, end="")
        if index % 3 != 0 and index % 5 != 0:
            print(index, end="")
        else:
            contador += 1
        print()  # Nueva línea después de cada número o texto
    return contador

veces_numeros = mi_fizzbuzz("Fizz", "Buzz")
print(f"Números impresos en lugar de textos: {veces_numeros}")