def recursividad(num):
    #Si el número introducido es mayor o igual a cero, se imprime y volvemos 
    # a llamar a la función restando 1 al nuúmero del parámetro
    if num >= 0:
        print(num)
        recursividad(num - 1)
        
recursividad(100)

#EXTRA
#Factorial
def factorial(num):
    if num < 0:
        return "Error, los factoriales no están definidos para números negativos."
    #Si num es igual a 0 o 1 la función devuelve 1
    elif num == 0 or num == 1:
        return 1
    #Si num es mayor que 1 hacemos que result sea igual al producto de dicho número 
    # por el resultado de aplicar la misma función menos 1
    else:
        return num * factorial(num - 1)

print(factorial(5))
print(factorial(-5))  

#Sucesión Fibonacci
def fibonacci(num_posicion):
    if num_posicion < 0:
        return "El número de la posición no puede ser negativo"
    #Si la posición es menor o igual a 1 devuelve su número de posición
    elif num_posicion <= 1:
        return num_posicion
    #Si el número de posición es mayor que 1, la función se llama a si misma dos veces,
    #para sumar los dos resultados y devolver el total
    else:
        return fibonacci(num_posicion - 1) + fibonacci(num_posicion - 2)

print(fibonacci(10))
print(fibonacci(-3))