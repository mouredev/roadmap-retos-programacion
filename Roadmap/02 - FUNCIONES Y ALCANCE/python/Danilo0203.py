# 📌 FUNCIONES BASICA

# Funciones simples
print("====== Funciones simples ======")
def saludar():
    print("Hola, Python")


saludar()


# Funciones con retorno
print("\n====== Funciones con retorno ======")
def return_saludar():
    return "Hola, Python"


print(return_saludar())


# Funciones con argumentos y parametros
print("\n====== Funciones con argumentos y parametros ======")
def arg_saludo(nombre):
    print(f"Hola, {nombre}!")


arg_saludo("Danilo")


def args_saludos(saludo, nombre):
    print(saludo, nombre)


args_saludos("Hola", "Mundo")

# Orden en los argumentos de las funciones
args_saludos(nombre="Mundo", saludo="Hola")


# Funcion con Argumentos prederterminados
print("\n====== Funciones con Argumentos prederterminados ======")
def default_arg_saludo(nombre="usuario"):
    print(f"!Hola, {nombre}¡")


default_arg_saludo()


# Funcion con argumentos y retorno
print("\n====== Funciones con Argumentos y retorno ======")
def return_args_saludar(saludo, nombre):
    return f"{saludo}, {nombre}"


print(return_args_saludar("Hola", "Danilo y Python"))


# Funcion con retorno de varios valores
print("\n====== Funciones con retorno de varios valores ======")
def multiple_return_saludo():
    return "Hola", "retorno de varios valores"


saludo, nombre = multiple_return_saludo()
print(saludo)
print(nombre)

# Funciones con un numero variable de argumentos
print("\n====== Funciones con un numero variable de argumentos ======")
def variable_arg_saludo(*names):
    for name in names:
        print(f"Hola, {name}")


variable_arg_saludo("Danilo", "Estuardo", "Calderon", "Barrios")

# Funciones con un numero de variables de argumentos con palabra clave
print(
    "\n====== Funciones con un numero de variables de argumentos con palabra clave ======"
)
def variable_key_arg_saludo(**names):
    for key, name in names.items():
        print(f"Hola, {name} ({key})")


variable_key_arg_saludo(nombre ="Danilo", nombre2= "Estuardo", apellido= "Calderon", apellido2="Barrios")

# Funciones dentro de Funciones
print("\n====== Funciones dentro de Funciones ======")
def funcion_afuera():
    def funcion_adentro():
        print('Funcion interna: Hola Phyton!')
    funcion_adentro()

funcion_afuera()

# Funciones propias del Lenguaje
print("\n====== Funciones propias del lenguaje ======")
print('print() --> es una funcion propia del lenguaje python')
print(f'len() es una funcion propia: {len('Hola')}')
print(f'type() es una funcion propia: {type('Hola')}')

# Variables Globales y Locales
print("\n====== Variables Globales y Locales ======")

variable_global = 'Variable global'
print(variable_global)

def bloque_local():
    variable_local = 'Variable Local'
    print(f'Hola, {variable_global} y {variable_local}')
bloque_local()
# print(variable_local) # Esta variable solo funciona en el bloque de codigo "bloque_local"

""" Extra 
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
print("\n====== EXTRA ======")
def extra (cadena1, cadena2)->int:
    count = 1
    numeros = []
    while(count <= 100):
        if(count % 3 == 0 and count % 5 ==0):
            print(f"{cadena1}{cadena2}, {count}")
        elif(count % 3 == 0):
            print(cadena1, count)
        elif(count % 5 == 0):
            print(cadena2, count)
        else:
            numeros.append(count)
        count+=1
    return len(numeros)

print(extra('hola', 'mundo'))
