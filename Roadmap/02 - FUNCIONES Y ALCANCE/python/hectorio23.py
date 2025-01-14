#! /bin/python3.11
# Autor: Héctor Adán 
# Github: https://github.org/hectorio23
'''
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
'''

# Simple funcion sin retorno
def foo_simple() -> None:
    print("Esta es una simple funcion")

# Funcion con retorno
def foo_retorno() -> str: 
    return "Esta es una simple funcion"

# Funcion con multiples parametros 
def suma(*args):
    return sum(*args)


def foo_main():

    def foo_other():
        return "Hola bro"

    return foo_other()


# Variable global
global_variable = "Soy global"

def example_function(text1, text2):
    # Variable local
    local_variable = "Soy local"

    def print_numbers():
        count = 0  # Variable local a esta función interna

        for i in range(1, 101):
            output = ""
            if i % 3 == 0:
                output += text1
            if i % 5 == 0:
                output += text2
            if output:
                print(output)
                count += 1

        return count

    return print_numbers()



############# ZONA DE LLAMADA DE FUNCIONES ############# 
foo_simple()
print(foo_retorno())
# Suma los numeros pares del 1 al 20
print(suma(element for element in range(0, 21) if element % 2 == 0))
foo_main()
# Probando la función
print(example_function("Múltiplo de 3 ", "Múltiplo de 5"))
print(f"VariableGlobal: { global_variable } ")  # Accediendo a la variable global
# print(local_variable)  # Esto dará un error ya que la variable local no está disponible fuera de la función
