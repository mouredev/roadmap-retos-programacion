'''
Uso la librería colorama para añadir color a algunas partes del código, como a los resultados.
Esta librería hay que instalarla, no viene incluída
'''

import colorama

color_green = colorama.Fore.GREEN
color_blue = colorama.Fore.BLUE
color_grey = colorama.Fore.BLACK
color_red = colorama.Fore.RED
end_color = colorama.Fore.RESET

import random

print('-'*10, "OPERADORES ARITMÉTICOS", '-'*10)

print("\tOperador '+':", color_green, "3+6 = ", 3+6, end_color)
print("\tOperador '-':", color_green, "6-3 = ", 6-3, end_color)
print("\tOperador '*':", color_green, "3*6 = ", 3*6, end_color)
print("\tOperador '/':", color_green, "6/3 = ", 6/3, end_color) 
#por defecto saca un float. Para que sea un int usamos '//' o especificamos que sea un int(n1/n2)
print("\tOperador '//':", color_green, "6//3 = ", 6//3, end_color)
print("\tOperador '**':", color_green, "6/3 = ", 6**3, end_color, "\n")


print('-'*10, "OPERADORES LÓGICOS", '-'*10)

print("\tOperador 'or':", color_grey, "True or False = ", True or False, end_color)
print("\tOperador 'and':", color_grey, "True and False = ", True and False, end_color)
print("\tOperador 'not':", color_grey, "not False = ", not False, end_color, "\n")


print('-'*10, "OPERADORES DE COMPARACIÓN", '-'*10)

print("\tOperador '<':", color_blue, "3 < 6 = ", 3<6, end_color)
print("\tOperador '>':", color_blue, "3 > 6 = ", 3>6, end_color)
print("\tOperador '==':", color_blue, "3 == 6 = ", 3==6, end_color)
print("\tOperador '!=':", color_blue, "3 != 6 = ", 3!=6, end_color)
print("\tOperador '<=':", color_blue, "3 <= 6 = ", 3<=6, end_color)
print("\tOperador '>=':", color_blue, "3 >= 6 = ", 3>=6, end_color)


print('-'*10, "OPERADORES DE ASIGNACIÓN", '-'*10)

print("\tOperador '=':", color_red, "x = 10 ", end_color)
x = 10
x+=2
print("\tOperador '+=':", color_red, "x += 2 ->", x, end_color)
x-=2
print("\tOperador '-=':", color_red, "x -= 2 ->", x, end_color)
x*=2
print("\tOperador '*=':", color_red, "x *= 2 ->", x, end_color)
x/=2
print("\tOperador '/=':", color_red, "x /= 2 ->", x, end_color)
x%=6
print("\tOperador '%=':", color_red, "x %= 6 ->", x, end_color)


print('-'*10, "OPERADORES DE IDENTIDAD", '-'*10)

print("\tOperador 'is':", color_green, "3 is 6 = ", 3 is 6, end_color)
print("\tOperador 'is not ':", color_green, "3 is not 6 = ", 3 is not 6, end_color)


print('-'*10, "OPERADORES DE PERTENENCIA", '-'*10)

print('proof_list = ["Python", "Kotlin", "Swift", "Go", "JavaScript", "COBOL"]')
proof_list = ["Python", "Kotlin", "Swift", "Go", "JavaScript", "COBOL"]

print("\tOperador 'in':", color_grey, "'Python' in proof_list ->", "Python" in proof_list, end_color)
print("\tOperador 'not in':", color_grey, "'Python' not in proof_list ->", "Python" not in proof_list, end_color)


print('-'*10, "OPERADORES DE BITS", '-'*10)
print("\tOperador '&':", color_blue, "3 & 6 = ", 3 & 6, end_color)
print("\tOperador '|':", color_blue, "3 | 6 = ", 3 | 6, end_color)
print("\tOperador '^':", color_blue, "3 ^ 6 = ", 3 ^ 6, end_color)
print("\tOperador '~':", color_blue, "~ 6 = ", ~ 6, end_color)
print("\tOperador '<<':", color_blue, "3 << 2 = ", 3 << 2, end_color)
print("\tOperador '>>':", color_blue, "3 >> 2 = ", 3 >> 2, end_color)


print('\n','-'*10, "EJEMPLOS CON ESTRUCTURAS DE CONTROL", '-'*10)

print('*'*3, "EJERCICIO 1", '*'*3)
while True:
    try:
        num = int(input("Pon un número:"))
        if num%2 == 0:
            print(color_green, "Es un número par", end_color)
        else:
            print(color_green, "Es un número impar", end_color)
        break
    except:
        print(color_red,"Que sea un número", end_color)

print('*'*3, "EJERCICIO 2", '*'*3)
word = input("Vamos a contar las vocales. Pon una palabra: ")
vocals = "aeiou"
count = []
for letra in word:
    if letra in vocals:
        count.append(letra)
    else:
        pass
print(len(count))

print('*'*3, "EJERCICIO 3", '*'*3)
chosen_number = random.randint(1, 30)
vidas = 5

choose = None

while chosen_number != choose:
    choose = int(input("Elige un número entre el 1 y el 30: "))
    vidas -= 1

    if chosen_number > choose:
        print(color_grey, f"El número es mayor, pon uno más grande. Te quedan {vidas} vidas", end_color)
    elif chosen_number < choose:
        print(color_grey, f"El número es menor, pon uno más pequeño. Te quedan {vidas} vidas", end_color)

    if vidas == 0:
        print(color_red, f"Perdiste. El número era {chosen_number}", end_color)
        break
else:
    print(color_green, "Ganaste!!", end_color)


print('\n','*'*13, "EXTRA", '*'*13)
#Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares,
#y que no son ni el 16 ni múltiplos de 3.

nums = []
for n in range(10,56):
    if n%2 == 0 and n%3 != 0 and n != 16:
        nums.append(n)

print("Números entre el 10 y 55 pares, no múltiplos de 3 y no 16:\n", color_blue, nums, end_color)
