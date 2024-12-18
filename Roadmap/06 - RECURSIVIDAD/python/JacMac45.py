# Recursividad

# Ejercicio

def cuenta_atras (numero: int):
    if numero >= 0:
        print (numero)
        cuenta_atras(numero - 1)
    
        
    
cuenta_atras (100)

# Extra

def factorial (number: int) -> int:
    if number < 0:
        return 0
    elif number == 0:
        return 1
    else:    
        return number * factorial(number - 1)    
    
    
print(factorial (5))

def fibonacci(number:int) -> int:
    if number <= 0:
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print (fibonacci(10))  # 55 sera el resultado     
