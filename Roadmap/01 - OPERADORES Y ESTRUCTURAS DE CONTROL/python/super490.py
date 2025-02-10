# Tipos de operadores

num_1 = 20
num_2 = 15

# Operadores aritméticos

print(num_1 + num_2)  # Suma: 35
print(num_1 - num_2)  # Resta: 5
print(num_1 * num_2)  # Multiplicación: 300
print(num_1 / num_2)  # División: 11.3333333333333333
print(num_1 // num_2)  # División entera: 1
print(num_1 % num_2)  # Módulo: 5
print(num_1 ** num_2)  # Exponenciación: 32768000000000000000

# Operadores de comparación
print(num_1== num_2)  # Igual a: False
print(num_1!= num_2)  # No igual a: True
print(num_1> num_2)  # Mayor que: True
print(num_1< num_2)  # Menor que: False
print(num_1>= num_2)  # Mayor o igual que: True
print(num_1<= num_2)  # Menor o igual que: False

# Operadores lógicos
print(num_1 > 18 and num_2 < 30)  # Verdadero si ambas condiciones son verdaderas: True
print(num_1 > 35 or num_2 > 10)  # Verdadero si al menos una condición es verdadera: True
print(not num_1 > 5)  # Invierte la condición: False

# Operadores de asignación
x = 10

#  Suma y asignación
x += 5  # x ahora es 15
print(x)

# Resta y asignación
x -= 3  # x ahora es 12
print(x)

# Multiplicación y asignación
x *= 2  # x ahora es 24
print(x)

# División y asignación
x /= 4  # x ahora es 6.0
print(x)

# Módulo y asignación
x %= 3  # x ahora es 0.0
print(x)

# Exponenciación y asignación
x **= 2  # x ahora es 0.0
print(x)

# División entera y asignación
x //= 2  # x ahora es 0.0
print(x)

print('///////////////////////////////////////////')

# Operadores de Identidad
x = 10
y = 10

print(x is y)  # True: x e y se refieren al mismo objeto (el entero 10)


a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False: a y b son listas iguales, pero están en diferentes ubicaciones de memoria

c = a  # c ahora se refiere al mismo objeto que a

print(a is c)  # True: a y c se refieren al mismo objeto

a.append(4)  # Modificamos la lista a través de a

print(c)  # c también se ve afectada, ya que se refiere al mismo objeto: [1, 2, 3, 4]


# Operadores de Membresía

frutas = ["manzana", "banana", "naranja"]

print("manzana" in frutas)    # True: "manzana" está en la lista frutas
print("uva" in frutas)        # False: "uva" no está en la lista frutas

print("manzana" not in frutas) # False: "manzana" está en la lista frutas
print("uva" not in frutas)     # True: "uva" no está en la lista frutas

texto = "Hola mundo"

print("mundo" in texto)      # True: "mundo" está en la cadena texto
print("Python" in texto)     # False: "Python" no está en la cadena texto

print("mundo" not in texto)   # False: "mundo" está en la cadena texto
print("Python" not in texto)  # True: "Python" no está en la cadena texto

# Operadores a nivel de bits

a = 5   # 0101 en binario
b = 3   # 0011 en binario

print(a & b)  # 1 (0001): AND bit a bit
print(a | b)  # 7 (0111): OR bit a bit
print(a ^ b)  # 6 (0110): XOR bit a bit

x = 4   # 0100 en binario

print(x << 2)  # 16 (10000): Desplazamiento a la izquierda 2 posiciones
print(x >> 1)  # 2 (0010): Desplazamiento a la derecha 1 posición

y = 2   # 0010 en binario

print(~y)  # -3 (complemento a 2): NOT bit a bit

# Manejos de excepciones
    
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except TypeError:
    print("Los operandos deben ser números.")
    
# DIFICULTAD EXTRA

# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for numero in range(10,58):
    if numero % 2 == 0:
        if numero != 16:
            if numero % 3 != 0:
                print(numero)