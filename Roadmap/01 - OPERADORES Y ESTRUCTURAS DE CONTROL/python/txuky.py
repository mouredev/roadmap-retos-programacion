### Ejemploi de operadores  ###

'''
Aritmeticos
+ - * / % // ** 
'''

print(4 + 5)
print(7 - 2)
print(12 / 3)
print(11 % 3)
print(10 // 3)
print(2 ** 3)

'''
de Comparacion
== != > < >= <=
'''
print(5 == 5)
print(5 != 3)
print(5 > 1)
print(2 < 5)
print(1 >= 1)
print(2 <= 5)

'''
logicos
and or not
'''
print(5 < 8 and 7 > 4)
print((6 + 5)==8 or (2 * 14) > 4)
print(not True)


my_number = 1

while my_number != 12 and my_number < 13:
    if my_number <= 6:
        print('Number es menor o igual que 6 es:', my_number )
    else:
        print('Number es mayor 6 es', my_number)
    my_number = my_number * 2
print('Number es mayor o igual a 12', my_number)    


my_other_number = 10

while my_other_number <= 55:
    if my_other_number !=16 and my_other_number % 3 != 0:
        print(my_other_number) 
    my_other_number += 2
    