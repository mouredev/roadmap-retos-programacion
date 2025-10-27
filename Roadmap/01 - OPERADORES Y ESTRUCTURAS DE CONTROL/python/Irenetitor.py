# 1. All operators categories: Arithmetic, Assignment, Comparison, Logical, Identity, Membership, Bitwise

#Arithmetic Operators: +, -, *, /, %, **, //
Addition = 10 + 5
Subtraction = 10 - 5    
Multiplication = 10 * 5
Division  = 10 / 5        #(always float )
Floor_Division  = 10 // 3   #(rounds down to nearest whole number)
Modulus  = 10 % 3    #(remainder of division)
Exponentiation = 10 ** 2

#Comparison Operators: ==, !=, >, <, >=, <=
Equal = (10 == 5)          #False(checks if values are equal)
Not_Equal = (10 != 5)      #True(checks if values are not equal)
Greater_than = (10 > 5)    #True
Less_than = (10 < 5)       #False
Greater_than_or_equal_to = (10 >= 5)  #True
Less_than_or_equal_to = (10 <= 5)     #False

#Logical Operators: and, or, not
Logical_AND = (10 > 5 and 5 < 3)  #False(both conditions must be true)
Logical_OR = (10 > 5 or 5 < 3)   #True(at least one condition must be true)
Logical_NOT = not(10 > 5)         #False(inverts the boolean value)

#Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=
a = 10      #Assigns value 10 to a
a += 5      #Equivalent to a = a + 5 (now a is 15)
a -= 3      #Equivalent to a = a - 3 (now a is 12)
a *= 2      #Equivalent to a = a * 2 (now a is 24)
a /= 4      #Equivalent to a = a / 4 (now a is 6.0)
a %= 4      #Equivalent to a = a % 4 (now a is 2.0)
a //= 2     #Equivalent to a = a // 2 (now a is 1.0)
a **= 3     #Equivalent to a = a ** 3 (now a is 1.0)

#Identity Operators: is, is not
x = ["apple", "banana"] #True (same object in memory)
y = ["apple", "banana"] #False (different objects in memory)

#Bitwise Operators: &, |, ^, ~, <<, >>
Bitwise_AND = 5 & 3    #1 (binary 0101 & 0011 = 0001)
Bitwise_OR = 5 | 3     #7 (binary 0101 | 0011 = 0111)
Bitwise_XOR = 5 ^ 3    #6 (binary 0101 ^ 0011 = 0110)
Bitwise_NOT = ~5       #-6 (inverts bits, ~0101 = 1010 which is -6 in two's complement)
Left_Shift = 5 << 1    #10 (binary 0101 << 1 = 1010)
Right_Shift = 5 >> 1   #2 (binary 0101 >> 1 = 0010) 

#Membership Operators: in, not in
fruits = ["apple", "banana", "cherry"] #True (checks if "banana" is in the list)
has_mango = "mango" not in fruits #True (checks if "mango" is not in the list)

# 2. Control structures: if, elif, else, for, while, break, continue, pass
#Sequential structure (default mode, executes statements one after another)
print("Start")
print("Middle")
print("End")

#A. Conditional Statements (decision-making)
age = 20
if age < 18:
    print("Minor")
elif age == 18:
    print("Just became an adult")
else:
    print("Adult")

#nested if
if age >= 18:
    if age < 65:
        print("Adult")
    else:
        print("Senior")


#B. Iteration (loops)
#For loop (iterates over a sequence)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#While loop (repeats as long as a condition is true)
count = 0
while count < 5:
    print(count)
    count += 1  #Increment count to avoid infinite loop

#Nested loops (loops inside loops) (Used for multi-dimensional logic)
for i in range(3):  #Outer loop
    for j in range(2):  #Inner loop
        print(f"i: {i}, j: {j}")

#C. Jump statements (alter the flow of loops)
#Continue statement (skips the current iteration)
for i in range(10):
    if i % 2 == 0:
        continue  #Skip even numbers
    print(i)  #Prints only odd numbers  

#Break statement (exits the loop)
for i in range(10):
    if i == 5:
        break  #Exit loop when i is 5
    print(i)

#Pass statement (does nothing, used as a placeholder)
for i in range(5):
    pass  #No operation, can be used to create empty loops or functions
print("Loop completed")

#D. Exception Handling (try, except, finally)
try:
    result = 10 / 0  #This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")
#The finally block always executes, regardless of whether an exception occurred or not.

#3. Print Examples

#4. Optional exercise 

for x in range(10, 56, 1):
    if x % 2 != 0 or x == 16 or x % 3 == 0:
        continue
    print(x)



