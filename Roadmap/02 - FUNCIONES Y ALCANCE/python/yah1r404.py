"""
FUNCIONES DEFINIDAS X EL USUARIO
"""
# SIMPLE

def salu2():
    print("hola, python!")
    
salu2()

# CON RETORNO

def return_salu2():
    return "Hola, python!"

print(return_salu2())

# CON ARGUMENTO

def saludo_name(name):
    print(f"hola, {name}!")

saludo_name("yahir")

# CON ARGUMENTOS

def saludo_name(saludo, nombre):
    print(f"{saludo}, {nombre}")

saludo_name("hola", "yahir!")

# CON ARGUMENTO PREDETERMINADO

def default_arg_saludo(name="python"):
    print(f"Hola, {name}!")

default_arg_saludo("benja")
default_arg_saludo()

# CON ARGUMENTOS Y RETORNO

def jujutsu_kaisen(okkotsu, toji, sukuna):
    return f"{okkotsu}, {toji}, {sukuna}"

print(jujutsu_kaisen("hechicero", "antagonista", "villano"))

# CON RETORNO DE VARIOS VALORES

def multiple_greet_return():
    return "hola", "python"

greet, name = multiple_greet_return()
print(greet)
print(name)

# CON UN NÚMERO VARIABLE DE ARGUMENTOS

def variable_arg_arcane(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_arcane("Vi", "Viktor", "Jinx", "Ecko", "Silco")

# CON UN NÚMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE

def variable_key_arg_arcane(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_arcane(
    Rojo="Vi",
    Castaño="Viktor",
    Azul="Jinx",
    Blanco="Ecko",
    Negro="Silco"
)

"""
FUNCIONES DENTRO DE FUNCIONES
"""

def funcion_externa():
    def funcion_interna():
        print("Función interna: Hola, Pythoooon!")
    funcion_interna()
funcion_externa()

"""
FUNCIONES DEL LENGUAJE PYTHON! (built-in)
"""

# Funciones de tipo y longitud
print(len("quesadilla sin queso"))        # Mide cuántos caracteres tiene el string
print(type(99999))                        # Devuelve el tipo de dato del valor

# Métodos de strings (no son built-in globales, pero sí muy usados)
print("quesadilla sin queso".upper())    # Convierte el string a mayúsculas
print("QUESADILLA CON QUESO".lower())    # Convierte el string a minúsculas
print("   hola mundo   ".strip())        # Elimina espacios al principio y final
print("quesadilla con queso".replace("con", "sin")) # Reemplaza parte del string
print("queso,pan,tomate".split(","))     # Separa un string por comas

# Funciones numéricas
print(abs(-25))                          # Valor absoluto
print(round(3.14159, 2))                 # Redondea con 2 decimales
print(pow(2, 3))                         # Potencia: 2^3

# Conversión de tipos
print(int("5"))                          # Convierte string a entero
print(str(100))                          # Convierte número a string
print(float("3.14"))                     # Convierte string a float
print(bool(0))                           # Devuelve False porque 0 es considerado "falsy"

# Funciones sobre colecciones
print(max([3, 7, 1]))                    # Mayor valor
print(min([3, 7, 1]))                    # Menor valor
print(sum([1, 2, 3, 4]))                 # Suma de todos los elementos
print(sorted([3999, 119, 40, 221]))              # Ordena los elementos

# Funciones útiles varias
print(chr(65))                           # Convierte número a letra según ASCII (65 = 'A')
print(ord('A'))                          # Convierte letra a su número ASCII

"""
VARIABLES LOCALES Y GLOBALES
"""
global_var = "I am global"

def scope_example():
    local_var = "I am local"
    print(global_var)   # Accessing global inside function
    print(local_var)
scope_example()
print(global_var)

"""
EJERCICIO EXTRA
"""

def extra_func(extra_1, extra_2)->int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(extra_1 + extra_2)       
        elif i % 3 == 0:
            print(extra_1)
        elif i % 5 == 0:
            print(extra_2)
        else:
            print(i)
            count += 1
    return count

print(extra_func("Fizz", "Buzz"))
