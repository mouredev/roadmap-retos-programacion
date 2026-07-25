#tipos de operadores en python
#operadores aritmeticos
suma = 2+2
resta = 2-2
multiplicacion = 2*2
division = 2/2
modulo = 2%2 #el residuo o resto  de la division
division_entera = 2//2 #devuelve la parte entera de la division
potencia = 2**2

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(division_entera)
print(potencia) 

#operadores de comparacion

igual_a = 2 == 2
distinto_de = 2 != 2
mayor_que = 2 > 2
menor_que = 2 < 2
mayor_o_igual_que = 2 >= 2
menor_o_igual_que = 2 <= 2

print(igual_a) 
print(distinto_de) 
print(mayor_que) 
print(menor_que) 
print(mayor_o_igual_que) 
print(menor_o_igual_que)

#operadores logicos
And = True and True
Or = True or False
Not = not True

print(And)
print(Or)
print(Not)

#operadores de asignacion
asignacion = 2 
asignacion += 2
asignacion -= 2
asignacion *= 2
asignacion /= 2
asignacion //= 2
asignacion %= 2
asignacion **= 2

print(asignacion)

#operadores bit a bit
bit_a_bit_and = 2 & 2
bit_a_bit_or = 2 | 2
bit_a_bit_xor = 2 ^ 2
complemento = ~2
desplazar = 2 << 2
desplazar_a_derecha = 2 >> 2

print(bit_a_bit_and)
print(bit_a_bit_or)
print(bit_a_bit_xor)
print(complemento)
print(desplazar)
print(desplazar_a_derecha)

#operadores de identidad
identidad = 2 is 2
no_identidad = 2 is not 2

print(identidad)
print(no_identidad)

#operadores de pertenencia
pertenece = 2 in [1, 2, 3]
no_pertenece = 2 not in [1, 4, 3]

print(pertenece)
print(no_pertenece)

#operadores de ternario 
edad = 18
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)  # Imprimirá: Eres mayor de edad

#Estructuras de control
#condicionales
edad = 18
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Acabas de cumplir la mayoría de edad")
else:
    print("Eres menor de edad")

#bucles
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

#otras estructuras de control

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        break
    print(numero)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

def mi_funcion():
    # Aquí iría el código de la función, pero por ahora solo vamos a poner pass
    pass

if 1 == 1:
    pass  # Hacer algo
else:
    pass  # No hacer nada en este caso

print(mi_funcion)

#programa extra 
for i in range(10, 56):
    if i == 16:
        continue
    if i % 3 == 0:
        continue
    print(i)