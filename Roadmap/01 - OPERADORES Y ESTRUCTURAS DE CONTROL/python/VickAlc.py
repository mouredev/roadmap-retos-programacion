#01 OPERADORES Y ESTRUCTURAS DE CONTROL

#_ Operadores de asignación
print('\n***Operadores de asignación***')
num1 = 10
num2 = 3
num3 = 7
##
num1 += 5
num2 -= 2
num3 *= 4
num1 /= 3
print(f'número 1 = {num1}')
print(f'número 2 = {num2}')
print(f'número 3 = {num3}')


#_ Operadores aritméticos
print('\n***Operadores aritméticos***')
suma = num1 + num2
print(f'suma = {suma}')

resta = num1 - num2
print(f'resta = {resta}')

mult = num1 * num2
print(f'multiplicación = {mult}')

div = num1/num2
print(f'división = {div}')

mod = num1 % num2
print(f'módulo = {mod}')

pot = num1 ** num2
print(f'potencia = {pot}')

div_ent = num1 // num2
print(f'división entera = {div_ent}')


#_ Operadores de comparación
print('\n***Operadores de comparación***')
igualdad = num1 == num3
print(igualdad)

desigualdad = num1 != num2
print(desigualdad)

mayor_que = num2 > num3
print(mayor_que)

menor_que = num2 < num1+num3
print(menor_que)

mayor_igual = num2 >= num3
print(mayor_igual)

menor_igual = num1 <= num2+num3
print(menor_igual)


#_ Operadores lógicos
print('\n***Operadores lógicos***')
resultado = num1 > num2 and num1 > num3
print(resultado)

resultado = num1 < num2 or num1 < num3
print(resultado)

resultado = not (num1 == num2)
print(resultado)


#_ Operadores de identidad
print('\n***Operadores de identidad***')
num4 = num1
lista1 = [1,2,3]
lista2 = [1,2,3]

op_is1 = num1 is num4
print(op_is1)

op_is2 = lista1 is lista2
print(op_is2)

op_is1 = num1 is not num4
print(op_is1)

op_is2 = lista1 is not lista2
print(op_is2)


#_ Operadores de pertenencia
print('\n***Operadores de pertenencia***')
resultado = num2 in lista1
print(resultado)

resultado = num2 not in lista1
print(resultado)


#_ Operadores de bits
print('\n***Operadores de bits***')
a = 10  # Representación binaria: 1010
b = 6   # Representación binaria: 0110

resultado_and = a & b
print("AND:", resultado_and)  # 2 en binario: 0010

resultado_or = a | b
print("OR:", resultado_or)  # 14 en binario: 1110

resultado_xor = a ^ b
print("XOR:", resultado_xor)  # 12 en binario: 1100

desplazamiento_izquierda = a << 2
print("Desplazamiento a la izquierda:", desplazamiento_izquierda)  # 40 en binario: 101000

desplazamiento_derecha = a >> 1
print("Desplazamiento a la derecha:", desplazamiento_derecha)  # 5 en binario: 0101

complemento_a = ~a
print("Complemento:", complemento_a)  # -11 en binario: -1011


#_ Estructuras de control
print('\n***Estructuras de control***')

# condicional
if num1 > num2:
    print(f'{num1} es mayor que {num2}')
else:
    print(f'{num1} es menor que {num2}')

# while
contador = 0
while contador <= (num1-2):
    print(contador)
    contador +=1

# for
for i in lista1:
    print(f'{i*10}')

lista3 = [1,2,3,4,5,6,7,8,9,10]
for i in lista3:
    if i ==2:
        continue
    if i == 3:
        pass
    if i == 5:
        break
    else:
        print(i)

# Excepciones
try:
    num0 = 0

    # División entre cero
    resultado = num1 / num0

except ZeroDivisionError:
    print("Error: No es posible dividir por cero.")


#_ Dificultad extra
print('\n***Dificultad extra***')
for i in range(10, 56):
    if (i % 2) != 0:
        continue
    elif i==16:
        pass
    elif (i % 3) == 0:
        continue
    else:
        print(i)