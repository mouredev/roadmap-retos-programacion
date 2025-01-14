#Operadores Aritmeticos
suma  = 2 + 5
resta = 8 - 2
multiplicacion = 3 * 5
division = 1 / 5
modulo = 6 % 2
potencia = 3 ** 9
division_entero = 18//5
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(potencia)
print(division_entero)

#Operadores Relacionales
mayor_que = 5 > 0
menor_que = 1 < 8
igual_que = 5 == 5
diferente_que = 8 != 4
mayor_o_igual = 5 >= 5 
menor_o_igual = 2 <= 3
print(mayor_que)
print(menor_que)
print(igual_que)
print(diferente_que)
print(mayor_o_igual)
print(menor_o_igual)

#Operadores de Asignacion
mi_numero = 2
mi_numero += 4
mi_numero -= 2
mi_numero *= 2
mi_numero /= 8
mi_numero %= 5
mi_numero **= 6
mi_numero //= 2
print(mi_numero)

#Operadores Logicos
mi_condicion_1 = True
mi_condicion_2 = False
print(mi_condicion_1)
print(mi_condicion_2)

conclusion_1 = mi_condicion_1 and mi_condicion_2
conclusion_2 = mi_condicion_1 or mi_condicion_2
conclusion_3 = not mi_condicion_2
print(conclusion_1)
print(conclusion_2)
print(conclusion_3)

#Operadores de Pertenencia
mi_lista_de_compras = [ 'leche', 'huevos', 'arroz']
condicion_3 = 'leche' in mi_lista_de_compras
condicion_4 = 'soda' not in mi_lista_de_compras
print(condicion_3)
print(condicion_4)

#Operadores de Identidad
a = 1
b = 2
c = a is b
d = b is not a
print(c)
print(d)

#DIFICULTAD EXTRA
for n in range(9,56):
  if n % 2 != 0:
    continue
  if n == 16:
    continue
  if n % 3 != 0:
    continue
  print(n)