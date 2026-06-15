# Crea una funcion recursiva que imprima numeros del 100 al 0

def hundred_recursive_numbers(number: int):
    if number >= 0:
        print(number)
        hundred_recursive_numbers(number - 1)

hundred_recursive_numbers(100)

# El factorial de un numero
def fact_number(number: int):
        if number <= 1:
            return number
        elif number > 1:
            return number * fact_number(number - 1)

print(fact_number(5))     


# Un elemento conreto segun su posicion en la sucesion de fibonacci
def recursive_fibonacci(n: int):
     if n == 0 or n == 1:
          return n
     elif n == 2:
          return 1
     else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
     
print(recursive_fibonacci(5))