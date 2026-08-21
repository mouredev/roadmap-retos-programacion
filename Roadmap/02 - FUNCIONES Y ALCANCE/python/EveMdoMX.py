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
def funcion_sin_parametros():
    print("Esta es una función sin parámetros ni retorno.")

funcion_sin_parametros()

def funcion_con_parametros(param1, param2):
    print(f"Esta es una función con parámetros: {param1} y {param2}.")

def funcion_saludar(nombre):
    mensaje= f"Esta es una función con un parámetro: {nombre}. ¡Hola, {nombre}!"
    print(mensaje)

funcion_con_parametros("parametro 1", "parametro2")
funcion_saludar("Alice")

def funcion_con_argumentos_clave(param1, param2):
    print(f"Esta es una función con argumentos clave: {param1} y {param2}.")

funcion_con_argumentos_clave(param2="valor2", param1="valor1")

def funcion_con_valores_por_defecto(param1, exp=2):
    mensaje = param1 ** exp
    print(mensaje)

funcion_con_valores_por_defecto(2)
funcion_con_valores_por_defecto(2, 3) #aqui se remplaza el valor por defecto de exp

def funcion_con_argumentos_arbitrarias(*argumentosArbitarios):
    suma= sum(argumentosArbitarios)
    print(f"Esta es una función con argumentos de posición arbitrarios: {argumentosArbitarios}. La suma es: {suma}.\n")

funcion_con_argumentos_arbitrarias(1, 2, 3, 4, 5)

def funcion_con_argumentos_clave_arbitrarios(**argumentosClaveArbitrarios):
    mensaje = f"Esta es una función con argumentos de clave arbitrarios: {argumentosClaveArbitrarios}.\n"
    print(mensaje)

funcion_con_argumentos_clave_arbitrarios(param1="valor1", param2="valor2", param3="valor3")

def funcion_con_argumentos_arbitrarias_y_clave_arbitrarios(*argumentosArbitarios, **argumentosClaveArbitrarios):
    suma= sum(argumentosArbitarios)
    mensaje = f"Esta es una función con argumentos de posición arbitrarios: {argumentosArbitarios} y \nargumentos de clave arbitrarios: {argumentosClaveArbitrarios}. \nLa suma es: {suma}."
    print(mensaje)

funcion_con_argumentos_arbitrarias_y_clave_arbitrarios(1, 2, 3, 4, 5, param1="valor1", param2="valor2", param3="valor3")

def funcion_con_retorno(param1, param2):
    suma = param1 + param2
    return suma

resultado = funcion_con_retorno(5, 10)
print(f"Esta es una función con retorno. La suma de 5 y 10 es: {resultado}.")

def funcion_multiples_retorno(valor):
    if valor > 0:
        return "Positivo", valor
    elif valor < 0:
        return "Negativo", valor
    else:
        return "Cero", valor


multiples_resultado = funcion_multiples_retorno(-5)
print(f"Esta es una función con múltiples retornos. El valor es: {multiples_resultado[0]}")

def funcion_con_retorno(param1, param2):
    suma = param1 + param2
    resta = param1 - param2
    multiplicacion = param1 * param2
    division = param1 / param2 if param2 != 0 else None
    return suma, resta, multiplicacion, division

resultado = funcion_con_retorno(10, 5)
print(resultado)


#parametros globales y locales
variable_global = "Soy una variable global"

def funcion_variable_local():
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)  # Accediendo a la variable global
    
    def funcion_interna():
        global variable_global
        nonlocal variable_local
        variable_global = "He modificado la variable global"
        variable_local = "He modificado la variable local"
        print("Esta es una función interna dentro de otra función.")
        print(variable_global)   # Accediendo a la variable local desde la función interna
        print(variable_local)    # Accediendo a la variable local desde la función interna
    funcion_interna()

# Accediendo a la variable global antes de llamar a la función
funcion_variable_local()


print(f"\n\n\n\n\n")

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 """


parametro1 = "---" #str(input("ingresa el primer parametro"))
parametro2 = "|||" #str(input("ingresa el segundo parametro"))


def funcion_multiplo_3(parametro1):
    print(parametro1)


def funcion_multiplo_5(parametro2):
    print(parametro2)


for contador in range(1, 101):

    if contador %3 == 0 and contador %5 == 0:
        print(parametro1 + parametro2)
    elif contador %3 == 0:
        funcion_multiplo_3(parametro1)
    elif contador %5 == 0:
        funcion_multiplo_5(parametro2)
    else:
        print(contador)


def funcion_multiplo_3_y_5(parametro3, parametro4):

    for contador in range(1, 101):
        if contador %3 == 0 and contador %5 == 0:
            print(parametro3 + parametro4)
        elif contador %3 == 0:
            print(parametro3)
        elif contador %5 == 0:
            print(parametro4)
        else:
            print(contador)



print(f"\n\n\n\n\n")

funcion_multiplo_3_y_5("uno", "dos")
