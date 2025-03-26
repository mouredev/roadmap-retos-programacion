"""
Funciones básicas
"""

# Simples

def saludar():
    print("Saludos, Python")
    
saludar()

# Con retorno

def sumar():
    return 2 + 2

resultado = sumar() # Guardar el retorno en variable
print(resultado)

# Con argumento
def saludo_argumento(nombre):
    print(f"Hola, {nombre}")

saludo_argumento("Juanma")

# Con argumento con valor por defecto
def resta_argumento(num = 10, num2 = 5):
    print(f"Resultado de {num} - {num2} = {num - num2}")

resta_argumento()

# Con argumentos y retorno
def suma_argumentos(num = 10, num2 = 5):
    return f"La suma de {num} + {num2} = {num + num2}"

suma = suma_argumentos()
print(suma)

# Funciones con número variable de argumentos

def saludo_argumentos_variables(*args):
    for nombre in args:
        print(f"Hola, {nombre}")

saludo_argumentos_variables("Juanma", "Maria", "David")

# Con número variable de argumentos y palabra clave
def saludo_argumentos_variables_key(**args):
    for parametro, nombre in args.items():
        print(f"{nombre} ({parametro})")

saludo_argumentos_variables_key(lenguage = "Python", 
                            nombre = "juanma", 
                            alias = "juanmax2"
                            )


"""
Funciones dentro de funciones
"""

def funcion_externa():
    def funcion_interna(): # Crear función interna
        print("Hola, Python")
    funcion_interna() # Llamar función interna 

funcion_externa()

"""
Funciones del lenguaje (built - in)
"""
# Funcion encargada de imprimir
print("Juanma")
# Retorna un entero con la longitud
print(len("Juanma"))
# Retorna el tipo de la variable
print(type(5))

"""
Variables: Locales y Globales
"""

variable_global = "Python"

def hello_python():
    variable_local = "Hola" # Esta variable solo funciona dentro de la funcón
    print(f"{variable_local}, {variable_global}")

hello_python()

"""
Dificultad extra
"""
'''
Crea una función que reciba dos parámetros 
de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
'''

def print_numeros(texto1, texto2):
    count = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + " " + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            count += 1
    return count
contador = print_numeros("Hola, Juanma", "Adiós, Juanma")
print(f"El número de veces que ha impreso un número es: {contador}")
