# Arithmetic Operators
print('Arithmetic Operators')
print('+ Addition: ',5+3)
print('- Subtraction: ',5-3)
print('* Multiplication: ',5*3)
print('/ Division: ',5/3)
print('% Modulus: ',5%3)
print('** Exponentiation: ',5**3)
print('// Floor division: ',5//3)

# Assignment Operators
print('\nAssignment Operators')
let =10
print('= Assigment: ',let)
let+=1
print('+= Addition assigment: ',let)
let-=1
print('-= Substraction assigment: ',let)
let *=10
print('*= Multiplication assigment: ',let)
let /=5
print('/= Division assigment: ',let)
let %=1.5
print('%= Modulus assigment: ',let)
var =5
var &=3
print('&= Bitwise AND assigment: ',var)
var |=3
print('|= Bitwise OR assigment: ',var)
var ^=7
print('^= Bitwise XOR assigment: ',var)
var >>=0
print('>>= right shift assigment: ',var)
var <<=1
print('<<= left shift assigment: ',var)

# Comparison Operators
print('\nComparison Operators')
print('> Greater than:',1 > 2)
print('> Less than:',1 < 2)
print('== Equal to:',1 == 2)
print('!= Equal to:',1 != 2)
print('>= Greater to:',1 >= 2)
print('<= Less to:',1 <= 2)

# Logical Operators
print('\nLogical Operators')
x = 2
print('and',x < 5 and  x < 10)
print('or',x < 5 or  x < 10)
print('not',not(x < 5 and x < 10))

# Identity Operators
print('is', 1 is 1)
print('is not', 1 is not 1)

# Membership Operators
fuits = ["apple", "banana"]
print("banana" in fuits)
print("pineapple" not in fuits)

# CONTROL STRUCTURES
print('\nCONTROL STRUCTURES')
print('if')
a = 33
b = 200
if b > a:
  print("b is greater than a")

print('\nelif')
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print('\nelse')
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print('\nShort Hand If')
a = 200
b = 33
if a > b: print("a is greater than b")

print('\nShort Hand If ... Else')
a = 2
b = 330
print("A") if a > b else print("B")

# Loops
print('\nwhile')
i = 1
while i < 6:
  print(i)
  i += 1

print('\nwhile with break statement')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print('\nwhile with continue statement')
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print('\nwhile with else Statement')
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print('\nfor')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

print('\nfor through a String')

for x in "banana":
  print(x)

print('\nfor with break Statement')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print('\nfor with continue Statement')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

print('\nfor with range() Function')
for x in range(6):
  print(x) 
  
# values from 2 to 6
for x in range(2, 6):
  print(x)

print('\nElse in For Loop')
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Challenge. Print numbers between 10 and 55(included), even and odd but not
# print 16 and multiple of 3.
print('\nchallenge')
for x in range(10, 56):
  if x >= 10 and x % 2 == 0 and x != 16 and not x % 3 == 0 or x == 55: 
    print(x)