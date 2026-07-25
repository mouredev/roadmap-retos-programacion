"""
* EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
"""
import random

class Fighter:
    
    def __init__(self, name: str, attr: dict, health: int) -> None:
        self.name = name
        self.attr = attr
        self.health = health

    def __str__(self) -> str:
        return f"{self.name} - {self.health} HP"
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
    def reset_health(self) -> None:
        self.health = 100

    @property
    def speed(self) -> int:
        return self.attr['speed']
    
    @property
    def attack(self) -> int:
        return self.attr['attack']
    
    @property
    def defense(self) -> int:
        return self.attr['defense']
    
    @property
    def is_alive(self) -> bool:
        return self.health > 0
    
    def take_damage(self, damage: int) -> None:
        
        attack_damage = 0

        if random.random() < 0.2:
            # print(f"{self.name} ha esquivado el ataque")
            attack_damage = 0
        else:
            if self.defense >= damage:
                attack_damage = damage * 0.1
            else:
                attack_damage = damage - self.defense

            attack_damage = int(attack_damage)

        self.health = max(self.health - attack_damage, 0)
        # print(f"{self.name} ha recibido {attack_damage} de daño")
        # print(f"Salud restante de {self.name}: {self.health}")


class Battle:
    
    def __init__(self, fighterA: Fighter, fighterB: Fighter) -> None:
        self.FighterA = fighterA
        self.FighterB = fighterB

    def start(self, verbose=True) -> Fighter:
        if verbose:
            print(f"\n***** {self.FighterA.name} vs. {self.FighterB.name} *****")

        if self.FighterA.speed > self.FighterB.speed:
            attacker = self.FighterA
            defender = self.FighterB
        else:
            attacker = self.FighterB
            defender = self.FighterA

        while attacker.is_alive and defender.is_alive:
            
            defender.take_damage(attacker.attack)
            if defender.is_alive:
                attacker.take_damage(defender.attack)

        if self.FighterA.is_alive:
            # print(f"\n{self.FighterA.name} es el ganador de la batalla")
            return self.FighterA
        else:
            # print(f"\n{self.FighterB.name} es el ganador de la batalla")
            return self.FighterB


class Tournament:
    
    def __init__(self, fighters: list, verbose: bool) -> None:
        self.fighters = fighters
        self.verbose = verbose

    def start(self) -> Fighter:
        round = 1
        if self.verbose:
            print("¡¡¡TORNEO DRAGON BALL!!!")
            print(f"Participantes: {', '.join([fighter.name for fighter in self.fighters])}")


        if len(self.fighters) % 2 != 0:
            raise ValueError(f"El número de luchadores debe ser potencia de 2 y hay {len(self.fighters)} luchadores.")
        
        while len(self.fighters) > 1:
            if self.verbose:
                print(f"\n***** Ronda {round} *****")

            random.shuffle(self.fighters)
            winners = []
            for i in range(0, len(self.fighters), 2):
                battle = Battle(self.fighters[i], self.fighters[i+1])
                if self.verbose:
                    winner = battle.start()
                else:
                    winner = battle.start(verbose=False)
                if self.verbose:
                    print(f"{winner.name} es el ganador de la batalla")
                winners.append(winner)
            
            self.fighters = winners
            self.reset_health()
            round += 1

        return self.fighters[0]

    def reset_health(self) -> None:
        for fighter in self.fighters:
            fighter.reset_health()

if __name__ == "__main__":

    fighters = [
        Fighter("Goku", {"speed": 80, "attack": 95, "defense": 85}, 100),
        Fighter("Vegeta", {"speed": 70, "attack": 80, "defense": 90}, 100),
        Fighter("Gohan", {"speed": 90, "attack": 70, "defense": 80}, 100),
        Fighter("Piccolo", {"speed": 60, "attack": 60, "defense": 60}, 100),
        Fighter("Freezer", {"speed": 95, "attack": 90, "defense": 75}, 100),
        Fighter("Krillin", {"speed": 95, "attack": 90, "defense": 75}, 100),
        Fighter("Célula", {"speed": 92, "attack": 70, "defense": 73}, 100),
        Fighter("Trunks", {"speed": 88, "attack": 88, "defense": 88}, 100)
    ]

    print("\nSIMULACIÓN DE TORNEO")
    result_sim = [Tournament(fighters, verbose=False).start().name
                  for _ in range(1000)]
    
    from collections import Counter
    print("\nRESULTADOS DE LA SIMULACIÓN")
    counter = dict(Counter(result_sim))
    counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print(f"El favorito para ganar es: {counter[0][0]} con {counter[0][1]/1000} de probabilidades.\n\n")

    tournament = Tournament(fighters, verbose=True)
    winner = tournament.start()
    print("\n¡¡¡TORNEO FINALIZADO!!!")
    print(f"El ganador del torneo es: {winner.name}")
    print("¡¡¡Felicidades!!!")



    