# Operadores Aritméticos
print (f"operador de suma 5 + 5 = {5+5}")
print (f"operador de resta 10 - 5 = {10-5}")
print (f"operador de division 5 / 5 = {5/5}")
print (f"operador de multiplicacion 5 * 5 = {5*5}")
print (f"operador de exponente 5 ** 5 = {5**5}")
print (f"operador de modulo 10 % 5 = {13%5}")
print (f"operador de division entera 5 // 5 = {5//5}")

#Operadores logicos
a =  True
b =  False
print (f"a and b = {a and b}") #devuelve true si ambas expresiones son verdaderas
print (f"a or b = {a or b}") # devuelve true al menos una expresion es verdaderas
print (f"a and not b = {a and not b}") # Invierte el valor logico de la expresion a and b es false y not lo vuelve true

#Operadores de comparacion
print (f"operador igualdad: 5 == 10 es: {5==10}")
print (f"operador distincion. 5 != 19 es: {5!=19}")
print (f"operador mayor que. 5 > 10 es: {5>10}")
print (f"operador menor que. 5 < 10 es: {5<10}")
print (f"operador mayor o igual que. 5 >= 5 es: {5>=5}")
print (f"operador menor o igual que. 5 <= 5 = {5<=5}")

#operadores de asignacion
x = 100
x += 10 #Suma y asigna 10 a x
print (f"operador suma y asignacion x += 10 = {x}") #resultado 110
x -= 10 #Suma y resta 10 a x
print (f"operador resta y asignacion x -= 10 = {x}") #resultado 100
x *= 5 #multiplica y asigna 5 a x
print (f"operador multiplicacion y asignacion x *= 5 = {x}") #resultado 500
x **= 2 #eleva x a la potencia de 2. El nuevo valor de x es 500 
print (f"operador exponente y asignacion x **= 2 = {x}") #resultado 250.000
x /= 50 #divide x entre 50. El nuevo valor de x es 50.000
print (f"operador division y asignacion x /= 50 = {x}") #resultado 5000.0
x //= 5 #divisio entera y asignacion.
print (f"operador division entera y asignacion x //= 5 = {x}") #resultado 1000.0
x %= 50 #operador modulo y asignacion.
print (f"operador modulo y asignacion x %= 50 = {x}") #resultado 0.0

#Operadores de identidad
a_1 = [1, 2, 3]
b_1 = a_1
c_1 = [1, 2, 3]

print(a_1 is b_1) #true (b_1 almacena a_1. por lo que son el mismo objeto)
print(a_1 is c_1) #false (c_1 tiene el mismo contenido, pero es un objeto diferente)
print(a_1 is not b_1) #false (b_1 es el mismo objeto que a_1)

#operadores de pertenencia
var = "python"
print("p" in var) #true (la letra p esta en la variable var)
print("z" not in var) #true (la letra z no esta en la variable var)

#operadores de bits
a_2 = 5      # 0b0101
b_2 = 3      # 0b0011
print(a_2 & b_2)   # 1  (0b0001)
print(a_2 | b_2)   # 7  (0b0111)
print(a_2 ^ b_2)   # 6  (0b0110)
print(~a_2)      # -6 (complemento a uno)
print(a_2 << 1)  # 10 (0b1010)
print(a_2 >> 1)  # 2  (0b0010)

#estructuras condicionales
# if, elif, else
x = 10
if x == 5:
    print("x es igual a 5")
elif x < 5:
    print("x es menor que 5")
elif x > 20:
    print("x es mayor que 20")
else:
    print("x no es ni mayor ni menor que 10")

# Estructuras iterativas
for i in range(5):
    print(f"iteracion:{i}")

contador = 10
while contador <15:
    print(f"contador: {contador}")
    contador += 1

# Excepciones
try:
    operacion = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print("Operación realizada con éxito.")
finally:
    print("fin del bloque de excepciones")

#otro metodo manejo de excepciones DIVISION POR DOS NUMEROS
try:
    var_1 = int(input("introduce el DIVIDIENDO: "))
    var_2 = int(input("introduce el DIVISOR: "))
    resultado = var_1 / var_2
except ZeroDivisionError:
    print("No puedes dividir por cero")
except ValueError:
    print("Incorrecto. Debes escribir numeros")
else:
    print(f"el resultado de la division es: {resultado}")
finally:
    print("fin del bloque de excepciones")

# DIFICULTAD EXTRA
for i in range(10 , 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
