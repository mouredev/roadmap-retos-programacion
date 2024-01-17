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

print("*****FUNCIONES SIN VALOR DE RETORNO*****")


def non_return_function():
    """
    Imprime un mensaje que indica que esta es una función sin parámetros o valores de retorno.
    """
    print("Esta es una función sin parámetros ni valores de retorno\n")


non_return_function()

print("*****FUNCIONES CON PARÁMETROS Y SIN VALOR DE RETORNO*****")


def function_with_parameters(parameter1, parameter2):
    """
    Una función que toma dos parámetros e imprime una cadena formateada.

    Parámetros:
        parámetro1 (any): el primer parámetro.
        parámetro2 (any): el segundo parámetro.

    Devoluciones:
        Ninguno
    """
    print(
        "Esta es una función con parámetros sin retorno: %s" % parameter1
        + " "
        + parameter2
        + "\n"
    )


function_with_parameters("Hello", "World")


print("*****FUNCIONES CON PARÁMETROS Y VALOR DE RETORNO*****")


def function_with_return(parameter1, parameter2):
    """
    Esta función toma dos parámetros y devuelve una cadena.Concatena los valores de `parámetro1` y` parámetro2` con un espacio intermedio,
    y agrega un carácter de nueva línea al final.Luego se devuelve la cadena resultante.

    : parámetro de parámetro1: el primer parámetro de la función.
    : parámetro de parámetro2: el segundo parámetro de la función.
    : return: una cadena que contiene los valores concatenados de `parámetro1` y` parámetro2`, seguido de un carácter nuevo.
    """
    return (
        "Esta es una función con parámetros y retorno: %s" % parameter1
        + " "
        + parameter2
        + "\n"
    )


print(function_with_return("Hello", "World"))

print("*****FUNCIONES CON PARÁMETROS POR DEFECTO Y VALOR DE RETORNO*****")


def function_with_default_parameters(parameter1, parameter2="World"):
    """
    Una función con parámetros predeterminados y una declaración de retorno.

    Args:
        Parámetro1: el primer parámetro de la función.
        Parámetro2: el segundo parámetro de la función.El valor predeterminado es "Mundo".

    Devoluciones:
        Una cadena que combina los valores del parámetro1 y el parámetro2.
    """
    return (
        "Esta es una función con parámetros por defecto y retorno: %s" % parameter1
        + " "
        + parameter2
        + "\n"
    )


print(function_with_default_parameters("Hello"))

print("*****FUNCIONES DENTRO DE FUNCIONES*****")


def function_inside_function():
    print("Esta es la función principal")

    def function_inside():
        """
        Esta función imprime un mensaje que indica que es la función dentro de la función principal.
        """
        print("Esta es la función dentro de la función principal\n")

    function_inside()


function_inside_function()

print("*****FUNCIONES YA CREADAS*****")

print(f"La función min() devuelve el número menor: {min(2, 4)}")
print(f"La función max() devuelve el número mayor: {max(2, 4)}\n")

print("*****VARIABLES LOCALES Y GLOBALES*****")

variable_global = "Soy una variable global.\n"


def function_variable_local():
    """
    Esta función define una variable local llamada `variable_local` e imprime su valor.
    También trata de imprimir una variable global llamada `variable_global`,
    suponiendo que se define en otra parte del código.

    Parámetros:
    Ninguno

    Devoluciones:
    Ninguno
    """
    variable_local = "Soy una variable local."
    print(variable_local)
    print(variable_global)


function_variable_local()

print("*****DIFICULTAD EXTRA*****")


def dif_extra(texto1, texto2):
    """
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

    Parameters:
        texto1 (str): La primera cadena de texto.
        texto2 (str): La segunda cadena de texto.

    Returns:
        None

    Description:
        Esta función recibe dos cadenas de texto como parámetros y realiza las siguientes operaciones:
        - Si un número es múltiplo de 3, imprime la cadena de texto del primer parámetro.
        - Si un número es múltiplo de 5, imprime la cadena de texto del segundo parámetro.
        - Si un número es múltiplo de 3 y de 5, imprime las dos cadenas de texto concatenadas.
        - Si un número no es múltiplo de 3 ni de 5, imprime que el número no le corresponde texto.
        Al final, la función imprime el número de veces que se ha impreso el número en lugar de los textos.

    Note:
        Esta función no retorna ningún valor, simplemente imprime los resultados.
    """
    veces = 0

    for num in range(1, 101):
        if num % 3 == 0:
            print(f"Posición {num}: {texto1}")
        elif num % 5 == 0:
            print(f"Posición {num}: {texto2}")
        elif num % 3 == 0 and num % 5 == 0:
            print(f"Cadenas de texto concatenadas en {num}: {texto1 + texto2}")
        else:
            print(f"Al numero {num} no le corresponde texto.")
            veces += 1
    return print(f"Veces que se ha impreso el numero en lugar del texto: {veces}")


dif_extra("Dificultad", "extra")
