# { ROADMAP PARA PROGRAMADORES }  #1 OPERADORES Y ESTRUCTURAS DE CONTROL
# BIBLIOGRAFY REFERENCE: Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)

# SIMPLE MATEMATICAL OPERATORS

# DIVISION
""" Python does integer division when both operands are integers. The behavior of Python's division operators have changed from Python 2.x and 3.x (*see also Integer Division ). """

a, b, c, d, e = 3, 2, 2.0, -3, 10

print(a / b) # = 1.5
print(a / c) # = 1.5
print(d / b) # = -1.5
print(b / a) # = 0.6666666666666666
print(d / e) # = -0.3

d /= b # = -1.5
print(d) # = -1.5


# The ' // ' operator in Python 2 forces floored division regardless of type.
print(a // c) # = 1.0 (Integer Division)
float(a) / float(b) # = 1.5 

''' Possible combinations (builtin types):
int and int (gives an int in Python 2 and a float in Python 3)
int and float (gives a float)
int and complex (gives a complex)
float and float (gives a float)
float and complex (gives a complex)
complex and complex (gives a complex) '''

# ADDITION

print(a + b) # = 5
a += e # = 13

# SUBSTRACTION

print(e - b) # = 8
e -= a + 2 # = -5

import operator # contains 2 argument arithmetic functions
operator.sub(b, a) # = -1

# MULTIPLICATION

print(e * e) # = 25
e *= b # = -10
print(e) # = -10

import operator
operator.mul(e, e) # = 25

# EXPONENTIATION

a, b = 2, 3
(a ** b) # = 8
pow(a, b) # = 8 

import math
math.pow(a, b) # = 8.0 (always float; does not allow complex results)

import operator
operator.pow(a, b) # = 8

# Another difference between the built-in pow and math.pow is that the built-in pow can accept three arguments:
a, b, c = 2, 3, 2
pow(2, 3, 2) # 0, calculates (2 ** 3) % 2, but as per Python docs,
# does so more efficiently

# MODULUS
print(3 % 4) # 3
print(10 % 2) # 0
print(6 % 4) # 2

#Or by using the operator module:
import operator
operator.mod(3 , 4) # 3
operator.mod(10 , 2) # 0
operator.mod(6 , 4) # 2

#You can also use negative numbers.
print(-9 % 7) # 5
print(9 % -7) # -5
print(-9 % -7) # -2

#If you need to find the result of integer division and modulus, you can use the divmod function as a shortcut:
quotient, remainder = divmod(9, 4)
# quotient = 2, remainder = 1 as 4 * 2 + 1 == 9

# INPLACE OPERATIONS

# It is common within applications to need to have code like this:
a = a + 1
# or
a = a * 2
# There is an effective shortcut for these in place operations:
a += 1
# and
a *= 2

''' Any mathematic operator can be used before the '=' character to make an inplace operation:
-= decrement the variable in place
+= increment the variable in place
*= multiply the variable in place
/= divide the variable in place
//= floor divide the variable in place # Python 3
%= return the modulus of the variable in place
**= raise to a power in place '''

#BITWISE OPERATORS
""" #The ~ operator will flip all of the bits in the number. Since computers use signed number representations — most notably, the two's complement notation to encode negative binary numbers where negative numbers are written with a leading one (1) instead of a leading zero (0). from 0000 0000 to 0111 1111 to represent numbers from 0 to 127 and reserve 1xxx xxxx to represent negative numbers.
#Eight-bit two's-complement numbers Bits Unsigned Value Two's-complement Value 0000 0000 0 0 0000 0001 1 1 0000 0010 2 2 0111 1110 126 126 0111 1111 127 127 1000 0000 128 -128 1000 0001 129 -127 1000 0010 130 -126 1111 1110 254 -2 1111 1111 255 -1
#In essence, this means that whereas 1010 0110 has an unsigned value of 166 (arrived at by adding (128 * 1) + (64 * 0) + (32 * 1) + (16 * 0) + (8 * 0) + (4 * 1) + (2 * 1) + (1 * 0)), it has a two's-complement value of -90 (arrived at by adding (128 * 1) - (64 * 0) - (32 * 1) - (16 * 0) - (8 * 0) - (4 * 1) - (2 * 1) - (1 * 0), and complementing the value).
#In this way, negative numbers range down to -128 (1000 0000). Zero (0) is represented as 0000 0000, and minus one (-1) as 1111 1111. """
#In general, though, this means ~n = -n - 1.
# 0 = 0b0000 0000
print(~0) # Out: -1
# -1 = 0b1111 1111
# 1 = 0b0000 0001
print(~1) # Out: -2
# -2 = 1111 1110
# 2 = 0b0000 0010
print(~2) # Out: -3
# -3 = 0b1111 1101
# 123 = 0b0111 1011
print(~123) # Out: -124
# -124 = 0b1000 0100
#Note, the overall effect of this operation when applied to positive numbers can be summarized:
#~n -> -|n+1|
#And then, when applied to negative numbers, the corresponding effect is:
#~-n -> |n-1|


# Unary Plus and Minus
# When the unary plus is applied to a non-numeric value, it converts it to a number.

str1 = "03"
str1 = int(str1)
print(str1)  # value becomes numeric 3

str2 = "1.4"
print(str1 + float(str2))  # 4.4

str2 = float(str2)
print(str2)  # value becomes numeric 1.4

str3 = "zaz"
str3 = float('nan')  # Cannot convert to number, becomes NaN
print(str3)  # value becomes NaN

bool_val = True
bool_val = int(bool_val)  # True becomes 1
print(bool_val)  # value becomes numeric 1

f_num = 2.8
f_num = float(f_num)  # no change, still 2.8
print(f_num)  # 2.8

class Obj:
    def __int__(self):
        return -5

obj = Obj()
obj = int(obj)  # value becomes numeric -5
print(obj)  # -5

# Negation
g_actions = 50
g_actions = -g_actions
print(g_actions)  # value becomes -50

str1 = -str1
print(str1)  # value becomes numeric -3

str2 = -str2
print(str2)  # value becomes numeric -1.4

str3 = -str3
print(str3)  # value becomes NaN

bool_val = -bool_val
print(bool_val)  # value becomes numeric -1

f_num = -f_num
print(f_num)  # no change, still -2.8

obj = -obj
print(obj)  # value becomes numeric 5

# Increment/Decrement
num1 = 10
num2 = 5
num3 = num1
num1 += 1
print(num3)  # 10
print(num1)  # 11
num3 = num1 + 1
print(num3)  # 12
print(num1)  # 11
num4 = num2
num2 -= 1
print(num4)  # 5
print(num2)  # 4
num4 -= 1
print(num4)  # 4
print(num2)  # 4
num4 += 1
print(num4)  # 5

# Bitwise Operators
# Bitwise NOT ~
n1 = 25  # binary 00000000000000000000000000011001
n2 = ~n1  # binary 11111111111111111111111111100110
print(n2)  # -26

# Bitwise AND &
n3 = 25 & 3
print(n3)  # 1

# Bitwise OR |
n3 = 25 | 3
print(n3)  # 27

# Bitwise XOR ^
n3 = 25 ^ 3
print(n3)  # 26

# Left Shift <<
number = 2  # 10 in binary code
new_number = number << 6  # 10000000 in binary code which is decimal 128
print(new_number)  # 128

# Signed Right Shift >>
number = 128  # 10000000 in binary code
new_number = number >> 6  # 10 in binary code which is decimal 2
print(new_number)  # 2

# Boolean Operators
# Logical NOT !
print(not False)  # True
print(not "shadow")  # False
print(not 0)  # True
print(not float('nan'))  # False
print(not "")  # True
print(not 57344)  # False
print(not None)  # True

# Logical AND &&
print(True and 'Angy')  # Angy
print(False and 'Angy')  # False
print(4 < 5 and 8 > 6)  # True

# Note: Both AND and OR are short-circuit operators, meaning sometimes only the first operator is evaluated.

# Multiplicative Operators
# There are three multiplicative operators in Python: multiply, divide, and modulus.
# These operators work similarly to their counterparts in languages such as Java, C, and Perl,
# but they also include some automatic type conversions when dealing with non-numeric values.

# Multiply Operator *
number = 4 * int('8')
print(number)  # Logs: 32

# Divide Operator /
number = 10 / 5
print(number)  # Logs: 2.0
number = 4 / 40
print(number)  # Logs: 0.1 

# Modulus (remainder) Operator %
number = 41 % 5
print(number)  # Logs: 1

# Exponentiation Operator **
number = 4 ** 2
print(number)  # Logs: 16
# same as
print(pow(4, 2))  # Logs: 16

# Add Operator +
number = 76 + 78
print(number)  # Logs: 154
print('76' + '78')  # Logs: 7678 (string concatenation)

number = 767867686876876 + 6757575755
print(number)  # Logs: 767874444452631

# Subtract -
number = 48 - 3
print(number)  # Logs: 45

# Note: These operators have particular behavior in some cases when used with 'inf'(Infinity), 0, 'nan'(NaN not a number).

# Relational Operators
# The less-than (<), greater-than (>), less-than-or-equal-to (<=), and greater-than-or-equal-to (>=)
# relational operators perform comparisons between values similarly to what you learned in math class.

computation = 76 < 4
print(computation)  # Logs: False
computation = 87 > 32
print(computation)  # Logs: True
computation = 43 <= 43
print(computation)  # Logs: True
computation = 44 >= 85
print(computation)  # Logs: False

user = {
    'name': 'Calvin & Hobbes'
}

try:
    print(user <= 4)  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Handle the error and print a message
# TypeError: '<=' not supported between instances of 'dict' and 'int'   
#This way the program doesn't interrup with the TypeError

print("43" < "8")  # Logs: True
try:
    print("43" < 8)  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Handle the error and print a message
# TypeError: '<' not supported between instances of 'str' and 'int'     

print('DeepState' < 'real people')  # Logs: True  
# True not only cause are more real people, but when we talk about strings the upper characters has lower codes than the regulars ones
print('deepstate' < 'real people')  # Logs: True
# True again ... well ummm sometimes we win 

#Comparison Behavior in Python
#Numeric Comparison:
#If both operands are numbers (integers or floats), Python performs a numeric comparison directly.

print(5 > 3)  # True

#String Comparison:
#If both operands are strings, Python compares them lexicographically (dictionary order) based on the Unicode code points of the characters.

print("apple" < "banana")  # True

#Mixed Types (Number and String):
#If one operand is a number and the other is a string, Python raises a TypeError. Unlike JavaScript, Python does not automatically convert types for comparison.

try:
    print(5 > "3")  # Raises TypeError
except TypeError:
    print("Cannot compare number and string!")  # This will be printed

#Boolean Comparison:
#Booleans in Python are a subclass of integers. True is treated as 1 and False as 0 when compared with numbers.

print(True == 1)  # True
print(False == 0)  # True

#Object Comparison:
#If the operands are objects, Python will use the __lt__, __le__, __gt__, __ge__, __eq__, or __ne__ methods defined in the class of the objects to perform the comparison. If these methods are not defined, Python will raise a TypeError if the objects are of incompatible types.

class MyClass:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

obj1 = MyClass(1)
obj2 = MyClass(2)
print(obj1 < obj2)  # True

# Equality operators
# Determining whether two variables are equivalent is one of the most important operations in programming.

# Equal or Equality Operator ==
print(2 == '2')  # Logs: False (2 is an integer, '2' is a string)

# Not-equal or Inequality Operator !=
print(2 != '2')  # Logs: True (2 is not equal to '2' because they are different types)

# In Python, there is no strict equality operator (===) or strict inequality operator (!==) like in JavaScript.
# The == and != operators perform value comparisons without type checking.

# Checking both value and type
print(2 == '2' and type(2) == type('2'))  # Logs: False
print(2 != '2' and type(2) != type('2'))  # Logs: True


#Equality and Comparison Rules in Python
#Boolean Values:
#In Python, when using the equality (==) operator, True is treated as 1 and False as 0. However, there is no implicit conversion of Booleans to numeric values for comparison; they are compared directly.
print(True == 1)  # True
print(False == 0)  # True

# String and Number Comparison:
# Python does not automatically convert strings to numbers for equality checks.
# Comparing a string with a number using == will return False, not raise an error.

print("5" == 5)  # Logs: False (no TypeError is raised)

# However, if you try to perform an operation that requires both to be the same type, it will raise a TypeError.
try:
    result = "5" + 5  # This will raise TypeError
except TypeError:
    print("Cannot add string and number!")  # This will be printed


# Object Comparison:
# In Python, if one operand is an object and the other is not, the comparison will depend on the type of the other operand.
# If the other operand is not compatible, a TypeError will be raised.

class MyClass:
    def __eq__(self, other):
        # Custom equality check (optional)
        return isinstance(other, MyClass)

obj = MyClass()

# Comparing the same object
print(obj == obj)  # True (same object)

# Comparing with a different object of the same class
another_obj = MyClass()
print(obj == another_obj)  # False (unless __eq__ is defined to return True for same class)

# Comparing with a non-object (like an integer)
try:
    print(obj == 5)  # This will raise TypeError if __eq__ is not defined for MyClass
except TypeError:
    print("Cannot compare object and non-object!")  # This will be printed if TypeError occurs

# If __eq__ is defined, it will return False instead of raising an error
print(obj == "string")  # This will raise TypeError if __eq__ is not defined for MyClass

# None Values:
# In Python, None is a singleton object and is used to signify 'no value' or 'null'.
# It is equal to itself but not equal to any other value.
print(None == None)  # True (None is equal to None)
print(None == 0)     # False (None is not equal to 0)

# NaN (Not a Number):
# Python has a specific representation for NaN, which is float('nan').
# In Python, NaN is not equal to itself, which is a property of NaN in the IEEE floating-point standard.
import math
print(math.isnan(float('nan')))  # True (math.isnan() correctly identifies NaN)
print(float('nan') == float('nan'))  # False (NaN is not equal to NaN)

# Additional note: NaN is often used in data analysis and scientific computing to represent undefined or unrepresentable values.

# Object Identity:
# In Python, the 'is' operator checks for object identity (whether two references point to the same object),
# while '==' checks for value equality.

a = [1, 2, 3]  # List a
b = a         # b references the same object as a
c = a[:]      # c is a shallow copy of a, so it is a different object

print(a is b)  # True (a and b point to the same object)
print(a == c)  # True (a and c have the same value)
print(a is c)  # False (a and c are different objects)

# Checking for NaN
import math
print(math.isnan(float('nan')))  # True (math.isnan() correctly identifies NaN)

# Boolean and None comparisons
print(True == 1)  # True (True is equal to 1 in Python)
print(None == float('nan'))  # False (None is not equal to NaN)
print(None is None)  # True (None is equal to itself)

# Conditional Operator (Ternary Operator)
# In Python, the conditional expression (also known as the ternary operator) allows for conditional assignment to a variable.
# The syntax is: true_value if condition else false_value

user = {'name': 'Nixon'}  # Example user dictionary

# Conditional expression to determine the login message
login = f"Successful login, Welcome {user['name']}" if user['name'] != 'Nixon' else "Sorry we don't have any user with that name"
print(login)  # Logs: Sorry we don't have any user with that name

# Assignment Operators
a = 'a'  # Initial assignment
a = a + a  # Concatenating the string with itself
print(a)  # Logs: aa

# Example of using an assignment operator with a number
number = 8
number += 2  # This is equivalent to number = number + 2
print(number)  # Logs: 10

# Compound assignment operators allow you to perform an operation and assign the result to a variable in one step.
# They are done with one of the arithmetic or bitwise operators followed by an equal sign (=).

number = 8  # Initial value
number *= number  # Equivalent to number = number * number
print(number)  # Logs: 64

number -= 4  # Equivalent to number = number - 4
print(number)  # Logs: 60

# Compound-assignment operators exist for each of the major mathematical operations and a few others as well.
# They are as follows:
# - Multiply/assign (*=)
# - Divide/assign (/=)
# - Modulus/assign (%=)
# - Add/assign (+=)
# - Subtract/assign (-=)
# - Left shift/assign (<<=)
# - Signed right shift/assign (>>=)

# Note: Python does not have an unsigned right shift operator (>>>=).

# Membership Operators
# The 'in' operator
Crows = {
    'description': "Mutant fat man lives beyond the margins of the known universe...",
    'age': 600,
}

print('description' in Crows)  # Logs: True
print('location' in Crows)  # Logs: False

# instanceof operator
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greeting(self):
        return f"Hi {self.name}. Welcome to Roadmap Exercise #01."

niko_zen = User('Niko', 41, 'duendeintemporal@hotmail.com')
print(niko_zen.greeting())  # Logs: 'Hi Niko. Welcome to Roadmap Exercise #01.'

print(isinstance(niko_zen, User))  # Logs: True
print(isinstance(niko_zen, object))  # Logs: True
print(isinstance(4, int))  # Logs: True (4 is a primitive value)
four = 4
print(isinstance(four, int))  # Logs: True

# Type Operators
# We can use isinstance or type() to check the type of an object.
print(type(True))  # Logs: <class 'bool'>
print(type(float('nan')))  # Logs: <class 'float'>
print(type(niko_zen))  # Logs: <class '__main__.User'>

# Destructuring Operations - spread operator equivalent in Python
# on arrays (lists)
books = ['Dune', 'Shibumi', 'El Maestro de Esgrima', 'El Perfume']
books2 = ['Eloquent JavaScript', 'You Don’t Know JS ES6 Beyond', 'Linux Command Line An Admin Beginners Guide', 'Learn Bash the Hard Way', 'Programming Algorithms', 'MATLAB Notes for Professionals']
mix_books = books + books2  # Concatenating two lists
frank_herbert, trevanian = books[0], books[1]  # Destructuring assignment
print(trevanian)  # Logs: Shibumi

# on objects (dictionaries)
email = niko_zen.email  # Accessing an attribute of the User instance
print(email)  # Logs: duendeintemporal@hotmail.com

niko_zen_settings = {
    'mode': 'dark',
    'avatar': 'moebius.svg',
    'interface': 'compact',
}

# Merging dictionaries using unpacking
niko_zen_data = {**niko_zen.__dict__, **niko_zen_settings}
print(niko_zen_data)  # Logs both objects niko_zen instance and niko_zen_settings

# Function to display user information
def show_user(user):
    print(f"User name: {user['name']}, age: {user['age']}, email: {user['email']}")

show_user(niko_zen.__dict__)  # Logs: User name: Niko, age: 41, email: duendeintemporal@hotmail.com

# Assigning default values in destructuring
config = {'font': 'monospace'}
font = config.get('font')  # Gets the value for 'font'
mode = config.get('mode', 'dark')  # Gets the value for 'mode', defaults to 'dark' if not found

print(font, mode)  # Logs: monospace dark

# Variable assignment and swapping
ninja1 = 'Hiroshi'
ninja2 = 'Neko'
ninja3 = 'Kage'

# Swapping values using destructuring
ninja1, ninja2, ninja3 = ninja2, ninja3, ninja1
print(ninja1)  # Logs: Neko

# Copying objects (dictionaries) without modifying the original
shinobi = {
    'skills': ['fast', 'quick', 'precise', 'lethal', 'computational thinking'],
    'location': 'not found',
}

trix = shinobi.copy()  # Create a shallow copy of the dictionary
trix['location'] = 'Bangkok, Thailand'  # Modify the copy

print(shinobi['location'])  # Logs: not found (original remains unchanged)
print(trix['location'])      # Logs: Bangkok, Thailand (modified copy)

# Using * operator to unpack list elements as arguments in functions
nums = [1, 3, 4, 5, 6]
print(max(*nums))  # Logs: 6 (unpacking the list to pass as arguments)

# Function to calculate average
def calculate_average(*numbers):
    total = sum(numbers)  # Sum of all numbers
    return total / len(numbers)  # Average calculation

average = calculate_average(90, 76, 45, 23, 67)
print(average)  # Logs: 60.2

# Converting a string into a list of its individual characters
maximum = 'in a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society'
maxim_arr = list(maximum)  # Converts string to list of characters
print(maxim_arr)  # Logs: ['i', 'n', ' ', 'a', ' ', 's', 'o', 'c', 'i', 'e', ...]

# Tuple unpacking (comma operator equivalent in Python)
number1, number2, number3, number4 = 1, 2, 3, None
print(number1, number2, number3, number4)  # Logs: 1 2 3 None

# Flow Control Statements
number = 225
if number:  # Checks if number is truthy (non-zero)
    number += 4
    print(number)  # Logs: 229

# Else statement
if number:
    number += 4
    print(number)  # Logs: 233
else:
    pass  # This block will not execute since number is truthy

# Else if statement (elif)
if number > 300:
    number += 4
    print(number)  # This block will not execute since number is not greater than 300
elif number > 200:
    number += 4
    print(number)  # Logs: 237 (since number is 233, which is greater than 200)
else:
    pass  # This block will not execute since the previous condition was true

# Do-while equivalent using a while loop
count = 0
while True:
    print("I'm learning a lot in this roadmap for coders, even with these basic exercises")
    count += 1
    if count >= 1:
        break  # This simulates a do-while loop by ensuring the loop runs at least once

# For loop to sum numbers from 1 to 100
number = 0
for i in range(1, 101):
    number += i  # Accumulate the sum of numbers from 1 to 100
print(number)  # Logs: 5050

# For-in statement to iterate over dictionary keys
user2 = {
    'name': 'Nikita',
    'age': 32,
    'location': 'Not Found',
}

for key in user2:
    print(key)  # Logs only the property (key): name
    print(key, user2[key])  # Logs the property and the value: name Nikita

# For-of equivalent to iterate over list elements
odd_nums = [1, 3, 5, 7, 9]
for num in odd_nums:
    print(num)  # Logs each number in the odd_nums list

# Using items() to iterate over dictionary
for key, val in user2.items():
    print(f"{key}: {val}")  # Logs key-value pairs in the dictionary

# Label statements equivalent using break
outer_loop = True
for i in range(11):
    for y in range(5):
        if (i == 2) and (y == 4):
            outer_loop = False  # Set flag to exit outer loop
            break
        if y == 4:
            break  # Breaks the inner loop when y reaches 4
        print('Is there anybody out there?')
    if not outer_loop:
        break  # Breaks the outer loop if the flag is set

# Break and continue statements
number = 0
while number < 5:
    if number == 3:
        break  # Exits the loop when number is 3
    print(number)  # Logs: 0, 1, 2
    number += 1

number = 0
while number < 5:
    if number == 3:
        number += 1  # Increment number to avoid infinite loop
        continue  # Skips the rest of the loop when number is 3
    print(number)  # Logs: 0, 1, 2, 4
    number += 1

# The Switch Statement equivalent using if-elif-else
user_name = user2['name']  # Assuming user2 is defined as in previous examples
if user_name == 'Nikita':
    print('Welcome agent')  # This will log because the name is 'Nikita'
elif user_name == 'Calvin & Hobbes':
    print('Bring me some cookies')
else:
    print('Turn off that TV')  # This will log if the name is neither 'Nikita' nor 'Calvin & Hobbes'

# Extra difficulty: Create a program that prints the even numbers from 10 to 55 inclusive
# and avoids printing the numbers if they are equal to 16 or multiples of 3.
for i in range(10, 56):  # Loop through numbers from 10 to 55
    if i % 3 == 0 or i == 16:  # Skip if the number is a multiple of 3 or equal to 16
        continue
    if i % 2 == 0:  # Check if the number is even
        print(i)  # Print the even number
