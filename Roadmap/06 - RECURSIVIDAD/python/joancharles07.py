def cuentaRegresiva(valor):
    print(valor)
    if(valor!=0):
        cuentaRegresiva(valor -1)
        
def factorial(numero):
    resultado=1
    if numero > 1:
        resultado=factorial(numero - 1) * numero
    else:
        return 1
    return resultado


def fibonacci(terminos):
    resultado=0
    if terminos != 1 and terminos !=0:
        resultado=fibonacci(terminos - 1) + fibonacci(terminos - 2)
    elif terminos == 1 :
        return 1
    else:
        return 0
    
    return resultado

#Prueba de uso comentadas para probarlas de una en una
#cuentaRegresiva(100)
#print(factorial(5))
#print(fibonacci(10))
