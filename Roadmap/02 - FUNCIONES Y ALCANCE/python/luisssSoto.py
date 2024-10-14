"""Functions"""

'''1. Common Functions'''
'''with parameters and return'''
def simplestFunction():
    print('Show something on the screen')

'''with parameters but without return'''
def simpleFunction(parameter1):
    print(parameter1)

'''with parameters and return'''
def commonFunction(parameter1, parameter2):
    return parameter1, parameter2

# Note: one thing is create a function and another is call the function, take a look at the next:

'''with parameters and return and variable inside it'''
def additionFunction(value1, value2):
    resultOfAddition = value1 + value2
    return resultOfAddition

result = additionFunction(10,5)
print(result)


'''2. Recursive Functions'''

def addition(number):
    if number <= 2:
        return 4
    else:
        return number + addition(number-2)
print(addition(10))

# Note: be carefull with the operations that are not commutatives:    
def substraction(number):
    if number <= 0:
        return 4
    else:
        return number - substraction(number-1)

print(substraction(5)) # 5-4, 4-3, 3-2, 2-1, 1-0 ---> return 4 ---> 1-4=-3, 2--3=5, 3-5=-2, 4--2=6, 5-6=-1

'''3. Python's functions'''
'''print() is an example of Integrated functions of Python'''
print('any', 'thing', sep="*", end="\n")

'''4. local and global variables'''
'''locals'''
# Note: all the variables are locals unless you add the "global" keyword before the variable
isLocal = True
def anyFunction():
    print('all the local variables are visible from anywhere', isLocal, 
          '''unless the variable is created in a delimited space''')
    fromFunction = "I'm hidden"

anyFunction()
try:
    print(fromFunction)
except NameError:
    print("it won't work")
    

'''globals'''
def anotherFunction():
    global isGlobal
    isGlobal = True
    print(isGlobal)

anotherFunction() # It's important first call the function otherwise the line of code below, is going to do an error "NameError"
print(isGlobal)

'''There is a concept calls scope to defines the scope's variable'''
var1 = 1
def localScope():
    var1 = 'one'
    return var1
print(var1)
print(localScope())
print(var1)

var2 = 2
def globalScope():
    global var2
    var2 = 'two'
    return var2
print(var2)
print(globalScope())
print(var2)

'''5. Extra difficult'''
def extraFunction(stringA, stringB):
    count = 0
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(stringA, stringB)
        elif i % 3 == 0:
            print(stringA)
        elif i % 5 == 0:
            print(stringB)
        else:
            print(i)
            count+=1
    return count

print(extraFunction('divisor by 3', 'divisor by 5'))



