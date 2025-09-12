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


# función sin parámetro
def mensaje():
    print('\nBienvenidos y Bienvenidas a la resolución de retos de programación')


mensaje()


# función con un solo parámetro sin retorno
def bienvenida(nombre: str):
    print(f'\nHola, {nombre}, ánimo con los retos de programación')


bienvenida('giulianovfz')


# función con un solo parámetro y valor por defecto, sin retorno
def saludo(nombre="compañeros y compañeras"):
    print(f'\nHola, {nombre}, ánimo con los retos de programación')


saludo()

valor1 = 8
valor2 = 5


# función con parámetros sin retorno
def suma(a, b):
    print(f'valor de la suma a+b: {a+b}')


suma(valor1, valor2)


# función con parámetros y retorno
def resta(a, b):
    return a-b


resultado_resta = resta(valor1, valor2)
print(resultado_resta)

"""
Funciones del lenguaje
"""

lista = list(("Pala", "Picota", "Rastrilo"))
print(lista)
print(len(lista))
print(list((enumerate(lista))))


"""
Variables locales y globales
"""

variable_global = "Planeta Tierra"


def continente():
    variable_local = "Continente Americano"
    print(f"""Variable global:{
          variable_global}, Variable local:{variable_local}""")


# crear una función dentro de otra
def modulo(numero: int):

    print(f'valor número: {numero}')

    def duplicar(aduplicar):
        return aduplicar*2

    if numero % 2 == 0:
        resultado = duplicar(numero)
        print(f'el valor duplicado es: {resultado} y es multiplo de 2')
    else:
        print(f'El valor ingresado: {numero} no es multiplo de 2')


modulo(5)


# dificultad extra
def imprimir(parametro1: str, parametro2: str):

    contador = 0

    # imprimir todos los números del 1 al 100
    for numero in range(1, 101):

        if numero % 3 == 0 and numero % 5 == 0:
            print(f'cadena de texto concatenadas parametro 1 y 2: {
                  parametro1}{parametro2}')
        elif numero % 5 == 0:
            print(f'cadena de texto segundo parametro: {parametro2}')
        elif numero % 3 == 0:
            print(f'cadena de texto primer parametro: {parametro1}')
        else:
            contador += 1
            print(f'número:{numero}')

    return contador


entrada1 = input('\ningresa el primer texto: ')
entrada2 = input('\ningresa el segundo texto: ')

respuesta = imprimir(entrada1, entrada2)

print(f'\n número de veces que se imprimio solo números:{respuesta}')
