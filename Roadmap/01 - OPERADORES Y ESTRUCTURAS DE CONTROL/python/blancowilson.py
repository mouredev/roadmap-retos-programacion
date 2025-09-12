a:int = 13
b:int = 5

addition = a + b
print(addition)
substract = a - b
print(substract)
multiply = a * b
print(multiply)
division = a/b
print(division)
integer_division = a//b
print(integer_division)
power = a**b
print(power)
remainder = a%b
print(remainder)

print ("comparation operatos == != > <")
compare = a == b
print(compare)
compare = a != b
print(compare)
compare = a > b
print(compare)
compare = a < b
print(compare)
compare = a >= b
print(compare)

print ("logical operators")
# Logical NOT with ~
print((~(2 == 2)))
# Logical AND with &
print((1!=1) & (1<1))
# Logical OR with |
print(( 1>=1 ) | (1 <1))
# Logical XOR with 
print((1 != 1) ^ ( 1< 1))

i=0

while i < 10:
    print(i,end=' ')
    i +=1



# Resolucion dificultad extra opcional
for i in range(10,56):
    odd = False
    odd= ((i % 2) == 0)
    multiply_of_three = not((i % 3) == 0)
    #print (f"{i} es multiplo de 3 {((i % 3) == 0)}")
    if odd and multiply_of_three and i !=16: print(i)