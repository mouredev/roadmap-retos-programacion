""" 
OPERADORES
"""
# Arimeticos
print(10 + 5) #suma
print(10 - 5) #resta
print(10 * 5) #multiplicacion
print(10 / 5) #division
print(10 // 4)#division entera
print(10 % 5) # modulo o rseto de la division
print(10 ** 5) #potenciacion
print(10 **(1/2)) # radicacion (a nivel practico)

# Comparacion
print(10 > 5) #mayor que
print(4  < 5) #menor que
print(10 == 10) #igual que
print(10 != 5) #difernte que
print(10 >= 5) #mayor o igual que
print(5 <= 5) # menor o igual que

#lLogicos
print(10 + 5 == 5 and 10 - 5 == 5)# AND
print(10 + 5 == 5 or 10 - 5 == 5)#OR
print(not 10 - 5 == 5) # NOT

#Asignacion
numero = 10   # asignacion
print(numero)  
numero += 1   # suma y asignacion
print(numero)
numero -= 1   # resta y asignacion
print(numero)
numero *= 2   # multiplicacion y asignacion
print(numero)
numero /= 2   # division y asignacion
print(numero)
numero //= 3  # division entera y asignacion
print(numero)
numero %= 3   # modulo y asignacion
print(numero)
numero **= 2  # potenciacion y asignacion
print(numero)
numero **= (1/2) # radicacion y asignacion
print(numero)
#Identidad
numero_nuevo = 10
print(numero_nuevo is numero)     # IS
print(numero_nuevo is not numero) # IS NOT

#Pertenecia
print('j' in 'johan')     # IN
print('k' not in 'johan') # NOT IN

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(10 & 3)  # comparacion bit a bit ANDA
print(10 | 3)  # 1011   comparacion bit a bit OR
print(10 ^ 3)  # 1001 comparacion bit a bit XOR
print(~10)  # NOT
print(10 >> 2)  # 0010 Desplazamiento a la derecha
print(10 << 2)  # 101000 Desplazamiento a la izquierda

"""
Estructuras de control
"""

# Condicionales

palabra = "johans"

if palabra == "enrique":
    print("mi palabra es 'enrique'")
elif palabrag == "johans":
    print("mi palabra es 'johans'")
else:
    print("mi palabra no es 'enrique' ni 'johans'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)



