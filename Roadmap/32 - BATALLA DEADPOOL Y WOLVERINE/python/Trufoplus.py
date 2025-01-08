from random import randint
import time


class BattleSystem:
    def damage(self):
        return randint(self.damage_range[0], self.damage_range[1])
    
    def critical_hit(self, damage):
        return damage == self.damage_range[1]
              
    def evasion_chance(self):
        return randint(0, 100) < self.evasion
    
    def dead(self):
        return self.health <= 0

    def __str__(self):
        return (
            f'Vida {self.name}: {self.health}'
            )
   
    
class Deadpool(BattleSystem):
    def __init__(self, health: int):
        self.name = 'Deadpool'
        self.health = health
        self.damage_range = [10, 100]
        self.regeneration = 1
        self.evasion = 25
        

class Wolverine(BattleSystem):
    def __init__(self, health: int):
        self.name = 'Wolverine'
        self.health = health
        self.damage_range = [10, 120]
        self.regeneration = 1
        self.evasion = 20


class BattleSimulation:
    @staticmethod
    def battle(deadpool: Deadpool, wolverine: Wolverine):
        turn = 1
        
        while True:
            #Comprueba si deadpool esta vivo   
            if deadpool.dead():
                print("\nDeadpool ha sido derrotado. ¡Wolverine gana!\n")
                break
            
            print(f'\nEstamos en el turno {turn}')
            
            #Si estamos empezando aun no se han realizado ataques
            if turn == 1:
                damage = 0
            #Ataca Deapool si no le han hecho un daño critico
            if not wolverine.critical_hit(damage):
                damage = deadpool.damage()
                
                if wolverine.evasion_chance():
                    print('Wolverine esquiva el ataque!!')
                else:
                    wolverine.health -= damage
                    print(f'+ Deadpool hace {damage} puntos de daño.')                    
                print(wolverine)
            
            #Comprueba si wolverine esta vivo
            if wolverine.dead():
                print("\nWolverine ha sido derrotado. ¡Deadpool gana!\n")
                break
            
            # Ataca wolverine si no le han hecho un daño critico
            if not deadpool.critical_hit(damage):
                
                damage = wolverine.damage()
                if deadpool.evasion_chance():
                    print('Deadpool esquiva el ataque!!')
                else:
                    deadpool.health -= damage
                    print(f'+ Wolverine hace {damage} puntos de daño.')
                print(deadpool)
            
            time.sleep(5)    
            turn += 1
            
        
        
        
        








# Pruebas
deadpool_char = Deadpool(int(input('Introduce la vida inicial de Deadpool: ')))
print(deadpool_char)
wolverine_char = Wolverine(int(input('Introduce la vida inicial de Wolverine: ')))
print(wolverine_char)

BattleSimulation.battle(deadpool_char, wolverine_char)