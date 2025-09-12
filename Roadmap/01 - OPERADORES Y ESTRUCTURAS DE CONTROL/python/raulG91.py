
#Arithmetic operations
sum = 2+3
print("Sum: ", sum)
diff =  5-1
print("Diff: ", diff)
multiply = 6*8
print("multiply: ", multiply)
division =  40 / 5
print("Division", division)
int_division = 3//2
print("Int division", int_division)
module = 30 % 2
print("Module", module)
power = 2**2
print("Power: ",str(power))

#Logical 
v_and = True and False
print("And: ",v_and)
v_or = True or False
print("Or : ", v_or)
v_not = not(True)
print("Not: ", v_not)

#Comparation
equal = True == True
print("Equal : ", equal)
not_equal = False != True
print("Not equal: ", not_equal)
greater = 3 > 2
print("> : ", greater)
greater_equal = 3>=3
print(">= :", greater_equal)
less = 5 < 10 
print("<: ", less)
less_equal = 5<= 2
print("<= : ",less_equal)

#Identity
identity = 1 is -1
print("is : ", identity)

#Belonging
beloning = 1 in [3,4,5,1]
print("in: ",beloning)

#Bits
bits_and = 1 & 1
print("& : ", bits_and)
bits_or = 1 | 1
print("| : ", bits_or)
bits_xor = 1 ^ 1
print("^ : ", bits_xor)
bits_not = ~ 1
print("~ : ",bits_not)

a = 5

#if - elif - else
if a < 3:
    print("Number less than 3")
elif a>=3 and a <10:
    print("Number between 3 and 9")
else:
    print("Number bigger than 10")  
    
#Loops    
for number in range(0,5):
    print(number)          

while (True):
    print("While loop")
    break    

try:
    n = float(input("Enter a number: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("Number entered is not correct")
else:
    print("Everything is ok")
       
'''
Extra Exercise: 
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''        

for num in range(10,56):
    if (num % 2 == 0) and (num !=16)  and (num % 3 != 0):
        print(num)
    