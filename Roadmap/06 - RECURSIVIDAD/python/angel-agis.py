#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.

def recursive(inicio):
    '''
    Mientras 'inicio' sea positivo, es decir, mientras no llegue a cero,
    lo imprimimos, le restamos uno, y volvemos a llamar recursivamente a la función
    '''
    if inicio:
        print(inicio)
        inicio-=1
        recursive(inicio)
    else:
        print("Has llegado al cero.")

recursive(100)

#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
        
def factorial(inicio, total=1):
    '''
    Recibe el numero sobre el que se quiere calcular el factorial
    Va guardando el total en la variable total, que inicialmente siempre es uno para poder multiplicar.
    '''
    if inicio:
        total = total * inicio
        inicio-=1
        factorial(inicio, total)
    else:
        print(f"Factorial: {total}")

factorial(5)

#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).

def sucesion_fibonacci(posicion, sucesion = []):
    
    if posicion:
        if len(sucesion) == 0:
            sucesion.append(0)
        elif len(sucesion) == 1:
            sucesion.append(1)
        else:
            sucesion.append(sucesion[len(sucesion)-1]+sucesion[len(sucesion)-2])
        sucesion_fibonacci(posicion-1)
    else:
        print(sucesion[len(sucesion)-1])

sucesion_fibonacci(20)