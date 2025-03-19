# Arithmetics Operators
addition = 4 + 8
subtraction = 10 - 4
multiplication = 12 * 2
division = 100 / 6
modulus = 30 % 7

print("\nArithmetic Operators")
print(f"addition result: {addition}")
print(f"subtraction result: {subtraction}")
print(f"multiplication result: {multiplication}")
print(f"division result: {division}")
print(f"modulus result: {modulus}")


# Assignment Operators
number_by_assigment = 777
assigment_operator = number_by_assigment
addition_assigment = 222
addition_assigment += number_by_assigment
subtraction_assigment = 999
subtraction_assigment -= number_by_assigment
multiplication_assigment = 12982
multiplication_assigment *= number_by_assigment
division_assigment = 1414
division_assigment /= number_by_assigment
modulus_assigment = 11000
modulus_assigment %= number_by_assigment

print("\n Assigment Operators")
print(f"addition_assigment result: {addition_assigment}")
print(f"subtraction_assigment result: {subtraction_assigment}")
print(f"multiplication_assigment result: {multiplication_assigment}")
print(f"division_assigment result: {division_assigment}")
print(f"modulus_assigment result: {modulus_assigment}")


# Comparison Operators
equal_to = 1 == 1
not_equal_to = 1 != 4
greatter_than = 20 > 40
less_than = 9 < 1
greatter_than_or_equal_to = 77 >= 22
less_than_or_equal_to = 23 <= 98

print("\n Comparison Operators")
print(f"equal_to result: {equal_to}")
print(f"not_equal_to result: {not_equal_to}")
print(f"greatter_than result: {greatter_than}")
print(f"less_than result {less_than}")
print(f"greatter_than_or_equal_to result: {greatter_than_or_equal_to}")
print(f"less_than_or_equaal_to result: {less_than_or_equal_to}")


# Logical Operators
and_operator = True == True and False == False
or_operator = 1 < 0 or 0 >= -3
not_operator = not False

print("\nLogical Operators")
print(f"and_operator result: {and_operator}")
print(f"or_operator result: {or_operator}")
print(f"not_operator result: {not_operator}")


# Ternary Opretator
ternary_operator = "Hello" if True else "Bye"

print("\nTernary Operator")
print(f"ternary_operator result: {ternary_operator}")


# Range Operator
range_Operator = range(0, 11)

print("\nRange Operator")
for n in range_Operator:
    print(f"the range_o[erator result now is: {n}")


# Bit Operators
first_binary = 22 # 0001 0110
second_binary = 44 # 0010 1100
bitwise_AND = first_binary & second_binary
bitwise_OR = first_binary | second_binary
bitwise_XOR = first_binary ^ second_binary
bitwise_NOT = ~first_binary
bitwise_left_shift = first_binary << 1
bitwise_right_shift = second_binary >> 1

print("\nBit Operators")
print(f"bitwise_AND result: {bitwise_AND}")
print(f"bitwise_OR result: {bitwise_OR}")
print(f"bitwise_XOR result: {bitwise_XOR}")
print(f"bitwise_NOT result: {bitwise_NOT}")
print(f"bitwise_left_shift result: {bitwise_left_shift}")
print(f"bitwise_right_shift result: {bitwise_right_shift}")


# Exception
print("\nExeption")
try:
    result = 10 / 0
except:
    print("Error")
else:
    print(result)
finally:
    print("End")


# Control Flow (if, else and elif)
print("\nControl Flow (if, else and elif)")
control_flow_test = 0
if control_flow_test == 1:
    print("Is 1")
elif control_flow_test == 2:
    print("Is 2")
else:
    print("Is 0")


# Loop (for)
print("\nLoop (for)")
for i in range(0, 11):
    print(f"The for result is now: {i}")


# Loop (while)
print("\nLoop (while)")
number_while = 22
while number_while < 33:
    print(f"The while result is now: {number_while}")
    number_while += 1




# Extra Dificulty
############################################################

def print_numbers():
    for number in range(10, 55):
        if number == 16:
            continue
        if number % 2 == 0 and number % 3 != 0:
            print(number)
        
print("\nNumbers from 10 to 55 without 16 and multiples of three")
print_numbers()