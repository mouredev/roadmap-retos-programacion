# Ejemplos de operadores aritmeticos

num_1 = 5
num_2 = 2

Op_arit = 0
print("##### Operaciones Aritmeticas #####")
Op_arit = num_1 + num_2
print(f"Suma: {Op_arit}")
Op_arit = num_1 - num_2
print(f"Resta: {Op_arit}")
Op_arit = num_1 * num_2
print(f"Multiplicación: {Op_arit}")
Op_arit = num_1 / num_2
print(f"División: {Op_arit}")
Op_arit = num_1 % num_2
print(f"Módulo: {Op_arit}")
Op_arit = num_1 ** num_2
print(f"Potencia: {Op_arit}")
Op_arit = num_1 // num_2
print(f"División entera: {Op_arit} \n")

""" Ejemplos de operadores relacionales, se usan para comparar
    y establecer una relación entre ellos, devuelven un valor
    booleano (true o false) basado en la condición.
"""
op_rel = False
op_rel = num_1 > num_2
print("##### Operaciones Relacionales ##### ")
print(f"Mayor: {op_rel}")
op_rel = num_1 < num_2
print(f"Menor: {op_rel}")
op_rel = num_1 == num_2
print(f"Igual: {op_rel}")
op_rel = num_1 >= num_2
print(f"Mayor o igual: {op_rel}")
op_rel = num_1 <= num_2
print(f"Menor o igual: {op_rel}")
op_rel = num_1 != num_2
print(f"Diferente: {op_rel} \n")

""" Ejemplos de operadores Bit a Bit
    consideramos a =2 (binario 10) y 
    b= 3 (binario 11)
"""
a = 2  # 10 en binario
b = 3  # 11 en binario

print("##### Operaciones Bit a Bit #####")
op_bit = a & b
print(f"And: {op_bit}")
op_bit = a | b
print(f"Or: {op_bit}")
op_bit = a ^ b
print(f"XOR: {op_bit}")
op_bit = ~a
print(f"NOT {op_bit}")
op_bit = a >> b
print(f"Desplazamiento a la derecha : {op_bit}")
op_bit = a << b
print(f"Desplazamiento a la izquierda : {op_bit} \n")

""" Operadores de asignación se utilizan para asignar valores a las variables
    gerenalmente se combinan con operadores aritmeticos 
"""
print("##### Operadores de asignación #####")
a = 5
print(f"Asignación directa a=5 : {a}")
a += 5
print(f"Asignación de sumar 5 (a += 5):  {a}")
a -= 5
print(f"Asignación de restar 5 (a -= 5):  {a}")
a *= 3
print(f"Asignación de multiplicar 3 (a *= 3):  {a}")
a /= 3
print(f"Asignación de dividir entre 3 (a /= 3):  {a}")
a %= 3
print(f"Asignación de módulo entre 3 (a %= 3):  {a}")
a **= 3
print(f"Asignación de elevar al 3 (a **= 3):  {a}")
a //= 3
print(f"Asignación de divier entero entre 3 (a //= 3):  {a}")

"""Operadores de pertenencia se utilizan para identificar si pertenece a alguna secuencia
    com listas, strings, tuplas, in y not in son operadores de pertenencia
"""
print("\n ##### Operadores de Pertenencia #####")
a = [1, 2, 3, 4, 5]
string = "Hello world this is python!"
r = 3 in a
print(r)
r = 12 not in a
print(r)
r = "World" in string
print(r)
r = "map" not in string
print(r)

print("\n ##### Operadores Lógicos #####")
x = True
y = False

re_log = x and y
print("AND:", re_log)
re_log = x or y
print("OR:", re_log)
re_log = not x
print("NOT:", re_log)


""" DIFICULTAD EXTRA (opcional):
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
"""
c = []
for i in range(10, 56):
    if i != 16 and i % 2 == 0 and i % 3 != 0 or i==55:
        c.append(i)

print(c)
