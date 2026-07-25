"""
Operadores

"""

#operadores aritméticos 

print (f"Suma: 10 + 3 = {10 + 3}")  #la "f" sirve para interpolar la suma en la cadena de texto

print (f"Resta: 10 - 3 = {10 - 3}") 

print (f"Multiplicación: 10 * 3 = {10 * 3}")

print (f"División: 10 / 3 = {10 / 3}") 

print (f"Módulo: 10 % 3 = {10 % 3}")   #es el resto de la división, es lo que nos queda despues de dividir

print (f"Exponente: 10 ** 3 = {10 ** 3}") 

print (f"División entera: 10 // 3 = {10 // 3}") # el resultado no tiene que dar un  numero entero a diferencia de la división que da como resultado decimales 3.33



#operadores de comparación: se pueden usar con números y con variables, para comparar numeros y cadenas de texto 

print (f"Igualdad: 10 == 3 {10 == 3}")

print (f"Desigualdad: 10 != 3 {10 != 3}")

print (f"Mayor que: 10 > 3 {10 > 3}")

print (f"Menor que: 10 < 3 {10 < 3}")

print (f"Mayor o igual que: 2 >= 3 {2 >= 3}")

print (f"Menor o igual que: 10 <= 3 {10 <= 3}")



#operadores lógicos 

print (f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es { 10 + 3 == 13 and 5 - 1 == 4}") #intenta que dos condiciones sean iguales

print (f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es { 10 + 3 == 13 or 5 - 1 == 4}")  # el OR pide que sea verdadera al menos una de las condiciones lógicas

print (f"NOT !: not 10 + 3 == 14 {not 10 + 3 == 14}")  #sirve para decir que algo no es, afirma que algo es incorrecto y devuelve  true, por el contrario, si afirmara que algo es incorrecto siendo correcto devolverá como resultado folse



#operadores de asignación: son operadores que actuan en conjunto con el valor de las variables

my_number = 11  #esto es una asignación 
print (my_number) #suma y asignación
my_number += 1  #le suma 1 al 11 que tengo como asignación
print (my_number)
my_number -= 1 #resta y asignación
print (my_number)
my_number *= 2 #multiplicación  y asignación
print (my_number)
my_number /= 2 #división  y asignación
my_number %= 2 #módulo  y asignación
print (my_number)
my_number **= 1 #exponente  y asignación
print (my_number)
my_number //= 1 #división entera  y asignación
print (my_number)


#operadores de identidad: IS sirve para comparar el valor de la pisición de memoria
my_new_number = my_number
print (f"my_number is my_new_number es {my_number is my_new_number}")

#operador de desigualdad: NOT
print (f"my_number is not my_new_number es {my_number is not my_new_number}")



#operadores de pertenencia

print (f"'i' in  'Yani' = {'i' in  'Yani'}")
print (f"'e'  not in 'Yani' = {'e' not in   'Yani'}")



#operadores de bit
a = 10  #1010 - en numeros binarios 0=0, 1=1, 2=10, 3=11, 4=100
b = 3 #0011

print (f"AND: 10 & 3 ={10 & 3 }") # 0010
"""el operador AND compara bit a bit si el numero es 1 devuelve 1 de lo contrario devuelve 0
    en el ejemplo dado: 1=0 resultado 0, 0= 0 resulado 0, 1=1 resultado 1, 
    0=0 resultado 0, en  el ejemplo con AND 0010= 2, se sigue el principio de contar en decimal, 
    pero con la diferencia de que solo se utilizan los dígitos 0 y 1 
"""
print (f"OR: 10 | 3 ={10 | 3 }")  #1011
"""compara bit a bit y si al menos uno de los operadores es 1 el resultado
    será 1   ejemplo 1=0 resultado 1, 0=0 reslutado 0, 1=1 resultado 1, 0=1 resultado 1 total= 1011"""
print (f"XOR: 10 ^ 3 ={10 ^ 3 }") #1001
"""el xor commpara los bit si el resultado es diferente entonces sera 1   en el ejercicio el resulado es 1001 
"""
print (f"NOT: ~10 ={~10}") # invierte el resultado sobre la respresentación 

print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #1010 con el desplazamiento 0010 = 2

print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 1010 con el desplazamiento 101000 = 40


"""
Estructura de control: tipos de estructuras ==>  

"""

# ==> Condicionales 

my_string = "Yani-Git"

if my_string == "Yani-Git.py":
    print ("my_String es 'Yan'")
elif my_string == "Yani":
    print ("my_String es 'Yani'")
else: 
    print ("my_String no es 'Yani-Git' ni 'Yani'")           


#Iterativas

for i in range (11):  # cuando imprime en la pantalla lo hace hasta el 10 no toma en cuenta el 11
     print(i)

i = 0

"""while i <= 10:    #se plantea una condición para que se ejecuta  mientras sea verdadera 
    print (i)     #bucle infinito """


while i <= 10:
    print (i)
    i += 1

# manejo de excepciones 

try:
    print (10 / 0)
except:
    print ("se ha producido un error")
finally:                                       #se va a ejecutar siempre que se maneje el error, se prodzca errer o no se produzca 
    print ("Ha finalizado el manejo de excepciones")
 




# Dificultad extra

for number  in range (10, 56):
    if number % 2 == 0 and number  != 16 and number %3 != 0:
        print (number)



