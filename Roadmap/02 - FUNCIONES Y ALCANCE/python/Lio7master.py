#  EJERCICIO:
#  - Crea ejemplos de funciones básicas que representen las diferentes
#    posibilidades del lenguaje:
#    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  - Comprueba si puedes crear funciones dentro de funciones.
#  - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  - Debes hacer print por consola del resultado de todos los ejemplos.
#    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
# 
#  DIFICULTAD EXTRA (opcional):
#  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
# 
#  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
# 


#Definimos una función como un bloque de codigo que lo creamos para poderlo reautilizar con una tarea especifica,
#para poder manejarla, escalarla, y mantenerla de forma facil.

#Funciones defindas por el sistema

#"def" es la palabra reservada para la función en python
#Simple
def greet():
    print('hola Python!')

#se manda llamar a la función
greet()

#Con retorno
#ejecuta una logica y devuelve un resultado
def return_greet():
    return "hola, Python desde el return!"
#directamente desde la funcion manejamos el return
print(return_greet())
#O asignandola a variable para manejo posterior
greetReturn = return_greet()
print (greetReturn, "desde fucion en variable")

#Funciones con arguamentos
#Le pasamos parametros a la funcion para que realice operaciones con el
def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Lio")


#Con Varios valores:
def args_greet(greet, name):
    print(f"{greet}, {name}!")

#Con Argumento predeterminado
args_greet("hola", "lio")

def default_arg_greet(name = "Python" ):
    print(f"Hola, {name}")

default_arg_greet()

#Declarando nombre parametros para evitar errores de orde default
args_greet(name= "Leo", greet= "Hola con parametros declarados")


def mult_return_greet():
    return "hola", "Python"

greet, name = mult_return_greet() #Se desestructuran los valores conforme fueron declarados
print(greet)
print(name)

#Funciones con numero variable de argumentos

def variable_arg_gree(*names):
    for name in names: #intera dentro de los argumentos recibidos
        print(f"hola, {name}")

variable_arg_gree("python", "cancun", "Leo", "Lio")

#Con un numero variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})")
              
variable_key_arg_greet(
    name = "Leo",
    edad = 31,
    lenguaje = "Python",
    alias = "Lio7Master"
)

#fucion dentro de funcion+

def outer_funtion():
    def inner_funtion():
        print ("Funcion interna: hola, Python!")
    inner_funtion() #Llamamamos a la funcion interna para que se ejecute dentro de la fucion principal.

outer_funtion()

#Funciones del lenguaje (Built-in), son funciones que vienen predeterminadas por el lenguje

#ejemplo print es una funcion que ya esta definida solo para llamar

print(len("Lio7master")) #Len conteo de la cadena
print(type(31)) #Tipo de dato
print("lio7master".upper()) #funcion asociado al tipo de dato

#concepto de  variables locales y globales
global_var = "Python"

def hello_python():
    local_var = "hola"
    print(f"Hello, {global_var}!")
    

print(global_var)
#print(local_var) no se puede acceder desde fuera de la funcion

hello_python()

#EXTRA: ejercicio de fizz buzz
def print_numbers(text_1, text_2 ) -> int:
    count = 0
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print(text_1)
        elif  number % 3 == 0:
            print(text_2)
        elif number % 5 ==  0:
            print(text_1, text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("fizz", "buzz"))