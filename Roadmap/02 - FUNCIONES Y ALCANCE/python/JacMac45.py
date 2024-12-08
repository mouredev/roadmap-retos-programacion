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

# Funcines dentro de funciones
def saludar(name): # Función padre
    def saludar2(name): # Función hija de la Función padre 
        return f"Hola, {name}"
    return saludar2(name)

print(saludar("Python"))

# Funciones del lenguaje
print("\n====== Funciones propias del lenguaje ======")

print('print() --> es una funcion propia del lenguaje python') # Funcion para imprimir en la consola
print(f'len() funcion propia para obtener la longitud: {len("Hola")}') # Funcion para obtener la longitud de una cadena
print(f'type() funcion propia para obtener el tipo de dato: {type("Hola")}') # Funcion para obtener el tipo de dato de una variable
print(f'abs() funcion propia para obtener el valor absoluto: {abs(-5)}') # Funcion para obtener el valor absoluto de un numero

# Variables Globales y Locales
print("\n====== Variables Globales y Locales ======")

variable_global = 'Variable global'
print(variable_global)


def variables():
    variable_local = 'Variable local'
    print(variable_global)  # Funciona porque es global
    print(variable_local)   # Funciona porque esta dentro de la funcion donde fue creada
    
print(variable_global)  # Funciona porque es global
# print(variable_local)   # Error: variable_local no esta definida fuera de la funcion

# Extra
print("\n====== DIFICULTAD EXTRA ======")

def numextra (string1, string2):
    contador = 0
    for num in range (1, 101):
        
        if num % 3 == 0 and num % 5 == 0:
           print (string1 + string2)
        elif num % 5 == 0:
            print (string2)
        elif num % 3 == 0:
            print (string1)    
        else:
            print(num)
            contador += 1
        
    print (f"Los numeros han aparecido: {contador} veces")    
             
numextra ("Hola", "Guapo")   