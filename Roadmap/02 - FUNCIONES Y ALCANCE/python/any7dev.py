""" /*
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
 */ """

def mi_funcion():
    print("Primera funcion")

def mi_funcion_dos(param):
    print(f"{param} funcion")

def mi_funcion_tres(param1, param2):
    return f"{param1} {param2}"

def funcion_variables():
    local_var = "Esto es una variable local"
    global global_var
    global_var = "variable global"
    print(f"{local_var} y esto una {global_var}")

def funcion_variables_dos():
    print(f"La {global_var} se puede usar desde cualquier función")

def mi_funcion_cuatro():
    cadena = "Mi función cuatro"
    def mi_funcion_cinco():
        print(f"{cadena} crea mi funcion cinco")
    mi_funcion_cinco()

def funcion_creada():
    return "print() Es una función ya creada en Python"

def extra(cadena1, cadena2):
    contador = 0
    for i in range(1,101):
        if i % 3 == 0 and not i % 5 == 0:
            print(f"{cadena1}")
        elif i % 5 == 0 and not i % 3 == 0:
            print(f"{cadena2}")
        elif i % 3 == 0 and i % 5 == 0:
            print(f"{cadena1} {cadena2}")
        else:
            print(i)
            contador += 1
    return contador

if __name__ == '__main__':
    parametro_uno = "Segunda"
    parametro_dos = "Tercera"
    parametro_tres = "Funcion"
    mi_funcion()
    mi_funcion_dos(parametro_uno)
    print(mi_funcion_tres(parametro_dos, parametro_tres))
    funcion_variables()
    funcion_variables_dos()
    mi_funcion_cuatro()
    print(funcion_creada())
    numero = extra(cadena1="Casi", cadena2="fizzbuzz")
    print(f"El número de veces que se ha impreso el número en lugar de los textos es {numero}")

    