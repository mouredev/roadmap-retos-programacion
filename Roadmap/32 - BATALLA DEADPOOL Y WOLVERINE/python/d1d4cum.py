import random
import time


class Character:
    name: str
    life: int
    min_atack: int
    max_atack: int
    evasion: int

    def __init__(self, name, life, min_atack, max_atack, evasion):
        self.name = name
        self.life = life
        self.min_atack = min_atack
        self.max_atack = max_atack
        self.evasion = evasion

    def atack(self):
        return random.randint(self.min_atack, self.max_atack)

    def avoid(self):
        result = True if random.random() < (self.evasion / 100) else False
        return result


def main():
    wolverine = Character(name="Wolverine", life=300, min_atack=10, max_atack=120, evasion=20)
    deadpool = Character(name="Deadpool", life=200, min_atack=10, max_atack=100, evasion=25)
    turn = 1
    atack_turn = wolverine
    defense_turn = deadpool

    finish = False

    def change_turn():
        nonlocal atack_turn, defense_turn

        if atack_turn == wolverine:
            atack_turn = deadpool
            defense_turn = wolverine
        else:
            atack_turn = wolverine
            defense_turn = deadpool

    def points_resume():
        nonlocal atack_turn, defense_turn, finish

        if defense_turn.life <= 0:
            print(f"{atack_turn.name}: {atack_turn.life} puntos")
            print(f"{defense_turn.name}: 0 puntos")
            print(f"{atack_turn.name} gana!!")
            finish = True
        else:
            print(f"{atack_turn.name}: {atack_turn.life} puntos")
            print(f"{defense_turn.name}: {defense_turn.life} puntos")

    while not finish:

        print(f"\nTurno {turn}")
        atack = atack_turn.atack()
        print(f"{atack_turn.name} ataca")

        if not defense_turn.avoid():
            defense_turn.life -= atack

            if atack != atack_turn.max_atack:
                print(f"{defense_turn.name} intenta evadir el ataque, pero recibe {atack} puntos de daño")
                points_resume()
                change_turn()
            else:
                print(f"{defense_turn.name} intenta evadir el ataque, pero recibe un ataque crítico")
                print(f"{defense_turn.name} pierde el turno")
                points_resume()

        else:
            print(f"{defense_turn.name} evade el ataque")
            points_resume()
            change_turn()

        time.sleep(1)
        turn += 1


if __name__ == '__main__':
    main()
