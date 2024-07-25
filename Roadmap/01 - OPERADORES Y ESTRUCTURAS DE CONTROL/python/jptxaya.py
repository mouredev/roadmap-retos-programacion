
my_integer_1 = 3
my_integer_2 = 2
#Operadores aritmeticos
print(my_integer_1 + my_integer_2)
print(my_integer_1 - my_integer_2)
print(my_integer_1 * my_integer_2)
print(my_integer_1 / my_integer_2)
print(my_integer_1 // my_integer_2)
print(my_integer_1 % my_integer_2)
print(my_integer_1 ** my_integer_2)

#Operadores logicos

my_boolean_1 = True
my_boolean_2 = False
print(my_boolean_1 and my_boolean_2)
print(my_boolean_1 or my_boolean_2)
print (not my_boolean_1)

#Operadores comparacion
print( my_integer_1 == my_integer_2)
print( my_integer_1 != my_integer_2)
print( my_integer_1 > my_integer_2)
print( my_integer_1 >= my_integer_2)
print( my_integer_1 < my_integer_2)
print( my_integer_1 <= my_integer_2)

#Operadores de Bit

print(my_integer_1 & my_integer_2)
print(my_integer_1 | my_integer_2)
print(my_integer_1 ^ my_integer_2)
print(my_integer_1 >> my_integer_2)
print(my_integer_1 << my_integer_2)

#Operadores de asignacion
my_integer_1 += 2
my_integer_1 -= 2
my_integer_1 *= 2
my_integer_1 /= 2
my_integer_1 //= 2
my_integer_1 **= 2
my_integer_2 &= 2
my_integer_2 |= 2
my_integer_2 ^= 2
my_integer_2 >>= 2
my_integer_2 <<= 2

#Operadores de pertenencia
a = [3,4,5]
print(3 in a)
print(3 not in a)

#Operadores de identidad
a = 3
b = 3
print (a is b)
print( a is not b)

#Estructuras de control

if a > 3:
    print("A mayor que 3")
elif a < 3:
    print("A es menor que 3")
else:
    print("A es igual que 3")
    
match a:
    case 1:
        print("case 1")
    case 2:
        print("case 2")
    case 3:
        print("case 3")
    
#While y for
while a < 10:
    print(f"while: {a}")
    if a == 8:
        break
    a += 1

print("******************")

for elem in range(0,10):
    print(f"for {elem}")

#Exception
try:
    print("try")
    a = a / 0
except:
    print("Excepcion")
else:
    print("Else exception")
finally:
    print("Finally exception")
    
print("Dificultad Extra")
for elem in range (10,56):
    if elem % 2 == 0 and elem != 16 and not elem % 3 == 0:
        print(elem)
