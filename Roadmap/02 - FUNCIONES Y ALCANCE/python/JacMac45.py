# Funciones definidas por el usuario

# simple
def saludar():
    print("Hola, soy una función simple")

saludar()

# con retorno
def saludar():
    return "Hola, soy una función con retorno"

print(saludar())

# con parámetros o argumentos
def saludar(name):
    print(f"Hola!! {name}")


saludar("Python")

# con varios parámetros o argumentos y con retorno
def sumar(num1, num2):
    return num1 + num2

print(sumar(1, 2))

# con parámetros o argumentos por defecto
def saludar(name = "Tito"):
    print(f"Hola!! {name}")

saludar()
saludar("Python")

# con retorno de múltiples valores
def sumar(num1, num2):
    return num1 + num2, num1 - num2

print(sumar(1, 2))

# con numero variable de parámetros o argumentos
def saludar(*names):
    for name in names:
        print(f"Hola, {name}!")

saludar("Python", "Java", "C++")

# con numero variable de parámetros o argumentos y con palabra clave ** 
def saludar(**names):
    for key, name in names.items():
        print(f"Hola, {name} ({key})!")

saludar(
    name1="Python", 
    name2="Java", 
    name3="C++"
    )

