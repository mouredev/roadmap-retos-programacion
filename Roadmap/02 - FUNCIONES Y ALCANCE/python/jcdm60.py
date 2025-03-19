# #02 FUNCIONES Y ALCANCE
#### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

## Ejercicio

#
# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#
# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#

# Función sin parámetros ni retorno
def saludo_simple():
    print("¡Hola, mundo!")

# Función con un parámetro y retorno
def cuadrado(numero):
    return numero ** 2

# Función con varios parámetros y retorno
def suma_y_producto(a, b):
    suma = a + b
    producto = a * b
    return suma, producto

# Función que llama a otras funciones
def operaciones_complejas(x, y):
    resultado_cuadrado = cuadrado(x)
    suma, producto = suma_y_producto(resultado_cuadrado, y)
    return suma, producto

# Función con variable local y global
def ejemplo_variables():
    variable_global = 10

    def funcion_interna():
        variable_local = 5
        return variable_global + variable_local

    resultado = funcion_interna()
    return resultado

# Uso de una función incorporada en Python
longitud_lista = len([1, 2, 3, 4, 5])

# Pruebas
saludo_simple()
print("Resultado del cuadrado:", cuadrado(4))

suma_resultado, producto_resultado = suma_y_producto(3, 5)
print("Suma y Producto:", suma_resultado, producto_resultado)

resultado_operaciones, producto_operaciones = operaciones_complejas(2, 3)
print("Resultado de operaciones complejas:", resultado_operaciones, producto_operaciones)

print("Ejemplo de variables locales y globales:", ejemplo_variables())
print("Longitud de la lista:", longitud_lista)


def imprimir_numeros_y_contar(texto1, texto2):
    contador = 0

    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)

        contador += 1

    return contador

# Ejemplo de uso
resultados = imprimir_numeros_y_contar("Fizz", "Buzz")
print("Número de veces que se ha impreso:", resultados)
