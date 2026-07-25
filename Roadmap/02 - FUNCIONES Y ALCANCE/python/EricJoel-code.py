# Funciones

# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define usando la palabra clave 'def', seguida del nombre de la función y paréntesis.

# Funciones definidas por el usuario

# Simple

def saludar():
    print("Hola, Python!")
    
saludar() # Llamada a la función

# Funcion con retorno

def retorno():
    return "Hola, mundo!"

mensaje = retorno()
print(mensaje)

# Función con parámetros

def sumar(a, b):
    return a + b

resultado = sumar(8, 9)
print(resultado)

# Función con parámetros por defecto

def nuevo_saludo(nombre="Eric"):
    print(f"Hola, {nombre}!")
    
nuevo_saludo() # Usa el valor por defecto
nuevo_saludo("Joel") # Sobrescribe el valor por defecto

# Funcion con retorno de varios valores

def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(10, 5)
print(f"Suma: {s}, Resta: {r}")

# Funciones con un numero variable de argumentos

def lista_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
        
lista_nombres("Eric", "JoelDev", "Python")

# Funciones con un numero de argumentos con palabra clave

def info_persona(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
        
info_persona(nombre="Eric", edad=30, ciudad="Brasil") 

# Funciones dentro de funciones

def externa():
    def interna():
        print("Funcion interna")
    interna()
    
externa()

# Funciones del lenguaje

print(len("Hola")) # Devuelve la longitud de una cadena
print(type(123)) # Devuelve el tipo de dato
print(isinstance(123, int)) # Verifica si un objeto es de un tipo específico
print(dir([])) # Devuelve los atributos y métodos de un objeto
print(help(str)) # Muestra la documentación de un objeto
print(abs(-10)) # Devuelve el valor absoluto
print(round(3.14159, 2)) # Redondea un número a un número específico de decimales
print(max(1, 5, 3)) # Devuelve el valor máximo
print(min(1, 5, 3)) # Devuelve el valor mínimo
print(sum([1, 2, 3, 4, 5])) # Suma los elementos de un iterable
print(sorted([3, 1, 4, 2])) # Devuelve una lista ordenada
print(reversed([1, 2, 3])) # Devuelve un iterador que invierte un iterable
print(enumerate(['a', 'b', 'c'])) # Devuelve un objeto enumerado

print("joel".upper()) # Convierte a mayúsculas
print("JOEL".lower()) # Convierte a minúsculas
print("  hola  ".strip()) # Elimina espacios en blanco al inicio y final
print("hola mundo".replace("mundo", "Python")) # Reemplaza una subcadena
print("hola mundo".split()) # Divide una cadena en una lista
print(" ".join(["Hola", "Python"])) # Une una lista en una cadena 
print(chr(65)) # Convierte un código ASCII a un carácter
print(ord('A')) # Convierte un carácter a su código ASCII
print(bin(10)) # Convierte un número a binario
print(hex(255)) # Convierte un número a hexadecimal
print(oct(8)) # Convierte un número a octal

# Variable local y global

a = "global"

def funcion():
    b = "local"
    print(a) # Accede a la variable global
    print(f"{a},{b}") # Accede a la variable global y local 
    
funcion()

print(a) # Accede a la variable global, se puede acceder desde fuera de la funcion
#print(b) # Error, b es una variable local, no se puede accerder desde fuera de la funcion

# Extra

def ejemplo(a, b) -> int:
    contador = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(a + b)
        elif number % 5 == 0:
            print(b)
        elif number % 3 == 0:
            print(a)
        else:
            print(number)
            contador += 1
    return contador

print(ejemplo("team","seal"))


    