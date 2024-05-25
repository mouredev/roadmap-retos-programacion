#                   Operadores de mi lenguaje:

#   Aritmeticos
a = 28
b = 11
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("Resto:", a % b)
print("Potenciación:", a ** b)
print("División entera:", a // b)

#   Relacional
print(f"{a} es mayor que {b}:", a > b)
print(f"{a} es menor que {b}:", a < b)
print(f"{a} es igual que {b}:", a == b)
print(f"{a} es distinto que {b}:", a != b)
print(f"{a} es mayor o igual que {b}:", a >= b)
print(f"{a} es menor o igual que {b}:", a <= b)

#   Lógicos
a = True
b = False
print("AND lógico:", a and b)  
print("OR lógico:", a or b)  
print("NOT lógico:", not a)
a = 28 # regreso a valor de entero inicial
b = 11 # regreso b valor de entero inicial


#   Bit a Bit
print("AND a nivel de bit:", a & b)
print("OR a nivel de bit:", a | b)
print("XOR a nivel de bit:", a ^ b)
print("NOT a nivel de bit:", ~a)
print("Desplazamiento a la izquierda:", b << 2)
print("Desplazamiento a la derecha:", a >> 2)

#   Asignación
print("Asignación de igualdad: a =", a)
a += 2
print("Asignación de suma:", a)
a -= 2
print("Asignación de resta:", a)
a *= 2
print("Asignación de multiplicación:", a)
a /= 2
print("Asignación de división:", a)
a %= 2
print("Asignación de resto:", a)
a **= 2
print("Asignación de potenciación:", a)
a //= 2
print("Asignación de división entera:", a)
a = 28 #restauro el valor inicial de a
a &= 2 
print("AND bit a bit con asignación:", a)
a |= 2
print("OR bit a bit con asignación:", a)
a^= 2
print("XOR bit a bit con asignación:", a)
a>>= 2
print("Desplazamiento a la derecha con asignación:", a)
a<<= 2
print("Desplazamiento a la izquierda con asignación:", a)

#   Pertenencia
a = [1, 2, 3]
print("¿1 pertenece en a?", 1 in a)
print("¿3 no pertenece en a?", 3 not in a)
texto = "Gracias al curso de Git/Github puedo participar sin saber programar :)"
resultado = "participar" in texto
print(resultado)
resultado_2 = "gracias" in texto
print(resultado_2) # Toma en cuenta mayusculas y minisculas por eso da falso
resultado_3 = "Eres grandioso Moure" not in texto
print(resultado_3)

#   Identidad
a = [1, 2, 3]
b = a
c = 4
print(f"{a} es identico a {b}:", a is b)
print(f"{a} no es identico {c}:", a is not c)


#                   Estructuras de control:

#   Condicionales
a = 11 # me encantan
b = 28 # estos numeros
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual que b")
else:
    print("a es menor que b")
    
#   Bucle for (iterativas)
for i in range(5):
    print("Bucle for, iteración:", i)

#   Bucle while
while a > 0:
    print("Bucle while, valor de a:", a)
    a -= 1
    
#   Excepciones
try:
    resultado = 10 / 0
except:
    print("Error: División por cero!")
finally:
    print("Bloque finally ejecutado")


#   Extra
for nrs in range(10,56,2):
    if nrs != 16 and nrs % 3 != 0:
        print(nrs)


















