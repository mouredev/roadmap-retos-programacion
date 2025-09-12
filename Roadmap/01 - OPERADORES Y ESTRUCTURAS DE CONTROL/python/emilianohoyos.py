"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
"""
operadores
"""
# Operadores aritmeticos
print(f"suma : 10+4={10+4}")
print(f"resta : 10-4={10-4}")
print(f"division : 10/4={10/4}")
print(f"multiplicacion : 10*4={10*4}")
print(f"modulo : 10%4={10%4}")
print(f"exponencial : 10**4={10**4}")
print(f"division entera : 10//4={10//4}")

# Operadores de comparación

print(f"Igualdad : 10==3 es {10==3}")
print(f"Negación : 10!=3 es {10!=3}")
print(f"Mayor que : 10>3 es {10>3}")
print(f"Menor que : 10>3 es {10>3}")
print(f"Mayor igual que : 10>=3 es {10>=3}")
print(f"Menor igual que : 10<=3 es {10<=3}")

#operadores Lógicos
print(f"And &&: 10+3==13 and 5-1==4 es {10+3==13 and 5-1==4 }")
print(f"Or &&: 10+3==14 or 5-1==4 es {10+3==14 or 5-1==4 }")
print(f"Not &&: 10+3==14 { not 10+3==14 }")

#operadores de asignación
my_number=11 #asignacion
print(my_number)
my_number+=1 #suma y asignacion
print(my_number)
my_number-=1 #resta y asignacion
print(my_number)
my_number*=2 #multiplicacion y asignacion
print(my_number)
my_number/=2 #division y asignacion
print(my_number)
my_number%=2 #modulo y asignacion
print(my_number)
my_number**=2 #modulo y asignacion
print(my_number)
my_number//=2 #division entera y asignacion
print(my_number)

# Operadores de identidad
my_new_number=my_number
print(f"Muy number is my_new_number es {my_number is my_new_number}")
print(f"Muy number is NOT my_new_number es {my_number is not my_new_number}")

#operadores de pertenencia
print(f"'y' in hoyos= {'y' in 'hoyos'}")
print(f"'b' not in hoyos= {'b' not in 'hoyos'}")

#operadores de bit
a=10 #1010
b=3 #  11

print(f"AND: 10 & 3={10&3}")#0010
print(f"OR: 10 | 3={10|3}")#1011
print(f"XOR: 10 ^ 3={10^3}")#1001
print(f"NOT: ~10={~10}")#0110
print(f"Desplazamiento a la derecha: 10>>2={10>>2}")#0010
print(f"Desplazamiento a la izquierda: 10<<2={10<<2}")#101000


"""
Estructuras de control
"""
#Condicionales
my_string="Emilianohoyos"
if my_string=="Emilianohoyos":
    print("my_string es 'EmilianoHoyos'")
elif my_string=="Brais":
    print("my_string es 'Brais'")
else:
    print("my_string No es 'EmilianoHoyos' ni 'Brais'")

#iterativa

for i in range(11):
    print(i)

i=0
while i<=10:
    print(i)
    i+=1

#manejo de excepciones
try:
    print(10/0)
except:
    print("se ha producido un error")
finally:
    print('ha finalizado el manejo de excepciones')

"""
extra
"""
for number in range(10,56):
        if number%2==0 and number!=16 and number%3!=0:
            print(number)

