# Operadores aritméticos
suma = 24 + 24
resta = 25 - 1
multiplicacion = 4 * 6
division = 48 / 2
potencia = 2 ** 3.585
mod = 48 % 24

# Operadores lógicos
resultado_and = (24 + 6 == 30) and (10 - 6 == 4)
resultado_or = (16 + 4 == 20) or (25 - 5 == 30)
resultado_not = not (24 - 4 == 10)

# Operadores de comparación
igual_a = (24 == 24)
no_igual_a = (24 != 42)
mayor_que = (42 > 24)
menor_que = (24 < 50)
mayor_o_igual_que = (14 >= 14)
menor_o_igual_que = (4 <= 5)

# Operadores de asignación
mi_variable = 5
mi_variable += 2
mi_variable -= 3
mi_variable *= 5
mi_variable /= 2
mi_variable %= 5

# Operadores de identidad
mi_lista1 = [1, 2, 3]
mi_lista2 = [1, 2, 3]
resultado_listas = mi_lista1 is mi_lista2

mi_lista3 = [3, 2, 1]
mi_lista4 = [3, 2, 1]
resultado_listas2 = mi_lista3 is not mi_lista4

# Operadores de pertenencia
mi_lista = [1, 2, 3, 4, 5]
resultado_lista = 3 in mi_lista

mis_lenguajes = ['Python', 'Java', 'C']
resultado_lenguaje = 'Kotlin' not in mis_lenguajes

# Operadores de bits
resultado_and_bits = 5 & 3
resultado_or_bits = 5 | 3
resultado_xor_bits = 5 ^ 3
resultado_shift_left = 5 << 1
resultado_shift_right = 5 >> 1

# Condicionales

numero = 20

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")

# Iterativas

contador = 0

while contador <= 100:
    print(contador)
    contador += 1

for i in range(0, 100, 2):
    print(i)

# Excepciones
try:
    print(10 / 1)
except:
    print("Hay un error")
finally:
    print("Fin del manejo de excepciones")    

#Extra

for i in range(10,56, ):
    if i % 2 == 0 and i != 16 and 1 % 3 != 0:
        print(i)

