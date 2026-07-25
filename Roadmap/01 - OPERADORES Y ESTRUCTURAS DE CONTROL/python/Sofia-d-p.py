#Operadores aritméticos
print("Operadores aritméticos")
print(f"sumar 10+3 = {10+3}")
print(f"restar 78-43 {78-43 }")
print(f"multiplicar 63*3 = {63*3}")
print (f"dividir 125/5 = {125/5}")
print(f"esto es elevar a una potencia 5**5= {5**5}")
print(f"es es una división entera 10 //3 {10//3}")
print(f"esto es el módulo de una división 10%3 = {10%3}")

#Operadores de comparación
print("Operadores de comparación")
print(f"este es el operador de igualdad 10 == 10 y es {10 == 10}")
print(f"este operador es desigual != {10!=3}")
print(f"este operador es mayor > {10>3}")
print(f"este operador es menor < {10<3}")
print(f"este operador es mayor o igual >= {10>=3}")
print(f"este operador es menor o igual <= {10<=3}")

#Operadores lógicos
print("Operadores lógicos")
print(f"Operador AND 25 + 10 = 35 and 25<50 {25 + 10 == 35 and 25<50}") #Se cumplen las 2 condiciones
print(f"Operador OR  25 + 10 = 45 OR 25<50 {25 + 10 == 45 or 25<50}") #Se cumple 1 sola condición
print(f"Operador NOT 25 > 50 {not 25>50}") #Niega condición 

#Operadores de pertenencia
print("Operadores de pertenencia")
print(f"F en Sofia = {'f' in 'sofia'}")

#Operadores de asignación
a=7; b=2
print("Operadores de asignación")
x=a; x+=b;  print("x+=", x)  # 9
x=a; x-=b;  print("x-=", x)  # 5
x=a; x*=b;  print("x*=", x)  # 14
x=a; x/=b;  print("x/=", x)  # 3.5
x=a; x%=b;  print("x%=", x)  # 1
x=a; x//=b; print("x//=", x) # 3
x=a; x**=b; print("x**=", x) # 49



"""
Estructuras de control
"""

#Condicionales 
print("Condicionales")

my_string = "Sofita aprende Python"

if my_string == "Sofita aprende Python":
    print("'my_string' es 'Sofita aprende Python'")
elif my_string == "Sofita":
    print("'my_string' es 'Sofita'")
else:
    print("'my_string' es otra")
    
#Iterativas
print("Iterativas")

for i in range(0, 5):
    print(i)
        
#Iterativa con while
x = 5
while x > 0:
    x -=1
    print(x)

#Manejo de excepciones
print("Excepciones")
try:
    print(10/0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Este bloque siempre se ejecuta")
    
"""
Dificultad extra
"""
#Todos los numeros todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3   
print("Dificultad extra")    
for i in range (10,56):
    if i % 2 ==0 and i != 16 and i % 3 != 0:
        print (i)

