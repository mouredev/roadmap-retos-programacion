print("FUNCIONES EN PYTHON")

print("1.1 Funciones simples")

def saludar():
    print("Hola, ¿cómo estás?")
    
saludar()

print("1.2 Funciones con retorno")
def obtener_nombre():
    return "jjgoco"

print("El nombre es:", obtener_nombre())

print("1.3 Funciones con argumentos")
def saludar_persona(saludar, nombre):
    print(f"{saludar}, {nombre}!")

saludar_persona(saludar="Hola", nombre="jjgoco")

print("1.4 Funciones con argumentos y retorno")
def saludar_persona_con_retorno2(saludar, nombre):
    return f"{saludar}, {nombre}!"

mensaje = saludar_persona_con_retorno2(saludar="Hola", nombre="jjgoco")
print(mensaje)

print("1.5 Funciones con retorno de varios valores")
def saludo():
    return "Hola", "jjgoco"

print(saludo())

def saludo():
    return "Hola", "jjgoco"

saludo, nombre = saludo()
print(saludo, nombre)

print("1.6 Funciones con argumentos variables")
def saludar_varios(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")
        
saludar_varios("jjgoco", "Juan", "María")

print("1.7 Funciones con argumentos por palabra clave")
def saludar_persona_con_kw(**nombres):
    for kw, value in nombres.items():
        print(f"{value} ({kw})")
        
saludar_persona_con_kw(
    saludo="Hola", 
    nombre="jjgoco",
    edad=33
)

print("1.8 Funciones con funciones dentro")
def funcion_externa(): 
    def funcion_interna():
        print("Función interna")
    funcion_interna()
funcion_externa()

print("1.9 Funciones de Python")
print("1.9.1 'len()': len('jjgoco') =", len("jjgoco"))
print("1.9.2 'type()': type(33) =", type(33))
print("1.9.3 'str()': str(33) =", str(33))
print("1.9.4 'int()': int('33') =", int("33"))
print("1.9.5 'upper()': 'jjgoco'.upper() =", "jjgoco".upper())
print("_" * 40)

print("VARIABLES LOCAL Y GLOBALES")
global_variable = "jjgoco"

def funcion_con_variables():
    local_variable = "Juan"
    print(f"Variable global: {global_variable}")
    print(f"Variable local: {local_variable}")

funcion_con_variables()

print("_" * 40)
print("EJERCICIO EXTRA")
print(" * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número. \
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que: \
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro. \
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro. \
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas. \
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. \
 * \
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.")

def imprimir_numeros(param1, param2)-> int:
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1 + " y " + param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
            contador += 1
    return contador
print(imprimir_numeros("Múltiplo de 3", "Múltiplo de 5"))