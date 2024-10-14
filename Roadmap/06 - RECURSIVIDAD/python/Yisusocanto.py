#imprimir numero desde el 100 al 0
def imprimir(n):
	if n >= 0:
		print(n)
		imprimir(n-1)

imprimir(100)		

#encontrar el factorial de un numero
def calcular(n):
	if n == 1 or n == 2:
		return(n)
	else:
		return n * calcular(n-1)

	    
print(f"el factorial de 4 es: ", calcular(4))

#valor de una posicion de fibonacci
def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)


print(fibo(6))			
