### Python Operators ###

#! Arithmetic

# Addition 
print(4 + 5)

# Subtraction
print(5 - 4)

# Multiplication
print(5 * 5)

# Division
print(15 / 3)

#* Modulus
print(10 % 2)

# Exponent
print(6**2)

# Floor Division
print(15 // 2)

#! Comparison Operators

# Equal
print(2 == 2)

#*Not Equal
print(2 != 2)

# Less Than
print(5 < 10)

# Greater Than
print(8 > 10)

# Less Than Or Equal To
print(8 <= 8)

# Greater Than Or Equal To
print(8 >= 8)

#! Assignment Operators

# Assignment Operator
x = "Hello"
print(x)

# Addition Assignment
my_num = 10
my_num += 8
print(my_num)

# Subtraction Assignment
my_num = 10
my_num -= 5
print(my_num)

# Multiplication Assignment
my_num = 10
my_num *= 2
print(my_num)

# Division Assignment
my_num = 20
my_num /= 2
print(my_num)

# Remainder Assignment
my_num = 50
my_num %= 5
print(my_num)

# Exponent Assignment
my_num = 5
my_num **= 2
print(my_num)

# Floor Division Assignment
my_num = 9
my_num //= 2
print(my_num)

#! Logical Operators

# And
print(True and True)
print(False and True)

# Or
print(True or True)
print(False or True)

# Not
print(not False)

#! Membership Operators

# In
my_list = [1, 5, 8, 5, 6]
print(1 in my_list)
print(10 in my_list)

# Not In
my_list = [1, 5, 8, 5, 6]
print(1 not in my_list)
print(10 not in my_list)

#! Identity Operators

# Is
num_one = 1
num_two = 2
print(num_one is num_one)
print(num_one is num_two)

num_one = 1
num_two = num_one
print(num_one is num_one)
print(num_one is num_two)

# Is Not
num_one = 1
num_two = 2
print(num_one is num_one)
print(num_one is num_two)

num_one = 1
num_two = num_one
print(num_one is not num_one)
print(num_one is not num_two)

#! Bitwise Operators

# Binary And
print(1 & 0)

# Binary Or
print(1 | 0)

# Binary Xor
print(1 ^ 0)

# Binary Complement
print(~1)

# Binary Left Shift
print(10 << 2)

# Binary Right Shift
print(40 >> 2)

###* Control Structures ###

#! Selection Statements

num_one = 55
num_two = 10

if num_one > num_two:
  print(f'Num one {num_one} is greater than num two {num_two}.')
elif num_one < num_two:
  print(f'Num two {num_two} is greater than num two {num_one}.')
else:
  print(f'Num one {num_one} and number two {num_two} are equal.')
  
num_one = 55
num_two = 100

if num_one > num_two:
  print(f'Num one {num_one} is greater than num two {num_two}.')
elif num_one < num_two:
  print(f'Num two {num_two} is greater than num two {num_one}.')
else:
  print(f'Num one {num_one} and number two {num_two} are equal.')
  
num_one = 55
num_two = 55

if num_one > num_two:
  print(f'Num one {num_one} is greater than num two {num_two}.')
elif num_one < num_two:
  print(f'Num two {num_two} is greater than num two {num_one}.')
else:
  print(f'Num one {num_one} and number two {num_two} are equal.')
  
my_var_one = True
my_var_two = True

if my_var_one and my_var_two:
  print('All of the items are True')
else:
  print('One of the Items is False')
  
my_var_one = True
my_var_two = False

if my_var_one and my_var_two:
  print('All of the items are True')
else:
  print('One of the Items is False')
  
my_var_one = True
my_var_two = False

if my_var_one or my_var_two:
  print('One of the items is True')
else:
  print('All of the Items are False')
  
my_var_one = False
my_var_two = False

if my_var_one or my_var_two:
  print('One of the items is True')
else:
  print('All of the Items are False')

#! Repetition

counter = 0

while counter <= 10:
  print(f'Counting to ten: {counter}')
  counter += 1
  
my_nums = [1 ,5 ,4 ,8, 10, 15]

for num in my_nums:
  print(num) if num != 5 else print(f'I\'m a five')

#! Optional Challenge

print('---Optional Challenge----')

for num in range(10, 56):
  if num == 55:
    print(num)
  
  if num % 2 == 0 and num % 3 != 0 and num != 16:
    print(num)
  
  
  
