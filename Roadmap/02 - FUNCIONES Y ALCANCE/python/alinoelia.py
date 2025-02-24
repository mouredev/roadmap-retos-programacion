"""
! ¿Que es una FUNCIÓN?
Funciones definidas por el usuario
"""

# ! Función Simple

def saludar():
    print("Hola, Aliz, esta es una funcion simple")

saludar() # ? Asi llamo a la función

# ! Funciones con Retorno

def devuelve_el_saludo():
    return "Hola, esta es una funcion con return"

print(devuelve_el_saludo())

# ! Funciones con Argumentos
# Nosotros le pasamos parametros a la función

def argumento_saludo(nombre):
    print(f"Hola, {nombre}! Esta es una función con un argumento")

argumento_saludo("Alizon")

def argumentos_saludo(greet, name):
    print(f"{greet}, {name}! Esta es una funcion con varios argumentos")

argumentos_saludo("Holaaa", "Alizzzz")

# ! Funciones con argumentos predeterminados

def default_argumento_saludar(name="Noelia"):
    print(f"Hello, {name}! esta es una funcion con un argumento por defecto") # ? Cuando yo no escribo un argumento usa el que puse por defecto

default_argumento_saludar("Alicia")
default_argumento_saludar()

# ! Funciones con argumentos y retorno

def return_argumentos_saludar(greet, name):
    return f"{greet}, {name}! esta es una funcion con argumentos y return"

print(return_argumentos_saludar("Holis", "Alizzzooonnn"))

# ! Funciones con retornos de varios valores

def multiple_return_saludos():
    return "Holitas", "Señorita", "Varios valores"

greet, name, otro = multiple_return_saludos()
print(greet)
print(name)
print(otro)

# ! Funciones con un numero variable de argumentos
def variable_argumentos_saludos(*names):
    for name in names:
        print(f"Holaa, {name}! Esta es una funcion con varios argumentos guardados en una sola variable")

variable_argumentos_saludos("Alicia", "Charli", "Charlizon", "Kyra", "Donita", "Albita", "Mundicita")

# ! Funciones con un número variable de argumentos con palabra clave

def variable_clave_argumentos_saludar(**names):
    for clave, valor in names.items():
        print(f"Hola, {valor} ({clave})! Esta es una funcion con palabras claves")

variable_clave_argumentos_saludar(
    lenguaje = "Python",
    nombre = "Aliz",
    alias = "alinoelia",
    edad = 27
)

"""
! FUNCIONES DENTRO DE FUNCIONES
"""

def funcion_externa():
    def funcion_interna():
        print("Esta es una Función Interna: Holaa, Alizon!")
    funcion_interna()

funcion_externa()

"""
! FUNCIONES DEL LENGUAJE (BUILT-IN) --> funciones que estan construidas dentro del lenguaje
"""

print(len("Charlizon")) # ? LEN --> cuenta cuantas letras tiene mi palabra
print(type("Charlizon")) # ? TYPE --> nos da el tipo de dato que le estoy pasando
print("Charlizon".upper()) # ? UPPER --> vuelve todas las letras en mayuscula, es una funcion propia del lenguaje


"""
! VARIABLES LOCALES Y GLOBALES
"""

variable_global = "Charlyzon"


def hola_charlyzon():
    variable_local = "Hello"
    print(f"{variable_local}, {variable_global}!")

print(variable_global)
# print(variable_local) --> No se puede acceder desde fuera de la función

hola_charlyzon()


"""
! DIFICULTAD EXTRAAAA
? Este suele ser un ejercicio de logica que usan las compañias
"""

def imprimir_numeros(texto_1, texto_2)-> int: # ? Imprime los numeros del 1 al 100
    contador = 0
    for number in range(1, 101): 
        if number % 3 == 0 and number % 5 == 0: # ? Devuelve los multiplos de 3 y 5 y concatena los textos
            print(texto_1 + texto_2)
        elif number % 3 == 0:
            print(texto_1)
        elif number % 5 == 0:
            print(texto_2)
        else:
            print(number)
            contador += 1
    return contador  # ? Retorna el numero de veces que se escribe un número y no la cadena de texto  

print(imprimir_numeros("Fizz", "Buzz"))