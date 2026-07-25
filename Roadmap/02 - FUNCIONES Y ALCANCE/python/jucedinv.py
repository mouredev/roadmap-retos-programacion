#02 - FUNCIONES Y ALCANCE
print('#02 - FUNCIONES Y ALCANCE')

#FUNCTION without parameters
def greeting():
    print('Welcome')
print('FUNCTION without parameters: greeting() --> Print text on console.')
greeting()

#FUNCTION with parameter
def isprime(number):
    sqrtn = int(number ** 0.5)
    for i in range(2,sqrtn + 1):
        if number % i == 0:
            print('The number not is prime.')
            break
    else:
        print('The nuber is prime.')
print('FUNCTION with parameter: isprime(21) --> Print if number 21 is prime or not.')
isprime(21)

#FUNCTION with output
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print('FUNCTION with output: factorial(5) --> Return the factorial of 5.')
print('factorial(5) = ', factorial(5))

#FUNCTION with parameters
def combinationf(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))
print('FUNCTION with parameters: combinationf(4,2) --> Return the 4 combination 2.')
print('combinationf(4,2) = ', combinationf(4,2))

#FUNCTION inside other function
def combinationfb(n, r):
    def factorialb(n):
        if n == 0:
            return 1
        else:
            return n * factorialb(n-1)
    return factorialb(n) / (factorialb(r) * factorialb(n-r))
print('FUNCTION inside other function: combinationfb(5,2) --> Return the 5 combination 2.')
print('Implements function factorialb(n) inside the combinationfb function.')
print('combinationfb(5,2) = ', combinationfb(5,2))

#FUNCTIONS Built-in
print('FUNCTIONS Built-in')
print('Function divmod() --> Return a tuple containing two values, the quotient and remainder of the division.')
print('divmod(11,2) = ', divmod(11,2))
print('Function enumerate() --> Returns an enumerate object, this is an iterator that yelds pairs of (index,value).')
print('enumerate ([\'apple\', \'orange\', \'banana\']) = ', list(enumerate (['apple', 'orange', 'banana'])))

#Use Variable Local and Global
global_variable = 0
def iteration1():
    for local_variable1 in range(1,11):
        global global_variable
        global_variable = global_variable + 1
    print('local_variable1 = ', local_variable1)
def iteration2():
    for local_variable2 in range(1,21):
        global global_variable
        global_variable = global_variable + 1
    print('local_variable2 = ', local_variable2)
print('Use Variable Local and Global in two iterations and count individuals and total iterations.')
iteration1()
iteration2()
print('global_variable = ', global_variable)

#DIFICULTAD EXTRA
def print100conditional(text1, text2):
    count = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            count += 1
    return count
print('DIFICULTAD EXTRA')
print(print100conditional('texta', 'textb'))