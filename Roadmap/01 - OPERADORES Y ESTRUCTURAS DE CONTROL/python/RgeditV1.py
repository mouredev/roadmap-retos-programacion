"""
Todos los operadores
'+' se utiliza para concatenar o sumar variables
'-' Se utuliza para restar valores
'*' Se utiliza para multiplicar valores
'/' Se utiliza para divir valores
'//' se utiliza para devolver divisiones en entero
'**' se utiliza para potenciacion
"""
print("OPERADORES ARITMETICOS")
sumar = 1+1
restar= 2-2
multiplicar = 3*3
dividir = 5/2
potencia = 5**3
divicion_entera = 6//4

print(f" sumar: {sumar}\n restar: {restar}\n multiplicar: {multiplicar}\n dividir: {dividir}\n potencia: {potencia}\n",
      f"division entera: {divicion_entera}")


"""Operadores Logicos

True or False indican si algo es verdadero o falso
el operador 'or' indica que si una de las condiciones es verdadera entonces devuelve True
el operador "and" indica que si todas las condiciones es verdadera entonces devuelve True
el operador "not" indica que si es lo contrario a algo entonces devuelve True o False
"""
print("OPERADORES LOGICOS EJEMPLOS\n")
print(True or False)

print(not False)

print(True and False)

"""Operadores de Comparacion
< indica si algo es menor que entonces es True
> si algo es mayor que entonces devuelve True
<= si algo es menor o igual entonces devuelve True
>= si algo es mayor o igual entonces devuelve True
!= si algo es diferente entonces devuelve True
== si algo es si o si igual entonces devuelve True
"""
print("EJEMPLOS OPERADORES DE COMPARACION")
x,y = 5,10
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x != y)
print(x == y)


#Ciclo For en Python
count = 12
for i in range(1,count+1): #este ciclo hara un conteo hasta el numero en variable count
    print(i)

#bucle While
i = 0
while not i > 10: # mientras no sea mayor seguira el bucle
    print("Mouredev gracias por los ejercicios ;)")
    i+=1 #aqui la var i incrementa en 1 cada vuelta
else:
    print('Vueltas terminadas')

#Condicionales en python
pe = ['robert','mouredev','Dalto','midudev']
dulces = 4

if dulces >= len(pe): #si hay mas o la misma cantidad de dulces que personas
    print('Se han repartido los duces equitativamente')
else: # si no es asi entonces
    print('No quedan tantos dulces, habra que comprar mas')

#Excepciones

while True:
    try: #intenta divir las dos variables
        num1 = int(input("Introduce digito 1: "))
        num2 = int(input("Introduce digito 2: "))
        print(num1/num2)
        break
    except ZeroDivisionError: # si se divide por cero imprime
        print('No se puede dividir por cero\n')
    except ValueError: # si se introduce texto entonces imprime
        print('Solo introduce Digitos\n')


#Dificultad extra completada

for i in range(10,56,2): #del 10 hasta el 56 multiplicando por 2
    if not i == 16 and not i%3 == 0: #si no es igual a 16 i no deja residuo cero al divir entre tres entonces
        print(i)
