import random
class Figther:

    def __init__(self,name,speed,attack,defense):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self._health = 100
    def setHeath(self,value:int):
        self._health = value
    def getHealth(self):
        return self._health
    def getName(self):
        return self.name    
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getSpeed(self):
        return self.speed
    def reduceHealth(self,value):
        self._health -= value

def is_pow_of_two(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0        
def simulate_combat(figther1:Figther,figther2:Figther)->Figther:

    figth_turn = []
    figther1.setHeath(100)
    figther2.setHeath(100)
    if figther1.getSpeed() > figther2.getSpeed():
        figth_turn.append(figther1)
        figth_turn.append(figther2)
    else:
        figth_turn.append(figther2)
        figth_turn.append(figther1)

    i = 0
    turno = 1
    print(f'Combate entre {figth_turn[i].getName()} y {figth_turn[(i+1)%2].getName()}')
    while figther1.getHealth() > 0 and figther2.getHealth() > 0:
        print(f'Turno {turno}')
        damage = abs(figth_turn[i].getAttack() - figth_turn[(i+1)%2].getDefense())
        skip = random.randint(0,100)
        if skip > 20:
            #Oponent doesn't skip the attack
            if figth_turn[(i+1)%2].getDefense() > damage:
                figth_turn[(i+1)%2].reduceHealth(damage*0.1)
            else:
                figth_turn[(i+1)%2].reduceHealth(damage)  
            print(f'Luchador {figth_turn[i].getName()} ataca con {damage} a {figth_turn[(i+1)%2].getName()} salud restante es: {figth_turn[(i+1)%2].getHealth()}')
        else:
            print(f'{figth_turn[(i+1)%2].getName()} esquiva el ataque de {figth_turn[i].getName()} ')
        i = (i+1) %2 
        turno += 1

    if figther1.getHealth() > 0:
        print(f'Ganador del combate es: {figther1.getName()}')
        return figther1
    else:
        print(f'El ganador del combate es: {figther2.getName()}')
        return figther2

def main():

    figthers = []
    figther = Figther("Goku",98,88,70)
    figthers.append(figther)
    figther = Figther("Krilin",90,80,50)
    figthers.append(figther)
    figther = Figther("Vegeta",95,85,45)
    figthers.append(figther)
    figther = Figther("Tortuga duende",80,90,53)
    figthers.append(figther)
    figther = Figther("Piccolo",85,78,51)
    figthers.append(figther)
    figther = Figther("Freezer",94,81,42)
    figthers.append(figther)
    figther = Figther("Celula",90,89,65)
    figthers.append(figther)
    figther = Figther("Zarbon",50,50,30)
    figthers.append(figther)
    if is_pow_of_two(len(figthers)):
        number_rounds = len(figthers)//2
        round = figthers.copy()
    
        for round_number in range(1,number_rounds):
            print(f'Empezando ronda {round_number}')
            winners = []
            while len(round) > 0:
                choice = random.randint(0,len(round)-1)
                figther1 = round[choice]
                del(round[choice])
                choice = random.randint(0,len(round)-1)
                fighter2 = round[choice]
                del(round[choice])
                winner = simulate_combat(figther1=figther1,figther2=fighter2)
                winners.append(winner)
            round = winners.copy() 
            if len(round) == 1:
                print(f'Ganador del torneo es: {round[0].getName()}')   
    else:
        print("Numero de participantes debe ser potencia de 2")


main()