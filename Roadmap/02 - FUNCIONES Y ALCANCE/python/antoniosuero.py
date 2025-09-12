# EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

def sin_parametros():
  print("Hola Mundo!")

sin_parametros()


def con_parametros(a, b):
  print(a + b)

con_parametros(5, 10)


def con_retorno(a):
  return a

print(con_retorno("Segovia"))


def suma(*elementos):
  suma = sum(elementos)
  return suma

print(f"La suma total es: {suma(1, 2, 3, 4, 5, 6, 7, 8, 9)}")


def funcion_dentro_funcion(x):
  def funcion_interna(y):
    return x + y
    
  resultado = funcion_interna(10)
  return resultado

print(funcion_dentro_funcion(5))


def funcion_llama_funcion(num):
  multiplica = suma(1, 2, 3, 4, 5) * num
  return multiplica

print(funcion_llama_funcion(3))

# ALGUNAS FUNCIONES DENTRO DE PYTHON
print(f"\n{"#" * 17} ALGUNAS FUNCIONES PYTHON {"#" * 17}\n")

print(f"print(), input(), len(), list(), round(), abs() y muchas más")

print(f"\n{"#" * 60}\n")


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def opcional(text_1, text_2):
    contador = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            contador += 1
    return contador

print(f"Números de veces que se ha imprimido el número en lugar del texto: {opcional("cola", "cao")} veces.")