
# 1

'''
Operadores
'''
# Operadores Aritméticos
print (f"Suma: 20 + 30 = {20 + 30}")
print (f"Resta: 80 - 30 = {80 - 30}")
print (f"División: 90 / 20 = {90 / 20}")
print (f"Multiplicación: 20 * 30 = {20 * 30}")
print (f"Módulo: 90 % 17 = {90 % 17}") # Resto de la división
print (f"Exponente: 3 ** 4 = {3 ** 4}") # Potencia
print (f"División entera: 90 // 20 = {90 // 20}") # División sin decimales

# Operadores de Comparación
print (f"Igualdad: 20 == 30 es {20 == 30}") # Igual que
print (f"Desigualdad: 20 != 30 es {20 != 30}") # Diferente de
print (f"Mayor que: 20 > 30 es {20 > 30}")
print (f"Menor que: 20 < 30 es {20 < 30}")
print (f"Mayor o igual que: 20 >= 30 es {20 >= 20}") # Mayor o igual que  
print (f"Menor o igual que: 20 <= 30 es {20 <= 30}") # Menor o igual que

# Operadores Lógicos
print (f"AND &&: (20 > 10) and (30 > 20) es {(20 > 10) and (30 > 20)}") # Ambas condiciones deben ser verdaderas para que el resultado sea verdadero
print (f"OR ||: (20 > 10) or (30 < 20) es {(10 > 10) or (30 < 20)}") # Suficiente con que una de las dos condiciones sea verdadera para que el resultado sea verdadero
print (f"NOT !: not(20 > 10) es {not(20 > 10)}") # Invierte el valor de verdad de la condición

# Operadores de Asignación
my_number = 120 # Asignación simple ya que el valor de la derecha se asigna a la variable de la izquierda por medio del operador "="
print (my_number)
my_number += 4 # Esta es una forma corta de escribir my_number = my_number + 4 y esto lo que hace es sumar 4 al valor actual de my_number y luego asignar el resultado a my_number y se puede hacer con cualquier operador aritmético
print (my_number) 
my_number -= 10 # Resta 10 al valor actual de my_number
print (my_number)
my_number *= 2 # Multiplica el valor actual de my_number por 2
print (my_number)
my_number /= 3 # Divide el valor actual de my_number entre 4
print (my_number)
my_number %= 7 # Calcula el resto de la división del valor actual de my_number entre 3
print (my_number)
my_number **= 3 # Eleva el valor actual de my_number a la potencia de 3
print (my_number)
my_number //= 2 # Realiza una división entera del valor actual de my_number entre 2
print (my_number)

# Operadores de Identidad
my_new_number = 108.0
print (f"my_number is my_new_number: {my_number is my_new_number}") # Devuelve True si ambas variables apuntan al mismo objeto en memoria a través del operador "is" cuya función es comprobar la identidad de los objetos y en este caso devuelve False porque aunque ambos tienen el mismo valor, tienen diferente posición en memoria.
my_new_number = my_number
print (f"my_number is my_new_number: {my_number is my_new_number}")
print (f"my_number is not my_new_number: {my_number is not my_new_number}") # En este caso devuelve False porque ambas variables apuntan al mismo objeto en memoria y el operador "is not" comprueba que no son el mismo objeto en memoria.

# Operadores de Pertenencia
print (f" 'a' in 'juan' = {'a' in 'juan'}") # Devuelve True si el valor de la izquierda se encuentra en el valor de la derecha
print (f" 'm' not in 'juan' = {'m' not in 'juan'}") # Devuelve True si el valor de la izquierda no se encuentra en el valor de la derecha

# Operadores de bit
j = 7 # En binario es 0111 (Este es en 4 bits)
k = 3 # En binario es 0011 (Este es en 4 bits)
print (f"AND: 7 & 3 = {7 & 3}") # Operador AND a nivel de bits, compara cada bit de los dos números y devuelve un nuevo número donde cada bit es 1 si ambos bits son 1, de lo contrario es 0. En este caso 0111 & 0011 = 0011 que es 3 en decimal.
print (f"OR: 7 | 3 = {7 | 3}") # Operador OR a nivel de bits, compara cada bit de los dos números y devuelve un nuevo número donde cada bit es 1 si al menos uno de los bits es 1, de lo contrario es 0. En este caso 0111 | 0011 = 0111 que es 7 en decimal.
print (f"XOR: 7 ^ 3 = {7 ^ 3}") # Operador XOR a nivel de bits, compara cada bit de los dos números y devuelve un nuevo número donde cada bit es 1 si los bits son diferentes, de lo contrario es 0. En este caso 0111 ^ 0011 = 0100 que es 4 en decimal.
print (f"NOT: ~7 = {~7}") # Operador NOT a nivel de bits, invierte todos los bits del número. En este caso ~0111 = 1000 que es -8 en decimal (~x = -(x + 1)).
print (f"Desplazamiento a la derecha: 7 >> 1 = {7 >> 1}") # Desplaza todos los bits del número a la derecha una posición. En este caso 0111 >> 1 = 0011 que es 3 en decimal. Una forma sencilla de verlo es que el desplazamiento a la derecha es equivalente a una división entera por 2: (7÷2)=3
print (f"Desplazamiento a la izquierda: 7 << 1 = {7 << 1}") # Desplaza todos los bits del número a la izquierda una posición. En este caso 0111 << 1 = 1110 que es 14 en decimal. Una forma sencilla de verlo es que el desplazamiento a la izquierda es equivalente a una multiplicación por 2: (7*2)=14


# 2

'''
Estructuras de Control
'''

# Condicionales
my_name = "JuanmaDev"

if my_name == "JuanmaDev": # Si my_name es igual a "Juanma"
    print ("Hola JuanmaDev") # Se ejecuta este bloque de código
elif my_name == "Manuel": # Si no se cumple la condición anterior, pero my_name es igual a "Manuel"
    print ("Hola Manuel") # Se ejecuta este bloque de código
else: # Si no se cumple ninguna de las condiciones anteriores
    print ("Hola desconocido") # Se ejecuta este bloque de código

# Iterativas
for i in range(5): # Bucle for que itera desde 0 hasta 4 (5 no incluido)
    print (f"Iteración {i}") # Imprime el valor de i en cada iteración desde 0 hasta 4 ya que range(5) genera una secuencia de números desde 0 hasta 4

i = 0
while i < 5: # Bucle while que se ejecuta mientras i sea menor que 5
    print (f"Iteración {i}") # Imprime el valor de i en cada iteración
    i += 1 # Incrementa i en 1 en cada iteración para evitar un bucle infinito

# Manejo de Excepciones
try: # Intenta ejecutar el siguiente bloque de código
    print (10 / 2) # Esto genera una excepción de división por cero
except: # Si se genera una excepción, se ejecuta este bloque de código
    print ("Se ha producido un error") # Imprime un mensaje de error
finally: # Este bloque de código se ejecuta siempre, haya o no una excepción
    print ("Ha finalizado el manejo de excepciones") # Imprime un mensaje indicando que ha finalizado el manejo de excepciones


'''
Ejercicio EXTRA
'''
for number in range (10, 56): # Itera desde 10 hasta 55 (56 no incluido)
    if number % 2 == 0 and number != 16 and number % 3 != 0: # Si el número es par, no es 16 y no es múltiplo de 3
        print (number)


