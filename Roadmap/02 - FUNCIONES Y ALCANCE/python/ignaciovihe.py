"""
Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""
#Función sin parametros ni retorno
def greet():
    print("Hello, Python!")

greet()

#Función con parametros
#Un parametro
def greet_with_param(name):
    print(f"Hello, {name}!")

greet_with_param("Ignacio")

#Dos parametros
def greet_with_params(greet, name):
    print(f"{greet}, {name}!")

greet_with_params("Hola", "Pedro")

#Parametros por defecto
def greet_default_params(greet = "Hello", name = "Python"):
    print(f"{greet}, {name}!")

greet_default_params()
greet_default_params("Hi")
greet_default_params("Pedro") #si sólo pasamos un parametro siempre sera el primero
greet_default_params(name = "Pedro") #si queremos que sea el nombre deberemos indicarselo
greet_default_params(name = "Ignacio", greet = "hi")

#Multiples parametros

names = ("Ignacio","Miguel","Lorena")

def greet_multiple_params(*args):
    for name in args:
        print(f"Hello, {name}")

greet_multiple_params(*names)

#Multiples parametros con clave-valor

names = {"Manager": "Ignacio","Developer": "Miguel","Designer": "Lorena"}

def greet_multiple_params(**kwargs):
    for role, name in kwargs.items():
        print(f"Hello, {name}. Your role is {role}")

greet_multiple_params(**names)

#Funcion con retorno

def greet_with_return(name = "Python"):
    return f"Hello, {name}"

print(greet_with_return("Ignacio"))

# Función con retorno multiple

def greet_multiple_return():
    return "Hola de nuevo", "Python"

greet, name = greet_multiple_return()
print(f"{greet}, {name}")


"""
Comprueba si puedes crear funciones dentro de funciones.
Utiliza algún ejemplo de funciones ya creadas en el lenguaje. map() int() sum()
"""
#Crear funcion dentro de otra
def sumar():

    def get_numbers():
        num1, num2 = map(int,input("Dame dos números separados por espacio: ").split())
        return num1, num2
    
    return(sum(get_numbers()))

print(sumar())
# get_numbers() No se puede llamar a funciones desde fuera de la funcion donde se creo.


"""
Pon a prueba el concepto de variable LOCAL y GLOBAL.
"""
username = "Ignacio"

def greet():
    edad = 40
    print(f"Hola, {username}, tienes {edad} años.")

greet()
#print(f"Hola, {username}, tienes {edad} años.") la variable edad sólo se puede utilizar dentro 
# del ambito donde se creo (funcion greet) al ser una variable local.

"""
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def multiples(multiple_of_3_text, multiple_of_5_text):
    
    non_multiples_count = 0
    for i in range (1,101):
        text = []

        if i % 3 == 0:
            text.append(multiple_of_3_text)
        if i % 5 == 0:
            text.append(multiple_of_5_text)

        if text:
            print(f"{i} {" ".join(text)}")
        else:
            print(i)
            non_multiples_count += 1

    return non_multiples_count

print(f"Numeros que nos son multiplos ni de 3 ni de 5: {multiples("Multiplo de 3", "Multiplo de 5")}")