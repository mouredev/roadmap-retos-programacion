# Aritméticos
print("ARITMÉTICOS")
op_add = 3 + 2 # sum
op_substraction = 5 - 3 # resta
op_multiplication = 3 * 3 # multiplicación
op_division = 9 / 3 # división
op_modulus = 10 % 5 # resto
op_exponentiation = 2 ** 4 # potencia
op_floor_division = 10 // 3 # cociente

print(f"3 + 2 = {op_add}")
print(f"5 - 3 = {op_substraction}")
print(f"3 * 3 = {op_multiplication}")
print(f"9 / 3 = {op_division}")
print(f"10 % 5 = {op_modulus}")
print(f"2 ** 4 = {op_exponentiation}")
print(f"10 // 3 = {op_floor_division}")

# Lógicos o booleanos
print("LÓGICOS O BOOLEANOS")
val_1 = True
val_2 = False
op_or = val_1 or val_2 #or
op_and = val_1 and val_2 #and
op_not = not val_1 #not

print(f"val_1 == {val_1}")
print(f"val_2 == {val_2}")
print(f"val_1 or val_2 = {op_or}")
print(f"val_1 and val_2 = {op_and}")
print(f"not val_1 = {op_not}")

# De comparación
print("DE COMPARACIÓN")
val_3 = 9
val_4 = 1

op_equal = val_3 == val_4
op_less_than = val_3 < val_4
op_greater_than = val_3 > val_4
op_less_equal = val_3 <= val_4
op_greater_equal = val_3 >= val_4
op_not_equal = val_3 != val_4

print(f"val_3 == {val_3}")
print(f"val_4 == {val_4}")
print(f"val_3 == val_4 -> {op_equal}")
print(f"val_3 < val_4 -> {op_less_than}")
print(f"val_3 > val_4 -> {op_greater_than}")
print(f"val_3 <= val_4 -> {op_less_equal}")
print(f"val_3 >= val_4 -> {op_greater_equal}")
print(f"val_3 != val_4 -> {op_not_equal}")

# Asignación
print("ASIGNACIÓN")
val_5 = 2
print(f"val_5 = {val_5}")

val_5 += 2

print(f"val_5 +=2 -> {val_5}")

val_5 -= 1
print(f"val_5 -= 1 -> {val_5}")

val_5 *= 2
print(f"val_5 *= 2 -> {val_5}")

val_5 /= 3
print(f"val_5 /= 3 -> {val_5}")

val_5 %= 2
print(f"val_5 %= 2 -> {val_5}")

val_6 = 10
print(f"val_6 = {val_6}")

val_6 //= 2
print(f"val_6 //= 2 -> {val_6}")

val_6 **= 2
print(f"val_6 **= 2 -> {val_6}")

val_6 &= 3
print(f"val_6 &= 3 -> {val_6}")

val_6 |= 4
print(f"val_6 |= 4 -> {val_6}")

val_6 ^= 6
print(f"val_6 ^= 6 -> {val_6}")

val_6 >>= 2
print(f"val_6 >>= 2 -> {val_6}")

val_6 <<= 3
print(f"val_6 <<= 3 -> {val_6}")

# Identidad
print("IDENTIDAD")
val_7 = 4
list_1 = [1, 2]
op_is = val_7 is 4
op_is_not = list_1 is not 2

print(f"val_7 = {val_7}")
print(f"list_1 = {list_1}")
print(f"val_7 is 4 = {op_is}")
print(f"list_1 is not 2 = {op_is_not}")

# Pertenencia
print("PERTENECIA")
list_2 = [1, 2, 3, 4]
string_1 = "First string"

op_in = "tri" in string_1
op_not_in = 5 not in list_2

print(f"list_2 = {list_2}")
print(f"string_1 = {string_1}")
print(f"'tri' in string_1 =  {op_in}")
print(f"5 not in list_2 = {op_not_in}")

# Bits
print("BITS")
val_8 = 2
val_9 = 7

op_bit_or = val_8 | val_9
op_bit_xor = val_8 ^ val_9
op_bit_and = val_8 & val_9
op_bit_n_left = val_9 << 2
op_bit_n_right = val_9 >> 2
op_bit_not = -val_8

print(f"val_8 = {val_8}")
print(f"val_9 = {val_9}")
print(f"val_8 | val_9 = {op_bit_or}")
print(f"val_8 ^ val_9 = {op_bit_xor}")
print(f"val_8 & val_9 = {op_bit_and}")

print(f"val_9 << 2 = {op_bit_n_left}")
print(f"val_9 >> 2 = {op_bit_n_right}")
print(f"-val_8 = {op_bit_not}")

