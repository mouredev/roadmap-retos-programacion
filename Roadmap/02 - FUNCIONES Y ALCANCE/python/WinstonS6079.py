"""Funciones definidas por el usuario"""

#Simple
def saludar():
    print("Hola, ¿cómo estás?")

saludar()


#Función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("La suma es:", resultado)


#Función con un argumento
def saludar_persona(nombre):
    print(f"Hola, {nombre}, ¿cómo estás?")

saludar_persona("Winston")


#Función con múltiples argumentos
def presentar_persona(nombre, edad):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")

presentar_persona("Winston", 30)


#Función con un argumento por defecto
def default_saludo(nombre="Winston"):
    print(f"Hola, {nombre}, ¿cómo estás?")

default_saludo()  # Usa el valor por defecto
default_saludo("Ana")  # Usa el valor proporcionado


#Función con argumento y retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print("La multiplicación es:", resultado)


#Función con retorno de múltiples valores
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = operaciones(10, 5)
print("La suma es:", resultado_suma)
print("La resta es:", resultado_resta)


#Función con argumentos variables
def saludar_varios(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}, ¿cómo estás?")
saludar_varios("Winston", "Ana", "Luis")


#Función con argumentos de palabra clave
def saludar_varios(**nombres):
    for key,value in nombres.items():
        print(f"{value}, ({key})!")

saludar_varios(
    language="Python",
    nombre="Yair",
    alias="WinstonS6079",
    edad=30,
)

#Función anidada
def funcion_externa(x):
    def funcion_interna(y):
        print(f"La suma es: {x + y}")
    return funcion_interna
funcion_externa(5)(3)  # Llama a la función interna con el valor 3


"""Funciones del lenguaje (built-in functions)"""

print(len("Hola, mundo!"))  # Devuelve la longitud de la cadena
print(type(42))  # Devuelve el tipo de dato del número
print(max([1, 2, 3, 4, 5]))  # Devuelve el valor máximo de la lista
print(min([1, 2, 3, 4, 5]))  # Devuelve el valor mínimo de la lista
print(sum([1, 2, 3, 4, 5]))  # Devuelve la suma de los elementos de la lista
print(sorted([5, 3, 1, 4, 2]))  # Devuelve una lista ordenada
print(abs(-10))  # Devuelve el valor absoluto del número
print(round(3.14159, 2))  # Redondea el número a 2 decimales
print(str(42))  # Convierte el número a una cadena
print(int("42"))  # Convierte la cadena a un número entero
print(float("3.14"))  # Convierte la cadena a un número de punto flotante
print(list("Hola"))  # Convierte la cadena en una lista de caracteres


"""Variables locales y globales"""

global_var = "Soy una variable global"
def hola_var():
    local_var = "Hola"
    print(f"{local_var}. {global_var}")  

hola_var()

print(global_var)  
#print(local_var) # Esto generaría un error porque local_var no está definida fuera de la función


