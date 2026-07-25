# EJERCICIO:
# * - Crea ejemplos de funciones básicas que representen las diferentes
# *   posibilidades del lenguaje:
# *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# * - Comprueba si puedes crear funciones dentro de funciones.
# * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# * - Debes hacer print por consola del resultado de todos los ejemplos.
# *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
# *
# * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


# Función sin parametros:

def funnoparametros():
    for i in range(5):
        print(i)


funnoparametros()

# Función con un parametro


def fun_con_parametro(nombre):
    print("¡Hola, "+nombre+"!")


fun_con_parametro("roy")

# Función con dos parametros


def fun_con_return(num1, num2):
    numeros_pares = []
    i = num1
    print("Estos son los numeros pares entre "+str(num1)+" y "+str(num2))
    while i < num2:
        if i % 2 == 0:
            numeros_pares.append(i)
        i += 1
    print(numeros_pares)


fun_con_return(1, 100)

# Función con return y tres parametros


def fun_return(a=5, b=8, c=3):
    return (a*b)/c


print(fun_return())

# Diferencia variable local y variable global
var = "Esto es una variable global"


def fun_var():
    var = "Esto es una variable local"
    return var


print(var)
print(fun_var())


def fun_var_glob():
    global var
    var = var + " bis"
    return var


print(fun_var_glob())
