
#1

"""
Funciones Definidas por el Usuario
"""


# Simple

def saludo(): # Definición de la función por medio de la palabra reservada def
    print("Hola, Python!") # Bloque de código que pertenece a la función que imprime un saludo

saludo() # Llamada a la función para que se ejecute el bloque de código que contiene y de esta forma evitar la repetición de código


# Con retorno

def return_saludo(): # Definición de la función por medio de la palabra reservada def
    return "Hola, Python!" # Bloque de código que pertenece a la función que retorna un saludo
return_saludo() # Llamada a la función pero como no hay un print no se muestra nada en la terminal

# A) Buscamos que se muestre en la terminal creando una variable y asignándole el retorno de la función
saludo = return_saludo() # Llamada a la función pero como no hay un print no se muestra nada en la terminal
print (saludo) # Se imprime la variable saludo que contiene el retorno de la función return_saludo

# B) Buscamos que se muestre en la terminal agregando un print a la llamada de la función
print(return_saludo()) # Se imprime directamente el retorno de la función return_saludo sin necesidad de crear una variable intermedia


# Con un Argumento

def arg_saludo(nombre): # Definición de la función por medio de la palabra reservada def y un argumento llamado nombre. Un argumento es un parámetro que se pasa a la función para que esta lo utilice en su bloque de código
    print (f"Hola, {nombre}!") # Bloque de código que pertenece a la función que imprime un saludo personalizado con el argumento nombre
arg_saludo("Loyle") # Llamada a la función con el argumento "Loyle" que se pasa a la función para que esta lo utilice en su bloque de código

# Con Argumentos

def args_saludo(nombre, apellido): # Definición de la función por medio de la palabra reservada def y dos argumentos llamados nombre y apellido.
    print (f"Hola, {nombre} {apellido}!") # Bloque de código que pertenece a la función que imprime un saludo personalizado con los argumentos nombre y apellido
args_saludo("Loyle", "Carner") # Llamada a la función con los argumentos "Loyle" y "Carner" que se pasan a la función para que esta los utilice en su bloque de código
args_saludo(apellido = "Carner", nombre = "Loyle") # Llamada a la función con los argumentos "Loyle" y "Carner" pero en diferente orden. Al usar los nombres de los argumentos, no importa el orden en que se pasen ya que la función los reconocerá por su nombre


# Con un Agumento Predeterminado

def defaul_arg_saludo(nombre = "Python"): # Definición de la función por medio de la palabra reservada def y un argumento llamado nombre con un valor predeterminado "Python". Si no se pasa ningún valor al llamar a la función, se utilizará el valor predeterminado.
    print (f"Hola, {nombre}!") # Bloque de código que pertenece a la función que imprime un saludo personalizado con el argumento nombre
defaul_arg_saludo() # Llamada a la función sin pasar ningún valor, por lo que se utilizará el valor predeterminado "Python"
defaul_arg_saludo("Loyle") # Llamada a la función pasando el valor "Loyle", por lo que se utilizará este valor en lugar del valor predeterminado


# Con Argumentos y Retorno

def args_return_saludo(nombre, apellido): # Definición de la función por medio de la palabra reservada def y dos argumentos llamados nombre y apellido. 
    return f"Hola, {nombre} {apellido}!" # Bloque de código que pertenece a la función que retorna un saludo personalizado con los argumentos nombre y apellido
print (args_return_saludo("Loyle", "Carner")) # Llamada a la función con los argumentos "Loyle" y "Carner" que se pasan a la función para que esta los utilice en su bloque de código y se imprime el retorno de la función


# Con Retorno de varios Valores

def varios_return(): # Definición de la función por medio de la palabra reservada def
    return "Loyle", "Carner", 25 # Bloque de código que pertenece a la función que retorna varios valores: dos cadenas de texto y un número entero

nombre, apellido, edad = varios_return() # Llamada a la función y asignación de los valores retornados a las variables saludo, apellido y edad
print (nombre) # Se imprime la variable saludo que contiene el primer valor retornado por la función varios_return
print (apellido) # Se imprime la variable apellido que contiene el segundo valor retornado por la función varios_return
print (edad) # Se imprime la variable edad que contiene el tercer valor retornado por la función varios_return

print (f"{saludo} {apellido} tiene {edad} años.") # Se imprime un mensaje personalizado con los valores retornados por la función varios_return


# Con un número variable de Argumentos

def variable_arg_saludo(*nombres): # Definición de la función por medio de la palabra reservada def y un número variable de argumentos llamado nombres. El asterisco (*) indica que se pueden pasar varios argumentos y que estos se almacenarán en una tupla.
    for nombre in nombres: # Bucle for que itera sobre cada nombre en la tupla nombres
        print (f"Hola, {nombre}!") # Bloque de código que pertenece a la función que imprime un saludo personalizado con cada nombre en la tupla nombres

variable_arg_saludo("Loyle", "Carner", "Python", "Retos Moure") # Llamada a la función con varios argumentos que se pasan a la función y se almacenan en la tupla nombres


# Con un número variable de Argumentos con Palabra Clave

def variable_key_arg_saludo(**nombres): # Definición de la función por medio de la palabra reservada def y un número variable de argumentos con palabra clave llamado nombres. El doble asterisco (**) indica que se pueden pasar varios argumentos con palabra clave y que estos se almacenarán en un diccionario.
    for clave, valor in nombres.items(): # Bucle for que itera sobre cada par clave-valor en el diccionario nombres
        print (f"{valor} ({clave})!") # Bloque de código que imprime un saludo personalizado con cada nombre y su correspondiente parámetro en el diccionario nombres

variable_key_arg_saludo (primer_nombre = "Loyle", primer_apellido = "Carner", lenguaje = "Python", curso = "Retos Moure") # Llamada a la función con varios argumentos con palabra clave que se pasan a la función y se almacenan en el diccionario nombres



#2

"""
Funciones Definidas por el Usuario
"""

def outer_function(): # Definición de la función por medio de la palabra reservada def
    print("Esta es la función externa.") # Bloque de código que pertenece a la función outer_function que imprime un mensaje indicando que es la función externa

    def inner_function(): # Definición de una función interna por medio de la palabra reservada def
        print("Esta es la función interna.") # Bloque de código que pertenece a la función inner_function que imprime un mensaje indicando que es la función interna

    inner_function() # Llamada a la función interna para que se ejecute el bloque de código que contiene que no puede llamarse porque su ámbito está limitado a la función externa
outer_function() # Llamada a la función externa para que se ejecute el bloque de código que contiene, incluyendo la llamada a la función interna. La función interna no puede ser llamada desde fuera de la función externa, ya que su ámbito está limitado a la función externa.



#3

"""
Funciones del Lenguaje (Built-in Functions)
"""

print("Hola, Python!") # Función print() que imprime un mensaje en la terminal
print(len("Hola, Python!")) # Función len() que devuelve la longitud de una cadena de texto
print(type("Hola, Python!") ) # Función type() que devuelve el tipo de dato de una variable o valor
print(int("25")) # Función int() que convierte una cadena de texto en un número entero
print(float("25.5")) # Función float() que convierte una cadena de texto en un número decimal
print(str(25)) # Función str() que convierte un número en una cadena de texto
print(list((1, 2, 3))) # Función list() que convierte una tupla en una lista
print(tuple([1, 2, 3])) # Función tuple() que convierte una lista en una tupla
print(dict(nombre="Loyle", apellido="Carner")) # Función dict() que crea un diccionario a partir de pares clave-valor
print(set([1, 2, 3, 3, 2, 1])) # Función set() que crea un conjunto a partir de una lista, eliminando los elementos duplicados
print(sum([1, 2, 3, 4, 5])) # Función sum() que devuelve la suma de los elementos de una lista
print(max([1, 2, 3, 4, 5])) # Función max() que devuelve el valor máximo de una lista
print(min([1, 2, 3, 4, 5])) # Función min() que devuelve el valor mínimo de una lista
print(round(25.5678, 2)) # Función round() que redondea un número decimal a un número específico de decimales
print(abs(-25)) # Función abs() que devuelve el valor absoluto de un número entero o decimal
print(sorted([5, 2, 3, 1, 4])) # Función sorted() que devuelve una lista ordenada a partir de una lista desordenada
print(reversed([1, 2, 3, 4, 5])) # Función reversed() que devuelve un iterador que invierte el orden de una lista
print(enumerate(["Loyle", "Carner", "Python"])) # Función enumerate() que devuelve un iterador que genera pares índice-valor a partir de una lista
print(zip(["Loyle", "Carner"], [25, 30])) # Función zip() que devuelve un iterador que agrupa elementos de dos o más listas en tuplas
print(all([True, True, False])) # Función all() que devuelve True si todos los elementos de una lista son True, de lo contrario devuelve False
print(any([True, False, False])) # Función any() que devuelve True si al menos un elemento de una lista es True, de lo contrario devuelve False
print(chr(65)) # Función chr() que devuelve el carácter correspondiente a un código ASCII entero
print(ord("A")) # Función ord() que devuelve el código ASCII entero correspondiente a un carácter
print(bin(10)) # Función bin() que convierte un número entero en su representación binaria
print("Hola, Python!".upper()) # Método upper() que convierte una cadena de texto a mayúsculas
print("Hola, Python!".lower()) # Método lower() que convierte una cadena de texto a minúsculas
print("Hola, Python!".replace("Python", "Mundo")) # Método replace() que reemplaza una subcadena por otra en una cadena de texto
print("Hola, Python!".split()) # Método split() que divide una cadena de texto en una lista de palabras
print(" ".join(["Hola", "Python!"])) # Método join() que une una lista de palabras en una cadena de texto separada por un espacio
print("   Hola, Python!   ".strip()) # Método strip() que elimina los espacios en blanco al inicio y al final de una cadena de texto
print("   Hola, Python!   ".lstrip()) # Método lstrip() que elimina los espacios en blanco al inicio de una cadena de texto
print("   Hola, Python!   ".rstrip()) # Método rstrip() que elimina los espacios en blanco al final de una cadena de texto
print("Hola, Python!".find("Python")) # Método find() que devuelve el índice de la primera aparición de una subcadena en una cadena de texto, o -1 si no se encuentra
print("Hola, Python!".count("o")) # Método count() que devuelve el número de apariciones de una subcadena en una cadena de texto
print("Hola, Python!".startswith("Hola")) # Método startswith() que devuelve True si una cadena de texto comienza con una subcadena específica, de lo contrario devuelve False
print("Hola, Python!".endswith("Python!")) # Método endswith() que devuelve True si una cadena de texto termina con una subcadena específica, de lo contrario devuelve False



#3

"""
Variables Locales y Globales
"""

global_variable = "Soy una variable global" # Variable global que puede ser accedida desde cualquier parte del código
print(global_variable) # Se imprime la variable global

def hello_python(): # Definición de la función por medio de la palabra reservada def
    local_variable = "Soy una variable local" # Variable local que solo puede ser accedida dentro de la función
    print(local_variable) # Bloque de código que pertenece a la función que imprime la variable local
    print (f"Hola, {global_variable}!") # Bloque de código que pertenece a la función que imprime un saludo personalizado con la variable global
    hello_python() # Llamada a la función para que se ejecute el bloque de código que contiene
    # Tener en cuenta que si intentamos acceder a la variable local desde fuera de la función, obtendremos un error ya que su ámbito está limitado a la función y que debemos determinar si una variable debe ser local o global según el uso que le vayamos a dar en nuestro código y evitar en la medida de lo posible el uso de variables globales para evitar conflictos y errores en nuestro código a no ser que sea estrictamente necesario.



#4

"""
EXTRA
"""

def print_numeros (text_1, text_2) -> int: # Definición de la función por medio de la palabra reservada def, dos argumentos llamados text_1 y text_2 y una anotación de tipo que indica que la función retorna un valor de tipo entero
    count = 0 # Variable local que se utiliza para contar el número de iteraciones del bucle
    for number in range (1, 101): # Bucle for que itera sobre un rango de números del 1 al 100
        if number % 3 == 0 and number % 5 == 0: # Condicional elif que verifica si el número es múltiplo de 3 y de 5
            print (text_1 + text_2) # Bloque de código que pertenece a la función que imprime la concatenación de los dos textos si el número es múltiplo de 3 y de 5
        elif number % 3 == 0: # Condicional if que verifica si el número es múltiplo de 3
            print (text_1) # Bloque de código que pertenece a la función que imprime el primer texto si el número es múltiplo de 3
        elif number % 5 == 0: # Condicional elif que verifica si el número es múltiplo de 5
            print (text_2) # Bloque de código que pertenece a la función que imprime el segundo texto si el número es múltiplo de 5
        else:
            print (number) # Bloque de código que pertenece a la función que imprime cada número en el rango
            count += 1 # Incremento de la variable count en 1 cada vez que imprima un número y no uno de los textos
    return count # Retorno de la variable count que indica el número de números impresos

print (print_numeros ("Fizz", "Buzz")) # Llamada a la función con los textos "Fizz" y "Buzz" que se pasan a la función para que esta los utilice en su bloque de código y se imprime el retorno de la función que indica el número de números impresos