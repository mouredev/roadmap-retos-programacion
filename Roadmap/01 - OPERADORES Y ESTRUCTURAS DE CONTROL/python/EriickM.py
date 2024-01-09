#Operadores Aritméticos:
print(f'suma            = {4 + 6}')
print(f'resta           = {8 - 4}')
print(f'multiplicacion  = {12 * 3}')
print(f'division        = {12 / 4}')
print(f'modulo          = {36 % 3}')
print(f'potencia        = {2**4}')
print(f'division_entera = {36//3}')
print(f'\n')

# Operadores de Comparación:
print(f'2 es igual que 2         = {2==2}')
print(f'"A" es distinto que "B"  = {"A"!="B"} ')
print(f'8 es menor que 10        = {8<10}')
print(f'8 es mayor que 10        = {8>10}')
print(f'20 es menor o igual a 20 = {20<=20}')
print(f'20 es mayor o igual a 20 = {12>=20}')
print(f'\n')

# Operadores Lógicos:
print(f'Solo sera True cuando ambas condiciones sean verdad : {2==2 and 3<1}')
print(f'Sera True cuando alguna condicion sean verdad       : {2==2 or 3<1}')
print(f'Negara el cualquier valor boleano                   : {2==2 and not(3<1)}')
print(f'\n')

# Operadores de Pertenencia:
print(f'Sera True cuando "A" PERTENESCA al conjunto de datos [A,B,C,D,E]    : {"A" in ["A","B","C","D"]}')
print(f'Sera True cuando "A" NO PERTENESCA al conjunto de datos [A,B,C,D,E] : {"A" not in ["A","B","C","D"]}')
print(f'\n')

# Operadores de Identidad:
print(f'El valor 3 es 3 :{3 is 3}')
print(f'El valor 3 es 3 :{3 is not [3]}')
print(f'\n')
# Estructuras de Control de Flujo:

# if-elif-else:
a = 20
b = 1
c = 3
d = 0
if b > a:
      print('Si el valor B es mayor que A')
elif a//c == 0:
      print(f'Sino entonce El valor {c}, es un dividendo de {a}')
else:
      print('Entonce ninguna condicion cumplida')
print(f'\n')
# Bucles:

# for: 
for d in range(5):
      if d > c:
            print(f'Se termina en {d}')
            break
      else:
            print(d)
            continue

print(f'\n')
# while
while True:
      try:
            resultado = d / a
            if (resultado == 0.3):
                  break
            print(f'El resultado es {resultado}')
      except:#Se ejecuta en cualquiera de los dos casos 
            print('Division no posible')
      finally: #Se ejecuta en cualquiera de los dos casos 
            d = d + 1
            print('Ya terminanos')
# Expresión Ternaria:
print(f'\n')
print(f'Esta es una operacion ternaria como un if pero con una estructura de una linea {"Si es verdad" if 2 > 5 else "Si es Falso" }')