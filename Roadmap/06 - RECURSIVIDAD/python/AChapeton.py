def recursiveFunction(value):
  print(value)
  if(value != 0):
    recursiveFunction(value - 1)


recursiveFunction(100)


# DIFICUTAL EXTRA

def obtenerFactorial(factorial):
  if(factorial < 0):
    return -1
  elif(factorial == 0):
    return 1
  else:
    return (factorial * obtenerFactorial(factorial - 1))

print('Factorial: ', obtenerFactorial(10))

def fibonacci(position):
  if(position <= 1):
    return 1
  result = fibonacci(position - 1) + fibonacci(position -2)
  return result

print('fibonacci: ', fibonacci(7))