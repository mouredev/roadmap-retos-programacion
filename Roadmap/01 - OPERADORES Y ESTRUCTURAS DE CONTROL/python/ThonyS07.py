# aritméticos
suma=10+3
resta=10-3
multiplicacion=10*3
division=10/3
modulo=10%3
exponente=10**3
divisionEntera=10//3
print("Aritmeticos:\nSuma: ", suma,"\nResta: ", resta,"\nMultiplicacion: ", multiplicacion,"\nDivision: ", division,"\nModulo: ", modulo,"\nExponente: ", exponente,"\nDivision entera: ", divisionEntera)


#relacionales
print(f"> True si izquierda es mayor que derecha: 5>3 es {5>3} false en caso contrario: 3>5 es {3>5}")
print(f"< True si izquierda es menor que derecha: 5<8 es {3<5} false en caso contrario: 8<5 es {5<3}")
print(f">= True si izquierda es mayor o igual que derecha: 5>=3 es {5>=3} false en caso contrario: 3>=5 es {3>=5}")
print(f"<= True si izquierda es menor o igual que derecha: 3<=5 es {3<=5} false en caso contrario: 5<=3 es {5<=3}")
print(f"== True si izquierda es igual que derecha: 3==3 es {3==3} false en caso contrario: 3==5 es {3==5}")
print(f"!= True si izquierda NO ES igual que derecha: 3!=5 es {3!=5} false en caso contrario: 3!=3 es {3!=3}")


#lógicos
print(f"and &: True si ambos operandos son true: {5+2==7 & 3-1==2} false si alguno es false {4 + 3 == 13 and 3 - 1 == 2}")
print(f"or |: True si alguno de los operandos es true: {5+3==7 | 3-1==2} false si ninguno es true {4 + 3 == 13 or 2 - 1 == 2}")
print(f"not !: True si alguno de los operandos es false: {not(5==7)} false si ninguno es false {(7!= 7 )}")

#pertenencia
print(f"in: True si el valor especificado se encuentra en la secuencia: 'hon' in 'thony' es { 'hon' in 'thony'} false en caso contrario 1 in [1, 2, 3] es {1 in [1, 2, 3]}")
print(f"not in: True si el valor especificado no se encuentra en la secuencia: 'z' not in 'thony' es { 'z' not in 'thony'} false en caso contrario: 1 not in [1, 2, 3] es {1 not in [1, 2, 3]}")

#asignacion
numero=5 
print(f"asignacion numero = {numero}")
numero+=5
print(f"suma y asignacion += {numero}") 
numero-=5 #resta y asignacion
print(f"resta y asignacion -= {numero}") 
numero*=3 #multiplicacion y asignacion
print(f"multiplicacion y asignacion *= {numero}") 
numero/=3 #división y asignacion
print(f"división y asignacion /= {numero}") 
numero%=3 #módulo y asignacion
print(f"módulo y asignacion %= {numero}") 
numero**=3 #exponente y asignacion
print(f"exponente y asignacion **= {numero}") 
numero//=3 #división entera y asignacion
print(f"división entera y asignacion //= {numero}") 

#identidad
a=3
b=3
c=4
print(f" is es true si los operandos se refieren al mismo objeto identidad a is b es {a is b}")
print(f"is not es true si los operandos no se refieren al mismo objeto identidad a is not b es {a is not b}")
print(f"identidad a is not c es {a is not c}")


# Operadores de bit
a = 2  # 10
b = 3  # 11
print(f"AND: 2 & 3 = {2 & 3}")  # 10
print(f"OR: 2 | 3 = {2 | 3}")  # 11
print(f"XOR: 2 ^ 3 = {2 ^ 3}") #01
print(f"NOT: ~2 = {~2}")#01
print(f"Desplazamiento a la derecha: 2 >> 3 = {2>> 3}")  # 0
print(f"Desplazamiento a la izquierda: 2<< 3 = {2 << 3}")  #10000

# Condicionales

my_variable="It's me"

if type(my_variable) == str:
    print(f"my_variable es {my_variable} una cadena de texto")
elif type(my_variable) == int:
    print(f"my_variable es {my_variable} un entero")
else:
    print("my_variable no es cadena de texto ni entero")

# Iterativas

for i in range(11):
    print(f"imprimiendo cada valor hasta culminar {i}")

i = 0

while i <= 5:
    print(f"imprimiendo cada valor hasta culminar {i}")
    i += 1

# Manejo de excepciones
try:
    print(10 / 2)
    print(10 / 0)
except:
    print("Hubo un error")
finally:
    print("Culminado el manejo de excepciones")


#EXTRA
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

