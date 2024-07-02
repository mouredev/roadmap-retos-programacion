# EJERCICIOS

# Tipos de operadores: Aritméticos, Lógicos, Relacionales, asignación, pertenencia, identidad
# Asignación: 

operador_a = 4
operador_b = 2

# Aritméticos
print("--- OPERADORES ARITMÉTICOS---")
print(f"Suma: {operador_a + operador_b} ")
print(f"Resta: {operador_a - operador_b}")
print(f"División: {operador_a / operador_b}")
print(f"Multiplicación: {operador_a * operador_b}")
print(f"Resto: {operador_a % operador_b}")
print(f"Potencia: {operador_a ** operador_b}")

# Lógicos
print("--- OPERADORES LÓGICOS ---")
print("si primer elemento es 2 y si segundo elemento es 4")
print(operador_a == 2 and operador_b == 4)
print("si primer elemento es 2 O segundo elemeto es 5")
print(operador_a == 2 or operador_b ==5 )
print("si primer elemento NO es 2")
print(not operador_a == 4)


# Relacionales
print("--- OPERADORES RELACIONALES ---")
print(f"2 es mayor que 4: {operador_b > operador_a}")
print(f"2 es menor que 4: {operador_b < operador_a}")
print(f"2 es igual que 4: {operador_b == operador_a}")
print(f"2 No es igual que 4: {operador_b != operador_a}")
print(f"2 es menor o igual que 4: {operador_b <= operador_a}")
print(f"2 es menor o igual que 4: {operador_b >= operador_a}")


# Asignación 

print("--- OPERADORES DE ASIGNACIÓN ---")

contador = 6 #asigna un valor
print(contador) 
contador += 1 #incremeta valor en 1 y lo asigna a la variable
print(contador) 
contador -= 1 #reduce valor en 1 y lo asigna a la variable 
print(contador)
contador *= 2
print(contador)
contador /= 2
print(contador)
contador %= 2
print(contador)


# Estructuras de control:  condicionales (if), iterativas (for, while), excepciones

a = 4
b = 3
c = 5

# CONDICIONALES 
if a == 3:
    print("a es igual a cuatro")
elif b != 5:
    print("b no es igual a cinco")
elif c == 4:
    print ("c es igual a cuatro")
else: 
    print("hemos llegado al final")

# ITERATIVAS: 
var = "fborjalv"

for i in var:
    print(i)

count = 0
while count < len(var):
    print(var[count])
    count +=1

try:
    print(10/0)
except:
    print("no se puede divir por cero")
finally:
    print("Fin al control de excepciones ")

# DIFICULTAD EXTRA: 

for num in range(10,56):
    if num % 2 == 0 and not (num == 16 or num % 3 == 0):
        print(num)


