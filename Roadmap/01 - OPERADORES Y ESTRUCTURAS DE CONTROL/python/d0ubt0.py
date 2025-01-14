#Operadores logicos Python

#Aritmeticos
print(1 + 1)
print(1 - 1 )
print(2 * 2)
print(4 / 2)
print(5 // 2)
print(12 % 3)
print(3 ** 2)

#Comparacion
print((2 == 3))
print((2 != 3))
print((2>3))
print((2<3))
print((2>=3))
print((2<=3))

#Logicos
print(False and True)
print(False or True)
print(not True)

#Identidad
a = 1
b = 1
print((a is b))
print((a is not b))

#Pertenencia
print('Python' in 'Estoy practicando en Python')

def es_multiplo_3(n : int):
    if n % 3 == 0:
        return True
    return False

def es_par(n: int):
    if n % 2 == 0:
        return True
    return False

for i in range(10 ,56):
    if i == 13 or es_multiplo_3(i):
        continue
    if es_par(i):
        print(i)
