"""Los operadores aritmeticos son:
+ - * / % // ** """
#Ejemplos
print(f"20+4= {20+4}")
print(f"20-4= {20-4}")
print(f"20*4= {20*4}")
print(f"20/4= {20/4}")
print(f"20%4= {20%4}")
print(f"20//4= {20//4}")
print(f"20**4= {20**4}")


#Ejemplo operadores relacionamiento
a=5
b=8
print(f"5 es menor que 8= {a<b}")
print(f"5 es mayor que 8= {a>b}")
print(f"5 es igual que 8= {a==b}")
print(f"5 es diferente que 8= {a!=b}")
print(f"5 es menor o igual que 8= {a<=b}")


#Ejemplo operadores lógicos
print(f"4-1 es igual a 2+1 = {4-1==3 and 2+1==3}")
print(f"uno de estos dos números es par: 9 o 4 {9%2==0 or 4%2==0}")
print(f"4+1 no es igual a 4-1= {not 4+1 == 4-1}")


#Ejemplo operadores de asignación
c=8
print(c)
c += 1
print(c)
c -=2
print(c)


#Ejemplo operadores de pertenencia
d= (8,4,3)
print(f"el 8 no esta en d: {8 not in d} ")
print(f"el 9 esta en d: {9 in d} ")


#Ejemplo operadores de identidad
capital= 'Bogota'
print(f"Bogota es una capital: {'Bogota' is capital} ")
print(f"Bogota no es una capital: {'Bogota'is not capital} ")

#Ejercicio extra
for z in range (10,56):
  if z%2 == 0 and z != 16 and z%3 != 0:
    print(z)
