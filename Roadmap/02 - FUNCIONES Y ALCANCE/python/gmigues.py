''' * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)'''

def sin_parametros():
    print("Hola, soy una función sin parámetros")


def con_parametros(parametro):
    print(f"Hola, mi nombre es: {parametro}")

def con_retorno():
    return "Hola, soy una función con retorno"
mensaje = con_retorno()

def funcion_con_multiples_parametros(parametro1, parametro2, parametro3):
    print(f"Los parámetro ingresados son: {parametro1}, {parametro2}, {parametro3}")

def funcion_dentro_de_funcion():
    def funcion_interna():
        print("Hola, soy una función interna")
    funcion_interna()

def con_x_parametros(*args):
    print(f"Los argumentos ingresados son: {args}")

def funcion_kwargs(**datos):
    print(datos["nombre"], datos["apellido"], datos["edad"], datos["pais"])

def suma(*num):
    i=0
    for n in num:
        i = i + n
    print(f"La suma es: {i}")


def variable_local():
    variable = "Soy una variable local"
    print(variable)

variable = "Soy una variable global"

def variable_global():
    global variable 
    print(variable)

def funcion_lambda():
    return lambda x: x + 10

def funcion_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + funcion_recursiva(n - 1)

def funcion_con_parametros_por_defecto(parametro1, parametro2 = "default"):
    print(f"Los parámetros ingresados son: {parametro1}, {parametro2}")



sin_parametros()
print("--------------------")
con_parametros("pepe")
print("--------------------")
print(mensaje)
print("--------------------")
funcion_con_multiples_parametros("pepe", "juan", "carlos")
print("--------------------")
funcion_dentro_de_funcion()
print("--------------------")
con_x_parametros("pepe", "juan", "carlos", "jose", "luis", "maria")
print("--------------------")
funcion_kwargs(nombre="Pepe",
               apellido="Martinez",
               edad="47",
               pais="Colombia")
print("--------------------")
variable_local()
print("--------------------")
variable_global()
print("--------------------")
print(funcion_lambda()(5))
print("--------------------")
print(funcion_recursiva(6))
print("--------------------")
funcion_con_parametros_por_defecto("pepe")
print("--------------------")
suma(10,10,5,5,70)
