#funciones
# Definición de la función  

"""
Una función en Python Y en diferentes LENGUAJES; es un bloque de código reutilizable que ejecuta una tarea específica.
Te permite organizar, reducir la repetición, y hacer tu código más limpio
"""

#📦 Función definida por el usuario

#funciones simples

"""se define con la palabra def, seguida del nombre de la función y paréntesis. Dentro de los paréntesis, puedes definir parámetros que la función puede recibir. Por ejemplo"""

def greet():
    print("Hola, Python")

# Llamada a la función

"""
Para ejecutar la función, simplemente la llamas por su nombre seguido de paréntesis, asi no creas logica demas por asi decirlo, 
es una funcion simple que no recibe parametros ni retorna nada, solo ejecuta una acción, por eso al invocar greet() se imprime "Hola, Python" en la consola en este caso.
Puedes llamar a la función varias veces si lo deseas, y cada vez que lo hagas, se ejecutará el código dentro de la función.
"""

greet()
greet()

#funciones con retorno 

"""Si deseas que una función devuelva un valor, puedes usar la palabra clave return.
 Esto permite que la función devuelva un resultado que puede ser utilizado más adelante en el código.
 Por ejemplo, si quieres que una función devuelva un saludo en lugar de imprimirlo directamente, puedes hacer lo siguiente:"""

def return_greet(): 
    return "Hola de nuevo, Python"  

return_greet()  # Llamada a la función
"""Al llamar a return_greet(), obtienes el valor de retorno "Hola de nuevo, Python". Puedes almacenar este valor en una variable o imprimirlo directamente."""

greeting = return_greet()  # Almacena el valor de retorno en una variable

print(greeting)  # Imprime el saludo almacenado

"""también puedes imprimir el valor de retorno directamente si lo prefieres."""

print(return_greet())

"""aquí puedes ver cómo se utilizan las funciones para obtener y mostrar información de manera más estructurada.
Las funciones te permiten encapsular la lógica y reutilizar el código de manera eficiente, lo que es especialmente útil en proyectos más grandes y complejos."""

#funciones con argumentos

"""Las funciones también pueden aceptar argumentos, que son parámetros que se pasan a la función cuando se llama.
Esto permite que la función realice operaciones con esos parámetros"""


def argumento_greet(name = "Python"): #aquí se define un argumento con un valor por defecto
    print(f"Hola, {name}")

argumento_greet() # Llamada a la función sin argumentos, usa el valor por defecto

"""En este caso, la función argumento_greet toma un argumento name con un valor por defecto de "Python". 
Si no se proporciona un argumento al llamar a la función, se utilizará el valor por defecto."""

argumento_greet("Iván")  # Llamada a la función con otro argumento
argumento_greet("Jessica")  # Llamada a la función con otro argumento

"""En este caso, la función argumento_greet toma un argumento (name) y devuelve un saludo personalizado.
Puedes llamar a la función con diferentes nombres para obtener saludos personalizados."""

#funciones con múltiples argumentos

def argumentos_multiples_greet(greeting="Hola", name="Python"):
    print(f"{greeting}, {name}")


argumentos_multiples_greet(name= "Iván", greeting= "Hola")  # Llamada a la función con múltiples argumentos y tambien a los argumentos es posibles de cambiar el orden siempre que se indique cual es cada uno
argumentos_multiples_greet("Buenos días", "Jessica")  # Llamada a la función con otros argumentos
argumentos_multiples_greet()  # Llamada a la función sin argumentos, usa los valores por defecto

"""En este caso, la función argumentos_multiples_greet toma dos argumentos: greeting y name, ambos con valores por defecto.
Puedes llamar a la función con diferentes combinaciones de argumentos para obtener saludos personalizados."""

#funciones con argumentos y retorno (return)

def return_argumentos_greet(greeting="Hola", name="Python"):
    return f"{greeting}, {name}"

print(return_argumentos_greet(name= "Iván", greeting= "Hola"))  # Llamada a la función con múltiples argumentos y tambien a los argumentos es posibles de cambiar el orden siempre que se indique cual es cada uno
print(return_argumentos_greet("Buenos días", "Jessica"))  # Llamada a la función con otros argumentos
print(return_argumentos_greet())  # Llamada a la función sin argumentos, usa los valores por defecto

"""
En este caso, la función return_argumentos_greet toma dos argumentos: greeting y name, ambos con valores por defecto.
Puedes llamar a la función con diferentes combinaciones de argumentos para obtener saludos personalizados,
 y también puedes almacenar el valor de retorno en una variable o imprimirlo directamente.
 """


#funcion con retorno de varios valores

def return_multiple_values():
    return "Hola", "Python"
# Llamada a la función
greeting, language = return_multiple_values()  # Desempaquetado de valores de retorno
print(greeting)  # Imprime "Hola"
print(language)  # Imprime "Python"
"""
En este caso, la función return_multiple_values devuelve dos valores: un saludo y un lenguaje .
Puedes desempaquetar estos valores en variables separadas al llamar a la función.
Esto es útil cuando necesitas devolver múltiples resultados de una función.
"""

#funciones con un número variable de argumentos
"""A veces, es posible que desees crear una función que acepte un número variable de argumentos.
Puedes lograr esto utilizando el operador *names en la definición de la función.
Esto te permite pasar cualquier cantidad de argumentos a la función, y se unirán en una tupla."""

def variable_arguments_greet(*names):
    for name in names:
        print(f"Hola, {name}!")
# Llamada a la función con un número variable de argumentos

variable_arguments_greet("Iván", "Jessica", "Python")

"""
En este caso, la función variable_arguments_greet utiliza el operador *names para aceptar un número variable de argumentos.
Puedes pasar cualquier cantidad de argumentos a la función, y estos se reciben como una tupla que se procesa individualmente en el bucle.
Esto es útil cuando no sabes cuántos argumentos se pasarán a la función.
"""
#funciones con un número variable de argumentos con nombre clave

"""De manera similar, puedes crear una función que acepte un número variable de argumentos con nombre clave utilizando el operador **kwargs.
Esto te permite pasar cualquier cantidad de argumentos con nombre a la función, y se unirán en un diccionario."""

def variable_keyword_arguments_greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Llamada a la función con un número variable de argumentos con nombre clave

variable_keyword_arguments_greet(name="Iván", greeting="Hola", language="Python")


"""
En este caso, la función variable_keyword_arguments_greet utiliza el operador **kwargs para aceptar un número variable de argumentos con nombre clave.
Puedes pasar cualquier cantidad de argumentos con nombre a la función, y estos se reciben como un diccionario que se procesa individualmente en el bucle.
Esto es útil cuando necesitas pasar múltiples parámetros con nombres específicos a la función.
"""

#funciones dentro de funciones

"""También puedes definir funciones dentro de otras funciones. Estas funciones internas pueden acceder a las variables y parámetros de la función externa.
Esto es útil para organizar el código y encapsular la lógica relacionada."""

def outer_function():
    def inner_function():
        print("Hola desde la función interna")
    inner_function()
# Llamada a la función externa

outer_function()

"""
En este caso, la función outer_function define una función interna llamada inner_function que imprime el mensaje pasado como argumento.
Cuando llamas a outer_function, se ejecuta inner_function y se imprime el mensaje.
Esto es útil para crear funciones que solo tienen sentido dentro del contexto de otra función.
"""

# Funciones del lenguaje (built-in functions)
""" 
Las funciones del lenguaje son funciones predefinidas que están disponibles en Python sin necesidad de definirlas.
 Estas funciones proporcionan funcionalidades comunes y útiles que puedes utilizar en tu código.   
 Algunas de las funciones del lenguaje más comunes incluyen:
 print(): Imprime un mensaje en la consola.
 len(): Devuelve la longitud de un objeto, como una cadena o una lista.
 type(): Devuelve el tipo de un objeto.
 range(): Genera una secuencia de números en un rango específico.
 sum(): Calcula la suma de los elementos de un iterable, como una lista o una tupla.
 """

#ejemplo de función del lenguaje

print(len("Paprikaistkrieg"))  # Imprime la longitud del archivo Paprikaistkrieg
print(type(42))  # Imprime el tipo de dato del número 42
print("Paprikaistkrieg".upper())  # Imprime el nombre del archivo Paprikaistkrieg
print(sum([1, 2, 3, 4, 5]))  # Imprime la suma de los números en la lista
for i in range(5):
    print(i)
    # range() genera una secuencia de números del 0 al 4

"""
Estas funciones del lenguaje son muy útiles y te permiten realizar tareas comunes de manera rápida y eficiente sin necesidad de definir tus propias funciones.
"""

#Variables locales y globales

"""
Ámbito o scope
En Python, las variables pueden tener diferentes ámbitos o "scope".
El ámbito de una variable determina dónde se puede acceder a ella en el código.
Las variables locales son aquellas que se definen dentro de una función y solo son accesibles dentro de esa función.
Las variables globales, por otro lado, se definen fuera de cualquier función y son accesibles en todo el código.
"""
mensaje = "Global"

def funcion():
    mensaje = "Local"
    ejemplo = "esto es un ejemplo de variable "
    print(ejemplo, mensaje)  # Imprime "Local"

funcion()
print(mensaje)  # Imprime "Global"

#print(ejemplo)  # Esto generará un error porque ejemplo es una variable local y no se puede acceder fuera de la función

"""
En este ejemplo, la variable mensaje se define como una variable global fuera de la función funcion.
Dentro de la función, se define una variable local con el mismo nombre, lo que oculta la variable global.
Cuando llamas a funcion(), imprime "Local" porque está accediendo a la variable local.
Fuera de la función, cuando imprimes mensaje, imprime "Global" porque estás accediendo a la variable global.
"""

"""como buena práctica, es recomendable evitar el uso de variables globales siempre que sea posible.
En su lugar, puedes pasar variables como argumentos a las funciones o utilizar variables locales dentro de las funciones para mantener el código más limpio y evitar confusiones.
Valorar la posibilidad de utilizar variables locales en lugar de globales es una buena práctica para mantener el código más limpio y evitar confusiones.
"""
#Extra
""" * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

def funcion_extra(texto1, texto2)->int:
    count = 0
    for numeros in range(1, 101):
        if numeros % 3 == 0 and numeros % 5 == 0:
            print(texto1 + texto2)
        elif numeros % 3 == 0:
            print(texto1)
        elif numeros % 5 == 0:
            print(texto2)
        else:
            print(numeros)
            count += 1

    return count

print(funcion_extra("Fizz", "Buzz"))

           