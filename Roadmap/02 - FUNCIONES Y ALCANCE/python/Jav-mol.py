" --- Funciones --- "

# Funcion sin parametros ni retornos
def funcion_simple():
    print('Esta es una funcion simle')
    
funcion_simple()

# Funcion con parametros
def saludar(nombre: str):
    print(f"Hola, me llamo {nombre}")

saludar('Javier')

# Funcion con varios parametros
def saludar2(nombre: str, edad: int):
    print(f"Hola, mi nombre es {nombre} y tengo {edad} años")

saludar2('Javier', 22)

# Funcion con retorno

def sumar(n1: int, n2: int) -> int:
    return n1 + n2

resultado = sumar(4,2)
print(resultado)

# Pasando una lista como argumento
def lenguajes(lista: list):
    for lenguaje in lista:
        print(f'Es un lenguaje de programacion: {lenguaje}')

lenguajes(["JavaScript", "Java", "Php", "Python", "Go"])

# Parámetros arbitrarios, *args
def ultimaPersona(*personas):
    print(f"La última persona que vino fue {personas[-1]}")

ultimaPersona('Javier', 'Valentina', 'Nicolas', 'Camila')

# Parámetros arbitrarios con keyword
def datos_personales(**datos):
    print(f"Nombre: {datos['nombre']} - Edad: {datos['edad']} - Pais: {datos['pais']}")
    
datos_personales(
    nombre = 'Javier',
    edad = 22,
    pais = 'Argentina'
)

# Funciones dentro de funciones



# Funciones del lenguaje
print(len("Argentina"))
print(type(2.34))
print("JavierMolina".upper())

# Variables locales y globales debtro de funciones
variable_global = 'Variable Global'

def variables():
    variable_local = 'Variable Local'
    def other_function():
        variable_local2 = 'Other Function'
        print(f"{variable_global} - {variable_local} - {variable_local2}")
    
    return other_function()
        
#print(variable_global, variable_local, variable_local2) No se pueden imprimir las variables locales      
        
variables()

""" --- EJERCICIO EXTRA --- """

def mi_funcion(text_1: str, text_2: str) -> int:
    
    num_impresos = 0
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"Numero: {num} - {text_1} - {text_2}")
        
        elif num % 3 == 0:
            print(f"Numero: {num} - {text_1}")

        elif num % 5 == 0:
            print(f"Numero: {num} - {text_2}")
        
        else:
            num_impresos += 1
            print(num)
    return f"Los numeros se han impreso: {num_impresos} veces"

print(mi_funcion('Mult-3','Mult-5')) 