""" 
# 42 - Torneo Dragon Ball 
"""

# Simula un Torneo de Artes Marciales, al más puro estilo de la saga, donde participarán diferentes luchadores, y el sistema decidirá quién es el ganador.

# Luchadores:
    # Nombre.
    # Tres atributos: velocidad, ataque y defensa
    # (con valores entre 0 a 100 que tú decidirás).
    # Comienza cada batalla con 100 de salud.

# Batalla:
    # En cada batalla se enfrentan 2 luchadores.
    # El luchador con más velocidad comienza atacando.
    # El daño se calcula restando el daño de ataque del
    # atacante menos la defensa del oponente.
    # El oponente siempre tiene un 20% de posibilidad de
    # esquivar el ataque.
    # Si la defensa es mayor que el ataque, recibe un 10%
    # del daño de ataque.
    # Después de cada turno y ataque, el oponente pierde salud.
    # La batalla finaliza cuando un luchador pierde toda su salud.

# Torneo:
    # Un torneo sólo es válido con un número de luchadores
    # potencia de 2.
    # El torneo debe crear parejas al azar en cada ronda.
    # Los luchadores se enfrentan en rondas eliminatorias.
    # El ganador avanza a la siguiente ronda hasta que sólo
    # quede uno.
    # Debes mostrar por consola todo lo que sucede en el torneo,
    # así como el ganador.


import random
import math

class Luchador:
    def __init__(self, nombre: str, velocidad: int, ataque: int, defensa: int) -> None:
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def reset_salud(self):
        self.salud = 100

    def __str__(self) -> str:
        return f"{self.nombre} (VEL:{self.velocidad} ATK:{self.ataque} DEF:{self.defensa})"
    
class Torneo:
    def __init__(self):
        self.participantes = []

    def agregar_participante(self, luchador: Luchador):
        self.participantes.append(luchador)
        
    def es_valido(self):
        """Verifica si el número de participantes es potencia de 2"""
        num_participantes = len(self.participantes)
        return num_participantes > 0 and math.log2(num_participantes).is_integer()
    
    def batalla(self, luchador1, luchador2):
        """Simula una batalla entre dos luchadores y retorna al ganador"""
        print(f"\n🥊 BATALLA: {luchador1.nombre} vs {luchador2.nombre} 🥊")
        print(f"{luchador1}")
        print(f"{luchador2}")
        
        # Resetear salud para la batalla
        luchador1.reset_salud()
        luchador2.reset_salud()
        
        # Determinar quién ataca primero (el más rápido)
        if luchador1.velocidad >= luchador2.velocidad:
            turno = 1  # Luchador 1 empieza
        else:
            turno = 2  # Luchador 2 empieza
        
        ronda = 1
        # Mientras ambos tengan salud
        while luchador1.salud > 0 and luchador2.salud > 0:
            if turno == 1:
                atacante, defensor = luchador1, luchador2
            else:
                atacante, defensor = luchador2, luchador1
                
            print(f"\nRonda {ronda} - Ataca {atacante.nombre}")
            
            # Comprobar si el defensor esquiva (20% de probabilidad)
            if random.random() < 0.2:
                print(f"¡{defensor.nombre} esquiva el ataque!")
            else:
                # Calcular daño
                daño = atacante.ataque - defensor.defensa
                
                # Si la defensa es mayor que el ataque
                if daño <= 0:
                    daño = int(atacante.ataque * 0.1)  # 10% del ataque
                    print(f"¡Defensa superior! {defensor.nombre} recibe sólo {daño} de daño")
                else:
                    print(f"{defensor.nombre} recibe {daño} de daño")
                
                # Aplicar daño
                defensor.salud = max(0, defensor.salud - daño)
                
            # Mostrar salud actualizada
            print(f"Salud de {luchador1.nombre}: {luchador1.salud}")
            print(f"Salud de {luchador2.nombre}: {luchador2.salud}")
            
            # Cambiar turno
            turno = 1 if turno == 2 else 2
            ronda += 1
        
        # Determinar ganador
        ganador = luchador1 if luchador1.salud > 0 else luchador2
        print(f"\n🏆 ¡{ganador.nombre} gana la batalla! 🏆")
        return ganador
    
    def ejecutar_torneo(self):
        """Ejecuta todas las rondas del torneo hasta determinar un campeón"""
        if not self.es_valido():
            print(f"Error: El número de participantes ({len(self.participantes)}) no es una potencia de 2")
            return None
        
        ronda = 1
        luchadores = self.participantes.copy()
        
        # Mientras haya más de un luchador
        while len(luchadores) > 1:
            print(f"\n===== RONDA {ronda} =====")
            print(f"Participantes: {len(luchadores)}")
            
            # Mezclar luchadores para emparejarlos aleatoriamente
            random.shuffle(luchadores)
            
            ganadores = []
            
            # Crear parejas y hacer que luchen
            for i in range(0, len(luchadores), 2):
                luchador1 = luchadores[i]
                luchador2 = luchadores[i + 1]
                
                ganador = self.batalla(luchador1, luchador2)
                ganadores.append(ganador)
            
            # Actualizar lista de luchadores para la siguiente ronda
            luchadores = ganadores
            ronda += 1
        
        # El último que queda es el campeón
        campeon = luchadores[0]
        print(f"\n🌟🏆🌟 ¡{campeon.nombre} ES EL CAMPEÓN DEL TORNEO! 🌟🏆🌟")
        return campeon

# Crear luchadores
def main():
    # Crear algunos luchadores de Dragon Ball
    goku = Luchador("Goku", 85, 90, 70)
    vegeta = Luchador("Vegeta", 80, 85, 75)
    piccolo = Luchador("Piccolo", 70, 75, 85)
    gohan = Luchador("Gohan", 75, 80, 80)
    krillin = Luchador("Krillin", 65, 60, 65)
    trunks = Luchador("Trunks", 78, 83, 72)
    cell = Luchador("Cell", 88, 87, 86)
    freezer = Luchador("Freezer", 82, 89, 78)
    
    # Crear torneo
    torneo = Torneo()
    
    # Agregar luchadores
    torneo.agregar_participante(goku)
    torneo.agregar_participante(vegeta)
    torneo.agregar_participante(piccolo)
    torneo.agregar_participante(gohan)
    torneo.agregar_participante(krillin)
    torneo.agregar_participante(trunks)
    torneo.agregar_participante(cell)
    torneo.agregar_participante(freezer)
    
    # Ejecutar torneo
    print("¡BIENVENIDOS AL TORNEO DE ARTES MARCIALES!")
    print("Participantes:")
    for i, luchador in enumerate(torneo.participantes, 1):
        print(f"{i}. {luchador}")
        
    torneo.ejecutar_torneo()

if __name__ == "__main__":
    main()