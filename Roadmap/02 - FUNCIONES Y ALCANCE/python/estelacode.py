#02 FUNCIONES Y ALCANCE

### 1. Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
#   Sin parámetros ni retorno

def saludar():
    print("Hola")

saludar()

#   Con uno o varios parámetros
def saludar(mensaje, name):
    print(f'{mensaje}, {name}!')

saludar('Hola', 'Estela')

#  con retorno  y con asignación de valores por defecto a todos los parametros de la función.

def returns_greeting(greeting = 'Hi', name = 'Python ♡︎ Lovers'):
    return f'{greeting}, {name}!'

print(returns_greeting()) # asigna valores por defecto permite llamar la función sin argumentos.
print(returns_greeting('Good morning', 'Estela'))

### 2. Comprueba si puedes crear funciones dentro de funciones.
#   * Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

def solucion(num1, num2):

    def suma(num1, num2):   
        return num1 + num2
    
    def resta(num1, num2):
        return num1 - num2
    
    return suma(num1, num2),  resta(num1, num2)

suma, resta = solucion(5,3)
print(f' El resultado de la suma es {suma} y resultado de la resta {resta}')

### 3. Pon a prueba el concepto de variable LOCAL y GLOBAL.
# NOTA:  Debes hacer print por consola del resultado de todos los ejemplos.(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

# variable global: Son aquellas variables que se definen fuera de cualquier función y que son accesibles en todo el programa, es decir, dentro y fuera de cada función.
# variable local: Son aquellas que se inicializan dentro de una función y pertenecen solo a esa función en particular. 
# NameError: se genera un error de tipo NameError: name 'x' is notdefined cuando el programa intenta acceder o utilizar una variable que no ha sido definida o a la que no se le ha asignado un valor.

## LOCAL SCOPE
#-----------------------------------------------------------------------------------
def local_scope():
    # local variables
    a = 'Python'
    b = 'Lovers'
    return a + b

# Se puede capturar con unico  bloque try/except la expeción de las dos variables locales.
try:
    result = local_scope() # Imprime 'PythonLovers' variables definidas dentro de la función. 
    print(result)
    # Si se intenta acceder a las variables 'a' y 'b' desde fuera de la función se producira un error.
    print(a) # NameError: name 'a' is not defined
    print(b) # NameError: name 'b' is not defined
except NameError:
    print("Error: NameError: Las variables 'a' o 'b' no son accesibles desde fuera de la función. Son variables locales")

# Se puede capturar diferentes excepciones  para dos variables locales distintas mediante bloques try/except separados.
try:
    print(a) # NameError: name 'a' is not defined
except NameError:
    print("Error: NameError: La variable 'a' no está definida")

try:
    print(b) # NameError: name 'b' is not defined
except NameError:
    print("Error: NameError: La variable 'b' no está definida")


## GLOBAL SCOPE
#-----------------------------------------------------------------------------------
def global_scope():
    '''This function uses global variable s'''
    print("Inside Function: ", s)

# Global scope
s = "Python ♡︎ Lovers"
global_scope()
print("Outside Function: ", s)

## SE DEFINE UNA VARIABLE GLOBAL Y UNA LOCAL CON EL MISMO NOMBRE
# #-----------------------------------------------------------------------------------

def same_name():
    v = "Local"
    print(f'Se imprime el valor de la variable local : {v}')

v="Global"
same_name()
print(f'Se imprime el valor de la variable global: {v}')


## MODIFICAL EL VALOR DE UNA VARIABLE GLOBAL
#-----------------------------------------------------------------------------------
# Si se trata de modificar el valor de una  variable global  desde dentro de una función, se obtiene el error:  'UnboundLocalError : se hizo referencia a la variable local 's' antes de la asignación'.
# para modificar el valor de una variable global desde dentro de una función, debemos utilizar la palabra clave "global" .

def modify_global_without_global():
    try:
        s += "♡︎..."  
    except UnboundLocalError:
        print("Error: 'UnboundLocalError : se hizo referencia a la variable local 's' antes de la asignación'.")

def modify_global():

    global s
    s += "♡︎♡︎♡︎"
    print(s)

# Global Scope
s = "Python is great!" 
modify_global_without_global()
modify_global()


### * DIFICULTAD EXTRA (opcional):
#-----------------------------------------------------------------------------------
''' * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    *   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 '''


def get_text_and_return_number(string1, string2):
    count = 0 # numero de veces que se imprime el numero.
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(string1 + string2)
        elif i % 5 == 0:
            print(string2)
        elif i % 3 == 0:
            print(string1)
        else:
            print(i)
            count += 1
    return count

print("Número de veces que se ha impreso el número en lugar de los textos: ", get_text_and_return_number("Multiplo de 3 ", "Multiplo de 5")) 