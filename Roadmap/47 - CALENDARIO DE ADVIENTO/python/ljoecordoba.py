"""
Este programa simula un calendario de Adviento interactivo llamado "aDEViento".
Funcionamiento:
1. Se representa un calendario con 24 días, distribuidos en una cuadrícula de 6 filas y 4 columnas.
2. Los días que aún no han sido descubiertos se muestran con su número dentro de asteriscos (*XX*).
3. Los días que han sido descubiertos se representan con asteriscos (****).
4. El usuario puede seleccionar un día para descubrirlo hasta que todos los días sean abiertos.
5. Se valida la entrada del usuario para evitar selecciones inválidas o repetidas.
6. Cuando todos los días han sido descubiertos, el programa finaliza con un mensaje de felicitación.
"""

def dibujar_calendario(dias_descubiertos):
    # Definir la cuadrícula de 6x4x3 (6 filas, 4 columnas, cada día 4x3)
    for fila in range(6):
        for columna in range(4):
            dia = fila * 4 + columna + 1  # Calcula el número de día
            if dia > 24:  # No dibujar días fuera del rango 1-24
                break
            # Si el día está descubierto, dibujar los asteriscos, si no, mostrar el día
            if dia in dias_descubiertos:
                print("****", end=" ")
            else:
                print(f"*{dia:02}*", end=" ")
        print()

def seleccionar_dia(dias_descubiertos):
    # Solicitar al usuario que seleccione un día
    try:
        dia = int(input("Selecciona el día que quieres descubrir (1-24): "))
        if dia < 1 or dia > 24:
            print("Por favor, ingresa un número de día válido (1-24).")
            return
        if dia in dias_descubiertos:
            print(f"¡El día {dia} ya ha sido descubierto!")
        else:
            dias_descubiertos.add(dia)  # Marcar el día como descubierto
            print(f"¡Has abierto el día {dia}!")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def main():
    dias_descubiertos = set()  # Usamos un conjunto para almacenar los días descubiertos

    while len(dias_descubiertos) < 24:  # Mientras no todos los días estén descubiertos
        print("\nCalendario de aDEViento:")
        dibujar_calendario(dias_descubiertos)
        seleccionar_dia(dias_descubiertos)

    print("\n¡Has descubierto todos los días del aDEViento! 🎉")

if __name__ == "__main__":
    main()
