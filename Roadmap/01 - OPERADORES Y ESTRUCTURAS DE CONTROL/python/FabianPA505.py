#---  OPERATORS  ---#

# Arithmetic ( +, -, *, /, %, **, // )
operand_1 = 10
operand_2 = 7
print(f'Addition: {operand_1 + operand_2}')           # returns the sum
print(f'Subtraction: {operand_1 - operand_2}')        # returns the difference
print(f'Multiplication: {operand_1 * operand_2}')     # returns the product
print(f'Division: {operand_1 / operand_2}')           # returns the quotient (includes decimals)
print(f'Modulus: {operand_1 % operand_2}')            # returns the remainder
print(f'Power: {operand_1 ** operand_2}')             # returns the exponentiation
print(f'Floor division: {operand_1 // operand_2}')    # returns the integer quotient


# Logical ( for boolean values ) -> AND, OR, NOT
print(True and True)        # returns True
print(True and False)       # returns False
print(True or False)        # returns True
print(not True)             # returns False
print(not False)            # returns True
print(not 0)                # zero is equivalent to False, returns True
print(not 1)                # one is equivalent to True, returns False


# Comparison ( >, <, ==, >=, <=, !=, ) -> returns a boolean value
print(f'Greater than: {operand_1 > operand_2}')         # returns True
print(f'Less than: {operand_1 < operand_2}')            # returns False
print(f'Equal to: {operand_1 == operand_2}')            # returns False
print(f'Greater or equal: {operand_1 >= operand_2}')    # returns True
print(f'Less or equal: {operand_1 <= operand_2}')       # returns False
print(f'Not equal: {operand_1 != operand_2}')           # returns True


# Assignment ( =, +=, -=, *=, /=, %=, **=, //= ) -> assign values to a variable
x = 5
print(f'Variable x: {x}')
x += 10 # equivalent to x = x + 10
print(f'Add 10 to variable x: {x}')
x -= 10 # equivalent to x = x - 10
print(f'Subtract 10 from variable x: {x}')
x *= 10 # equivalent to x = x * 10
print(f'Multiply variable x by 10: {x}')
x /= 10 # equivalent to x = x / 10
print(f'Divide variable x by 10: {x}')
y = 45
y %= 10 # equivalent to y = y % 10
print(f'Modulus 10 with variable y: {y}')
y **= 10
print(f'Power 10 to variable y: {y}')
y //= 5
print(f'Floor division of variable y by 5: {y}')


# Identity ( is, is not) -> check if two variables reference the same memory location
x = 3
y = 3
z = 4
print(x is y)               # returns True
print(x is not y)           # returns False
print(x is z)               # returns False
print(x is not z)           # returns True


# Membership ( in, not in) -> check if a value is in a sequence (lists, tuples, strings)
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)          # returns True
print(15 not in numbers)     # returns True

text = 'Hello, how are you?'
print('how' in text)         # returns True
print('of' in text)          # returns False
print('He' in text)          # returns True
print('he' in text)          # returns False, case sensitive



#---  CONTROL STRUCTURES ( Conditional, iterative, exception handling... )  ---#

# CONDITIONAL
# If, elif, else ( check if one or multiple conditions are met -> use comparison and logical operators)
total_purchase = 120

if total_purchase <= 100:
    print('Pay with cash')
elif 100 < total_purchase < 500:
    print('Pay with debit card')
else:
    print('Pay with credit card')


# ITERATIVE
# While ( perform an action while a condition is true. Stops when the condition is false)
count = 0
while count <= 10:
    print(count)
    count += 1


# For ( iterate over a collection - Lists or Tuples)
colors = ('green', 'red', 'yellow', 'blue', 'orange')
for color in colors:
    print(color)


# EXCEPTION HANDLING
while True:
    # exception control
    try:
        number = int(input('Enter a number: '))
        break # if a valid number is entered, exit the loop
    
    # if an invalid input is entered, handle the error
    except ValueError:
        print('Error! Invalid input. Please try again.')


#---  Extra Challenge  ---#
# Use a For loop to iterate over the range and an If statement with comparison operators
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
