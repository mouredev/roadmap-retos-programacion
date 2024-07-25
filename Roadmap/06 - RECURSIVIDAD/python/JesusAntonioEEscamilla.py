# #06 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
# Definimos la función
def imprimir_números(n):
    if n < 0:
        return
    print(n)
    # Aquí es donde realiza la Recursividad
    imprimir_números(n - 1)

imprimir_números(100)



"""
EXTRA
"""
# Pendiente