# Operadores del lenguaje Python
#-----------------------------------------
''' Aritméticos '''
#-----------------------------------------
# Suma
suma = 4 + 5
# Resta 
resta = 5 - 4 
# Multiplicación 
multiplicación = 4 * 5 
# División 
división = 20 / 4 
# Resto 
resto = 20 % 3 
# División entera (Redondea el resultado al número inmediato inferior)
div_entera = 20 // 3
# Exponenciación 
exponen = 2 ** 3

#-----------------------------------------
''' Comparativos '''
#-----------------------------------------
# El igual a ( == )
igual_a = 4 == 4
# distinto a ( != )
distinto = 5 != 4
# Mayor que ( > )
mayor = 5 > 4
# Menor que ( < )
menor = 4 < 5
# Mayor o igual que ( >= )
mayor_igual = 5 >= 4
# Menor o igual que ( <= )
menor_igual = 4 <= 5

#-----------------------------------------
'''Lógicos'''
#-----------------------------------------
# And (Se cumple cuando ambas condiciones son verdaderas)
and_condition = True and True
# Or (Una de las condiciones es verdadera)
or_condition = False or True
# not (condicion negativa)
not_condition = not False

#-----------------------------------------
'''De asignación'''
#-----------------------------------------
# Asignación simple (=)
variable_simple = 20
# Asignación más adición 
variable_simple += 5 
# Asignación más resta
variable_simple -= 5
# Asignación más multiplicación 
variable_simple *= 5
# Asignación más división 
variable_simple /= 5
# Asignación más resto 
variable_simple %= 5
# Asignación más exponenciación 
variable_simple **= 2 
# Asignación más división entera
variable_simple //= 5

#-----------------------------------------
'''Estructuras de control'''
#-----------------------------------------
'''Condicionales'''
Juan = 16

if Juan >+ 18 and Juan < 60: 
    print("Juan es mayor de edad")
elif Juan < 18 :
    print("Juan es un adolescente")
else:
    print("Juan es un señor mayor")

#-----------------------------------------
'''Iterativas'''

message = "Hello, Python!"
for i in message:
    print(i) 

try:
    10/0
except ZeroDivisionError as e:
    print(f"{e}, is not possible")
else:
    print('Division success')
finally:
    print("Test finished")

#-----------------------------------------
'''Dificultad Extra'''
#-----------------------------------------
for i in range(10,56):
    if i % 2 == 0 and i != 16 and not i % 3 == 0:
        print(i)