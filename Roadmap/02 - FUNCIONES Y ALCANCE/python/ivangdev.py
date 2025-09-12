# --------- Funciones ---------------------
def funcion_1():
    print("Funcion sin retorno ni parametros")


mi_funcion_1 = funcion_1()


def funcion_2(a, b):
    print("Suma de 2 parametros: ", a + b)


mi_funcion_2 = funcion_2(2, 4)


def funcion_3(a, b):
    resta = a - b
    return f"Retorna la resta: {resta}"


mi_funcion_3 = funcion_3(5, 4)
print(mi_funcion_3)


# ---------------------- Funcion dentro de funcion -------------------
def suma(a, b):
    suma = a + b

    def division(suma):
        if suma % 2 == 0:
            print("Es divisible")

    division(suma)


mi_funcion_4 = suma(3, 5)

# -------------------- Varibale Local y Global ------------------
a = "prueba"


def funcion_global():
    global a
    a = "Soy global"

    def local():
        a = "Local"
        print(f"Valor a local: {a}")

    print(f"Valor a global: {a}")
    local()


funcion_global()
print(f"Valor de a modificado por la funcion_global: {a}")

# --------------- DIFICULTAD EXTRA (opcional): -------------
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


def cadena_texto(texto1, texto2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)

        elif numero % 5 == 0:
            print(texto2)

        elif numero % 3 == 0:
            print(texto1)

        else:
            contador += 1
            print(numero)

    return f"total impresiones {contador}"


print(cadena_texto("Hola", "ivan"))
