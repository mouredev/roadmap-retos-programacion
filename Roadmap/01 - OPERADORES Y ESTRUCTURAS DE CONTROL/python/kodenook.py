
num1:int = 3
num2:int = 2

""" Arithmetic Operators"""

# addition
print(f'sum: {num1 + num2}')
# subtraction
print(f'subtraction: {num1 - num2}')
# multiplication
print(f'multiplication: {num1 * num2}')
# division
print(f'division: {num1 / num2}')
# modulus
print(f'modulus: {num1 % num2}')
# exponentiation
print(f'exponentiation: {num1 ** num2}')
# floor division (rounds the result down to the nearest whole number)
print(f'floor division: {num1 // num2}')

""" Assignment Operators"""

num3 = 2 # assignment
print(num3)
num3 += 1
print(num3)
num3 -= 2
print(num3)
num3 *= 2
print(num3)
num3 /= 2
print(num3)
num3 %= 3
print(num3)
num3 **= 2
print(num3)
num3 //= 1
num3 = 4
print(num3)
num3 &= 1
print(num3)
num3 |= 1
print(num3)
num3 ^= 1
print(num3)
num3 <<= 1
print(num3)
num3 >>= 1
print(num3)

""" Comparison Operators """

print(3 == 2) # equal
print(4 != 2) # not equal
print(4 > 2) # greater than
print(4 < 2) # less than
print(4 >= 2) # greater than or equal than
print(4 <= 2) # less than or equal than

""" Logical Operators """

print(1 and 2) # true if both are true
print(1 or 3) # true if either are true
print(not(1)) # return false if result is true

""" Identity Operators """

print(1 is 1) # return true if are the same
print(1 is not 1) #return true if are not the same

""" Membership Operators """

print('h' in 'hi') # true if value is present in the object
print('h' not in 'hi') # true if value is not present in the object

""" Bitwise Operators """

print(6 & 3) # compare each bit and set it to 1 if both are 1, otherwise it is set to 0
print(6 | 3) # compare each bit and set it to 1 if one or both are 1, otherwise it is set to 0
print(6 ^ 3) # compare each bit and set it to 1 if only one is 1, otherwise it is set to 0
print(~3) # inverts each bit, 0 becomes 1 and 1 becomes 0
print(3 << 2) # insert the specified numbers of 0's (in this case 2) from the right
print(8 >> 2) # insert the specified numbers of 0's (in this case 2) from the left

""" If """

if 3 > 1:
    print(3)
elif 3 < 4:
    print(4)
else:
    print('other result')

""" Short hand if """

if 3 == 3: print('equals')
print('A') if 'A' > 'B' else print('B')
print('A') if 'a' > 'b' else print('=') if 'a' == 'A' else print('B')

""" Loop while """

i = 1
while i < 2:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

""" Loop for """

for x in range(6):
    print(x)
else:
    print("Finally finished!")

""" Exceptions """

try:
    if 2 == 2:
        raise Exception("Sorry, no numbers below zero")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
  print("The 'try except' is finished")


""" Exercise """
for x in range(10, 56):
    if x % 2 == 0 and x != 16 and x % 3 != 0:
        print(x)