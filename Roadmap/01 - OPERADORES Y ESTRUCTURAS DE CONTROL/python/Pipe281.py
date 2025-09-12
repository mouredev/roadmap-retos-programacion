#01 OPERADORES Y ESTRUCTURAS DE CONTROL

#Aritmeticos
edad = 2024 - 1990
ingreso_anual = 500000 * 12 
a = 10 + 5
b = 10 * 5
c = 12 / 5
d = 16 % 5 #Residuo
e = 16 ** 5 #Potencia
f = 16 // 5 # División con numeros enteros 


#Lógicos + Comparación
if edad >= 18 and  ingreso_anual >=  30000000:
    print("Tu sueldo alcanza para realizar un prestamo")
else:
    print("Tu sueldo NO alcanza para realizar un prestamo, muy pobre, Lo siento 8(")

if edad >= 18 or ingreso_anual >=  3000000:
    print("Tu sueldo alcanza para realizar un prestamo")
else:
    print("Tu sueldo NO alcanza para realizar un prestamo, muy pobre, Lo siento 8(")

usuario_autenticado = False

if not usuario_autenticado:
    print("Acceso denegado. Debes iniciar sesión.")
else:
    print("¡Bienvenido!")

# Asignación (Toma los valores ingresados mas arriba y los calcula)
edad = 33
a += 5
b -= 5
c *= 5    
d /= 5

#Operadores de Identidad
a = 10
b = 20
c = 10

print(a is b) # Muestra False
print(a is c) # Muestra True
print(a is not b) # Muestra True

#Operadores Pertenencia
a = [1,2,3,4,5]

print(2 in a) # Muestra True
print(6 in a) # Muestra False
print(6 not in a) # Muestra True

#Operadores Bit a Bit
"No los entiendo"

#Ejemplos
a = [b, c, d, e]
for numeros in a:
    print(numeros)

for a in range():
    print(a)