"""
FUNCIONES DEFINIDAS POR EL USUARIO
"""

# FUNCIONES SIMPLES

def saludo():
    print("hola a todos")
saludo()

# FUNCIONES CON RETORNO

def saludoconretorno():
    return "hola chicas"
print(saludoconretorno())

# CON ARGUMENTO(S)

def saludo(parametro1):
    print(f"simon dice: {parametro1}")
saludo("hola chicos")

# CON ARGUMENTO(S) PREDETERMINADO

def saludos(parametro1="ola que ace"):
    print(f"simon dice: {parametro1}")
saludos()

#  ESTABLECIENDO PARAMETROS AL LLAMAR LA FUNCION

def short(question,answer):
    print(question,answer)

short(answer="vientos",question="como le baila?")

# CON ARGUMENTO(S) Y RETORNO

def saludoyretorno(parametro1):
    return(f"simon dice: {parametro1}")
print(saludoyretorno("de que hablan?"))

# CON RETORNO DE VARIOS VALORES
def multiple_return_greet():
    return "js", "Python"
greet, name = multiple_return_greet() #Se asignan dos variables diferentes
print(greet)
print(name)

# CON UN NUMERO VARIABLE DE ARGUMENTOS

def arg_numbers(*names):
    print("Vamos a contar")
    for name in names:
        print(name)
arg_numbers("uno","dos","tres")

# CON UN NUMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE

def arg_numbers_key(**names):
    print("Vamos a contar")
    for key, value in names.items():
        print(value,key)
arg_numbers_key(
    one="uno",
    two="dos",
    three="tres"
)

"""
FUNCIONES DENTRO DE FUNCIONES
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Todo bien ahi fuera?")
    inner_function()

outer_function()    

"""
FUNCIONES DEL LENGUAJE (BUILT-IN)
"""

print("DEVCHERRY1".lower())
print(f"Cuantos caracteres tiene tu user: {len("devcherry1")}")
print(f"Y si hablamos del tipo: {type("devcherry1")}")

"""
VARIABLES LOCALES Y GLOBALES
"""
global_variable = "Python"

def hello_python():
    global_variable = "JS"
    print(f"Hello, {global_variable}!")
hello_python()

print(f"Hello, {global_variable}!")

"""
EXTRA (Fizz Buzz)
"""

def extra(palabra1,palabra2):
    numeros = 0
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(palabra1 + " y tambien " + palabra2)
        elif i % 3 == 0:
            print(palabra1)
        elif i % 5 == 0:
            print(palabra2)
        else:
            numeros += 1
    print(f"Cantidad de numeros dedl 1 al 100 que no son multiplos de 3 ni de 5: {numeros}")
    
extra("multiplo de 3","multiplo de 5") 
