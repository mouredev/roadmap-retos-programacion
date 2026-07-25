import random

class Personaje:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def __str__(self):
        return f"{self.nombre} (Velocidad: {self.velocidad}, Ataque: {self.ataque}, Defensa: {self.defensa}, Salud: {self.salud})"
    
    def resetear_salud(self):
        self.salud = 100


class Torneo:
    def __init__(self, luchadores):
        if len(luchadores) & (len(luchadores) - 1) != 0:
            raise ValueError("El número de luchadores debe ser una potencia de 2.")
        self.luchadores = luchadores
        self.rondas = []  # Para almacenar el progreso de cada ronda

    def emparejar_luchadores(self):
        random.shuffle(self.luchadores)
        parejas = [(self.luchadores[i], self.luchadores[i + 1]) for i in range(0, len(self.luchadores), 2)]
        return parejas

    def realizar_batalla(self, luchador1, luchador2):
        print(f"\nBatalla: {luchador1.nombre} vs {luchador2.nombre}")
        
        while luchador1.salud > 0 and luchador2.salud > 0:
            if luchador1.velocidad >= luchador2.velocidad:
                atacante, defensor = luchador1, luchador2
            else:
                atacante, defensor = luchador2, luchador1

            # Posibilidad de esquivar al 20%
            if random.random() < 0.2:
                print(f"{defensor.nombre} esquiva el ataque de {atacante.nombre}!")
            else:
                # Cálculo de daño
                if defensor.defensa >= atacante.ataque:
                    dano = 0.1 * atacante.ataque  # Recibe 10% del daño si la defensa es mayor
                else:
                    dano = atacante.ataque - defensor.defensa

                defensor.salud -= max(dano, 0)
                print(f"{atacante.nombre} inflige {dano:.2f} puntos de daño a {defensor.nombre}. Salud restante de {defensor.nombre}: {defensor.salud:.2f}")
            
            # Cambiamos rles en la siguiente iteracion
            luchador1, luchador2 = luchador2, luchador1

        ganador = luchador1 if luchador2.salud <= 0 else luchador2
        print(f"¡{ganador.nombre} gana la batalla!\n")
        return ganador

    def realizar_torneo(self):
        ronda_num = 1
        while len(self.luchadores) > 1:
            print(f"\n===== Ronda {ronda_num} =====")
            parejas = self.emparejar_luchadores()
            ganadores = []

            for luchador1, luchador2 in parejas:
                ganador = self.realizar_batalla(luchador1, luchador2)
                ganadores.append(ganador)
                ganador.resetear_salud()  # Restablecemos salud para la próxima ronda

            self.luchadores = ganadores
            self.rondas.append(parejas)
            ronda_num += 1

        print(f"\n===== ¡{self.luchadores[0].nombre} es el ganador del torneo! =====")

    def mostrar_esquema(self):
        print("\n===== Esquema del Torneo =====")
        for ronda, parejas in enumerate(self.rondas, start=1):
            print(f"\nRonda {ronda}:")
            for luchador1, luchador2 in parejas:
                print(f"{luchador1.nombre} vs {luchador2.nombre}")


goku_1 = Personaje('Goku', 89, 92, 88)
vegeta = Personaje('Vegeta', 89, 92, 88)
piccolo = Personaje('Piccolo', 75, 95, 70)
gohan = Personaje('Gohan', 85, 88, 80)
krillin = Personaje('Krillin', 60, 50, 55)
trunks = Personaje('Trunks', 89, 92, 88)
freezer = Personaje('Freezer', 88, 100, 89)
cell = Personaje('Cell', 88, 95, 80)
majin_buu = Personaje('Majin Buu', 81, 85, 95)
broly = Personaje('Broly', 78, 70, 85)
yamcha = Personaje('Yamcha', 55, 45, 40)
ten_shin_han = Personaje('Ten Shin Han', 65, 70, 60)
android_18 = Personaje('Android 18', 80, 85, 75)
android_17 = Personaje('Android 17', 82, 88, 78)
ginyu = Personaje('Ginyu', 68, 72, 65)
zarbon = Personaje('Zarbon', 63, 66, 62)
bulma = Personaje('Bulma', 25, 15, 20)
videl = Personaje('Videl', 55, 60, 50)
nappa = Personaje('Nappa', 50, 75, 70)
raditz = Personaje('Raditz', 60, 68, 60)


luchadores = [goku_1, vegeta, piccolo, gohan, krillin, trunks, freezer, cell, majin_buu, 
              broly, yamcha, ten_shin_han, android_18, android_17, ginyu, zarbon]
torneo = Torneo(luchadores)
torneo.mostrar_esquema()

torneo.realizar_torneo()
