# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# #47  CALENDARIO DE ADVIENTO
# ------------------------------------

"""
* EJERCICIO:
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
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
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
 *   al usuario.
 """

mtx = [[f"*{i*6+j+1:02d}*" for j in range(6)] for i in range(4)]
ln = "**** " * 6 + "\n"

while True:
    for row in mtx:
        print(ln +" ".join(row) + "\n" + ln)

    day = input("Día a descubrir: ")
    if day.isdigit() and int(day) > 0 and int(day) <= 24:
        r = (int(day) - 1) // 6 
        c = (int(day) - 1) % 6
        if mtx[r][c] == "****":
            print(f"El día {day} ya está descubierto.")
        else:
            mtx[r][c] = "****"
    else:
        print("Día inválido, debe ser entre 1 y 24.")
