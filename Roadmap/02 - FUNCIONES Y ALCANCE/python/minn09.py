# Funciones sin parametros, con parametros y varios parametros
def funcion_con_retorno():
    return 1


def funcion_sin_retorno():
    print("No tengo retorno")


def funcion_varios_retornos():
    return "nombre", "apellido", "edad"


def funcion_con_parametro(numero):
    return numero


def funcion_sin_parametro():
    return 1


def funcion_varios_parametros(numero, letra, vocal):
    return f"{numero} {letra} {vocal}"


# Funciones anonimas
cuadrado = lambda x: x**2


# Variable global
global variable_global


def imprimir_multiplos(palabra_multiplo_3: str, palabra_multiplo_5: str) -> int:
    cantidad_multiplo_3 = 0
    cantidad_multiplo_5 = 0

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            palabra = f"{palabra_multiplo_3}, {palabra_multiplo_5}"
            cantidad_multiplo_3 += 1
            cantidad_multiplo_5 += 1
        elif i % 3 == 0:
            palabra = palabra_multiplo_3
            cantidad_multiplo_3 += 1
        elif i % 5 == 0:
            palabra = palabra_multiplo_5
            cantidad_multiplo_5 += 1
        else:
            palabra = i
    resultado = f"La cantidad de veces que se ha impreso: (multiplo de tres, multiplo de 5): {cantidad_multiplo_3, cantidad_multiplo_5}"
    return resultado


print("====================================================")
print(f"Funcion con retorno: {funcion_con_retorno}")
print(f"Funcion sin retorno: {funcion_sin_retorno}")
print(f"Funcion con parametro: {funcion_con_parametro(7)}")
print(f"Funcion sin paramtro: {funcion_sin_parametro}")
print(f"Funcion con varios parametros: {funcion_varios_parametros(2, 'F', 'A')}")
print(f"Funcion que retorna varios elementos: {funcion_varios_retornos()}")
print(f"Funcion anonima: {cuadrado(3)}")

print("------------------------------------------")
print(imprimir_multiplos("tres", "cinco"))
print("------------------------------------------")

print("====================================================")
