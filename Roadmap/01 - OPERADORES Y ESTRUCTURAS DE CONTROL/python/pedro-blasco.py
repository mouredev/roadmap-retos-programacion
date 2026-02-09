a = float(input("Introduce el valor de a: ")) # El input devuelve un string con el valor introducido por el usuario
b = float(input("Introduce el valor de b: ")) # El input devuelve un string con el valor introducido por el usuario


"""
Operadores Aritmeticos:
"""
Suma = a + b # La suma devuelve el resultado de sumar a y b
Resta = a - b # La resta devuelve el resultado de restar b a a
Multiplicacion = a * b # La multiplicacion devuelve el resultado de multiplicar a por b
Division = a / b # La division devuelve un numero decimal aunque el resultado sea un numero entero
Division_Entera = a // b # La division entera devuelve el resultado de dividir a entre b sin decimales, redondeando hacia abajo
Exponente = a ** b # El exponente devuelve el resultado de elevar a a la potencia de b
Modulo = a % b # El modulo devuelve el resto de la division entre a y b

"""
Operadores de Asignacion:
"""

x = 5 # El operador de asignacion "=" asigna el valor de 5 a la variable x
x += 3 # El operador de asignacion "+=" suma 3 al valor actual de x y asigna el resultado a x
x -= 2 # El operador de asignacion "-=" resta 2 al valor actual de x y asigna el resultado a x
x *= 4 # El operador de asignacion "*=" multiplica el valor actual de x por 4 y asigna el resultado a x
x /= 2 # El operador de asignacion "/=" divide el valor actual de x entre 2 y asigna el resultado a x
x //= 3 # El operador de asignacion "//=" divide el valor actual de x entre 3 sin decimales y asigna el resultado a x
x **= 2 # El operador de asignacion "**=" eleva el valor actual de x a la potencia de 2 y asigna el resultado a x
x %= 4 # El operador de asignacion "%=" calcula el resto de dividir el valor actual de x entre 4 y asigna el resultado a x

"""
Operadores de Comparacion:
"""

a_igual_a_b = a == b # El operador de comparacion "==" devuelve True si a es igual a b, False en caso contrario
a_par = a % 2 == 0 # El operador de comparacion "==" devuelve True si a es par, False en caso contrario
a_distinto_de_b = a != b # El operador de comparacion "!=" devuelve True si a es distinto de b, False en caso contrario
a_menor_que_b = a < b # El operador de comparacion "<" devuelve True si a es menor que b, False en caso contrario
a_menor_o_igual_a_b = a <= b # El operador de comparacion "<=" devuelve True si a es menor o igual a b, False en caso contrario
a_mayor_que_b = a > b # El operador de comparacion ">" devuelve True si a es mayor que b, False en caso contrario
a_mayor_o_igual_a_b = a >= b # El operador de comparacion ">=" devuelve True si a es mayor o igual a b, False en caso contrario

"""
Operadores Logicos:
"""

# El operador logico "and" devuelve True si ambas condiciones son True, False en caso contrario

condicion1 = a > 0 and b > 0 # Devuelve True si a es mayor que 0 y b es mayor que 0, False en caso contrario

# El operador logico "or" devuelve True si al menos una de las condiciones es True, False en caso contrario

condicion2 = a > 0 or b > 0 # Devuelve True si a es mayor que 0 o b es mayor que 0, False en caso contrario

# El operador logico "not" devuelve True si la condicion es False, False si la condicion es True

condicion3 = not(a > 0) # Devuelve True si a no es mayor que 0, False si a es mayor que 0

"""
Operadores de Pertenencia e Identidad:
"""

# El operador de pertenencia "in" devuelve True si el elemento esta en la secuencia, False en caso contrario

y = [1, 2, 3, 4, 5] # Lista de numeros del 1 al 5
pertenencia = 3 in y # Devuelve True si el numero 3 esta en la lista y, False en caso contrario

# Se puede utilizar "not in" para comprobar si un elemento no esta en la secuencia

# El operador de identidad "is" devuelve True si ambas variables apuntan al mismo objeto en memoria, False en caso contrario

a = [1, 2, 3] # Lista de numeros del 1 al 3
b = [3, 2, 1] # Lista de numeros del 3 al 1
identidad = a is b # Devuelve False porque a y b son listas diferentes en memoria, aunque tengan los mismos elementos
indentidad2 = a is not b # Devuelve True porque a y b son listas diferentes en memoria, aunque tengan los mismos elementos

# No creo necesario agregar los operadores bit a bit porque son mas avanzados y actualmente no los comprendo

# Print de todos los ejemplos anteriores para comprobar que funcionan correctamente
print("Operadores Aritmeticos:")
print("Suma:", Suma)
print("Resta:", Resta)
print("Multiplicacion:", Multiplicacion)
print("Division:", Division)
print("Division Entera:", Division_Entera)
print("Exponente:", Exponente)
print("Modulo:", Modulo)
print("\nOperadores de Asignacion:")
print("x:", x)
print("\nOperadores de Comparacion:")
print("a igual a b:", a_igual_a_b)
print("a es par:", a_par)
print("a distinto de b:", a_distinto_de_b)
print("a menor que b:", a_menor_que_b)
print("a menor o igual a b:", a_menor_o_igual_a_b)
print("a mayor que b:", a_mayor_que_b)
print("a mayor o igual a b:", a_mayor_o_igual_a_b)
print("\nOperadores Logicos:")
print("condicion1 (a > 0 and b > 0):", condicion1)
print("condicion2 (a > 0 or b > 0):", condicion2)
print("condicion3 (not(a > 0)):", condicion3)
print("\nOperadores de Pertenencia e Identidad:")
print("pertenencia (3 in y):", pertenencia)
print("identidad (a is b):", identidad)
print("identidad2 (a is not b):", indentidad2)

""" 
DIFICULTAD EXTRA (OPCIONAL): Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 """
 
print("\nDificultad Extra:")
print("\nNúmeros comprendidos entre 10 y 55, pares, y que no son ni el 16 ni múltiplos de 3:")
for i in range(10, 56): # Itera numeros desde el 10 al 55
    if i % 2 == 0 and i != 16 and i % 3 != 0: # Comprueba que el numero es par, no es 16 y no es multiplo de 3
        print(i) # Imprime el numero si cumple las condiciones