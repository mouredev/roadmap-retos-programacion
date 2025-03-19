import random

class Luchador:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def esquivar(self):
        return random.random() < 0.2

def batalla(luchador1, luchador2):
    print(f"¡Batalla entre {luchador1.nombre} y {luchador2.nombre}!")
    atacante = luchador1 if luchador1.velocidad >= luchador2.velocidad else luchador2
    defensor = luchador2 if atacante == luchador1 else luchador1

    while luchador1.salud > 0 and luchador2.salud > 0:
        if defensor.esquivar():
            print(f"{defensor.nombre} esquivó el ataque de {atacante.nombre}!")
        else:
            danio = atacante.ataque - defensor.defensa
            if danio <= 0:
                danio = atacante.ataque * 0.1
            defensor.salud -= danio
            print(f"{atacante.nombre} ataca a {defensor.nombre} y causa {danio:.2f} de daño. Salud restante de {defensor.nombre}: {defensor.salud:.2f}")
        atacante, defensor = defensor, atacante

    ganador = luchador1 if luchador1.salud > 0 else luchador2
    print(f"¡{ganador.nombre} es el ganador de la batalla!\n")
    return ganador

def main():
    num_luchadores = int(input("Ingrese el número de luchadores (debe ser una potencia de 2): "))
    if (num_luchadores & (num_luchadores - 1)) != 0 or num_luchadores <= 0:
        print("El número de luchadores debe ser una potencia de 2.")
        return

    luchadores = []
    for i in range(num_luchadores):
        nombre = input(f"Ingrese el nombre del luchador {i + 1}: ")
        velocidad = int(input(f"Ingrese la velocidad de {nombre} (0-100): "))
        ataque = int(input(f"Ingrese el ataque de {nombre} (0-100): "))
        defensa = int(input(f"Ingrese la defensa de {nombre} (0-100): "))
        luchadores.append(Luchador(nombre, velocidad, ataque, defensa))

    print("¡Comienza el torneo de Dragon Ball: Sparking! ZERO!\n")
    while len(luchadores) > 1:
        ganadores = []
        random.shuffle(luchadores)
        for i in range(0, len(luchadores), 2):
            ganador = batalla(luchadores[i], luchadores[i + 1])
            ganadores.append(ganador)
        luchadores = ganadores

    print(f"¡El ganador del torneo es {luchadores[0].nombre}!")

if __name__ == "__main__":
    main()
