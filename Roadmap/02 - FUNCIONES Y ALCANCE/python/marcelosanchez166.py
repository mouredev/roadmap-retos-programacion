""" EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda."""


def funcion_sin_parametros():
    print("Esta es una función sin parámetros ni retorno.")

def funcion_con_parametros(param1, param2):
    print(f"Esta es una función con parámetros: {param1} y {param2}.")

def funcion_con_retorno(param1, param2):
    resultado = param1 + param2
    print(f"Esta es una función con retorno: {resultado}.")
    return resultado

def funcion_anidada():
    def funcion_interna():
        print("Esta es una función interna dentro de otra función.")
    funcion_interna()

funcion_sin_parametros()

funcion_con_parametros("Hola", "Mundo")

resultado = funcion_con_retorno(5, 10)

print(f"Resultado de la función con retorno: {resultado}.")

funcion_anidada()

# Ejemplo de variable global y local
variable_global = "Soy una variable global"
def funcion_con_variable_local():
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)  # Acceso a la variable global

funcion_con_variable_local()
print(variable_global)  # Acceso a la variable global desde fuera de la función

# Ejemplo de función ya creada en el lenguaje
lista = [1, 2, 3, 4, 5]
def funcion_existente(lista):
    suma = sum(lista)
    print(f"La suma de los elementos de la lista es: {suma}.")
funcion_existente(lista)



def imprimir(caracter1, caracter2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(caracter1+caracter2)
        elif i % 3 == 0:
            print(caracter1)
        elif i % 5 == 0:
            print(caracter2)
        else:
            print(i)
            count += 1
    return f"{count} Cantidad de números impresos."


print(imprimir("fizz", "buzz"))
