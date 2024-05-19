

#operadore aritmeticos
print (f"suma: 10+3 = {10+3}")
print (f"resta: 10-3 = {10-3}")
print (f"mulriplicacion: 10*3 = {10*3}")
print (f"division: 10/3 = {10/3}")
print (f"modulo: 10%3 = {10%3}")
print (f"exponente: 10**3 = {10**3}")
print (f"division entera: 10//3 = {10//3}")

#operadores de comparacion

print (f"igualdad 10 == 3 es {10 == 3}")
print (f"desigualdad 10 != 3 es {10 != 3}")
print (f"mayor que 10 > 3 es {10 > 3}")
print (f"menor que 10 < 3 es {10 < 3}")
print (f"mayor o igual que 10 >= 3 es {10 > 3}")
print (f"menor o igual que 10 <= 3 es {10 < 3}")

#operadores logicos

print (f"AND &&: 10 + 3 == 13 and 5 -1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print (f"OR: 10 + 3 == 13 or 5 -1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")
print (f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")


# operadores de asignacion 
my_number = 11 #asignacion
print (my_number)
my_number += 1
print (my_number)
my_number -= 1
print (my_number)
my_number *= 2
print (my_number)
my_number /= 2
print (my_number)
my_number %= 2
print (my_number)
my_number **= 1
print (my_number)
my_number //= 1

# operadores de identidad 
my_new_number = my_number
print (f"my_number is my_new_number es {my_number is my_new_number}")
print (f"my_number is not my_new_number es {my_number is not my_new_number}")

#operadores de pertenecia 

print (f" ' o ' in 'Simon' = {'o' in 'Simon'}")
print (f" ' h ' not in 'Simon' = {'o' not in 'Simon'}")

# operadores de bit

a = 10 # 1010
b = 3 # 0011
print (f"AND: 10 & 3 = {10 & 3}")
print (f"OR: 10 | 3 = {10 | 3}")
print (f"XOR: 10 ^ 3 = {10 ^ 3}")
print (f"NOT: 10 ~ 3 = {~10}")
print (f"desplazamiento a la derecha : 10 >> 2 = {10 >> 2}")
print (f"desplazamiento a la izquierda : 10 << 2 = {10 << 2}")


#estructuras de control

# Condicionales

my_string = "simons"
if my_string == "simons":
   print ("my_string es 'simons'")
elif my_string == "Brais":
   print ("my_string es brais")
else: 
   print ("my_string no es 'simons' ni 'brais'")

 # iterativas 

for i in range(11):
   print (i)

i = 0
while i <= 10:
   print (i)
   i+=1

# manejo de exepciones
try:
 print (10/0)
except:
   print ("se ha prodcuido un error")
finally:
   print ("ha finalizado el manejo de exepciones")


#extra

for number in range(10, 56):
   if number % 2 == 0 and number != 16 and number % 3 != 0:
      print (number)