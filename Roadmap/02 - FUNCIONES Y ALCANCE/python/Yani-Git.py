#una función es un bloque de código. Se crea para poder realizar una acción específica
#proporciona una forma de organizar el código en bloques lógicos

"""
funciones definidas por el usuario. 
las crea el usuario como le de la gana
la función se define con "def"

"""

#Simple


def greet ():
    print ("Hola, Python")

greet ()


#Funcion con retorno va a acabar devolviendo algo 

def return_greet():       #en python aunque no se defina algo puedría devolverlo porque es un leguaje de tipado dinamico
    return "Hola, Python!"


# greet = return_greet()
print (return_greet())


# funciones con un argumento: sigunifica que le podemos pasar parámetros a la función 

def arg_greet (name):
    print (f"Hola, {name}!")

arg_greet ("Yani")


#con argumentos 

def arg_greet (greet, name):
    print (f"{greet}, {name}!")

arg_greet ("Hi","Yani")
arg_greet (name="Yani", greet="Hi")



#con un argumento predeterminado


def defoult_arg_greet (name ="Python"):
    print (f"Hola, {name}!")

defoult_arg_greet ("Yani")
defoult_arg_greet ()

#funciones con argumentos  y retornos 

def return_arg_greet (greet, name):
    return f"{greet}, {name}!"

print(return_arg_greet("Hi", "Yani"))


#funcion con retorno de varios valores-tupla de valores 

def multiple_return_greet ():
    return "Hola", "Python"

greet, name =multiple_return_greet()
print(greet)
print (name)


"""

en python se pueden crear funciones básicas

>>ejemplo de funciones básicas = 

1.- con un numero  variables de argumentos

2.- con un numero  variables de argumentos pero con palabra clave 

"""


#1.- con un numero  variables de argumentos

def variable_arg_greet(*names):  #el asterisco indica que le podemos pasar mas de un nombre separados por coma, es decir, guarda mas de un resultado en la memoria
    for name in names:
        print (f"Hola, {name}!")

variable_arg_greet ("Python", "Yani","Yanines", "Github")


#2.- con un numero  variables de argumentos pero con palabra clave 

def variable_key_arg_greet(**names):  # se colocan dos asteriscos para indicar una clave a cada argumento, lo que significa que cada argumento estará formado por una clave y un valor
    for key, value in names.items ():
        print (f"{value} ({key})!")

variable_key_arg_greet (

    leguaje ="Python", 
    name="Yani", 
    alias ="Yanines", 
    age= 47

    )

"""
funciones dentro de funciones 

"""

def outer_function():
    def inner_function():
        print ("Función interna: Hola, Python !")
    inner_function()

outer_function()

"""
funciones construidas dentro del lenguaje (built- in)


"""

print (len("yanines")) #funcion "len" le pasamos un texto y devuelve un entero
print (type("yanines")) #nos dice el tipo dato que le estamos poniendo en la  variable, en este caso es una cadena de texto
print ("yanines".upper()) #devuelve la función en mayuscula

"""
Variables locales y globales 

    tiene que ver con el concepto de ámbito, 

"""

global_var = "Python"
print (global_var)


def hello_python():  #las funciones se definen, imprimen y se llaman, si no la llamo no se imprime
    local_var = "Hola"  #solo se va poder acceder a la variable  dentro de la función 
    print (f"{local_var}, {global_var}!")

print (global_var)
#print (local_var) no se puede acceder a una variable local fuera de la función 
#hay que valorar o ponderar si resulta conveniente que la variable sea global o local 


hello_python ()

"""
Extra, ejercicios 

"""
def print_numbers (text_1, text_2)-> int:
    count =0 
    for number in range (1, 101):
        if  number % 3 ==0 and number % 5 ==0: 
             print (text_1 + text_2)
        elif number % 3 ==0:
            print (text_1)
        elif number % 5 ==0:
            print (text_2)
        else: 
            print(number)
            count += 1
    return count

#print_numbers("Texto 1","Texto 2")

print (print_numbers("Fizz","Buzz"))
