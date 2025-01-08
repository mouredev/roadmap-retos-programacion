for num in range(0,101):
    print(100 - num)
    
    
def calc_fact (entero):
    factorial = 1
    for numero in range  (1,entero+1):
        factorial = factorial * numero 
        
    print(factorial)
    
calc_fact(5)

def fibonacci(pos):
    a = 0
    b = 1
   
    for x in range (0,pos-1):
        
        c = a + b
        a = b
        b = c
    print(a)
        

fibonacci(7)