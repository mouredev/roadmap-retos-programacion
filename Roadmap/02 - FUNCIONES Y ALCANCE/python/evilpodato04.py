#/*
# * EJERCICIO:
# * - Crea ejemplos de funciones básicas que representen las diferentes
# *   posibilidades del lenguaje:
# *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

def funcion_sin_parametro_ni_retorno():
    print("Hello, world!")

def funcion_con_parametros(nombre, edad):
    print(f"My name is {nombre}, tengo {edad} años de edad")

def funcion_con_parametros_y_retorno(pasatiempo, comida_favorita):
    return f"I love {pasatiempo} and to eat {comida_favorita} at weekends"

funcion_sin_parametro_ni_retorno()

funcion_con_parametros("Samunta", "19")

retorno = funcion_con_parametros_y_retorno("to play games", "pizza")
print(retorno)

# * - Comprueba si puedes crear funciones dentro de funciones.

def funcion_exterior(param):
    def funcion_interior():
        return "This is the internal function return"
    
    return funcion_interior() if param == True else "This is the external function return"

print(funcion_exterior(True))
print(funcion_exterior(False))

# * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

print("I'm hungry")
print(len(["Sandwich", "Pizza", "Chocolate", "Donut"]))
print(input("Write something cool: "))

# * - Pon a prueba el concepto de variable LOCAL y GLOBAL.

juego_actual = "Genshin Impact"
juego_siguiente = "Aún no elegido"

def empezar_juego():
    juego_siguiente = "Legend of Zelda"
    print("LOCAL SCOPE:", juego_actual)
    print("LOCAL SCOPE:", juego_siguiente)

empezar_juego()
print("GLOBAL SCOPE:", juego_actual)
print("GLOBAL SCOPE:", juego_siguiente)

# * - Debes hacer print por consola del resultado de todos los ejemplos.
# *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)


# * DIFICULTAD EXTRA (opcional):
# * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
# *
# * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
# */

def desafio(texto_1, texto_2):
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto_1)
            print(texto_2)
        elif numero % 3 == 0:
            print(texto_1)
        elif numero % 5 == 0:
            print(texto_2)
        else:
            print(numero)
    return numero

desafio("Pizza", "Sandwich")
