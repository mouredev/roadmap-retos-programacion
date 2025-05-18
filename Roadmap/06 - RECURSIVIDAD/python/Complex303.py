"""
Recursividad: es cuando una función se llama a sí misma para resolver un problema.
Se usa cuando un problema se puede dividir en problemas más pequeños del mismo tipo.
"""

# def ejemplo():
#     for i in range(100,-1,-1):
#         print(i)

# ejemplo()


def recursividad(num: int):
    if num >= 0:
        print(num)
        recursividad(num -1)
    
recursividad(10)


"""* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición). """


#Factorial de un numero

# Definimos una función llamada factorialNumero que recibe un número entero como argumento
def factorialNumero(numero: int):
    
    # Primer caso: Si el número es menor que 0, no se puede calcular el factorial
    if numero < 0:
        print("El numero debe ser positivo")
        return None  # Terminamos la función y devolvemos None (sin resultado)
    
    # Segundo caso: Si el número es mayor o igual a 1
    elif numero >= 1:
        # Devolvemos el número multiplicado por el factorial del número anterior (n * (n-1)!)
        return numero * factorialNumero(numero - 1)
        # Aquí es donde ocurre la recursividad: la función se llama a sí misma con (numero - 1)
        # y se sigue llamando hasta que llegue a 0
    
    # Tercer caso: Si el número es 0, su factorial es 1 (por definición matemática)
    else:
        return 1


factorial = 5

print(f"El factorial de {factorial} es: {factorialNumero(factorial)}")



#Con bucle
def factoriabucle(num: int):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        print('El resultado debe de ser un numero positivo')
        return None
    else:
        resultado = 1
        for num in range(1, num +1):
            resultado *= num
        return resultado
    
print(factoriabucle(-2))





#Sucesion fibonassi

# Definimos una función llamada sucesion_fibonassi que recibe un número entero
# y devuelve otro entero (por eso el -> int)
def sucesion_fibonassi(num: int) -> int:

    # Si la posición es menor a 0, no es válida para la sucesión de Fibonacci
    if num < 0:
        print("La posicion tiene que ser mayor que 0")
        return 0  # Terminamos la función devolviendo 0

    # Caso base: si la posición es 1, el valor es 0 en Fibonacci (según esta versión)
    if num == 1:
        return 0

    # Caso base: si la posición es 2, el valor es 1 en Fibonacci
    if num == 2:
        return 1

    # Caso recursivo: para cualquier otro número
    else:
        # Se devuelve la suma de los dos números anteriores en la secuencia de Fibonacci
        return sucesion_fibonassi(num - 1) + sucesion_fibonassi(num - 2)

print(sucesion_fibonassi(5))
    

#bucle for
def fibonassi(num: int):
    # Definimos una función llamada 'fibonassi' que recibe un número entero 'num'
    
    num1 = 0  # Primer número de la sucesión de Fibonacci
    num2 = 1  # Segundo número de la sucesión de Fibonacci

    # Usamos un bucle for para repetir 'num' veces
    for i in range(num):
        # Imprimimos el valor actual de 'num1' seguido de un espacio, sin salto de línea
        print(num1, end=" ")

        # Actualizamos ambos valores al mismo tiempo:
        # - 'num1' toma el valor de 'num2'
        # - 'num2' toma la suma de 'num1' (antes de actualizar) y 'num2'
        num1, num2 = num2, num1 + num2

# Llamamos a la función para mostrar los primeros 5 números de Fibonacci
fibonassi(5)





        
        




