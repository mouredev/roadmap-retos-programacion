"""
Funciones definidas por el usuario
"""

#simple

def greet():
    print("Hola, Python!!")

greet()

#con retorno

def return_greet():
    return "Hola, Python!"

#greet = return_greet()
print(return_greet())



#con un argumento
def arg_greet(name):
    print(f'Hola {name}')

arg_greet('Eddy')


#con argumentos
def args_greet(greet, name):
    print(f'{greet} {name}')

args_greet('Hola', 'Eddy')
args_greet(name = 'Luis', greet='Hola') #le cambio el orden


#con un argumento predeterminado

def default_arg_greet(name = 'Python'):
    print(f'Hola {name}')

default_arg_greet('Eddy')
default_arg_greet()


#con argumento y retorno
def return_arg_greets(greet, name):
    return f'{greet}, {name}!!'

print( return_arg_greets('Hola', 'Eddy'))



#con retorno de varios valores
def multiple_return_gree():
    return 'Hola', 'Python'

greet, name = multiple_return_gree()
print(greet)
print(name)


#con un número variable de argumento

def variable_args_greet(*names):
    for name in names:
        print(f'hola {name}')

variable_args_greet('Python', 'Eddy', 'Complex')


#con un número variable de argumento con palabra clave
def variable_key_args_greet(**names):
    for key, value in names.items():
        print(f'{value} ({key})!!')

variable_key_args_greet (
    language = 'Python',
    name = 'Eddy',
    Alias = 'Complex',
    age = 24
)

"""
Funciones dentro de funciones
"""
def outer_function():
    def inner_function():
        print("Funcion interna: Hola python")
    inner_function()

outer_function()


"""
Funciones del lenguaje (built in)
"""

print(len('Complex'))
print(type(3.4))
print('eddy'.upper())

"""Variables 
locales y globales"""

global_variable = 'Python'

print(global_variable)

def hello_python():
    local_variable = 'Hello'
    print(f"{local_variable} {global_variable}")

#print(local_variable) #No se puede acceder desde afuera de la funcion
hello_python()


""" * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""



def funcion_numero(txt, txt2) -> int:
    contador = 0
    for num in range(1,101):
        if num % 3 ==0 and num % 5 ==0:
            print(f'{txt+ ' '+txt2}')
        elif num % 3 ==0:
            print(txt)
        elif num % 5  ==0:
            print(txt2)
        else:
            print(num)
            contador +=1
    return contador


print(funcion_numero('Fizz', 'Buzz'))
    
