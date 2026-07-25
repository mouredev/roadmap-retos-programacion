'''
 EJERCICIO:
1. Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje: sin parámetros ni retorno, con uno 
   o varios parámetros, con retorno...
2. Comprueba si puedes crear funciones dentro de funciones.
3. Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
4. Pon a prueba el concepto de variable LOCAL y GLOBAL.
* Debes hacer print por consola del resultado de todos los ejemplos.
  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 
 DIFICULTAD EXTRA (opcional):
7. Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
'''

# 1. Ejemplos de funciones basicas:

# Funcion sin parametros de retorno:

def greet():
    print("Hello, world!")

greet()

# Funcion con parametros pero sin retorno:

def greet_user(name):
    print("Hello, " + name + "!")

greet_user("Jesus")

# Funcion con retorno pero sin parametros:

def days_per_year():
    return 365

result = days_per_year()
print("The year has " + str(result) + " days")

# Funciones con parametros y con retorno:

def addition(a,b):
    return a + b

result = addition(5,7)
print("Sum: " + str(result))

# 2. Funciones dentro de funciones (Funciones anidadas)

def welcome(name):
    def message():
        return "Hello, Welcome to my Website"
    
    full_welcome_message = message()+ name +"!"
    print(full_welcome_message)

welcome("Jesus")

# 3. Funciones ya creadas en el lenguaje (Funciones built-in)

text = "This is a text to work with Python Built-In Functions"
print("Lowecase text:", text.lower()) # str.lower()
print("Uppercase text:", text.upper()) # str.upper()

numbers = [1, 3, 6, 8]
print("Max:", max(numbers)) # max()
print("Min:", min(numbers)) # min()
print("Sorted:", sorted(numbers)) # sorted()
print("sum:", sum(numbers)) # sum()

# 4. Variables locales y globales

message = "Hello from outside" # Global Variable
answer = "I don't get any answer!?"

def show_message():
    answer = " I can hear you but you can't hear me!"
    print("Inside of the function: "+message+"..."+answer)

show_message()
print("Outside of the function:", answer)

# 5. Función que reciba dos parámetros de tipo cadena de texto y retorne un número

def multiples(message1,message2):
    count = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(message1 + " and " + message2)
        elif num % 3 == 0:
            print(message1)
        elif num % 5 == 0:
            print(message2)
        else:
            print(num)
            count += 1
    print ("The amount of times that the fuction print a num was: ")
    return print(count)
message1 = "This number is multiples of 3"
message2 = "This number is multiples of 5"
multiples(message1,message2)
