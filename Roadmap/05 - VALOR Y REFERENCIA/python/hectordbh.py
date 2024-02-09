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

# DIFICULTAD EXTRA
# -------------- Primer programa ---------------
def prog1(v1, v2):
    """Intercambio de variables por valor

    Args:
        v1 (int): primer número
        v2 (int): segundo número

    Returns:
        tuple: tupla con los valores intercambiados
    """
    tmp = v1
    v1 = v2
    v2 = tmp
    return (v1, v2)

# Variables originales
VAR1 = 1
VAR2 = 2
# Variables nuevas
new_var1, new_var2 = prog1(VAR1, VAR2)
# Salida
print(f"Las variables originales son {VAR1} y {VAR2}",
      "y las nuevas varibles son {new_var1} y {new_var2}")


# -------------- Segundo programa ---------------
def prog2(l1, l2):
    """Intercambio de variables por referencia

    Args:
        l1 (list): lista de valores 1
        l2 (list): lista de valores 2

    Returns:
        tuple: tupla de listas de valores
    """
    new_l1 = l2
    new_l2 = l1
    return (new_l1, new_l2)
# Variables originales
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
# Variables nuevas
new_lst1, new_lst2 = prog2(lst1, lst2)
# Salida
print(f"Las variables originales son {lst1} y {lst2}",
      "y las nuevas varibles son {new_lst1} y {new_lst2}")

