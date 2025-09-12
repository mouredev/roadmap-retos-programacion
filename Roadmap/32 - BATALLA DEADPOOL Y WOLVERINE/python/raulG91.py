from abc import ABC,abstractmethod
from random import randint
import  time

class Hero(ABC):
    def __init__(self,max_life):
        self.life = max_life
    @abstractmethod
    def attack(self)->int:
        pass
    @abstractmethod
    def defende(self)->bool:
        pass
    @abstractmethod
    def getMaxAttack(self)->int:
        pass
    def getLife(self)->int:
        return self.life
    def reduceLife(self,number):
        self.life -= number    

class Deadpool(Hero):
    def attack(self) -> int:
        #Generate a random number between 10 and 100
        number = randint(10,100)
        return number         
    def defende(self) -> bool:
        number = randint(0,100)
        if number <=25:
            return True
        else:
            return False
    def getMaxAttack(self) -> int:
        return 100

class Wolverine(Hero):
    def attack(self) -> int:
        #Generate a random number between 10 and 100
        number = randint(10,120)
        return number         
    def defende(self) -> bool:
        number = randint(0,100)
        if number <=20:
            return True
        else:
            return False
    def getMaxAttack(self) -> int:
        return 120       


print("Enter max life for Deadpool")
max_life = int(input())

deadpool = Deadpool(max_life)

print("Enter max life for Wolverine")
max_life = int(input())
wolverine = Wolverine(max_life)

turn = 1
skip_turn = False

while(True):
    
    if deadpool.getLife()<=0 or wolverine.getLife() <= 0:
        #One of the heroes doesn't have life
        print("Ending battle")
        break
    else:
        print(f'Starting turn {turn}')
        if skip_turn:
            if turn % 2 != 0:
                print("Skipping this turn for Deadpool")
            else:
                print("Skipping turn for Wolverine")
            skip_turn = False    
            turn += 1
        else:  
            if turn % 2 != 0:
                #Deadpool attack
                attack = deadpool.attack()
                defense = wolverine.defende()
                print(f'Deadpool attack {attack} ')
                if not(defense):
                    wolverine.reduceLife(attack) 
                else:
                    print("Wolverine will defend Deadpool's attack")    
                if attack == deadpool.getMaxAttack():
                    skip_turn = True    
            else:
                #Wolverine attack
                attack = wolverine.attack()
                defense = deadpool.defende()
                print(f'Wolverine attack {attack} ')
                if not(defense):
                    deadpool.reduceLife(attack)    
                else:
                    print("Deadpool will defend Wolverine's attack")   
                if attack == wolverine.getMaxAttack():
                    skip_turn = True    
            print(f'Deadpol remains life is {deadpool.getLife()}')
            print(f'Wolverine remains life is {wolverine.getLife()}')   
            turn += 1     
            time.sleep(1)


