""" EJERCICIO """
# Asignación de variables por valor
S = "Pedro" # variable de tipo cadena
NUM = 32 # variable de tipo int

# Asignación de variables por referencia
var3 = [1, 2, 3] # variable de tipo lista

# Función con variable pasada "por valor"
def doblar_valor(numero):
    """Función para doblar el valor del argumento dado

    Args:
        numero (int or float): número al que doblar su valor

    Returns:
        int or float: doble del número pasado como argumento
    """
    numero *= 2
    return numero
print(doblar_valor(NUM))
print(NUM, "- Su valor no se ha vista afectado\n") # valor original no modificado

# Función con variable pasada "por referencia"
def doblar_valores(numeros):
    """Doblar valores de argumento

    Args:
        numeros (list): lista de números a doblar
    """
    for item in numeros:
        numeros[item] *= 2
doblar_valores(var3)
print(var3, "- Su valor sí se ha vista afectado") # valor original modificado
