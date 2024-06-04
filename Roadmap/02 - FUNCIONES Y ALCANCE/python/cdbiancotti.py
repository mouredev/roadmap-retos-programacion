from typing import List, Dict, Callable

# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

print('\n=== Variaciones a en la definicion de una funcion ===\n')


def func1() -> None:
    print('funcion sin parametros ni retorno', 1 + 2)


def func2(a: int, *args: List[int], b=3, **kwargs: Dict[str, int]) -> int:
    return a + sum(args) + b + sum([num for num in kwargs.values()])


func1()
print('funcion con parametros por posicion, por nombre, indefinidos (*args, **kwargs), con valor por defecto,'
      ' con return. Resultado de ejecucion:', func2(2, 2, 5, 3, 5, 4, 76, 3, 2, 3, 4, c=15, z=35, f=62))

print('Muestra de una funcion anonima. Resultado:', (lambda x: x ** 2)(5))

print('\n=== Definir una funcion dentro de otra ===\n')


def out_function() -> Callable:
    print('out_function')

    def in_function() -> None:
        print('funcion interna de out_function')

    return in_function


function_from_inside = out_function()
function_from_inside()

print('\n=== Uso de una funcion built-in ===\n')
print('ejecucion de "max(1,2,3)":', max(1, 2, 3))

print('\n=== Prueba de variable Local y Global ===\n')
global_variable_1: str = 'variable global 1'
global_variable_2: str = 'variable global 2'


def change_global_variable() -> None:
    global global_variable_1
    global_variable_1 = 'new data from change_global_variable'
    print('Se puede llamar a una variable de un scope superior al de la funcion. Resultado:', global_variable_2)
    local_variable: str = 'Soy una variable local de la funcion.'


change_global_variable()
print('global_variable_1 modificada desde dentro de la funcion gracias al la sentencia "global". Resultado:',
      global_variable_1)
try:
    print(local_variable)
except Exception:
    print('No se puede llamar a una variable local de una funcion desde fuera de la misma.')

print('\n=== Dificultad extra ===\n')


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def custom_1_to_100(val1: str, val2: str) -> int:
    count_of_printed_numbers: int = 0
    for num in range(1, 101):
        multiple_of_3: bool = num % 3 == 0
        multiple_of_5: bool = num % 5 == 0
        if multiple_of_3 and multiple_of_5:
            print(val1 + val2)
        elif multiple_of_3:
            print(val1)
        elif multiple_of_5:
            print(val2)
        else:
            print(num)
            count_of_printed_numbers += 1
    return count_of_printed_numbers


result = custom_1_to_100('multiple of 3', 'multiple of 5')
print('La cantidad de numeros printeada fue', result)
