# Funciones definidas 

# Función simple sin parámetros ni retorno
def saludo():
    print("Hola, Mundo!")

saludo()

# Función con un argumento
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Ejecución de las funciones básicas
saludo()  # Vuelve a llamar a la función sin parámetros
saludar("Python")  # Llama a la función con un argumento

# Función con retorno
def return_saludar():
    return "Hola Python!"

print(return_saludar())  # Imprime el valor retornado por la función

# Función con varios argumentos y sin retorno
def saludos(saludo, nombre):
    print(f"{saludo}, {nombre}")

saludos("Hi", "Joan")  # Los argumentos se pasan en orden
saludos(nombre="Joan", saludo="Hi")  # Argumentos pasados por nombre

# Función con un argumento con valor por defecto
def default_saludar(nombre="Python"):
    print(f"Hola, {nombre}!")

default_saludar("Joan")  # Llama a la función con argumento
default_saludar()  # Llama a la función sin argumentos, usando el valor por defecto

# Función con retorno de varios valores
def multiple_default_saludar():
    return "Hola", "Python"

# Asignación de múltiples valores retornados por la función
saludo, nombre = multiple_default_saludar()
print(saludo)
print(nombre)

# Función dentro de una función
def operacion():
    def resta(a, b):
        return a - b
    print(f"La resta de 10 y 5 es: {resta(10, 5)}")

operacion()  # Llama a la función que contiene otra función

# Función con un número variable de argumentos
def variable_arg_saludo(*nombres):  # El * significa que se le pueden pasar varios argumentos
    for nombre in nombres:
        print(f"Hola, {nombre}")

variable_arg_saludo("Joan", "Python", "Comunidad")  # Llama a la función con múltiples argumentos

# Función con un número variable de argumentos con palabra clave
def variable_key_arg_saludo(**nombres):
    for key, value in nombres.items():
        print(f"{value} ({key})")

variable_key_arg_saludo(
    lenguaje="Python",
    nombre="Joan",
    alias="Joandevpy", 
    edad=34
)

# Función dentro de una función
def otra_operacion():
    def interna_operacion():
       print(f"Funcion interna: Hola, Python")
    interna_operacion()

otra_operacion()  # Llama a la función que contiene una función interna

# Uso de funciones incorporadas (Built-in)
print(len("joandevpy"))  # Imprime la longitud de la cadena
print(type(35)) # Imprime el tipo de la variable
print("joandevpy".upper())  # Convierte la cadena a mayúsculas

# Variables locales y globales
global_variable = "Soy una variable global"

print(global_variable)  # Imprime la variable global

def prueba_variables():
    local_variable = "Esto sería"  # Esta variable solo existe dentro de la función
    print(f"{local_variable}, {global_variable}")  # Imprime las variables local y global

prueba_variables()
print(global_variable)  # Imprime la variable global

# Función que recibe dos parámetros de tipo cadena de texto y retorna un número
def print_numbers(text_1, text_2) -> int:
    count = 0  # Inicializar el contador
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

# Llamar a la función
print(print_numbers("Fizz", "Buzz"))
