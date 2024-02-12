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
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */ """

# Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...


def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


numero = 10
print(f"El factorial de {numero} es: {factorial(10)}")


def suma(a, b, c):
    resultado = a + b + c
    print(f"{a} + {b} + {c} == {resultado}")
    resultado


print(
    f"El resultado de sumar tres veces {numero} es: {suma(numero, numero, numero)}")


def holaMundo():
    print("Hola mundo\n")


holaMundo()

# Comprueba si puedes crear funciones dentro de funciones.


def funcion():
    def funcion_2():
        print("Sí se puede\n")
    return funcion_2()


funcion()

# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
cadena = "Hola python"
print(f"La longitud de la cadena es {len(cadena)}\n")

# Pon a prueba el concepto de variable LOCAL y GLOBAL.
global_variable = 10


def producto():
    local_variable = 5
    global_variable = 2
    print(
        f"Variable global con valor local: {global_variable} y variable local: {local_variable}")


producto()
print(f"Valor de variable global:  {global_variable}")

""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. 
"""

print("\nFunción que recibe dos parámetros y retorna un número")
cadena1 = input("Ingrese primera cadena: ")
cadena2 = input("Ingrese segunda cadena: ")


def contador(cadena1, cadena2):
    count = 0
    for i in range(0, 101):
        if i % 5 == 0 and i % 3 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            count += 1
    return (count)


print("La cantidad de veces que se mostaron números fueron: ",
      contador(cadena1, cadena2))
