#Arimetics Operators
print( "~~Arimetics Operators~~")
print(f"10 + 10 equal to  {10+10}") # Addition
print(f"10 - 5 equal to {10-5}") #Subtraction 
print(f"10 * 10 equal to {10*10}" )  #Multiplication
print(f"10 / 5 equal to {10/5}")# Division sometime return a float number or a integer number 
print(f"10 % 2 equal to {10%2}") # Modulo  
print(f"10 ** 2 equal to {10**2}") # Exponentiation
print(f"10 // 3 equal  {10 //3}") # Floor Division  Always return  a integer number

# Assigement Operators
my_number = 11  # assigment
print(my_number)
my_number += 1  # adittion and assigment
print(my_number)
my_number -= 1  # substraction and assigment
print(my_number)
my_number *= 2  # multiplication and assigment
print(my_number)
my_number /= 2  # division and assigment
print(my_number)
my_number %= 2  # modulo and assigment
print(my_number)
my_number **= 1  # exponitation and assignament
print(my_number)

#Comparation Operators
print("~~Comparation Operators~~")
print(f"10 == 10 is {10==10}") #Equal
print(f"10 !=  5 is {10!=5}") #Not Equal
print(f"50 < 100 is {50<100}") #Less than
print(f"100 > 50 is {100>50}") #Greater than
print(f"15 <= 20 is {20<=15}") #Less than or equal to    
print(f" 20 >= 15 is {20<=15}") #Greater than or equal to

#Logical Operators
n = 10
print ('~~Logical Operators~~')
print (n <= 10 and n >= 0) # Returns True if both statements are true
print (n == 10 or n > 5 )  #Returns True if one of the statements is true
print (not( n < 15 and n > 8 )) #Reverse the result, returns False if the result is true

#Idebtity Operators
a = ["apple", "banana"]
b = ["apple", "banana"]
c = a

print("~~Identity Operators~~")
print(f"a and b are the same object? {a is b}") #	Returns True if both variables are the same object
print( f"a and c are the same object? {a is c}")
print( f"a and c are the same object? {a == c}")
print(f"a and b are not the same object? {a is not b}") #Returns True if both variables are not the same object

#Membership Operators
fruits = ["banana", "apple", "orange"]
print ("~~Membership Operators~~")
print (f"banana is in fruits {"banana"in fruits}") #Returns True if a sequence with the specified value is present in the object
print (f"cherry is not in fruits {"cherry" not in fruits}") #Returns True if a sequence with the specified value is not present in the object

#Bitwise Operators
print ("~~Bitwise Operators~~")
# 15 = 1111
# 4 = 0100
print (f"AND: 15 & 4 ={15 & 4} ") #The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print (f"OR: 15 | 4 = {15 | 4}") # Sets each bit to 1 if one of two bits is 1

print (f"XOR: 15 ^ 4 = {15  ^4}") #Sets each bit to 1 if only one of two bits is 1

print (f"NOT: ~15 = {~15}" ) #	Inverts all the bits

print (f"Shift Left: 15 << 2 = {15<<2}") #Shift left by pushing zeros in from the right and let the leftmost bits fall off

print (f"Shift right: 15 >> 2 = {15 >> 2}") #Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

print ("~~~~Control Structutre ~~~~")
#Conditionals
print ("IF and ELSE")
age = 20
if age >= 18:
    print ("you are adult")
else :
    print ("you are children")
print( "IF, ELSE, ELIF")
score = 10
if score == 10:
    print ("you are the best")
elif score == 8:
    print ("you are regular")
else :
    print ("you are bad")

print ("WHILE")
time = 0
while time <= 12:
    print (time)
    time = time +1
print("it's time to devlope")
    
print("FOR")
for number in range(1, 6):
    print(number)

print("FOR USED LISTS")
fruts = ["apple", "orange", "cherry"]
for frut in fruts:
    print(frut)

print("BREAK")
for x in range(1, 10):
    if x == 5:
        break
    print(x)

print("CONTINUE")
for Y in range(1, 6):
    if Y == 3:
        continue
    print(Y)

print("TRY / CATCH")
try:
    num = int(input("get into a number: "))
    print(num)
except:
    print("it's not a number")
#EXTRA
for number in range(10,56):
    is_pair = number % 2
    is_notmult = number % 3
    if is_pair == 0 and number != 16 and is_notmult != 0:
        print(number)  

print ("otra forma")
for numberx in range (10,56):
    if numberx % 2 == 0 and numberx != 16 and numberx % 3 != 0:
        print (numberx)


