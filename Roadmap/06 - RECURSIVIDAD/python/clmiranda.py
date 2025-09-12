# RECURSIVIDAD

# FUNCIÓN RECURSIVA QUE IMPRIMA LOS NÚMEROS DEL 100 AL 0
def recursion_100_to_0(num: int) -> str:
    print(num, end=" ")
    if num != 0:
        recursion_100_to_0(num - 1)

recursion_100_to_0(100)



# EJERCICIO - DIFICULTAD EXTRA


# CALCULAR EL FACTORIAL DE UN NÚMERO CONCRETO (LA FUNCIÓN RECIBE ESE NÚMERO)
def recursion_factorial(num: int) -> int:
    return num if num == 1 else num * recursion_factorial(num - 1)

print(f"\nEl factorial de 7 es: {recursion_factorial(7)}")



# CALCULAR EL VALOR DE UN ELEMENTO CONCRETO (SEGÚN SU POSICIÓN) EN LA SUCESIÓN DE FIBONACCI
def recursion_fibonacci(num: int) -> int:
    return 1 if num in [1, 2] else recursion_fibonacci(num - 1) + recursion_fibonacci(num - 2)

print(f"La posición 4 de la serie Fibonacci es: {recursion_fibonacci(4)}")