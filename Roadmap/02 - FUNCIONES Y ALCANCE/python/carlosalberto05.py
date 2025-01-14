'''
Funciones definidas por el usuario
'''

#Simple y con argumentos
def saludo(name):
	print("Hola " + name)
 
saludo("Carlos")

#Con retorno y argumentos
def return_greet(name):
    return "Hola " + name

greet = return_greet("Roberto")
print(greet)

#Funcion con argumentos
def sum(a,b):
    return f"La suma es: {a + b}"

print(sum(3,9))

#Funcion con argumentos y valores por defecto
def mul(a = 2,b = 2):
    return f"La suma es: {a * b}"

print(mul(3))

#Funcion con argumentos y valores por defecto en distinto orden
def mul(a = 2,b = 2):
    return f"La suma es: {a / b}"

print(mul(b=3, a=9))

#Funcion con retorno de varios valores
def multiple_return():
    return "Juan", "Pedro"

print(multiple_return())

name_one, name_two = multiple_return()
print(name_one)
print(name_two)

#Funciones con un número variable de argumentos
def variable_arg(*names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_arg("Python", "JavaScript", "Swift")

#Funciones con un número variable de argumentos pero con palabras clave
def variable_key_arg(**names):
    for key, name in names.items():
        print(f"Hola, {name} ({key})!")
        
variable_key_arg(language = "Python", lang = "JavaScript", apple ="Swift")

'''
Funciones dentro de funciones
'''

def outer_function():
    def inner_function():
        print("Función interna: Hola Charly")
    inner_function() 

outer_function()

'''
Funciones del lenguaje
'''

print() #print es una función de python
print(len("carlos")) #len también es una función de python como el length de js
print(type(3)) #type nos dice el tipo de dato como typeof de js
print("carlos".upper()) #es otra función de python similar a upperCase de js


'''
Variables locales y globales
'''

global_var = "python"

print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var},{global_var}")
    

#print(local_var) no se puede acceder desde fuera de la función por que es local
print(global_var)
    
hello_python()


'''
Extra
'''

def print_number(str1, str2):
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{str1} {str2}")
        elif number % 3 == 0 :
            print(str1)
        elif number % 5 == 0: 
            print(str2)
        else :
            print(number)
            count += 1
    return count
    

print(print_number("Fizz", "Buzz"))