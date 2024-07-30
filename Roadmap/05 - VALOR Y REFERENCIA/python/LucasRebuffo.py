""" /*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */ """

""" En python el pasaje por valor o por referencia esta determinado por el tipo de valriable,
    Si es de tipo compuesto se pasa por referencia y si es de tipo simple se pasa por valor """


""" Ejemplos: tipos de datos simples """


def pasaje_valor_1(valor: int):
    valor += 1


def pasaje_valor_2(valor: bool):
    valor = not valor


def pasaje_valor_3(valor: str):
    valor.upper()


def pasaje_valor_4(valor: float):
    valor *= 3


valor = 2

pasaje_valor_1(valor)
print(valor)

valor = True

pasaje_valor_2(valor)
print(valor)

valor = "lucas"

pasaje_valor_3(valor)
print(valor)

valor = 1.3

pasaje_valor_4(valor)
print(valor)

""" Ejemplos tipos complejos """


def pasaje_referencia_1(valor: list):
    valor.append("copa")


valor = ["America", "arg"]

pasaje_referencia_1(valor)
print(valor)


def pasaje_referencia_2(valor: set):
    valor.add("copas")


valor = {"America", "arg"}

pasaje_referencia_2(valor)
print(valor)


def pasaje_referencia_1(valor: list):
    valor.append("copa")


valor = ["America", "arg"]

pasaje_referencia_1(valor)
print(valor)


def pasaje_referencia_3(valor: dict):
    valor["nueva llave"] = "nuevo valor"


valor = {"America": "arg"}

pasaje_referencia_3(valor)
print(valor)

""" Lo que esta pasando es que cuando usamos tipos de datos 'primitivos' o simples, se le pasa una copia del valor
    que tiene la variable pero cuando pasamos los tipos de datos complejos como listas, sets, diccionarios u objetos
    le pasamos la direccion de memoria donde se aloja esa variable.  """

""" * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */ """


def programa_valor(value_param1, value_param2):
    aux = value_param1
    value_param1 = value_param2
    value_param2 = aux

    return value_param1, value_param2


def programa_referencia(ref_param1, ref_param2):
    aux = ref_param1 # copio la direccion de memoria en aux 
    ref_param1 = ref_param2 # ahora los dos paramentros apuntan a la misma direccion de memoria
    ref_param2 = aux # hago que el param 2 apunte a la direccion de aux que era la de param 1

    return ref_param1, ref_param2


var_1 = 5
var_2 = "lucas"

var_3, var_4 = programa_valor(var_1, var_2)

print(var_1, var_2)
print(var_3, var_4)


var_5 = ["lista","valor"]
var_6 = {"set","valor"}

var_7, var_8 = programa_valor(var_5, var_6)

print(var_5, var_6)
print(var_7, var_8)
