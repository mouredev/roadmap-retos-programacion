"""
Funciones definidad por el usuario
"""

# Función simple

def greet():
    print("Hola, Python!")

greet()

# Función con retorno

def return_greet():
    return "Hola, Python!"
greet = return_greet()
print(greet)
print(return_greet())

# Función con 1 argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet('Liner')


# Función con argumentos

def arg_greet(greet,name):
    print(f"{greet}, {name}!")

arg_greet('Hi','Liner')
arg_greet(name = 'HannyDev',greet = 'Hello')

# Función con un argumento predeterminado
def arg_greet(name = 'Java'):
    print(f"Hola, {name}!")

arg_greet('Hanny')
arg_greet()


# Función con argumentos y return

def return_args_greet(greet, name):
    return f'{greet}, {name}!'

print(return_args_greet('Hello', 'Camilo'))

# Con retorno de varios valores

def multiple_return_greet():
    return "Holaaaa", "Python"

greet, name = multiple_return_greet()
print(greet, name)

# funcion con un número de variables de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Holaaaa, {name}!")
variable_arg_greet('Python','Brais','Comunidad')


# Con un número variable de argumento con palabras claves

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")
variable_key_arg_greet(language = "Python",name = "Brais",alias = "MoureDev",age = 36)


# Funciones dentro de funciones

def outer_function():
    def inner_function():
        print('Función interna: Hola, Python!')
    inner_function()
outer_function()


# Funciones del lenguaje(built-in)

print(len('MoureDev')) #Función len
print(type(36)) #Función type
print('MoureDev'.upper()) #Función upper
print(complex(5)) #Función complex
lista = [4,5,6]
print(sum(lista)) #Función suma
print('MoureDev'.lower()) #Función lower
print('moureDev brais'.title()) #Función title
print('mouredev brais'.capitalize()) #Función capitalize
x = input('Inserte su número: ') # Función input
print(x)
print(int(5.740)) #función int


""" 
Variables locales y globales
"""

global_variable = 'python' #Variable global

print(global_variable)

def hello_python():
    #local_var = 'hola' , es una variable local y no se puede llamar afuera de la función
    #print(f'{local_var}, {global_variable}')
    print(f'Hola, {global_variable}')
hello_python()
#print(local_var)


#DIFICULTAD EXTRA

def extra(text_1,text_2)-> int:
    count = 0
    for i in range(101) :
        if i % 3 == 0 and i % 5 == 0:
            print(f'{text_1}, {text_2}') 
        elif i % 3 == 0:
            print(f'{text_1}') 
        elif i % 5 == 0:
            print(f'{text_2}')
        else:
            print(i)
            count += 1
    return count
 
cantidad = extra("Fizz","Buzz")
print(cantidad) 