def print_numbers(num):
  if num < 0:
    return
  print(num)
  print_numbers(num - 1)

print_numbers(100)

#Dificultad Extra 

#Factorial
def factorial(num):
  if num == 0 or num == 1:
    return 1
  return num * factorial(num - 1)

print(factorial(23))  

#Fibonacci
def fibonacci(num):
  if num <= 1:
    return num
  return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(23))  