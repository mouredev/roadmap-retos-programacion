


def numeros_recursivo(n):

    if n > 100:
        return "fin de la lista"
    else:
        print (n)
        return numeros_recursivo (n+1)
    
print (numeros_recursivo(0))


# Ejercicios extra dificultad

def factorial(n):

    if n == 0:
     return 1
    else:
       return (n * factorial(n-1)) 
    
print (factorial(9))



def fibonacci (n:int) -> int:
   if n <= 0:
    print ("La posicion tiene que se mayor a 0")
    return 0
   elif n == 1:
    return 0
   elif n == 2:
    return 1
   else:
    return fibonacci(n-1) + fibonacci (n-2)


print (f"el numero en la posicion ingresada es {fibonacci(10)}")

   
      
      
   
      






