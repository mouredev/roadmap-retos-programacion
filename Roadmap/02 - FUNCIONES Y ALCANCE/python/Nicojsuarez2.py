# #02 FUNCIONES Y ALCANCE

'''
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
'''

# Función sin parámetros ni retorno
def hello():
    print("Hello World!")

hello()

#Funcion con un parametro
def hello_name(name):
    print(f"Hello {name}!")

hello_name("Nico")

#Funcion con parametro por defecto
def potencia(base, exponente=2):
    return base ** exponente

print(f"El cuadrado de 5 es: {potencia(5)}")

#funcion con parametros no definidos
def sumar_varios(*args):
    return sum(args)

print(f"La suma de varios números es: {sumar_varios(1, 2, 3, 4, 123)}")

#funcion con argumentos nombrados
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Nico", edad=23, ciudad="Bogotá")

#funcion lambda
print((lambda x: x * 2)(7))

#funcion con una funcion dentro
def operacion(x):
    def cuadrado(n):
        return n ** 2
    return cuadrado(x)

print(f"El cuadrado de 6 es: {operacion(6)}")



#funcion 
def suma(a, b):
    return a + b    

print(suma(2, 3))

def funcion():
    def funcion_interna():
        print("Función interna")
    funcion_interna()

funcion()

def funcion_global():
    global a
    a = 5
    print(a)

funcion_global()

def funcion_local():
    a = 5
    print(a)