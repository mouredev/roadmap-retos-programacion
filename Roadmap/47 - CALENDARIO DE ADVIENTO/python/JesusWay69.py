import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 *
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** **** **** **** ****
 * *01* *02* *03* *04* *05* *06*
 * **** **** **** **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** **** 
 * **** *02* *03* ...
 * **** **** ****
 *
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario."""

calendar = []
used_numbers = set()
for i in range(6):
            calendar.append("****")

for i in range(1, 25):
    day:str = f"*{str(i).zfill(2)}*"
    calendar.append(day)
    if i % 6 == 0:
        for i in range(6):
            calendar.append("****")

def show_calendar(calendar:list):
    for i in range (1, len(calendar) + 1):
        print(calendar[i-1], end=' ')
        if i % 6 == 0:
            print()
    
while True:
    show_calendar(calendar)
    number:str = input("\nIntroduzca el día del calendario del 1 al 24 o enter para salir: ")
    if number == '':
         break

    elif not number.isdigit or int(number) > 24 or int(number) < 1:
        print("El dato debe ser numérico entre 1 y 24, intente de nuevo")
        continue
    
    else:
        target:str = number.zfill(2)
        for number in used_numbers:
            if number == target:
                print(f"El número {target} ya se ha seleccionado antes, intente con otro") 
            continue  
        for j in range(len(calendar)):
            if target in calendar[j]:
                calendar[j] = "****"
                used_numbers.add(target)
          
        