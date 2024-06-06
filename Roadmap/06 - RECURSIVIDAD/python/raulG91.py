
def print_numbers(number):
    
    if number == 0:
        print(number)
    else:
        print(number)
        print_numbers(number -1)    
        
print_numbers(100)        


def factorial(number):
    
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
 
print("Factorial")    
print(factorial(10))    

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)


print("Fibonacci")
print(fibonacci(10))