#02 FUNCIONES Y ALCANCE

'''
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
'''
##
def func_1():
    print("Hola, funcion simple")
func_1()

## 
def func_2(val):
    print(f'Parametro de entrada: {val}')
func_2("Hola")

##
def func_3(val):
    return val
print(f'Un argumento, un retorno {func_3('Parameter')}')

##
def func_4(val = "Hola"):
    print(f"{val} mundo!!")
func_4()

##  
def func_5(val_1, val_2):
    return val_1, val_2
print(f'Dos arguments, un retorno {func_5('Hola', 'Mundo')}')
print(f'Dos arguments, un retorno {func_5(val_2='Mundo', val_1='Hola')}')
val_1, val_2 = func_5('Hola', 'Mundo')
print(f'Dos arguments, un retorno {val_1} y {val_2}')

## Numero variables de argumentos
def func_6(*names):
    for name in names:
        print(name)

func_6("H", "o", "l","a")

##
def func_7(**args):
    for key in args:
        print(f"Hola, {args[key]} ({key})!")

func_7(language="Python", name="Rigo", alias="rigo93acosta", age=30)

##
def outer_func():
    def inner_function():
        print("Funcion interna: Hola, Python")
    inner_function()

outer_func()

##
print(len("Rigo"))
print(type(36))
print("Rigo".upper())

##
global_varible = "Python"
print(global_varible)

def func_8():
    local_var = "Hola"
    print(f"{local_var}, {global_varible}")
func_8()
# print(local_var)

## Extra
def func_extra(var_1, var_2)-> int:
    counter = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(var_1)
        elif number % 5 == 0:
            print(var_2)
        elif number % 3 == 0:
            print(f'{var_1} {var_2}')
        else:
            counter += 1
            print(number)
        
    return counter

print(func_extra("Fizz", "Buzz"))
