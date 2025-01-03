# asignement operator
n1 = 10
n2 = 3
n1 += 2 # same that n1 = n1 + 2

# Aricmethic operators
add = 2 + 2
sub = 3 - 2 
mult = 5 * 2 
div = 10 * 2 # 5.0 (Division always return a float number)
mod = 10 % 3 # Module (return the reaminder) 1 
floor_division = 10 // 3 # 3, Return a integer of division
exponential = 2 ** 3 # 2 * 2 * 2

#Logic operators
"""
AND = Return True if both conditions are true
OR = Return True if one of the statement is true
NOT = Invert the result, if not True = False 
"""
print(3 < 5 and 4 < 5) # True
print(3 < 5 and 5 < 5) #False
print(3 < 5 or 5 < 5) #True
print(3 < 2 or 4 < 2) #False
print(not True) #False 
print(not False) #True

#Comparison operators
"""
== equal
> mayor than
>= mayor or equal than
< menor than
<= menor or equal than
!= not equal or diferent
"""
print("-----Comparison Operators-----")
print(3 == 2) # False
print(3 == 3) #True
print(3 > 2) #True
print(3 > 3) #False
print(5 >= 2) #True
print(2 >= 3) #False
print(2 < 3) #True
print(3 < 2) # False
print(2 <= 2) #True
print(2 <= 1) #False
print(2 != 3) #True
print(3 != 3) #False

print("-----Identity Operators-----")
"""
Identity Operators are used to compare objects
IS = is the same object?
IS NOT = Is no the same object
"""
x = 10
y = 8 
print(x is 5 + 5) # True, because 10 is equal that 5+5=10
print(y is not 4 * 2) # False, because 8 is 8

print("-----Membership operators-----")
"""
Are used to test if a statement is present in an object
IN = Return True if a Sequence specific in an object
NOT IN = Return True if a statement specific is not present in the object 
"""
print(f"'D' in 'Duban:' {'D' in 'Duban'}")
print(f"'S' not in 'Duban': {'S' not in 'Duban'}") #True


print("-----Bit Operators-----")
"""
Integer numbers to binary numbers
AND (&)
OR (|)
XOR (^)
NOT (~)
MOVE TO RIGHT (>>)
MOVE TO LEFT (<<)
"""
a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {a & b}") # 0010 = 2
print(f"OR: 10 | 3 = {a | b}") # 1011 = 11
print(f"XOR: 10 ^ 3 = {a ^ b}") # 1001 = 9
print(f"NOT: {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010 = 2
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000 = 40


print("-----Control estructures-----")
#Conditionals
"""
if- elif - else
"""
print("IF STATEMENT")
grade = -1
if 9 <= grade <= 10: # if
    print("Excelent")
elif 6 <= grade < 9:  # elif
    print("Aprobbed")
elif 0 <= grade <= 5:
    print("Reprobbed")  
else:
    print("Invalid grade")

# Iteratives

"""
while
"""
counter = 1
while counter <=10:
    print(counter)
    counter += 1

# for
# Using the range function
my_list = ["Orange", "Pineapple", "Strawberry", "Watermelon"]
for i in my_list:
    print(i) # Print each element of my list

#try - except

try:
    number = int(input("enter a int number: "))
except:
    print("X is not integer")
else:
    print(f"your number: {number}")
finally:
    print("Continue with the program")


"""Extra difficulty"""

for num in range(10,56):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)