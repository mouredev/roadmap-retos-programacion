
### Operators ###

# Arithmetic Operators #
print ("Arithmetic Operators")
print (5+5) # sum 
print (5-5) # substraction 
print (5*5) # multiplication 
print (5**5) # power 
print (5/5) # division 
print (10//5) # floor 
print (12%5) # mod 
print ("\n")

# Assignment Operators #
x=5 # x = 5
print ("Assignment Operators")
print (x)
x=+5 # x = x+5
print (x)
x=-5 # x = x-5
print (x)
x*=5 # x = x*5
print (x)
x/=5 # x = x/5
print (x)
x%=5 # x = x%5
print (x)
x//=5 # x = x//5
print (x)
x**5 # x= x**5
print (x)
print ("\n")

# Comparison Operatos #
x= 10
y= 20
print ("Comparison Operatos")
print (x==y) # Equal 
print (x!=y) # Not Equal 
print (x<y) # Less Than
print (x>y) # Greater Than
print (x<=y) # Less or Equal 
print (x>=y) # Greater or Equal 
print ("\n")

# Logical Operatos #
x=1
y=2
print ("Logical Operators")
print (x==y and x<=y) # Both conditions must be true, otherwise is False
print (x==y or x<=y) # Juts one condition must be true
print (not(x==y and x<=y)) # It changes the result, if is True changes to False, and vice-versa
print ("\n")

#  Identity Operators #
x=2
y=1
print ("Identity Operators")
print (x is y) # It returns true if both are the same, otherwise is false
print (x is not y) # It returns true if both are not the same 
print ("\n")

# Member Operators #
var1= "Python"
var2= "Hello"

print ("Member Operators")
print ("o" in var1) # It returns true if the value is presented, otherwise is false
print ("a" not in var2) # It returns true if the value is not presented, otherwise is ture
print ("\n")


# Challenge #
"""
Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
"""

print ("CHallenge")
for x in range(10, 56):
    if x%2==0 and x != 16 and x % 3 != 0:
        print (x, end=' ')
