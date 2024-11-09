'''EJERCICIO:
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
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.'''
 
# Función simple

def holaSoyUnaFuncion():
    print("Hola, soy una función")

# Ejecución de la función
holaSoyUnaFuncion() 

# Funcion con parametros

def getNombreCompleto(nombre, apellido):
    return f"{nombre} {apellido}"

# Ejecución de la función con parametros

print(getNombreCompleto("Piero", "Zavala"))

# Funcion con parametros por defecto

def getNombreCompleto(nombre = "Piero", apellido = "Zavala"):
    return f"{nombre} {apellido}"

# Ejecución de la función con parametros por defecto

print(getNombreCompleto())

# Funcion dentro de una función

def caminar():
    def moverLasPiernas():
        print("Moviendo las piernas")
    moverLasPiernas()
    print("Caminando")

# Ejecución de la función dentro de una función
caminar()

# Funcion del lenguaje

def obtenerMaximo(lista):
    return max(lista)

# Variable global

a = 0

def suma_uno():
    global a
    a = a + 1

suma_uno()
print(a)

# variable local

def suma_uno_local():
    a = 0
    a = a + 1
    print(a)

suma_uno_local()

# Dificultad extra

def imprimirNumerosMultiplos(texto1, texto2):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{texto1}{texto2}")
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
    return i

imprimirNumerosMultiplos("Fizz", "Buzz")

