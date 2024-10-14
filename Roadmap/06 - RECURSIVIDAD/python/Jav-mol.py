# --- Funciones Recursivas ---

def mostrar_numeros(n:int):
    """ La funcion toma un numero y le va sumando uno hasta llegar a 100. 

    Args:
        n (int): Numero Entero menor que 100
    """
    if n == 100:
        return
    elif n > 100 or n < 0:
        return
    else:
        print(n)
        n += 1
        mostrar_numeros(n)
        
mostrar_numeros(101)
mostrar_numeros(-1)
mostrar_numeros(1)

""" Dificultad Extra """

# Factorial de un numero
def factorial(n:int):
    print(n)
        
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


# Calcular la posicion de un numero en fibonacci
def calcular_posicion(posic:int, fibo:list=[0,1]):
    
    if posic < fibo[-1]:
        print(fibo)
        return f'La posicion no es valida'
    elif posic == fibo[-1]:
        print(fibo)
        return f'La posicion en fibonacci es {fibo.index(posic) + 1}'

    fibo.append(fibo[-1]+fibo[-2])
    
    return calcular_posicion(posic)    
    
print(calcular_posicion(233))
