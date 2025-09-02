"""
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# Funcion sin parametro y sin retorno
def imprimir():
    print("\nHola, Python!")

imprimir()

# Funcion con parametro y sin retorno
def imprimir_nombre(nombre):
    print(f"\nHola, {nombre}!")

imprimir_nombre("Manuel")

# Funcion sin parametro y con retorno
def obtener_pi():
    return 3.1416

print(f"\n{obtener_pi()}")

# Funcion con parametros y con retorno
def sumar(numero1, numero2):
    return numero1 + numero2

print(f"\n{sumar(3, 5)}")

# Funcion con retorno multiple
def operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta

print(f"\nSuma: {operaciones(4, 4)[0]}")
print(f"Resta: {operaciones(5, 3)[1]}")

# Funcion con parametro por defecto
def saludar(nombre = "Manuel"):
    print(f"\nHola, {nombre}!")

saludar()
saludar("Juan")

# Funcion con numero variable de argumentos
def sumar_todos(*args): # Argumentos posicionales
    return sum(args)

print(f"\n{sumar_todos(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

def impresion(**kwargs): # Argumentos nombrados
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

impresion(nombre= "Manuel", edad= 29)

# Funcion dentro de otra funcion
def imprimir():
    print("\nHola, ", end= "")
    def imprimir_segundo():
        print("Python!")
    imprimir_segundo()

imprimir()

# Funciones ya creadas en Python (built-in)
print(f"\n{len("Manuel")}")
print(sum([1, 2, 3, 4]))
print(str(6))

# Uso de variables locales y globales
variable_global = "Global"

def imprimir_local():
    variable_local = "Python"
    print(f"\nVariable global: {variable_global}\nVariable local: {variable_local}")

imprimir_local()
print(f"\n{variable_global}")
# print(f"{variable_local}") # No accede ya que solo se puede usar en la funcion en que fue declarada

# EXTRA
def imprimir_cadenas(cadena1, cadena2) -> int:
    contador = 0
    print()
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(cadena1 + cadena2)
        elif numero % 3 == 0:
            print(cadena1)
        elif numero % 5 == 0:
            print(cadena2)
        else:
            print(numero)
            contador += 1
    
    return contador

print(imprimir_cadenas("Fizz", "Buzz"))