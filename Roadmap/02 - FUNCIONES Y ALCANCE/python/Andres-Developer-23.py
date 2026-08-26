# funciones simples
def saludar():
    print("Hola, Mundo")
saludar()

# funciones con retorno
def saludar():
    return "Hola, Mundo"
print(saludar())

# funciones con un argumento
def saludar(nombre):
    print(f"Hola, {nombre}")
saludar("Andres")

# funciones con 2 argumentos
def sumar(a, b):
    print(f"{a} + {b} = {a + b}")
sumar(3, 6)

# funciones con argumentos predeterminados
def saludar(nombre="anonimo"):
    print(f"Hola, {nombre}")
saludar()
saludar("Andres")

# funciones con multiples argumentos
def lista_estudiantes(*nombres):
    print("Estudiantes")
    for nombre in nombres:
        print(f"-> {nombre}")
lista_estudiantes("Andres", "Felipe", "Carlos", "Camilo", "Roberto")

# funciones con multiples argumentos con clave y valor
def usuario(**nombres):
    print("Usuario")
    for key, value in nombres.items():
        print(f"-> {key}: {value}")
usuario(
    Nombre="Andres",
    Apellido="Bravo",
    Correo="andres@gmail.com",
)

# funciones dentro de funciones

def externa():
    print("Esta es una funcion externa")
    def interna():
        print("Esta es una funcion dentro de otra funcion")
    interna()
externa()

# funciones del lenguaje
print("Hola, mundo".upper())
print(type(10.56))
print(len("Python"))

# variables locales y globales

variable_global = "Variable global"
def mensaje():
    variable_local = "Variable local"
    print(variable_local)
    print(variable_global)
mensaje()
# print(variable_local) = NameError: name 'variable_local' is not defined

# Extra
def mostrar_number(text_1, text_2):
    count = 0
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
print(mostrar_number("Fizz", "Buzz"))