"""
Funciones definidas por el usuario
"""

def saludo():
    print("Hello world")

saludo()

def devuelve_saludo():
    return "Hola Python"

print(devuelve_saludo())

def arg_saludo(greet,name):
    print(f"{greet}, {name}")
    

arg_saludo("Hola", "Leo")
arg_saludo(name="Rafa", greet="Hola")

def default_arg_agree(name="Leonardo"):
    print(f"Hola, {name}")
    
default_arg_agree()

def arg_saludos(greet,name):
    return f"{greet}, {name}"

print(arg_saludos("Hi", "Leo"))


def multiple_return_greet():
    return "Hi", "Pyth0n"

greet, name = multiple_return_greet()

print(greet, name)

#Con un numero varaible de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"hola, {name}")

variable_arg_greet("Leo", "Arthur", "Messi")

#Con un numero varaible de argumentos (Palabra clave)

def variable_arg_greet_key(**names):
    for param, name in names.items():
        print(f"hola, {name} ({param})")

variable_arg_greet_key(
    language="Python",
    name="Leo", 
    second_name="Arthur", 
    age=22
)

# Funcion dentro de funcion

def outer_function():
    def inner_function():
        print("Desde la funcion interna")
    inner_function()
    print("Desde la funcion de fuera")

outer_function()

# Funciones ya existentes del lenguaje

print("La funcion de impresión por el terminal")
funcion_len = len("Leonardo")
print(funcion_len)
print(type("Leo"))
print("LEONARDO".lower())

"""
Variables locales y globales
"""

global_var = "python"
print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")

#hello_python(local_var) No funciona por lo que no se puede acceder a la variable local fuera de la funcion

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def text_to_number(word_1,word_2) -> int:
    j=0
    for i in range (100):
        if i%3 == 0 and i%5 == 0:
            print (word_1+word_2)
        elif i%3 == 0:
            print(word_1)
            print()
        elif i%5 == 0:
            print(word_2)
            print()
        else:
            print(i)
            j+=1
    return j
    


print(text_to_number("Leo","nardo"))


