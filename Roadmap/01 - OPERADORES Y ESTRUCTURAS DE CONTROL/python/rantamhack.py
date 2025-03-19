
# OPERADORES ARITMETICOS
# toman los operadores que se le indican y realizan un cálculo matemático

suma = 3 + 5
resta = 5 - 3
multiplicacion = 5 * 3 
division = 5 / 2
modulo = 10 % 3  # Modulo es el resto que nos queda de la división en éste caso es 1
potencia = 10**3 # Eleva a la potencia 3 el pirmer operando que le pasamos 
resultado_entero = 10 // 3 # El resultado de esta división sería el resto como numero entero
print(f"{suma}\n{resta}\n{multiplicacion}\n{division}\n{modulo}\n{potencia}\n{resultado_entero}")

print("\n\n=======================================================================\n\n")

# OPERADORES RELACIONALES
# Son los que relacionan dos elementos entre sí

print(5 > 3) # Devuelve True si es verdadero 
print(5 >= 3) # Devuelve True si es verdadero
print(5 < 3) # Devuelve True si es verdadero
print(5 <= 3) # Devuelve True si es verdadero
print(5 == 3) # Devuelve True solo si los dos operandos son iguales
print(5 != 3) # Devuelve True solo si los dos operandos son diferentes

print("\n\n=======================================================================\n\n")

# OPERADORES LOGICOS
# Se usan basandonos en condiciones

# El operando "and" devuelve True siempre que los dos operandos sean correctos
print((3 + 2 == 5) and (7 * 2 == 14))
# El operando "or" devuelve True siempre que uno de los dos operandos sea correcto
print((3 + 2 == 5) or (7 * 2 == 10))
# El operando "not" devuelve True siempre que uno de los dos operandos sea falso
print(not(10 + 3 == 14))

print("\n\n=======================================================================\n\n")

# OPERADORES DE ASIGNACION
# Son los que se usan para dar valor a una variable por ejemplo
my_variable = 5         # Asignación    
print(my_variable)

my_variable += 1
print(my_variable)      # Suma y Asignación

my_variable -= 1
print(my_variable)      # Resta y Asignación

my_variable *= 2
print(my_variable)      # Multiplicación y Asignación

my_variable /= 2
print(my_variable)      # División y Asignación

my_variable //= 2
print(my_variable)      # Division entera y Asignación

my_variable **= 3                   
print(my_variable)      # Exponente (al cubo) y Asignación

my_variable %= 3
print(my_variable)      # Mòdulo y aAsignación

print("\n\n=======================================================================\n\n")

# OPERADORES DE IDENTIDAD
# Se usan para indicar si dos variables usan la misma ubicación en la memoria
my_new_variable = my_variable

print(f"my_variable is my_new_variable es {my_variable is my_new_variable}")
print(f"my_variable is not my_new_variable es {my_variable is not my_new_variable}")

print("\n\n=======================================================================\n\n")

# OPERADORES DE PERTENENCIA
# Se usan para ver la pertenencia de un elemento a una estructura

print(f"'y' in 'my_variable' = {'y' in 'my_variable'}")
print(f"'y' not in 'my_variable' = {'y' not in 'my_variable'}")

print("\n\n=======================================================================\n\n")

# Operadores de bit
# Realiza operaciones en los operandos bit a bit

a = 10 # 1010 en binario
b = 3  # 0011

print(f"AND: 10 & 3 = {10 & 3}")  # 0010 (2) and bit a bit 1+0=0; 0+0=0; 1+1=1; 0+1=0; los dos bits han de ser uno para dar uno
print(f"OR: 10 | 3 = {10 | 3}")   # 1011 (11) or bit a biy  1|0=1; 0|0=0; 1|1=1; 0|1=1; al menos uno de los dos bits ha de ser uno para dar uno
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001 (9) xor bit a bit 1^0=1; 0^0=0; 1^1=1; 0^1=1; si los dos son iguales el resultado es cero, si uno cambia el resultado es uno
print(f"Not: ~10 = {~10}")        # 0101 Inetercambia el valor bit a bit de cualquiera de los elementos
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 3}")      # 0001 (1) Desplazamos a la derecha 3 bits y rellenamos con ceros por delante
print(f"Desplazamiento a la izquierda: 10 << 3 = {10 << 3}")    #1010000 (80) Cubrimos con ceros por detras las posiciones que nos pide el segundo operando

print("\n\n=======================================================================\n\n")

# ESTRUCTURAS DE CONTROL 
# CONDICIONALES 

my_name = "juan"

if my_name is "luis":
    print("mi nombre es luis")
elif my_name is "juan":
    print("mi nombre es juan")
else:
    print("mi nombre no sale en el programa")

print("\n\n=======================================================================\n\n")

# ESTRUCTURAS DE CONTROL 
# ITERATIVAS

for i in range(1, 11):
    print(i) 

print("\n\n=======================================================================\n\n")

n = 11

while n < 21:
    print(n)
    n += 1

print("\n\n=======================================================================\n\n")

# ESTRUCTURAS DE CONTROL 
# MANEJO DE EXCEPCIONES

try:
    print(1 / 0)
except:
    print("ZeroDivisionError")
finally:
    print("Fin del manejo de excepciones")

print("\n\n=======================================================================\n\n")


for number in range(10, 56):
    if number % 2==0 and number != 16 and number % 3 != 0:
        print(number)
