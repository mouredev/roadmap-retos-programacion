### Python Recursion ###

def count_back(num):
  print(num)
  
  if num == 0:
    return
  else:
    count_back(num - 1)
    
  
#! Optional Challenge

#** Factorial

def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num - 1)
  
my_num_factorial = factorial(8)
print(my_num_factorial)

#** Fibonacci Value

def fibonacci_value(pos):
  if pos < 0:
    return 'Value must be positive'
  
  if pos == 1:
    return 1
  
  if pos == 0:
    return 0
  
  return fibonacci_value(pos - 1) + fibonacci_value(pos - 2)

print(fibonacci_value(20))
  