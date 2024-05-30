"""
Tipos de funciones
"""

print("\n ---- Tipos de funciones ----\n")

# Sin parámetros ni retorno
def no_param_no_return():
    # Function body
    print("Hola! soy una función sin parámetros ni retorno.")

no_param_no_return()

# Con retorno  
def retorno():
    # Function body
    print("Hola! soy una función con retorno, y te devuelvo un 5")
    return 5

print(retorno())

# Con un parámetro SIN retorno
def saludo(nombre):
    # Function body
    print(f"Hola! soy una función con un parámetro, y te saludo a ti, {nombre}")

saludo("Worlion")

# Con un parámetro predeterminado
def saludoDef(nombre="Worlion"):
    # Function body
    print(f"Hola! soy una función con un parámetro POR DEFECTO ('Worlion'), y te saludo a ti, {nombre}")
    
saludoDef()
saludoDef("Juan")

# Con parámetros y retorno
def suma(a, b):
    # Function body
    print("Hola! soy una función con parámetros y retorno, y te devuelvo la suma de los dos parámetros")
    return a + b

print(suma(2, 3))

#retorno multiple
def return_args_greet():
    return "Hola", "Worlion"

print(return_args_greet())

saludo, nombre = return_args_greet()
print(saludo)
print(nombre)

#Con nume3ro variable de argumentos
def variable_arg_saludo(*nombres):
    for nombre in nombres:
        print (f"Hola, {nombre}!")
        
variable_arg_saludo("Worlion", "Mou", "Pepito", "Peña")

# Con un número variable de argumentos con palabra clave


def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f" - {key} = {value}!")


variable_key_arg_greet(
    language="Python",
    name="Imanol",
    alias="Worlion",
    age=40
)

"""
Funciones dentro de funciones
"""

print("\n ---- Funciones dentro de funciones ----\n")

def funcionExterna():
    def funcionInterna():
        print(" - Soy una función interna")
    print("Soy una función externay voy a llamar a la interna:")

    funcionInterna()
    
funcionExterna()

"""
Funciones predefinidas del lenguaje
"""
print("\n ---- Funciones definidas en el lenguaje ----\n")

name = "Worlion"
print(f"len: {len(name)}")
array = [10, 52, 32, 14, 25]
print(f"max: {max(array)}")

"""
variable LOCAL y GLOBAL
"""

print("\n ---- Variable local y global ----\n")
var_global = "Worlion"

def funcion():
    var_local = "Python"
    print(f"Variable local: {var_local}")
    print(f"Variable global: {var_global}")
    
print("aqui puedo usar la variable global: ", var_global)
print("aqui NO puedo usar la variable local:  :(")

"""
DIFICULTAD EXTRA (opcional)
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

def funcionExtra(text1, text2):
    count = 0;
    def multiplo(a, b):
        return a % b == 0
        
    for i in range(1,100):
        if(multiplo(i, 3) and multiplo(i,5)):
            print(text1 + text2)
        elif(multiplo(i,3)):
            print(text1)
        elif(multiplo(i,5)):
            print(text2)
        else:
            print(i)
            count += 1
    
    return count;
        
print("total: " + str(funcionExtra("chori", "pan"))  )
            
    