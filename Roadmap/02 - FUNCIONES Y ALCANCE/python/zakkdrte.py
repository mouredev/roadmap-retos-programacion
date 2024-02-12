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
 
'''

# funcion simple sin parametro ni return 
def simple():
    print("Esta es una funcion simple")

simple() 

# funcion con parametros y un formateo
def funcion_con_parametros(name,surname):
    print(f"Mi nombre es {name} y mi apellido es {surname}")
    
funcion_con_parametros("Juan", "Chavez")

# funcion sin parametros pero con return
def retorno_sin_parametros():
    resultado = 2 + 5
    return resultado
print(retorno_sin_parametros())

# funcion con parametros y un return
def retorno_con_parametros(num1,num2):
    resultado = num1 + num2
    return resultado
print(retorno_con_parametros(10,5))

# funcion en funcion
def funcion_en_funcion(a):
    def funcion(b):
        suma_de_valores = a + b
        return suma_de_valores
    return funcion(5)

print(funcion_en_funcion(2))

# funcion en funcion pero introduciendo los valores en el print donde llamamos la funcion
def funcion_en_funcion(a):
    def funcion(b):
        suma_de_valores = a + b
        return suma_de_valores
    return funcion

print((funcion_en_funcion(6))(8))

# funcion con valor por defecto 
def funcion_valor_por_defecto(name = "JUAN"):
    return name
print(funcion_valor_por_defecto())

# funcion con variable local
def local_value():
    local_value_1 = "Juanito"
    local_value_2 = "Sanchez"
    return (f"Hola mi nombre es {local_value_1} y mi apellido es {local_value_2}")

print(local_value())

# funcion con variable global
def global_value():
    global global_value_1
    global global_value_2
    
    global_value_1 = 24
    global_value_2 = 58
    result = global_value_1 + global_value_2
    return (f"la suma entre 24 y 58 es: {result}")

print(global_value())

# print de una lambda que se igualo a una variabl, y que el print tiene formateo
multiplicacion_entre_valores = lambda x,y,z: x*y*z

print(f"Esta es el resultado de multiplicar 10*10*10: {multiplicacion_entre_valores(10,10,10)}")
'''
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
# se uitliza ciclo for en una funcion para imprimir los numeros y luego se le pone condicionales para poder hacer uso de los parametros que se necesitan para el reto
# para averiguar si un numero es multiplo del otro se utiliza el % que devuelve el residuo de un numero divido por el otro, ya que si un numero es multiplo de otro su residuo siempre sera 0. 
def function(value1, value2):
    numeros_no_cumplidos = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{value1} : {value2}")
        elif i % 5 == 0:
            print(f"{value2}")
        elif i % 3 == 0:
            print(f"{value1}")
        else:
            print(i)
            numeros_no_cumplidos += 1
    return (f"Estos son el total de los numeros que no cumplieron ninguna de las condicionales: {numeros_no_cumplidos}")

print(function("fizz","buzz"))