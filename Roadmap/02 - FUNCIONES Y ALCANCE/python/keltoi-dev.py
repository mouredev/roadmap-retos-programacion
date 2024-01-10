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
var_1 = "Chau"
var_2 = "2023"


# Funcion sin parametros ni retorno
def sin_parametros():
    print("Hola Python")
    print(2 * 5)


print("\nFuncion sin parametros")
sin_parametros()


# Funcion con parametros, pero sin retorno
def sin_retorno(num1, num2):
    print(num1 + num2)


print("\nFuncion con parametros, pero sin retorno")
sin_retorno(3, 4)


# Funcion con parametros y con retorno
def con_retorno(num1, num2):
    resultado = num1 * num2
    return resultado


print("\nFuncion con parametros y retorno")
print(con_retorno(5, 6))


# Funcion con variable local
def var_local():
    local_1 = 4
    local_2 = 6
    print("La suma de las variables locales es: ", local_1 + local_2)


print("\nEjemplo de variable local")
var_local()


# Funcion Lambda o anonima
resta = lambda x, y: x - y
print("\nEl resultado de la funcion Lambda es:", resta(5, 3))


# Funcion con variable global
def var_global():
    global var_1
    global var_2
    var_1 = "Hola"
    var_2 = "2024"


print(f"\nEl valor de las variables globales antes de una funcion: {var_1} {var_2}")
var_global()
print(f"El valor de las variables globales despues de una funcion: {var_1} {var_2}")


# Una funcion dentro de otra funcion
def funcion_1(dato_1, dato_2):
    def funcion_2(dato):
        print(f"Esta es {dato}")
        return f"Salio de {dato}"

    print(f"Esta es {dato_1}")
    print(funcion_2("la funcion 2"))
    print(f"Esta de nuevo en {dato_1}")
    return f"Salio de {dato_1}"


print("\nFuncion dentro de otra funcion")
print(funcion_1("la funcion 1", "la funcion 2"))


# Funcion recursiva
def factor(factores, factoreo):
    numero = factores[-1]
    if numero == 1:
        return factores, factoreo
    elif numero == 0:
        return [], 1
    else:
        numero -= 1
        factoreo *= numero
        factores.append(numero)
        return factor(factores, factoreo)


print("\nEjemplo de funcion recursiva")
num = 3
factores, factoreo = factor([num], num)
print("El factoreo es:", factores)
print("El resultodo del factoreo es:", factoreo)


# Dificultad extra
def dificultad_extra(texto_1, texto_2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto_1, texto_2)
        elif i % 3 == 0:
            print(texto_1)
        elif i % 5 == 0:
            print(texto_2)
        else:
            print(i)
            contador += 1
    return contador


print("\nDificultad extra")
cantidad = dificultad_extra("Fizz", "Buzz")
print(f"Se han impreso {cantidad} numeros")
