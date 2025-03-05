#operadores aritmeticos
print(f""" 
Nombre          | Representacion  |  Ejemplo
Suma            +                    1 + 2
Resta           -                    10 - 2
Multiplicacion  *                    1 * 2
Division        /                    10 / 5
Division entera //                   10.5 // 4
Modulo          %                    10 % 3
Exponente       **                   10 ** 2
""")

#Operadores de comparacion
print(f""" 
Nombre          | Representacion  |  Ejemplo
Igual a           ==                    2 == 2
Distinto de       !=                   10 != 2
menor que         <                    1 < 2
Mayor que         >                    10 > 5
Menor o igual que <=                   10.5 <= 
Mayor o igual que >=                   10 >= 3
""")

#Operadores logicos
print(f""" 
Nombre          | Representacion  |  Ejemplo
AND               and             True and True        
OR                or             True or False   
NOT               not            not True
""")

#Operadores de asignacion
print(f""" 
Nombre          | Representacion  |  Ejemplo
A.Suma            +=                    1 + 2
A.Resta           -=                    10 - 2
A.Multiplicacion  *=                    1 * 2
A.Division        /=                    10 / 5
A.Division entera //=                   10.5 // 4
A.Modulo          %=                    10 % 3
A.Exponente       **=                   10 ** 2
A.bitwise AND     &=                   h &= 3
A.bitwise OR      |=                   h |= 5
A.bitwise XOR     ^=                   h ^= 5 
""")

#Operadores de identidad(compara posicion en memoria)
print(f""" 
Nombre          | Representacion  |  Ejemplo
Es               is                  a is b
No es           not is               a is not b
""")

#Operadores de pertenencia
print(f""" 
Nombre          | Representacion  |  Ejemplo
Esta              in                  2 in [1,2,3,4,5]
no esta           not in              2 is not [1,2,3,4,5]
""")

#Operadores de bitwise
print(f""" 
Nombre          | Representacion  |  Ejemplo
AND bit a bit     &                  a & b
OR bit a bit      |                  a | b
XOR bit a bit     ^                  a ^ b
Desplazamiento a la izq. <<          a<< b
Desplazamiento a la der. >>          a >> b
""")

#Operadores de ternario
print(f""" 
Nombre          | Representacion  |  Ejemplo
ternario         is-else            a if x == b else b
""")

#Operadores de walrus
print(f""" 
Nombre          | Representacion  |  Ejemplo
walrus           :=                (x := valor)
""")





#control de flujo iterativo

#for con funcion range
for i in range(10):
    print(i)

#While
number = 0
while(number < 10):
    print(number)
    number += 1
    
#Control de flujos condicionales

if 10 < 15:
    print("10 es menor que 15")
elif 10 < 20:
    print("10 es menor que 20")
else:
    print("Esto es un else, se entra cuando las condiciones anteriores no se completaron")
    
    
print("Ejercicio extra")

my_list = [item for item in range(10, 56)if item != 16 and item % 2 == 0 and item % 3 != 0]
print(my_list)




