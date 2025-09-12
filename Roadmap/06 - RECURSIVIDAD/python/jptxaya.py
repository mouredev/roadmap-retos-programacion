
#Recursividad
def funcion_contar_atras(mint):
    if mint < 0:
        return
    print(mint)
    funcion_contar_atras(mint - 1)

funcion_contar_atras(100)

#Dificultad Extra
print("Dificultad Extra")
def factorial(my_int):
    if my_int == 1:
        return 1
    result = factorial(my_int -1) * my_int
    return result

print("Calcular factorial")
factor = int(input("Introducir numero a calcular:"))
print(f"Resultado:{factorial(factor)}")

def posicion_fibonacci(my_pos):
    if my_pos == 0:
        return 0
    elif my_pos == 1:
        return 1
    else:
        return posicion_fibonacci(my_pos - 2) + posicion_fibonacci(my_pos - 1)
    

print("Calcular numero en posicion Fibonacci")
posicion = int(input("Introducir posicion:"))
print(f"Resultado:{posicion_fibonacci(posicion)}")
