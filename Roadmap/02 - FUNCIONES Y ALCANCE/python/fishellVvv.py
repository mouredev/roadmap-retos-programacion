# función simple
def greet():
    print("Hola, Python!")

# función con retorno
def return_greed():
    return "Hola, Python!"

# función con argumentos
def arg_greed(name):
    print(f"Hola, {name}!")

# función con argumentos predeterminados
def default_arg_greet(name = "Python"):
    print(f"Hola, {name}!")

# función con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"

# función con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

# función con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})")

# funciones dentro de funciones
def outer_function():
    def inner_function():
        print("Hola, Python! (función interna)")
    inner_function()

# funciones del lenguaje
print(len("fishellVvv"))
print(type("fishellVvv"))
print("fishellVvv".upper())

# variables locales y globales
global_var = "Python"
def greed_2():
    print(f"Hola, {global_var}!")
    local_var = "Mundo"
    print(f"Hola, {local_var}!")
greed_2()
print(f"Hola, {global_var}!")

# extra
def print_numbers(text_1, text_2)-> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text_1 + text_2)
        elif i % 3 == 0:
            print(text_1)
        elif i % 5 == 0:
            print(text_2)
        else:
            count += 1
            print(i)
    return count
print(print_numbers("Fizz", "Buzz"))