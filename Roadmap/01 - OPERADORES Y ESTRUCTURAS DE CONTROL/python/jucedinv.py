#01 - OPERADORES Y ESTRUCTURAS DE CONTROL
print('01 - OPERADORES Y ESTRUCTURAS DE CONTROL')
#Addition - Adds values on either side of the operator.
r_addition1 = 10 + 20 #10 + 20 will give 30
r_addition2 = 10 + -20 #10 + -20 will give -10
print('Addition - Adds values on either side of the operator.')
print('10 + 20 = ', r_addition1)
print('10 + -20 = ', r_addition2)
#Subtraction - Subtracts right hand operand from left hand operand.
r_subtraction1 = 20 - 10 #20 - 10 will give 10
r_subtraction2 = 10 - 20 #10 - 20 will give -10
print('Subtraction - Subtracts right hand operand from left hand operand.')
print('20 - 10 = ', r_subtraction1)
print('10 - 20 = ', r_subtraction2)
#Multiplication - Multiplies values on either side of the operator.
r_multiplication1 = 10 * 20 #10 * 20 will give 200
r_multiplication2 = 10 * 0.5 #10 * 0.5 will give 5.0
print('Multiplication - Multiplies values on either side of the operator.')
print('10 * 20 = ', r_multiplication1)
print('10 * 0.5 = ', r_multiplication2)
#Division - Divides left hand operand by right hand operand.
r_division1 = 20 / 10 #20 / 10 will give 2
r_division2 = 10 / 20 #10 / 20 will give 0.5
print('Division - Divides left hand operand by right hand operand.')
print('20 / 10 = ', r_division1)
print('10 / 20 = ', r_division2)
#Modulus - Divides left hand operand by right hand operand and returns remainder.
r_modulus1 = 20 % 10 #20 % 10 will give 0
r_modulus2 = 22 % 10 #22 % 10 will give 2
print('Modulus - Divides left hand operand by right hand operand and returns remainder.')
print('20 % 10 = ', r_modulus1)
print('22 % 10 = ', r_modulus2)
#Exponent - Performs exponential (power) calculation on operators.
r_exponent1 = 10 ** 2 # 10 ** 2 will give 100
r_exponent2 = 100 ** 0.5 # 100 ** 0.5 will give 10
print('Exponent - Performs exponential (power) calculation on operators.')
print('10 ** 2 = ', r_exponent1)
print('100 ** 0.5 = ', r_exponent2)
#Floor Division - The division of operands where the result is the quotient in which the dig its after the decimal point are removed.
r_fdivision1 = 9 // 2 #9//2 is equal to 4
r_fdivision2 = 9.0 // 2.0 #9.0//2.0 is equal to 4.0
print('Floor Division - The division of operands where the result is the quotient in which the dig its after the decimal point are removed.')
print('9 // 2 = ', r_fdivision1)
print('9.0 // 2.0 = ', r_fdivision2)
#Equality - checks if the value of two operands are equal or not, if yes then condition becomes true.
r_equality1 = 20 == 10 #20 == 10 is not true.
r_equality2 = 10 == 10 #10 == 10 is true.
print('Equality - checks if the value of two operands are equal or not, if yes then condition becomes true.')
print('20 == 10 = ', r_equality1)
print('10 == 10 = ', r_equality2)
#Inequality - Checks if the value of two operands are equal or not, if values are not equal then condition becomes true.
r_inequalityA1 = 20 != 10 #(20 != 10) is true.
r_inequalityA2 = 10 != 10 #(10 != 10) is not true.
print('Inequality - Checks if the value of two operands are equal or not, if values are not equal then condition becomes true.')
print('20 != 10 = ', r_inequalityA1)
print('10 != 10 = ', r_inequalityA2)
#Inequality (obsolet) - Checks if the value of two operands are equal or not, if values are not equal then condition becomes true.
#r_inequalityB1 = 20 <> 10 #(20 <> 10) is true. This is similar to != operator in version 2.0
#r_inequalityB2 = 10 <> 10 #(10 <> 10) is not true. This is similar to != operator in version 2.0
#Greater-than - Checks if the value of left operand is greater than the value of right operand, if yes then condition becomes true.
r_greater_than1 = 20 > 10 #(20 > 10) is true.
r_greater_than2 = 10 > 20 #(10 > 20) is not true.
print('Greater-than - Checks if the value of left operand is greater than the value of right operand, if yes then condition becomes true.')
print('20 > 10 = ', r_greater_than1)
print('10 > 20 = ', r_greater_than2)
#Less-than - Checks if the value of left operand is less than the value of right operand, if yes then condition becomes true.
r_less_than1 = 20 < 10 #(20 > 10) is not true.
r_less_than2 = 10 < 20 #(10 > 20) is true.
print('Less-than - Checks if the value of left operand is less than the value of right operand, if yes then condition becomes true.')
print('20 < 10 = ', r_less_than1)
print('10 < 20 = ', r_less_than2)
#Greater than or equal to - Checks if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true.
r_greater_than_or_equal_to1 = 20 >= 10#(20 >= 10) is true.
r_greater_than_or_equal_to2 = 10 >= 20#(10 >= 20) is not true.
r_greater_than_or_equal_to3 = 20 >= 20#(20 >= 20) is true.
print('Greater than or equal to - Checks if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true.')
print('20 >= 10 = ', r_greater_than_or_equal_to1)
print('10 >= 20 = ', r_greater_than_or_equal_to2)
print('20 >= 20 = ', r_greater_than_or_equal_to3)
#Less than or equal to - Checks if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true.
r_less_than_or_equal_to1 = 20 <= 10#(20 >= 10) is not true.
r_less_than_or_equal_to2 = 10 <= 20#(10 >= 20) is true.
r_less_than_or_equal_to3 = 20 <= 20#(20 >= 20) is true.
print('Less than or equal to - Checks if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true.')
print('20 <= 10 = ', r_less_than_or_equal_to1)
print('10 <= 20 = ', r_less_than_or_equal_to2)
print('20 <= 20 = ', r_less_than_or_equal_to3)
#Assignment - Simple assignment operator - Assigns values from right side operands to left side operand.
r_assignment1 = 10#r_assignment1 = 10 will assigne value 10 into r_assignment1
r_assignment2 = 20#r_assignment2 = 20 will assigne value 20 into r_assignment2
r_assignment3 = 10 + 20#r_assignment3 = 10 + 20 will assigne value of 10 + 20 into r_assignment3
print('Assignment - Simple assignment operator - Assigns values from right side operands to left side operand.')
print('r_assignment1 = 10 ----> Value of r_assignment1 = ', r_assignment1)
print('r_assignment2 = 20 ----> Value of r_assignment2 = ', r_assignment2)
print('r_assignment3 = 10 + 20 ----> Value of r_assignment3 = ', r_assignment3)
#Addition assignment - Add AND assignment operator, It adds right operand to the left operand and assig n the result to left operand.
#c += a is equivalent to c = c + a
r_addition_assignment1 = 1
r_addition_assignment1 += 3#r_addition_assignment1 += 3 is equivalent to r_addition_assignment1 = r_addition_assignment1 + 3, result 4.
r_addition_assignment2 = 1
r_addition_assignment2 += -3#r_addition_assignment2 += -3 is equivalent to r_addition_assignment2 = r_addition_assignment1 + -3, result -2.
print('Addition assignment - Add AND assignment operator, It adds right operand to the left operand and assig n the result to left operand.')
print('r_addition_assignment1 = 1')
print('r_addition_assignment1 += 3 ----> Value of r_addition_assignment1 = ', r_addition_assignment1)
print('r_addition_assignment2 = 1')
print('r_addition_assignment2 += -3 ----> Value of r_addition_assignment2 = ', r_addition_assignment2)
#Subtract assignment - Subtract AND assignment operator, It subtracts right operand from the left operand and assig n the result to left operand.
#c -= a is equivalent to c = c - a
r_subtraction_assignment1 = 10
r_subtraction_assignment1 -= 3#r_subtraction_assignment1 -= 3 is equivalent to r_subtraction_assignment1 = r_subtraction_assignment1 - 3, result 7.
r_subtraction_assignment2 = 10
r_subtraction_assignment2 -= -3#r_subtraction_assignment2 -= -3 is equivalent to r_subtraction_assignment2 = r_subtraction_assignment2 - -3, result 13.
print('Subtract assignment - Subtract AND assignment operator, It subtracts right operand from the left operand and assig n the result to left operand.')
print('r_subtraction_assignment1 = 10')
print('r_subtraction_assignment1 -= 3 ----> Value of r_subtraction_assignment1 = ', r_subtraction_assignment1)
print('r_subtraction_assignment2 = 10')
print('r_subtraction_assignment2 -= -3 ----> Value of r_subtraction_assignment2 = ', r_subtraction_assignment2)
#Multiplication assignment - Multiply AND assignment operator, It multiplies right operand with the left operand and assign the result to left operand.
#c *= a is equivalent to c = c * a
r_multiplication_assignment1 = 10
r_multiplication_assignment1 *= 2#r_multiplication_assignment1 *= 2 is equivalent to r_multiplication_assignment1 = r_multiplication_assignment1 * 2, result 20.
r_multiplication_assignment2 = 10
r_multiplication_assignment2 *= 0.5#r_multiplication_assignment2 *= 0.5 is equivalent to r_multiplication_assignment2 = r_multiplication_assignment2 * 0.5, result 5.
print('Multiplication assignment - Multiply AND assignment operator, It multiplies right operand with the left operand and assign the result to left operand.')
print('r_multiplication_assignment1 = 10')
print('r_multiplication_assignment1 *= 2 ----> Value of r_multiplication_assignment1 = ', r_multiplication_assignment1)
print('r_multiplication_assignment2 = 10')
print('r_multiplication_assignment2 *= 0.5 ----> Value of r_multiplication_assignment2 = ', r_multiplication_assignment2)
#Division assignment - Divide AND assignment operator, It divides left operand with the rig ht operand and assign the result to left operand.
#c /= a is equivalent to c = c / a
r_division_assignment1 = 10
r_division_assignment1 /= 2#r_division_assignment1 /= 2 is equivalent to r_division_assignment1 = r_division_assignment1 / 2, result 5.0.
r_division_assignment2 = 10
r_division_assignment2 /= 0.5#r_division_assignment2 /= 0.5 is equivalent to r_division_assignment2 = r_division_assignment2 / 0.5, result 20.0.
print('Division assignment - Divide AND assignment operator, It divides left operand with the rig ht operand and assign the result to left operand.')
print('r_division_assignment1 = 10')
print('r_division_assignment1 /= 2 ----> Value of r_division_assignment1 = ', r_division_assignment1)
print('r_division_assignment2 = 10')
print('r_division_assignment2 /= 0.5 ----> Value of r_division_assignment2 = ', r_division_assignment2)
#Modulus assignment - Modulus AND assignment operator, It takes modulus using two operands and assign the result to left operand.
#c %= a is equivalent to c = c % a
r_modulus_assignment1 = 10
r_modulus_assignment1 %= 2#r_modulus_assignment1 %= 2 is equivalent to r_modulus_assignment1 = r_modulus_assignment1 % 2, result 0.
r_modulus_assignment2 = 10
r_modulus_assignment2 %= 3#r_modulus_assignment2 %= 3 is equivalent to r_modulus_assignment2 = r_modulus_assignment2 % 3, result 1.
print('Modulus assignment - Modulus AND assignment operator, It takes modulus using two operands and assign the result to left operand.')
print('r_modulus_assignment1 = 10')
print('r_modulus_assignment1 %= 2 ----> Value of r_modulus_assignment1 = ', r_modulus_assignment1)
print('r_modulus_assignment2 = 10')
print('r_modulus_assignment2 %= 3 ----> Value of r_modulus_assignment2 = ', r_modulus_assignment2)
#Exponent assignment - "Exponent AND assignment operator, Performs exponential (power) calculation on operators and assign value to the left operand.
#c **= a is equivalent to c = c ** a
r_exponent_assignment1 = 10
r_exponent_assignment1 **= 2#r_exponent_assignment1 **= 2 is equivalent to r_exponent_assignment1 = r_exponent_assignment1 ** 2, result 100.
r_exponent_assignment2 = 100
r_exponent_assignment2 **= 0.5#r_exponent_assignment2 **= 0.5 is equivalent to r_exponent_assignment2 = r_exponent_assignment2 ** 0.5, result 10.0.
print('Exponent assignment - "Exponent AND assignment operator, Performs exponential (power) calculation on operators and assign value to the left operand.')
print('r_exponent_assignment1 = 10')
print('r_exponent_assignment1 **= 2 ----> Value of r_exponent_assignment1 = ', r_exponent_assignment1)
print('r_exponent_assignment2 = 100')
print('r_exponent_assignment2 **= 0.5 ----> Value of r_exponent_assignment2 = ', r_exponent_assignment2)
#Floor Division assignment - Floor Dividion and assigns a value, Performs floor division on operators and assign value to the left operand.
#c //= a is equivalent to c = c // a
r_floor_division_assignment1 = 9
r_floor_division_assignment1 //= 2#r_floor_division_assignment1 //= 2 is equivalent to r_floor_division_assignment1 = r_floor_division_assignment1 // 2, result 4.
r_floor_division_assignment2 = 11
r_floor_division_assignment2 //= 3#r_floor_division_assignment2 //= 3 is equivalent to r_floor_division_assignment2 = r_floor_division_assignment2 // 3, result 3.
print('Floor Division assignment - Floor Dividion and assigns a value, Performs floor division on operators and assign value to the left operand.')
print('r_floor_division_assignment1 = 9')
print('r_floor_division_assignment1 //= 2 ----> Value of r_floor_division_assignment1 = ', r_floor_division_assignment1)
print('r_floor_division_assignment2 = 11')
print('r_floor_division_assignment2 //= 3 ----> Value of r_floor_division_assignment2 = ', r_floor_division_assignment2)
#Logical AND operator - If both the operands are true then then condition becomes true.
r_logical_and1 = False and False #(False and False) is not true.
r_logical_and2 = True and False #(True and False) is not true.
r_logical_and3 = False and True #(False and True) is not true.
r_logical_and4 = True and True #(True and True) is true.
print('Logical AND operator - If both the operands are true then then condition becomes true.')
print('False and False = ', r_logical_and1)
print('True  and False = ', r_logical_and2)
print('False and True  = ', r_logical_and3)
print('True  and True  = ', r_logical_and4)
#Logical OR Operator - If any of the two operands are non-zero then then condition becomes true.
r_logical_or1 = False or False #(False or False) is not true.
r_logical_or2 = True or False #(True or False) is true.
r_logical_or3 = False or True #(False or True) is true.
r_logical_or4 = True or True #(True or True) is true.
print('Logical OR Operator - If any of the two operands are non-zero then then condition becomes true.')
print('False or False = ', r_logical_or1)
print('True  or False = ', r_logical_or2)
print('False or True  = ', r_logical_or3)
print('True  or True  = ', r_logical_or4)
#Logical XOR Operator - If any of the two operands are diferents then then condition becomes true.
r_logical_xor1 = False ^ False #(False ^ False) is not true.
r_logical_xor2 = True ^ False #(True ^ False) is true.
r_logical_xor3 = False ^ True #(False ^ True) is true.
r_logical_xor4 = True ^ True #(True ^ True) is not true.
print('Logical XOR Operator - If any of the two operands are diferents then then condition becomes true.')
print('False ^ False = ', r_logical_xor1)
print('True  ^ False = ', r_logical_xor2)
print('False ^ True  = ', r_logical_xor3)
print('True  ^ True  = ', r_logical_xor4)
#Logical NOT Operator - Use to reverses the logical state of its operand. If a condition is true then Logical NOT operator willmake false.
r_logical_not1 = not False #not False is true.
r_logical_not2 = not True #not True is not true.
print('Logical NOT Operator - Use to reverses the logical state of its operand. If a condition is true then Logical NOT operator willmake false.')
print('not False = ', r_logical_not1)
print('not True  = ', r_logical_not2)
#Membership operator found - Evaluates to true if it finds a variable in the specified sequence and false otherwise.
r_membership_found1 = 1 in [1,2,3,4] # 1 in [1,2,3,4] is true, because 1 is member of list [1,2,3,4].
r_membership_found2 = 10 in [1,2,3,4] # 10 in [1,2,3,4] is not true, because 10 not is member of list [1,2,3,4].
print('Membership operator found - Evaluates to true if it finds a variable in the specified sequence and false otherwise.')
print('1  in [1,2,3,4] = ', r_membership_found1)
print('10 in [1,2,3,4] = ', r_membership_found2)
#Membership operator not found - Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
r_membership_notfound1 = 1 not in [1,2,3,4] # 1 not in [1,2,3,4] is not true, because 1 is member of list [1,2,3,4].
r_membership_notfound2 = 10 not in [1,2,3,4] # 10 not in [1,2,3,4] is true, because 10 not is member of list [1,2,3,4].
print('Membership operator not found - Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.')
print('1  not in [1,2,3,4] = ', r_membership_notfound1)
print('10 not in [1,2,3,4] = ', r_membership_notfound2)
#Identity operator - is	"Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
#x is y, here is results in 1 if id(x) equals id(y).
a = [1,3,5,10]
b = a
c = [1,3,5,10]
r_identity1 = a is b # a is b is true because id(a) is equals to id(b).
r_identity2 = a is c # a is b is not true because id(a) is not equals to id(c).
print('Identity operator - is	"Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.')
print('a = [1,3,5,10]')
print('id(a) = ',id(a))
print('b = a')
print('id(b) = ',id(b))
print('c = [1,3,5,10]')
print('id(c) = ',id(c))
print('a is b = ', r_identity1)
print('a is c = ', r_identity2)
#Identity operator inverse - Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
#x is not y, here is not results in 1 if id(x) is not equal to id(y).
a = [1,3,5,10]
b = a
c = [1,3,5,10]
r_identity_inv1 = a is not b # a is not b is not true because id(a) is equals to id(b).
r_identity_inv2 = a is not c # a is not b is true because id(a) is not equals to id(c).
print('Identity operator inverse - Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.')
print('a = [1,3,5,10]')
print('id(a) = ',id(a))
print('b = a')
print('id(b) = ',id(b))
print('c = [1,3,5,10]')
print('id(c) = ',id(c))
print('a is not b = ', r_identity_inv1)
print('a is not c = ', r_identity_inv2)

#Binary AND Operator - Perform bit a bit (bitwise) and. Copies a bit to the result if it exists in both operands.
r_binary_and1 = 10 & 20 # (10 & 7) binary representation: (001010 & 010100), will give 0 because is 000000 in binary.
r_binary_and2 = 10 & 7 # (10 & 7) binary representation: (1010 & 0111), will give 2 because is 0010 in binary.
print('Binary AND Operator - Perform bit a bit (bitwise) and. Copies a bit to the result if it exists in both operands.')
print('10 & 20 = ',r_binary_and1)
print(format(10, '08b'), ' &')
print("\033[4m"+format(20, '08b')+"\033[0m")
print(format(r_binary_and1,'08b'))
print('10 & 7 = ',r_binary_and2)
print(format(10, '08b'), ' &')
print("\033[4m"+format(7, '08b')+"\033[0m")
print(format(r_binary_and2,'08b'))
#Binary OR Operator - Perform bit a bit (bitwise) or. Copies a bit if it exists in eather operand.
r_binary_or1 = 10 | 20 # (10 | 7) binary representation: (001010 | 010100), will give 30 because is 011110 in binary.
r_binary_or2 = 10 | 7 # (10 | 7) binary representation: (1010 | 0111), will give 15 because is 1111 in binary.
print('Binary OR Operator - Perform bit a bit (bitwise) or. Copies a bit if it exists in eather operand.')
print('10 | 20 = ',r_binary_or1)
print(format(10, '08b'), ' |')
print("\033[4m"+format(20, '08b')+"\033[0m")
print(format(r_binary_or1,'08b'))
print('10 & 7 = ',r_binary_or2)
print(format(10, '08b'), ' |')
print("\033[4m"+format(7, '08b')+"\033[0m")
print(format(r_binary_or2,'08b'))
#Binary XOR Operator - Perform bit a bit (bitwise) xor. Copies the bit if it is set in one operand but not both.
r_binary_xor1 = 10 ^ 20 # (10 ^ 7) binary representation: (001010 ^ 010100), will give 30 because is 011110 in binary.
r_binary_xor2 = 10 ^ 7 # (10 ^ 7) binary representation: (1010 ^ 0111), will give 13 because is 1101 in binary.
print('Binary XOR Operator - Perform bit a bit (bitwise) xor. Copies the bit if it is set in one operand but not both.')
print('10 ^ 20 = ',r_binary_xor1)
print(format(10, '08b'), ' ^')
print("\033[4m"+format(20, '08b')+"\033[0m")
print(format(r_binary_xor1,'08b'))
print('10 ^ 7 = ',r_binary_xor2)
print(format(10, '08b'), ' ^')
print("\033[4m"+format(7, '08b')+"\033[0m")
print(format(r_binary_xor2,'08b'))
#Binary Ones Complement Operator - Perform not each bit in 8 bits, this result a negative numbre (Two's Complement Representation).
#Is unary and has the efect of 'flipping ' bits.
r_binary_complement1 = ~7 # (~7) binary representation: (~00000111), will give -8 because is 11111000 in binary (Two's Complement Representation).
r_binary_complement2 = ~10 # (~7) binary representation: (~00001010), will give -11 because is 11110101 in binary (Two's Complement Representation).
r_binary_complement3 = ~20 # (~7) binary representation: (~00010100), will give -21 because is 11101011 in binary (Two's Complement Representation).
print('Binary Ones Complement Operator - Perform not each bit in 8 bits, this result a negative numbre (Two\'s Complement Representation).')
print('~7 = ',r_binary_complement1)
print(format(7, '08b'), ' (Standard binary form of 7)')
print(format((1 << 8) + r_binary_complement1,'08b'), ' (Two\'s Complement Representation of -8)')
print(format(r_binary_complement1,'08b'), ' (Standard binary form of -8)')
print('~10 = ',r_binary_complement2)
print(format(10, '08b'), ' (Standard binary form of 10)')
print(format((1 << 8) + r_binary_complement2,'08b'), ' (Two\'s Complement Representation of -11)')
print(format(r_binary_complement2,'08b'), ' (Standard binary form of -11)')
print('~20 = ',r_binary_complement3)
print(format(20, '08b'), ' (Standard binary form of 20)')
print(format((1 << 8) + r_binary_complement3,'08b'), ' (Two\'s Complement Representation of -21)')
print(format(r_binary_complement3,'08b'), ' (Standard binary form of -21)')
#Binary Left Shift Operator - The left operands value is moved left by the number of bits specified by the right operand.
r_binary_left_shift1 = 7 << 1 # (7) << 1 binary representation: (00000111) << 1, wil give 14 because is 00001110 in binary.
r_binary_left_shift2 = 7 << 2 # (7) << 2 binary representation: (00000111) << 2, wil give 28 because is 00011100 in binary.
r_binary_left_shift3 = 10 << 3 # (7) << 3 binary representation: (00001010) << 3, wil give 80 because is 01010000 in binary.
print('Binary Left Shift Operator - The left operands value is moved left by the number of bits specified by the right operand.')
print('7 << 1 = ',r_binary_left_shift1)
print(format(7, '08b'), ' << 1')
print(format(r_binary_left_shift1,'08b'))
print('7 << 2 = ',r_binary_left_shift2)
print(format(7, '08b'), ' << 2')
print(format(r_binary_left_shift2,'08b'))
print('10 << 3 = ',r_binary_left_shift3)
print(format(10, '08b'), ' << 3')
print(format(r_binary_left_shift3,'08b'))
#Binary Right Shift Operator - The left operands value is moved rig ht by the number of bits specified by the right operand.
r_binary_right_shift1 = 7 >> 1 # (7) >> 1 binary representation: (00000111) >> 1, wil give 3 because is 00000011 in binary.
r_binary_right_shift2 = 7 >> 2 # (7) >> 2 binary representation: (00000111) >> 2, wil give 1 because is 00000001 in binary.
r_binary_right_shift3 = 10 >> 3 # (7) >> 3 binary representation: (00001010) >> 3, wil give 1 because is 00000001 in binary.
print('Binary Right Shift Operator - The left operands value is moved rig ht by the number of bits specified by the right operand.')
print('7 >> 1 = ',r_binary_right_shift1)
print(format(7, '08b'), ' >> 1')
print(format(r_binary_right_shift1,'08b'))
print('7 >> 2 = ',r_binary_right_shift2)
print(format(7, '08b'), ' >> 2')
print(format(r_binary_right_shift2,'08b'))
print('10 >> 3 = ',r_binary_right_shift3)
print(format(10, '08b'), ' >> 3')
print(format(r_binary_right_shift3,'08b'))

#The IF statement (single line) - They allow specific line of code to execute only when a given condition evaluates to True.
edad = 17
print('The IF statement (single line) - They allow specific line of code to execute only when a given condition evaluates to True.')
print('edad = ', edad)
if edad < 18: print('Es menor de edad.')
#The IF statement - They allow specific blocks of code to execute only when a given condition evaluates to True.
edad = 18
print('The IF statement - They allow specific blocks of code to execute only when a given condition evaluates to True.')
print('edad = ', edad)
if edad >= 18:
    print('Es mayor de edad.')
    print('Puede Votar.')
#The ELSE statement with IF - Provide an alternative block of code to be executed when none of the preceding conditions are met.
#It acts as a "catch-all" for any scenario not covered by the previous conditions.
edad = 0
print('The ELSE statement with IF - Provide an alternative block of code to be executed when none of the preceding conditions are met.')
print('edad = ', edad)
if edad >= 18:
    print('Es mayor de edad.')
    print('Puede Votar.')
else:
    print('No es mayor de edad.')
#The ELIF statement - Is used in conjunction with an if statement to check for multiple conditions sequentially.
edad = 5
print('The ELIF statement - Is used in conjunction with an if statement to check for multiple conditions sequentially.')
print('edad = ', edad)
if edad >= 18:
    print('Es mayor de edad.')
    print('Puede Votar.')
elif edad >= 0:
    print('Es menor de edad.')
    print('No puede Votar.')
else:
    print('Edad no válida')
#The WHILE loop (single statement suit) -  used for repeatedly executing a single statement as long as a specified condition remains true.
count = 1
print('The WHILE loop (single statement suit) -  used for repeatedly executing a single statement as long as a specified condition remains true.')
while count <= 5: print(count); count += 1
#The WHILE loop - used for repeatedly executing a block of code as long as a specified condition remains true.
count = 2
print('The WHILE loop - used for repeatedly executing a block of code as long as a specified condition remains true.')
while count <= 10:
    print(count)
    count += 2
#The ELSE statement with WHILE - The else block associated with a while loop executes only if the loop terminates normally, meaning the while condition eventually becomes False.
count = 1
print('The ELSE statement with WHILE - The else block associated with a while loop executes only if the loop terminates normally, meaning the while condition eventually becomes False.')
while count <= 5:
    print(count)
    count += 1
else:
    print('Loop finished normaly.')
#The BREAK statement with WHILE - The break statement provides a way to exit this loop prematurely, even if the while condition is still True.
count = 1
print('The BREAK statement with WHILE - The break statement provides a way to exit this loop prematurely, even if the while condition is still True.')
while count <= 5:
    print(count)
    if count == 4: break
    count += 1
else:
    print('This will NOT be printed because of break.')
#The CONTINUE statement with WHILE - used to skip the rest of the code within the current iteration of the loop and immediately proceed to the next iteration. 
count = 1
print('The CONTINUE statement with WHILE - used to skip the rest of the code within the current iteration of the loop and immediately proceed to the next iteration.')
while count <= 5:
    count += 1
    if count == 4: continue
    print(count)
else:
    print('Loop finished normaly.')
#The PASS statement with WHILE - is a null operation; when it is executed, nothing happens.
count = 1
print('The PASS statement with WHILE - is a null operation; when it is executed, nothing happens.')
while count <= 5:
    count += 1
    if count == 4:
        pass
    else:
        print(count)
else:
    print('Loop finished normaly.')
#The FOR loop - is a control flow statement used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects.
lst_leters = ['a','b','c','d','e']
print('The FOR loop - is a control flow statement used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects.')
for leter in lst_leters:
    print(leter)
#The FOR loop (using enumerate()) - simultaneously accessing both the index and the value of each item.
lst_leters = ['a','b','c','d','e']
print('The FOR loop (using enumerate()) - simultaneously accessing both the index and the value of each item.')
for index, leter in enumerate(lst_leters):
    print(index, ' - ', leter)
#Handling an EXCEPTION - is a mechanism to handle the event that disrupts the normal flow of a program's execution.
print('Handling an EXCEPTION - is a mechanism to handle the event that disrupts the normal flow of a program\'s execution.')
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    #Handle another specific exception and get its details
    print(t)
except Exception as e:
    #Catch any other unhandled exceptions
    print(e)
else:
    print('Operation completed successfully.')
finally:
    print('Cleanup operations completed.')
#The EXCEPTION clause with no exceptions - when no specific exception define
print('The EXCEPTION clause with no exceptions - when no specific exception define')
try:
    result = 10 / 0
    print(result)
except:
    print('An exception occurred')
else:
    print('Operation completed successfully.')
finally:
    print('Cleanup operations completed.')
#The EXCEPTION clause with multiple exceptions - when multiple exceptions are defined
print('The EXCEPTION clause with multiple exceptions - when multiple exceptions are defined')
try:
    result1 = 10 / 10
    result2 = 10 + '10'
    print(result1, ' - ', result2)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
else:
    print('Operation completed successfully.')
finally:
    print('Cleanup operations completed.')
#Raising an EXCEPTIONS - allows you to explicitly signal that an error or an unexpected condition has occurred during program execution.
def process_number(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    if number < 0:
        raise ValueError("Number cannot be negative.")
    return number * 2
print('Raising an EXCEPTIONS - allows you to explicitly signal that an error or an unexpected condition has occurred during program execution.')
try:
    result = process_number('5')
    print(result)
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
#user-defined EXCEPTIONS
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
print('user-defined EXCEPTIONS')
try:
    raise Networkerror('Bad hostname')
except Networkerror as n:
    print(n.args)