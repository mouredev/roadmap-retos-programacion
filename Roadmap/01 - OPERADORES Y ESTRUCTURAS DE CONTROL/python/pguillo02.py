#En python existen las principales aritmético-lógicas propias de la computación

#Suma, resta, multiplicación y división
print(2-1)

print(2*2)

print(4/2)

print(1+1)

#Aglutinadores

2==0 and 1==1

3==3 or 2==4

#También encontramos comparaciones lógicas

print(1==1)

print(1<0)

print(2>1)

print(1<=0)

print(2>=1)

print(1!=0)

#También tenemos operaciones especiales como los módulos o la divisón entera

print(1%1)

print(1//1)

#En lo que a listas se refiere contamos con sentencias de permanencia y existencia

1 in [1,2,3] 

1 is int

#En lo que a estructuras de control contamos con la típica clausa if que se emplea para manejara flujos de control

if 1==1:
    print("Caso afirmativo")
elif 1 == 0:
    print("Caso secundario")
else:
    print("caso negativo")


#Además, contamos con los típicos bucles iterativos for y while

for item in range(10):
    print(item)

i=0

while i<10:
    print(i)
    i+=1

#Optativo

for item in range(10, 56):
    if item != 16 and item % 3 != 0 and item % 2 == 0:
        print(item)
        


