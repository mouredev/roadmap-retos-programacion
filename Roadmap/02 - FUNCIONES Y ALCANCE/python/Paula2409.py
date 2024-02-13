""" 
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
 """
 
# Function without parameters and no return
def function_without():
    print('Function without parameters and no return')
    
# Function with parameters and no return   
def function_with(number=5):
    print('Function with parameters and no return')
    print(number)

# Function with parameters and return   
def function_with_return(word_first='Hello', word_second='World'):
    return word_first + ' ' + word_second

# Function inside other function
def first_function():
    print('This is the first function')
    
    def second_function():
        print('This is the second function')
    second_function()

# Built-in functions Pyhton
def built_in_examples():
    max_function = max(5,10)
    min_function = min(-2,0)
    len_function = len('Lenght of this sentence')
    round_function = round(4.5)
    type_function = type(5)
    id_function = id(max_function)
    print(f'Function max between two numbers: {max_function}')
    print(f'Function min between two numbers: {min_function}')
    print(f'Function lenght of sentence: {len_function}')
    print(f'Function round number closer to next number: {round_function}')
    print(f'Function type of object: {type_function}')
    print(f'Function id (identifier memory adress): {id_function}')

# Test local and global variables
global_var = 'Global variable'
def variables_global_local_test():
    print(f'Global variable inside function {global_var}')
    
    local_var = 'Local variable'
    print(f'Local variable inside function {local_var}')
      
    def other_function():
        print(f'Test global variable from other function: {global_var}')
        print(f'Test local variable from other function: {local_var}')
    other_function()
            
function_without()
function_with()
print(f'Function with parameters and return: {function_with_return()}\n' )
print('Function inside other function: ')
first_function()
print()
built_in_examples()
print()
print('Test local and global variables: ')
variables_global_local_test()
print(f'Global variable outside function: {global_var}')
try:
    print(f'Local variable out the function: {local_var}')
except Exception:
    print('Error: Variable local out the context\n')

# Extra difficult
def extra_exercise(firs_parameter,second_parameter):
    counter_number = 0
    for number in range(1,101):
        if number % 15 == 0:
            print(firs_parameter+second_parameter)
        elif number % 5 == 0:
            print(second_parameter)
        elif number % 3 == 0:
            print(firs_parameter)
        else:
            print(number)
            counter_number += 1
    return f'Times number has been printed: {counter_number}'

# Test extra difficult
print(extra_exercise('Fizz','Buzz'))
    