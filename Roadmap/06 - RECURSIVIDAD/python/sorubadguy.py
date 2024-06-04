"""
*Recursividad
"""

def numeros(numero):
    if(numero<100):
        numero += 1
        numeros(numero)
        print(numero)
    

numeros(0)