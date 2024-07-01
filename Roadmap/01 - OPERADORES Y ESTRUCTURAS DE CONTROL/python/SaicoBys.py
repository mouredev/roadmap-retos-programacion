# Operadores aritméticos
x = 10
y = 3
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
division_entera = x // y
modulo = x % y
potencia = x ** y

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("division entera:", division_entera)
print("Modulo:", modulo)
print("Potencia:", potencia)

# Operadores de comparacion
a = 5 
b = 8
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Operadores lógicos
c = True
d = False
print("c and d:", c and d)
print("c or d:", c or d)
print("not c:", not c)

# Operadores de asignación
e = 15
e += 5  # e = e + 5
print("e += 5:", e)
e -= 3  # e = e - 3
print("e -= 3:", e)

# Operadores de identidad
f = [1, 2, 3]
g = [1, 2, 3]
h = f
print("f is g:", f is g)  # False (objetos diferentes)
print("f is h:", f is h)  # True (misma referencia)
print("f == g:", f == g)  # True (mismo contenido)

# Operadores de pertenencia
lista = [1, 2, 3, 4]
print("1 in lista:", 1 in lista)
print("5 in lista:", 5 in lista)

# Condicionales
edad = 25

if edad < 18:
  print("Eres menor de edad")
elif edad >= 18 and edad < 65:
  print("Eres adulto")
else:
  print("Eres jubilado")

# Iterativas (bucles)
for i in range(1, 6):  # Imprime números del 1 al 5
  print(i)

numero = 1
while numero <= 5:  # Imprime números del 1 al 5
  print(numero)
  numero += 1

# Excepciones
try:
  resultado = 10 / 0  # División por cero (error)
except ZeroDivisionError as e:
  print("Error:", e)
finally:
  print("Fin del programa")
