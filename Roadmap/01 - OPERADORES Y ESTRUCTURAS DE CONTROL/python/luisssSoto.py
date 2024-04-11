'''aritmetic operators'''
var1 = 10
var2 = 20
print(var1 + var2)
print(var1 - var2)
print(var1 * var2)
print(var1 / var2)
print(var1 // var2) #floor division
print(var1 % var2)
print(var1 ** var2,)
print()

'''relational operators'''
'''1. strict operators'''
print(var1 < var2)
print(var1 > var2)
print()

'''2. no strict operators'''
print(var1 <= var2)
print(var1 >= var2)
print()

'''3. equal operators'''
print(var1 == var2)
print(var1 != var2)
print()

'''bits operators'''
print(var1 | var2)
print(var1 & var2)
print(~var1)
print(var1 ^ var2)
print(var1 << var2)
print(var1 >> var2)
print()

'''logic operators'''
print(var1 and 10 == var2)
print(var1 or var2 > 10)
print(not True)

'''Conditional Selective structures'''
'''1. if'''
if (var1 < var2):
    print(var1, 'is less than', var2)

'''2. if else'''
if (var1 > var2):
    print(var1, 'is greater than', var2)
else:
    print(var1, 'is less than', var2)

'''3. if elif else'''
if (var1 > var2):
    print(var1, 'is greater than', var2)
elif (var1 == var2):
    print(var1, 'is exactly equal to', var2)
else:
    print(var1, 'is less than', var2)

'''Repetitive Structure'''
'''1. for'''
for i in range(10):
    print(i, end=' ')
    if i == 9:
        print()

'''2. while'''
count = 5
while count > 0:
    print(count)
    count -= 1

'''Exceptions'''
try:
    print('try to do this:')
    print(10/0)
except ZeroDivisionError:
    print('Division between 0 is impossible')
print()

'''Last Excercise'''
for number in range(10, 56):
    if number % 2 == 0:
        if number == 16: continue
        elif number % 3 == 0: continue
        else: print(number, end=' ')

