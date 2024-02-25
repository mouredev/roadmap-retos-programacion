def recur_1al100(n): return n if n < 0 else print(n) or recur_1al100(n-1)
recur_1al100(100)

print()

# EXTRA
#   factorial de un numero
def factorial(n): return 1 if (n==1 or n==0) else n * factorial(n - 1);
print(factorial(3))

print()

#   posicion de numero fibonacci
def valor_fibonacci(n):
  if n <= 0:
    return "La posición tiene que ser mayor que cero"
  elif n == 1: return 0
  elif n == 2: return 1
  else: 
    return valor_fibonacci(n-1) + valor_fibonacci(n-2)
print(valor_fibonacci(0))
