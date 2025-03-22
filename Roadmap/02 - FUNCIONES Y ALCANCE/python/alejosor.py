"""
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
"""

# Función sin parametros ni retorno
def mi_primera_funcion():
    print("Holaa")

mi_primera_funcion()

# Función con un parámetro
def mi_segunda_funcion(mensaje):
    print(f"Esta función imprime el mensaje: {mensaje}")

mi_segunda_funcion("Bienvenido a la comunidad")

# Función con varios parámetros
def mi_tercera_funcion(x,y,z):
    print(f"La sumatoria de {x}, {y} y {z} es {x+y+z}")

mi_tercera_funcion(1,2,3)

# Función con retorno
def mi_cuarta_funcion(x,y):
    multi = x*y
    return multi

multiplicacion = mi_cuarta_funcion(5,4)
print("La multiplicación es:",multiplicacion)

# Comprueba si puedes crear funciones dentro de funciones
# Utiliza algún ejemplo de funciones ya creadas en el lenguaje
# Pon a prueba el concepto de variable LOCAL y GLOBAL

mensaje_global = "Hola desde la variable GLOBAL"

def funcion_externa():
    mensaje = "Hola desde la funcion EXTERNA (variable LOCAL)"
    print(mensaje)

    def funcion_interna():
        print("Usando función interna:")
        print(mensaje.upper())
    
    funcion_interna()

funcion_externa()
print("Mensaje global fuera de la función:", mensaje_global)

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

print("\n***** Extra *****")
def extra(cadena1,cadena2):
    contador = 0
    
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(cadena1 + cadena2)
        elif num % 3 == 0:
            print(cadena1)
        elif num % 5 == 0:
            print(cadena2)
        else:
            print(num)
            contador += 1
    
    return contador

respuesta = extra("Fizz", "Buzz")
print(f"El total de veces que se imprimió el número en vez de los textos son: {respuesta}")