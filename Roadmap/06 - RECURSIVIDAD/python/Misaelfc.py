"""
    Ejercicio
"""

def cuenta_regresiva(numero):
    if numero < 0:
        return
    print(numero)
    cuenta_regresiva(numero - 1)
    
cuenta_regresiva(100)

"""
Extra
"""
# El factorial de un número se calcula multiplicándolo por todos sus antecesores positivos
def factorial(numero):
    if numero < 0:
        raise ValueError("No se pueden introducir números negativos")
    
    elif numero == 0:
        return 1
    
    return numero * factorial(numero - 1)
print(factorial(5))  # Output: 5040

# Finobacci sequence
def finobacci(posicion):
    if posicion < 0:
        raise ValueError("No se pueden introducir números negativos")
    
    elif posicion == 0:
        return 0
    
    elif posicion == 1:
        return 1
    
    return finobacci(posicion - 1) + finobacci(posicion - 2)
print(finobacci(10))  # Output: 55
