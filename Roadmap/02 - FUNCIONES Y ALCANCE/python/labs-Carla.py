"""
Funciones definidas por el usuario
"""

#Función simple, función que no recibe ningún parametro, ejecuta lo de adentro, se llama desde donde sea y se ejecuta.

def greet():
    print("Hola, soy Python!")

greet()
greet()

#Con retorno

def return_greet():
    return "Hola Python!"

print(return_greet())

#Con argumentos

def arg_greet(greet,name):
    print(f"{greet} {name}!")

arg_greet("Saluda","Carla")

#Con un argumento predeterminado

def arg_greet(greet,name):
    print(f"{greet} {name}!")

arg_greet("Saluda","Carla")

def default_arg_greet(name="Carla"):
    print (f"tu nombre es {name}")

default_arg_greet("Tatiana")

#Con  argumentos y retorno

def return_args_greet(greet,name):
    return f"{greet} {name}"

print(return_args_greet("HOLA", "TATIANA"))

#Con múltiples retornos

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

#Con un número variable de argumentos

def variable_arg_signs(*signs):
    for sign in signs:
        print(f"Tu signo de tierra es {sign}")

variable_arg_signs("virgo","capricornio","tauro")

#Con un número variable de argumentos con palabra clave


def variable_key_arg_signs(**signs):
    for key, value in signs.items():
        print(f"Tu {key} : ({value})")

variable_key_arg_signs(
    elemento = "Tierra",
    signo = "Virgo",
    modalidad = "Mutable"
)

"""Funciones dentro de funciones"""

def outer_function():
    def inner_function():
        print("a function whitin a function")
    inner_function()

outer_function()

"""Funciones del lenguaje (built-in)"""

print(len("Carla"))
print(type(8000))
print("Carla".upper())

"""Variables locales y globales (scope)"""

globalVariable = "Python"  #scope global

print(globalVariable)

def hello_python ():
    local_var = "python" #scope local
    print (f"Hello {local_var}") 

hello_python()


 
def extra_function (str1,str2) -> int:
    count = 0
    for i in range(1,101):
        if(i%3==0 and  i%5==0):
             print(str1+str2)
        elif(i%5==0):
            print(str2)
        elif(i%3==0):
            print(str1)
        else:
            print(i)
            count += 1
    return count
    

print(extra_function("fizz", "buzz"))