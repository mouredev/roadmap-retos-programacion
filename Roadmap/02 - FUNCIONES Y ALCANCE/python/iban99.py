#Sin parámetro ni retorno (SIMPLE)
def saludo ():
    print("hola mundo")
    
saludo()

#Con retorno
def return_saludo ():
    return "Hola mundo"

#Si no pongo el print, no lo imprime por pantalla, o bien pongo el print o bien 
#Lo incluyo dentro de la variable
print(return_saludo())

#Con argumento
def argumento(name, apellido):
    print(f"Hola, {name} {apellido}")
    
argumento("Miriam", "Iban")
argumento(apellido="Iban", name="Miriam")

#Con argumento predeterminado
def arg_default(name = "Python"):
    print(f"Hola, {name}")

arg_default()

#Con parámetro y retorno
def return_args(saludo, nombre):
    return(f"{saludo}, {nombre}")

print(return_args("Hola", "Miriam"))

#Con retorno de varios valores
def multiple_return():
    return "Hola", "Python"

saludo, nombre = multiple_return()
print(saludo)
print(nombre)

#Con un numero variable de argumentos
#Puedo pasar más de un nombre
def variable_arg_greet(*names):
    for name in names:
        print (f"Hola, {name}!")

variable_arg_greet("Python", 'Miriam', "Comunidad")

#Con un numero variable de argumentos con palabra clave
#Cada argumento está formado por una clave y un valor
def variable_key_arg_greet(**names):
    for key, name in names.items():
        print (f"Hola, {name} ({key})!")

variable_key_arg_greet(lenguage="Python", name='Miriam', age="25")



#Función dentro de función
def outer_function (a, b):
    x = a - b
    def inner_function (c):
        g = x*c
    return (g)


def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python")
    #Necesito llamar a la función para que llegue a printearse
    inner_function()
    
outer_function()


#Funciones de lenguaje
print(len("Miriam")) #Len()
print(type("Miriam")) #Type()
print("MoureDev".upper()) #Upper()


#Variables GLOBALES
global_variable = "Python"

print(global_variable)

def hello_python():
    print(f"Hello, {global_variable}")
    
hello_python()
    

#Variables LOCALES
def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_variable}")

hello_python()
print(global_variable)
# print(local_var) --> no puedo acceder directamente 


#Dificultad extra
def print_number(texto_1, texto_2):
    count = 0
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print(texto_1+texto_2)
        elif i%3 == 0:
            print (texto_1)
        elif i%5 == 0:
            print (texto_2)
        else:
            print(i)
            count +=1
    return count

print(print_number("Fizz", "Buzz"))