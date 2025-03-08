''' 
Ejercisio
'''
def countdown(n: int):
    if n >= 0:
        print(n)
        countdown(n-1)

    
# countdown(100)

'''
Extra   
'''

def factorial(n:int):
    if n < 0:
        print('los numeros negativos no son validos ')
        return 0
    elif n == 0:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))

def fibonacci(n:int):
    if n <= 1:
        return n 
    else: return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(10))