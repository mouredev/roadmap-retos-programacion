# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

# #############################################################
# ################ DEFINICION DE FUNCIONES ####################
# #############################################################

def suma_referencia(value1, value2):
    # Imprime a su vez la variable y su dirección de memoria
    print("***Dentro de la funcion que recibe valores por referencia***")
    print(f"&a  ->   {id(value1)}")
    print(f"&b  ->   {id(value2)}")
    return value1 + value2

def suma_copia(value1, value2):
    # Imprime a su vez la variable y su dirección de memoria
    print("\n***Dentro de la funcion que recibe valores por copia***")
    print(f"a   ->   {id(value1)}")
    print(f"b   ->   {id(value2)}")
    return value1 + value2

def intercambio_valores_referencia(value1, value2):
    value1, value2 = value2, value1
    return [value1, value2]

def intercambio_copia(value1, value2):
    value1, value2 = value2, value1
    return [value1, value2]

# #############################################################
# ################### PROGRAMA PRINCIPAL ######################
# #############################################################

if __name__ == "__main__":
    # Variables las cuales se van a usar como conejillos de indias
    numero = 94
    numero2 = 6

    # En esta sección se imprimirán la dirección en memoria de las variables
    print("*** Estos son las direcciones en memoria de las variables previamente definidas***")
    print(f"Ubicación en memoria de numero: {id(numero)}")
    print(f"Ubicación en memoria de numero2: {id(numero2)}")

    suma_referencia(numero, numero2)
    suma_copia(numero, numero2)

    print("\n******************\n")

    print("Valor de las variables originales")
    print(f"a -> {numero}")
    print(f"b -> {numero2}")

    # Después de hacer el cambio de variables mediante una función que recibe los parámetros por copia
    resultado_copia = intercambio_copia(numero, numero2)
    copia1 = resultado_copia[0]
    copia2 = resultado_copia[1]

    print("\nValor de las variables después de hacer un intercambio de valores (copia)")
    print("Variables originales")
    print(f"a -> {numero}")
    print(f"b -> {numero2}")
    print("Variables retornadas")
    print(f"copia a -> {copia1}")
    print(f"copia b -> {copia2}")

    # Después de hacer el cambio de variables mediante una función que recibe los parámetros por referencia
    resultado_referencia = intercambio_valores_referencia(numero, numero2)
    referencia1 = resultado_referencia[0]
    referencia2 = resultado_referencia[1]

    print("\nValor de las variables después de hacer un intercambio de valores (referencia)")
    print("Variables originales")
    print(f"a -> {numero}")
    print(f"b -> {numero2}")
    print("Variables retornadas")
    print(f"copia a -> {referencia1}")
    print(f"copia b -> {referencia2}")