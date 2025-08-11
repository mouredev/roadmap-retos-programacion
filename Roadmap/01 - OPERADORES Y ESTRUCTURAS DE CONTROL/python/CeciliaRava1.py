numberOne = 1
numberTwo = 2

sum = numberOne + numberTwo
sub = numberOne - numberTwo
multiplication = numberOne * numberTwo
division = numberOne / numberTwo
module = numberOne % numberTwo


if numberTwo > numberOne:
    print(f'{numberTwo} is higher than {numberOne}')
elif numberTwo != numberOne:
    print(f'{numberOne} and {numberTwo} are differents')
else:
    print(f'{numberOne} is higher than {numberTwo}')

while numberOne != numberTwo:
    numberOne += 1

'''
Create a program that prints to the console all numbers between 10 and 55 (inclusive), that are even, and are neither 16 
nor multiples of 3.
'''

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)