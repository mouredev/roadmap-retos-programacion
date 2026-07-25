r"""
 EJERCICIO:
 ¡El último videojuego de Dragon Ball ya está aquí!
 Se llama Dragon Ball: Sparking! ZERO.

 Simula un Torneo de Artes Marciales, al más puro estilo
 de la saga, donde participarán diferentes luchadores, y el
 sistema decidirá quién es el ganador.

 Luchadores:
 - Nombre.
 - Tres atributos: velocidad, ataque y defensa
   (con valores entre 0 a 100 que tú decidirás).
 - Comienza cada batalla con 100 de salud.
 Batalla:
 - En cada batalla se enfrentan 2 luchadores.
 - El luchador con más velocidad comienza atacando.
 - El daño se calcula restando el daño de ataque del
   atacante menos la defensa del oponente.
 - El oponente siempre tiene un 20% de posibilidad de
   esquivar el ataque.
 - Si la defensa es mayor que el ataque, recibe un 10%
   del daño de ataque.
 - Después de cada turno y ataque, el oponente pierde salud.
 - La batalla finaliza cuando un luchador pierde toda su salud.
 Torneo:
 - Un torneo sólo es válido con un número de luchadores
   potencia de 2.
 - El torneo debe crear parejas al azar en cada ronda.
 - Los luchadores se enfrentan en rondas eliminatorias.
 - El ganador avanza a la siguiente ronda hasta que sólo
   quede uno.
 - Debes mostrar por consola aquello lo que sucede en el torneo,
   así como el ganador.
"""
from random import randint


class Fighter:

    def __init__(self, name: str, attack: int, defense: int, speed: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = 100
        self.speed = speed

    def set_health(self, damage: int):
        self.health -= damage


class Fight:

    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.round = 1

    @staticmethod
    def attack(attack, defense, dodge):
        damage = attack - defense if attack >= defense else ((defense - attack) / 10).__ceil__()
        damage = damage if dodge > 2 else 0
        if dodge < 3:
            print("\t\tAttack dodged => damage 0")
        else:
            print(f"\t\tEffective attack: damage injuried {damage}")
        return damage

    @staticmethod
    def dodge():
        y = 0
        for x in range(0, 1000):
            y = randint(1, 10)
        return y

    def fight(self):
        if self.round % 2:
            if self.fighter1.speed >= self.fighter2.speed:
                attacker = self.fighter1
                defender = self.fighter2
            else:
                attacker = self.fighter2
                defender = self.fighter1
        else:
            if self.fighter1.speed >= self.fighter2.speed:
                attacker = self.fighter2
                defender = self.fighter1
            else:
                attacker = self.fighter1
                defender = self.fighter2
        self.round += 1
        dodging = self.dodge()
        print(f"\t{attacker.name} attacks with power/speed {attacker.attack}/{attacker.speed} <=> health level = {attacker.health}")
        print(f"\t{defender.name} defends with power/speed {defender.defense}/{defender.speed} <=> health level = {defender.health}")
        damage = self.attack(attacker.attack, defender.defense, dodging)
        defender.set_health(damage)


class Tournament:

    def __init__(self, competitors: list):
        if competitors.__len__() in [pow(2, x) for x in range(1, 11)]:
            pass
        else:
            raise "No hay suficientes inscriptos."
        self.fight = None
        self.competitors = competitors

    def combat(self):
        winner = None
        self.fight = Fight(self.competitors.pop(randint(0, self.competitors.__len__() - 1)), self.competitors.pop(randint(0, self.competitors.__len__() - 1)))
        print(f"\nRound {self.fight.fighter1.name} vs {self.fight.fighter2.name}")
        while True:
            self.fight.fight()
            if self.fight.fighter1.health <= 0:
                winner = self.fight.fighter2
                break
            if self.fight.fighter2.health <= 0:
                winner = self.fight.fighter1
                break
        self.competitors.append(winner)
        return winner


tolo = Fighter("Tolo", 77, 48, 27)
pipa = Fighter("Pipa", 69, 81, 42)
chino = Fighter("Chino", 91, 37, 31)
lalo = Fighter("Lalo", 65, 78, 33)

torneo = Tournament([tolo, pipa, chino, lalo])

while torneo.competitors.__len__() > 1:
    winner = torneo.combat()
    print(f"\n{winner.name} Won this combat and pass to the next round")

print(f"\nn{torneo.competitors[0].name} Won the tounament.")
