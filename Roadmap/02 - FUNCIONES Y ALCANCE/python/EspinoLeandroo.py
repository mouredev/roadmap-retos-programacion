# Función sin parámetros ni retorno
def saludar():
    print("¡Hola! Esta es una función de saludo.")

# Función con parámetros y retorno
def suma(a, b):
    return a + b

# Función con parámetros predeterminados
def saludar(nombre="Mundo"):
    print("¡Hola,", nombre + "!")

# Función con retorno múltiple
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

# Función que utiliza una función interna
def externa():
    def interna():
        print("Esta es una función interna.")
    interna()

# Variable global
variable_global = 10

# Función que utiliza una variable global
def funcion():
    variable_local = 5
    print("Variable local dentro de la función:", variable_local)
    print("Variable global dentro de la función:", variable_global)

# Llamada a las funciones
saludar()
resultado = suma(3, 5)
print("La suma es:", resultado)
saludar("Juan")
resultados = operaciones(10, 5)
print("Resultados:", resultados)
externa()
funcion()
print("Variable global fuera de la función:", variable_global)
