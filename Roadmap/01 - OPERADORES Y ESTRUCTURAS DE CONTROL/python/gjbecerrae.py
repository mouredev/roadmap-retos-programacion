a = 3
b = 4
enabler = True
#numero 8 en decimal
bitNumber = '1000'

while True:
    try:
        bitNumber = int(input("ingresa un numero "))
        a = int(input("ingresa un numero a "))
        b = int(input("ingresa un numero b "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

if a > b:
    print('a es mayor que b')
elif a < b:
    print('a es menor que b')
else:
    print('a es igual a b')

for i in range (0,b):
    print(f'Esta es la iteracion {i}')
    print('si multiplicamos por 3 la iteracion tenemos:', 3*i)
print(bitNumber >> 1)

#ntbitNumber >> 1 se desplaza 1 bit a la derecha y se compara con 4. 1000(8)  se convierte en 0100(4)
if bitNumber >> 1 > 4 :
    print ('bitnumber es mayor que 8')
elif bitNumber >> 1 < 4:
    print ('bitnumber era menor a 8')
else:    
    print ('bitnumber era 8 o 9')

print('\n Ejercicio opcional \n')
for i in range (10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print (i)
    elif i == 55:
        print (i)







