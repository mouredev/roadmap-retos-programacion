### BATALLA DEADPOOL VS WOLVERINE
from abc import ABC, abstractmethod
from random import randint
from time import sleep

class Character(ABC):
    
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def dodge(self):
        pass
    
    @abstractmethod
    def regenerate(self):
        pass

class Deadpool(Character):
    def __init__(self, health: int = 250):
        self.name = "Deadpool"
        self.health = health
        self.max_health = health
        self.min_damage = 10
        self.max_damage = 100
        self.dodge_habilities = ['baile sexy', 'moonwalker', 'voltereta hacia atrás', 'chiste malo']
    
    def attack(self, opponent: object) -> int:
        damage = randint(self.min_damage, self.max_damage)
        opponent.health -= damage
        
        return damage
    
    def dodge(self):
        return randint(1,4) == 1 #25% de posibilidades de sacar el valor
    
    def regenerate(self):
        self.health += 15 if self.health < self.max_health else self.max_health
        print(f"{self.name} ha regenerado su salud, ahora tiene {self.health} puntos")

class Wolverine(Character):
    def __init__(self, health: int = 350):
        self.name = "Wolverine"
        self.health = health
        self.max_health = health
        self.min_damage = 10
        self.max_damage = 120
        self.dodge_habilities = ['agacharse', 'barrido lateral', 'doble tirabuzón', 'mortal invertido']

    def attack(self, opponent: object) -> int:
        damage = randint(self.min_damage, self.max_damage)
        opponent.health -= damage
        
        return damage
    
    def dodge(self):
        return randint(1,5) == 1 #20% de posibilidades de sacar el valor
    
    def regenerate(self):
        self.health += 25 if self.health < self.max_health else self.max_health
        print(f"{self.name} ha regenerado su salud, ahora tiene {self.health}/{self.max_health} puntos")



def simulate_battle():
    
    #Instanciamos los personajes
    deadpool = Deadpool()   
    wolverine = Wolverine()

    turn = 0
        
    #Decidimos quien ataca y quien defiende en primera instancia
    attacker = deadpool if turn % 2 == 0 else wolverine
    defender = wolverine if turn % 2 == 0 else deadpool
    
    print("#### Inicio de la Pelea ####")
    print("-" * 30)
    
    while deadpool.health>0 or wolverine.health>0:
        print(f"Turno {turn + 1}")
        print(f"Turno de {attacker.name}")
        if defender.dodge():
            print(f"{defender.name} ha conseguido esquivar el Ataque con {defender.dodge_habilities[randint(0, len(defender.dodge_habilities)-1)]}")
        else:
            damage = attacker.attack(opponent=defender)
            print(f"{attacker.name} ha lanzando una ataque de fuerza {damage} ahora {defender.name} tiene una salud de {defender.health}/{defender.max_health}")
            defender.regenerate() if damage != attacker.max_damage and defender.health>0 else None
        print("-" * 50)
        #Comprobamos la salud del defensor por si ha acabado la batalla
        if defender.health <= 0:
            print(f"{defender.name} ha sido derrotado")
            break
        
        #Cambiamos de turno si no se ha dado un ataque con el máximo de daño
        if damage != attacker.max_damage:
            attacker, defender = defender, attacker #Intercambiamos los papeles
        
        turn += 1
        sleep(1)
        
    print("#### Fin de la Pelea ####")
    print("-" * 30)

simulate_battle()
### FIN BATALLA DEADPOOL VS WOLVERINE