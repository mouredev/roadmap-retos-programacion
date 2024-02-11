### Aritméticos

suma = 8 + 3
print(suma)
resta = 9 - 5
print(resta)
multiplicacion = 7 * 3
print(multiplicacion)
division = 4 / 2 
print(int(division))
potencia = 4**2
print(potencia)
modulo = 16 % 3
print(modulo)
division_enteros = 18 // 7
print(division_enteros)

### Lógicos
x = 3
y = 5
z = x or y # Imprime por consola uno u otro numero
print(z)
s = x and y # Imprime por consola ambos numeros
print(s)

### Comparación
menor_que = x < y
print(menor_que)
menor_igual = x <= y
print(menor_igual)
mayor_que = x > y
print(mayor_que)
mayor_igual = x >= y
print(mayor_igual)
igual = x == y
print(igual)
distinto = x != y
print(distinto)
igualdad = x is y
print(igualdad)
desigualdad = x is not y
print(desigualdad)

### Asignación

numero = 4
print(numero)
numero += 1
print(numero)
numero -= 2
print(numero)
numero *= 4
print(numero)
numero /= 3
print(int(numero))
numero **= 3
print(int(numero))
numero %= 3
print(int(numero))
numero //= 1
print(int(numero))

### Identidad
new_number = 8
print(f"Mi numero y mi nuevo numero es {numero is new_number} ")
print(f"Mi numero y mi nuevo numero es {numero is not new_number} ")

### Pertenencia
print(f"'e' in 'kike' {'e' in 'kike'}")
print(f"'p' in 'enrique' {'p' not in 'enrique'}")

### Operadores de bit

b = 15 # 1111
c = 7 # 111
print(f"OR: 15|7 {15|7} ")
print(f"XOR: 15^7 {15^7}")
print(f"AND: 15&7 {15&7}")
print(f"El valor desplazado a la izquierda {b << 5}")
print(f"El valor desplazado a la derecha {c >>3}")
print(f"invierte los bits {~c}")

        ### Estructuras de control  ###

### Condicionales

my_var = "Enrique"

if my_var == "Enrique":
    print("Mi variable es Enrique")
elif my_var == "k-90":
    print("Mi variable es k-90")
else:
    print("Mi variable no es Enrique ni k-90")

### iterativas (Loops)
    
for i in range (7):
    print(i)

i = 0

while i >= 6:
    print(i)
    i += 1

### Manejo de Excepciones

try:
    print(7/0)
except:
    print("No se puede dividir entre 0")
finally:
    print("La excepcion ha finalizado")

### Extra ###
    
for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)






