# Funciones (bloque de codigo para reutilizarlo 

"""
Funciones definidas por el usuario
"""
#simple 

def saludo():
    print("Hola, bienvenido a la funcion saludo")

saludo()

#Con retorno

def devolver_saludo():
    return "Hola, bienvenido a la funcion devolver_saludo"

print(devolver_saludo())

#Con argumento

def saludo_personalizado(nombre):
    return f"Hola {nombre}, bienvenido a la funcion saludo_personalizado"

print(saludo_personalizado("Carlos"))


#Con varios argumentos

def saludos_personalizados(nombre,apellido):
    return f"Hola {nombre} {apellido}, bienvenido a la funcion saludos_personalizados" 

print(saludos_personalizados("Carlos", "Sotoia"))


#Con argunmentos predeterminados

def saludo_arg_predeterminado(nombre="Python",apellido="IA"):
    return f"Hola {nombre} {apellido}, bienvenido a la funcion saludo_arg_predeterminado"

print(saludo_arg_predeterminado())

# Con argumentos y retorno

def saludo_arg_retorno(nombre,apellido):
    return f"Hola {nombre} {apellido}, bienvenido a la funcion saludo_arg_retorno"

print(saludo_arg_retorno("Sotoia", "Carlos"))


#Con retorno de varios valores

def multiples_retorno():
    return "Hola" , "Python"

saludo, nombre =multiples_retorno()

print(saludo)
print(nombre)


# Con un numero variable de argumentos

def varios_argumentos_nombre(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}, bienvenido a la funcion varios_argumentos_nombre")

varios_argumentos_nombre("Carlos", "Sotoia", "Python", "IA")


# Con un numero variable de argumentos con clave

def varios_argumentos_clave(**kwargs):  
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

varios_argumentos_clave(nombre="Carlos", apellido="Sotoia", lenguaje="Python", especialidad="IA")



"""
Funciones dentro de funciones
"""

def funcion_externa():
    def funcion_interna():
        print("Esta es la funcion interna")
    funcion_interna()

funcion_externa()


"""
Funciones del lenguaje(built-in)    
"""

print(len("Hola, bienvenido a la funcion len()"))  # Devuelve la longitud de un objeto cuenta el número de elementos que contiene
print(type(123))  # Devuelve el tipo de dato de un objeto
print(max(1, 2, 3, 4, 5))  # Devuelve el valor máximo de una secuencia
print(min(1, 2, 3, 4, 5))  # Devuelve el valor mínimo de una secuencia
print(sum([1, 2, 3, 4, 5]))  # Devuelve la suma de los elementos de una secuencia
print(sorted([5, 2, 3, 1, 4]))  # Devuelve una lista ordenada de los elementos de una secuencia
print(abs(-10))  # Devuelve el valor absoluto de un número
print(round(3.14159, 2))  # Devuelve un número redondeado a un número específico de decimales
print(isinstance(123, int))  # Devuelve True si el objeto es una instancia de la clase especificada
print(dir([]))  # Devuelve una lista de los atributos y métodos de un objeto
print(help(len))  # Muestra la documentación de la función len()
print(eval("2 + 2"))  # Evalúa una expresión y devuelve el resultado
print(all([True, True, False]))  # Devuelve True si todos los elementos de la secuencia son verdaderos
print(any([False, False, True]))  # Devuelve True si al menos un elemento de la secuencia es verdadero
print(bin(10))  # Devuelve la representación binaria de un número
print(oct(10))  # Devuelve la representación octal de un número
print(hex(10))  # Devuelve la representación hexadecimal de un número   
print(chr(65))  # Devuelve el carácter correspondiente al valor Unicode especificado
print(ord("A"))  # Devuelve el valor Unicode correspondiente al carácter especificado
print(repr("Hola"))  # Devuelve una representación de cadena de un objeto
print(str(123))  # Devuelve una representación de cadena de un objeto
print(list((1, 2, 3)))  # Convierte un objeto iterable en una lista
print(tuple([1, 2, 3]))  # Convierte un objeto iterable en una tupla
print(set([1, 2, 3, 3, 2, 1]))  # Convierte un objeto iterable en un conjunto
print(dict([("a", 1), ("b", 2), ("c", 3)]))  # Convierte un objeto iterable en un diccionario
print(reversed([1, 2, 3]))  # Devuelve un iterador que recorre los elementos de una secuencia en orden inverso
print(enumerate(["a", "b", "c"]))  # Devuelve un iterador que devuelve pares de índice y valor de una secuencia
print(zip([1, 2, 3], ["a", "b", "c"]))  # Devuelve un iterador que combina elementos de varias secuencias
print(map(lambda x: x**2, [1, 2, 3, 4, 5]))  # Devuelve un iterador que aplica una función a cada elemento de una secuencia
print(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))  # Devuelve un iterador que filtra los elementos de una secuencia según una función
#print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # Devuelve un valor acumulado aplicando una función a los elementos de una secuencia
print(sum([1, 2, 3, 4, 5]))  # Devuelve la suma de los elementos de una secuencia
print("carlos otoia".upper())  # Devuelve una cadena en mayúsculas
print("CARLOS OTOIA".lower())  # Devuelve una cadena en minúsculas
print("carlos otoia".capitalize())  # Devuelve una cadena con la primera letra en mayúscula
print("carlos otoia".title())  # Devuelve una cadena con la primera letra de cada palabra en mayúscula 
print("carlos otoia".replace("carlos", "Carlos"))  # Devuelve una cadena con las ocurrencias de una subcadena reemplazadas por otra
print("carlos otoia".split())  # Devuelve una lista de subcadenas separadas por espacios
print("carlos otoia".join(["Hola", "mundo"]))  # Devuelve una cadena que es la concatenación de una secuencia de cadenas, separadas por la cadena original


"""
Variables locales y globales
"""

global_variable = "Soy una variable global"

print(f"Variable global: {global_variable}")

def funcion_variable_local():
    global global_variable
    global_variable = "Soy una variable global modificada"
    print(f"Variable global modificada: {global_variable}")

funcion_variable_local()


"""
EXTRA
"""
def print_numeros (text_1, text_2) -> int:
    contador = 0
    for numero in range (1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(text_1, text_2)
        elif numero % 3 == 0:
            print(text_1)
        elif numero % 5 == 0:
            print(text_2)
        else:
            print(numero)
            contador += 1
    return contador
      

print(print_numeros("text_1", "text_2"))    


