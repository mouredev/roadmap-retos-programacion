# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
# developers. Del 1 al 24 de diciembre: https://adviento.dev
# 
# Dibuja un calendario por terminal e implementa una
# funcionalidad para seleccionar días y mostrar regalos.
# - El calendario mostrará los días del 1 al 24 repartidos
#   en 6 columnas a modo de cuadrícula.
# - Cada cuadrícula correspondiente a un día tendrá un tamaño 
#   de 4x3 caracteres, y sus bordes serán asteríscos.
# - Las cuadrículas dejarán un espacio entre ellas.
# - En el medio de cada cuadrícula aparecerá el día entre el
#   01 y el 24.
#
# Ejemplo de cuadrículas:
# **** **** ****
# *01* *02* *03* ...
# **** **** ****
#
# - El usuario selecciona qué día quiere descubrir.
# - Si está sin descubrir, se le dirá que ha abierto ese día
#   y se mostrará de nuevo el calendario con esa cuadrícula
#   cubierta de asteríscos (sin mostrar el día).
#
# Ejemplo de selección del día 1
# **** **** ****
# **** *02* *03* ...
# **** **** ****
#   
# - Si se selecciona un número ya descubierto, se le notifica
#   al usuario.


def create_adeviento():
    adeviento = []
    for i in range(1, 25):
        if i < 10:
            adeviento.append([f"0{int(i)}", False])
        else:
                adeviento.append([str(i), False])
    return adeviento

def show_calendar(adeviento: list):
    row = "**** "
    top_line = ""
    middle_line = ""
    bottom_line = ""
    for i , cell in enumerate(adeviento):
        top_line += row
        if not cell[1]:
            middle_line += f"*{cell[0]}* "
        else:
            middle_line += row
        bottom_line += row
        if (i + 1) % 6 == 0:
            print(top_line)
            print(middle_line)
            print(bottom_line)
            print()
            top_line = ""
            middle_line = ""
            bottom_line = ""

def open_box(adeviento: list, day: int):
    day -= 1
    if not  adeviento[day][1]:
        adeviento[day][1] = True
        print("Caja abierta.")
    else:
        print("La caja ya esta abierta.")

def main():
    adeviento = create_adeviento()
    show_calendar(adeviento)
    print("Calendario de aDEViento.")
    while True:
        choose = input("1. Abrir caja\n2. salir\n")
        match choose:
            case "1":
                try:
                    day = int(input("Indique un número del calendario de aDEViento: "))
                    if day < 1 or day > 24:
                        print("El número ha de ser entre 1 y 24.")
                        continue
                    open_box(adeviento, day)
                except ValueError as e:
                    print(f"ERROR: {e}")
                    continue
                show_calendar(adeviento)
            case "2":
                print("Saliendo del calendario de aDEViento.")
                break
            case _:
                print("Opción no valida.")

if __name__=="__main__":
    main()