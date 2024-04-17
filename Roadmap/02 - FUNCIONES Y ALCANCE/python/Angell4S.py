"""
Funciones definidas por el usuario
"""

# simple

def greet():
   print("Hola, python!")

greet()

# con retorno (return)
def return_greet():
   return "Hola, python!"

greet = return_greet()
print(greet)

# con un argumento
def arg_greet(name):
   print(f"Hola, {name}!")

arg_greet("Angel")

# con un argumentos
def args_greet(greet, name):
   print(f"{greet}, {name}!")

args_greet("HI","Angel")
args_greet(name="Angel", greet="HI")

# con un argumento predeterminado
def default_arg_greet(name="Python"):
   print(f"Hola, {name}!")

default_arg_greet("Angel")
default_arg_greet()

# con un argumentos y retorno
def return_args_greet(greet, name):
   return f"{greet}, {name}!"

print(return_args_greet("HI","Angel"))

# Con retorno de varios valores
def multiple_return_greet():
   return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable con argumentos
def variable_arg_greet(*names):
   for name in names:
      print(f"Hola, {name}!")

variable_arg_greet("Python", "Angel", "Mouredev", "Comunidad")

# Con un número  variable de argumentos con palabras clave
def variable_key_arg_greet(**names):
   for key, value in names.items():
      print(f"{value} ({key})!")

variable_key_arg_greet(language="Python", name="Angel", alias="Mouredev", age=36)

"""
Funciones dentro de funciones
"""
def outer_funcion():
   def inner_function():
      print("Función interna: Hola python")
   inner_function()

outer_funcion()

"""
Funciones del lenguaje (built-in)
"""
print(len("Angell4S"))
print(type(36))
print("angell4s".upper())

"""
Variables locales y globales
"""
global_var = 'Python'
print(global_var)

def hello_python():
   local_var = 'Hola'
   print(f'{local_var}, {global_var}!')

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
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

print(print_numbers('Fizz', 'Buzz'))