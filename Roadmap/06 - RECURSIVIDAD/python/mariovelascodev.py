def recursividad(num):
    #Si el número introducido es mayor o igual a cero, se imprime y volvemos a llamar a la función restando 1 al nuúmero del parámetro
    if num >= 0:
        print(num)
        recursividad(num - 1)
        
recursividad(100)

#EXTRA
#Factorial
def factorial(num):
    #Si num es igual a 0 o 1 la función devuelve 1
    if num == 0 or num == 1:
        result = 1
    #Si num es mayor que 1 hacemos que result sea igual al producto de dicho número por el resultado de aplicar la misma función menos 1
    elif num > 1:
        result = num * factorial(num - 1)
    return result

print(factorial(5))  
