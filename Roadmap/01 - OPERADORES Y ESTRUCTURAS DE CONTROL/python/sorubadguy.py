num1 = 2
num2 = 10
num3 = 100
#Operadores Aritmeticos

print(f"suma: {num1} + {num2} = {num1 + num2}")
print(f"resta: {num2} - {num1} = {num2 - num1}")
print(f"multiplicacion: {num1} * {num2} = {num1 * num2}")
print(f"divicion: {num2} / {num1} = {num2 / num1}")
print(f"suma: {num1} + {num2} = {num1 + num2}")
print(f"modulo: {num2} % {num1} = {num2 % num1}")
print(f"exponente: {num1} ** {num2} = {num1 ** num2}")
print(f"division entera: {num3} // {num2} = {num3 // num2}")

#Operadores de comparacion

print(f"igual que: {num1} == {num2} = {num1 == num2}")
print(f"distinto que: {num1} != {num2} = {num1 != num2}")
print(f"mayor que: {num1} > {num2} = {num1 > num2}")
print(f"menor que: {num1} < {num2} = {num1 < num2}")
print(f"mayor o igual que: {num1} >= {num2} = {num1 >= num2}")
print(f"menor o igual que: {num1} <= {num2} = {num1 <= num2}")

#Operadores Logicos

print(f"AND: {num1} + {num2} = {num3} and {num2} ** {num1} == {num3} = {(num1 + num2 == num3) and (num2 ** num1 == num3)}")
print(f"OR: {num1} + {num2} = {num3} or {num2} ** {num1} == {num3} = {(num1 + num2 == num3) or (num2 ** num1 == num3)}")
print(f"NOT: not {num2} ** {num1} == {num3} = {not(num2 ** num1 == num3)}")

#Operadores de Asignacion

num3 = num1 + num2
print(f"num3 = num1 + num2: {num3}")
num3 += num1
print(f"num3 += num1: {num3}")
num3 -= num1
print(f"num3 -= num1: {num3}")
num3 *= num1
print(f"num3 *= num1: {num3}")
num3 /= num1
print(f"num3 /= num1: {num3}")
num3 **= num1
print(f"num3 **= num1: {num3}")
num3 //= num1
print(f"num3 //= num1: {num3}")
num3 %= num1
print(f"num3 %= num1: {num3}")