a = 2
b = 2

#Operadores Aritméticos
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo= a % b
potencia = a ** b

print("Operadores aritmeticos:","\n Suma:", suma, "\n Resta:", resta, "\n Multiplicación:", multiplicacion, "\n División:", division , "\n División entera:", division_entera, "\n Módulo:", modulo, "\n Potencia:", potencia)

#Operadores logicos
op_and = (a > 1) and (b > 1)
op_or = (a > 1) or (b < 1)
op_not = not(a > 1)

print("\nOperadores lógicos:","\n AND:", op_and, "\n OR:", op_or, "\n NOT:", op_not)

#Operadores de comparación
igualdad = (a == b)
diferencia = (a != b)
mayor_que = (a > b)
menor_que = (a < b)
mayor_o_igual = (a >= b)
menor_o_igual = (a <= b)

print("\nOperadores de comparación:","\n Igualdad:", igualdad, "\n Diferencia:", diferencia, "\n Mayor que:", mayor_que, "\n Menor que:", menor_que, "\n Mayor o igual:", mayor_o_igual, "\n Menor o igual:", menor_o_igual)

#Operadores de asignación
x = 5
ope_asig= ['+=', '-=', '*=', '/=', '//=', '%=', '**=']

for i in ope_asig:
    print(f"\nvalor anterior de x: {x}")
    exec(f"x {i} 2")
    print(f"Operacion realizada x{i}2: x = {x}")

#Operadores de identidad
y = x
op_is = (x is y)
op_is_not = (x is not b)
print("\nOperadores de identidad:","\n is:", op_is, "\n is not:", op_is_not)

#Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
op_in = (3 in lista)
op_not_in = (6 not in lista)
print("\nOperadores de pertenencia:","\n in:", op_in, "\n not in:", op_not_in)

#Operadores a nivel de bits
and_bit = a & b 
or_bit = a | b 
xor_bit = a ^ b
not_bit = ~a
left_shift = a << 1
right_shift = a >> 1
print("\nOperadores a nivel de bits:","\n AND:", and_bit, "\n OR:", or_bit, "\n XOR:", xor_bit, "\n NOT:", not_bit, "\n Left Shift:", left_shift, "\n Right Shift:", right_shift)


lista=[]
print(lista)

for i in range(10,55):
    if i % 2==0 and  i %3!=0 and i !=16:
        lista.append(i)
    
print("Lista de números entre 10 y 54 que son pares y no múltiplos de 3:", lista)