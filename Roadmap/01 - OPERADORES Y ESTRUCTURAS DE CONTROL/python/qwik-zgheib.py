# -- aritmetics
addition: int = 1 + 2
subtraction: int = 1 - 2
multiplication: int = 1 * 2
division: float = 1 / 2
exponentiation: int = 1**2
modulo: int = 1 % 2
print("----- aritmetics -----")
print(f"addition: {addition}")
print(f"subtraction: {subtraction}")
print(f"multiplication: {multiplication}")
print(f"division: {division}")
print(f"exponentiation: {exponentiation}")
print(f"modulo: {modulo}")

# -- logic
and_op: bool = True and False
or_op: bool = True or False
logical_not: bool = not True
print("----- logic -----")
print(f"and_op: {and_op}")
print(f"or_op: {or_op}")
print(f"logical_not: {logical_not}")

# -- comparison
equal: bool = 1 == 2
not_equal: bool = 1 != 2
greater_than: bool = 1 > 2
less_than: bool = 1 < 2
greater_than_or_equal: bool = 1 >= 2
less_than_or_equal: bool = 1 <= 2
print("----- comparison -----")
print(f"equal: {equal}")
print(f"not_equal: {not_equal}")
print(f"greater_than: {greater_than}")
print(f"less_than: {less_than}")
print(f"greater_than_or_equal: {greater_than_or_equal}")
print(f"less_than_or_equal: {less_than_or_equal}")

# -- assignment
print("----- assignment -----")
assignment: int = 5
print(f"assignment: {assignment}")
assignment += 3
print(f"assignment += 3: {assignment}")
assignment -= 3
print(f"assignment -= 3: {assignment}")
assignment *= 3
print(f"assignment *= 3: {assignment}")
assignment /= 3
print(f"assignment /= 3: {assignment}")
assignment %= 3
print(f"assignment %= 3: {assignment}")
assignment **= 3
print(f"assignment **= 3: {assignment}")

# -- membership
membership: bool = 1 in [1, 2, 3]
not_membership: bool = 1 not in [1, 2, 3]
print("----- membership -----")
print(f"membership: {membership}")
print(f"not_membership: {not_membership}")

# -- bitwise
bitwise_and: int = 1 & 2
bitwise_or: int = 1 | 2
bitwise_xor: int = 1 ^ 2
bitwise_not: int = ~1
bitwise_left_shift: int = 1 << 2
bitwise_right_shift: int = 1 >> 2
print("----- bitwise -----")
print(f"bitwise_and: {bitwise_and}")
print(f"bitwise_or: {bitwise_or}")
print(f"bitwise_xor: {bitwise_xor}")
print(f"bitwise_not: {bitwise_not}")
print(f"bitwise_left_shift: {bitwise_left_shift}")
print(f"bitwise_right_shift: {bitwise_right_shift}")

# -- conditional
print("----- conditional -----")
condition: bool = 5 > 6
if condition:
    print("5 is greater than 6")
else:
    print("5 is not greater than 6")


print("\n----- extra -----")


def print_numbers():
    for i in range(10, 56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            print(i)


print_numbers()
