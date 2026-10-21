suma = 4 + 4
resta = 10 - 7
multiplicacion = 13 * 3
division = 12 / 9
modulo = 10 % 2 
comparativo = 2 < 1
igualdad = 2 == 2
operando_or= 1 or 1
operando_or_v2= 0 or 0
operando_and = 1 and 1
operando_and_v2 = 1 and 0
operando_desigualdad = 2 != 0
potencia = 2 ** 3
division_redondeada = 6 // 4
operando_not = not 3 + 7 == 12

# Operador de identidad

my_new_number = potencia is operando_not
my_new_number_isnot = potencia is not operando_not

# pertenencia

palabra = 'e' in 'Leonardo'
palabra2 = 'e' not in 'Leonardo'

# bit
a = 10 # 1 0 1 0
b = 4  # 0 1 0 0

bit_and = 10 & 4
bit_or = 10 | 4
bit_xor = 10 ^ 4
bit_not = ~10 
bit_deplazamiento_der = 10 >> 2
bit_deplazamiento_izq = 10 << 2

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(comparativo)
print(igualdad)
print(operando_or)
print(operando_or_v2)
print(operando_and)
print(operando_and_v2)
print(operando_desigualdad)
print(potencia)
print(division_redondeada)
print(operando_not)
print(my_new_number)
print(my_new_number_isnot)
print(palabra)
print(palabra2)
print(bit_and)
print(bit_or)
print(bit_xor)
print(bit_not)
print(bit_deplazamiento_der)
print(bit_deplazamiento_izq)

# estructuras de control

if suma != 8:
    print("Condicional if dice False")
elif suma == 8:
    print("Condicional if dice True")
else:
    print("Condicional if dice False")
    
# iterativas (bucles)

for i in range(10):
    print(i+1)
    
print()
i = 0
while i <= 10:
    print(i)
    i+=1

# excepciones
try:
    print()
    print(10/1)
except:
    print("Error")
finally:
    print("Ha finalizado el manejo de la excepcion")
    
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
for i in range(10,56):
    if i%2 == 0 and i != 16 and i%3 !=0:
        print(i)
    