#Que hacia una caja en el gym? entrenaba para ser caja fuerte :D hahahahahahahahahaha
x =x2 =x3 =x4 =0

#ARITMETICOS ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
print('\naritmeticos: ')
x = 2 + 1
print('x = 1 + 2 =', x)
x = 2 - 1
print('x = 1 - 2 =', x)
x = 2 * 1
print('x = 1 * 2 =', x)
x = 2 / 1
print('x = 1 / 2 =', x)
x = 2 % 1 
print('x = 1 % 2 =', x)


#LOGICOS ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
print('\nLogicos: ')
x  = 0
x3 = 10
while (x != 5 and x3 != 5):
    x  += 1
    x3 -= 1
    print('\nx: ', x)
    print('x3:', x3) 
while x < 10 or x3 < 10:
    x  += 1
    x3 += 1
    print('\nx:', x)
    print('x3', x3)     

verdad = False
if not verdad:
    print('No es verdad, es una mentira! somos todos una ilusion...') 



#COMPARACION y ASIGNACION ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
print('\nComparacion y asignacion: ')

x2 = 10
print('x2 =', x2)
if x + 2 == 2:
    x2 += x
    print('x2 + x =', x2)
elif x - 2 != 2:
    x2 -= x
    print('x2 - x =', x2)
elif x > 2:
    x2 /= x
    print('x2 / x =', x2)
elif x < 2:
    x2 *= x
    print('x2 * x =', x2)    
elif x >= 2:
    x2 %= x
    print('x2','%','x =', x2)
elif x <= 2:
    x2 **= x
    print('x2 ** x =', x2)  
else:
    print('hola mundo!')                  


#IDENTIDAD ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
x = [1,2,3,4,5]
y = x
if x is y:
    print('\nx = ',x)



#PERTENENCIA ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
if 2 in x:
    print('\nx contiene el valor "2" ')
if 0 not in x:
    print('x no contiene el valor "0" ')
        
#BITS ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
a = 5 #101
b = 2 #010    
    #OR
c = a | b 
print('\na | b =', c)
    #AND
c = a & b 
print('a & b =', c)
    #XOR
c = a ^ b 
print('a ^ b =', c)

    #NOT
c = ~c 
print('~c =', c)
    #>>
c = a >> b 
print('a >> b =', c)
    #<<
c = a << b 
print('a << b =', c)


#Dificultad extra ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬

for i in range(10, 56):
    if i % 2 == 0 and i % 3 != 0 and i != 16: 
      print(i) 