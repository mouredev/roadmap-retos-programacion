'''
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
'''
### Libraries
import random
import time

### Classes

class Character():
    
    def __init__(self, name, health, attack, evade):
        self.name = name
        self.health = health
        self.attack = attack
        self.evade = evade

    def action_attack(self):
        return random.randint(self.attack[0], self.attack[1])

    def action_evade(self):
        return random.randint(1, 100) <= self.evade
    
    def get_health(self):
        return self.health

    def get_critical(self):
        return self.attack[1]

if __name__ == "__main__":
    
    deadpool_health = int(input("Ingrese la vida de Deadpool: "))
    wolverine_health = int(input("Ingrese la vida de Wolverine: "))
    deadpool = Character("Deadpool", deadpool_health, [10, 100], 25)
    wolverine = Character("Wolverine", wolverine_health, [10, 120], 20)

    ## Eleccion de quien inicia
    flag_init = random.randint(0, 1) ## 0 Deadpool, 1 Wolverine
    flag_deadpool_recovery = False ## Deadpool se está regenerando
    flag_wolverine_recovery = False ## Wolverine se está regenerando
    print("================== Batalla Wolwerine vs Deadpool ==================")

    turn = 1
    while True:
        
        print(f"\n================== Turno {turn} ==================\n")

        if flag_deadpool_recovery:
            print("==== Deadpool se está regenerando ==== ")
            flag_deadpool_recovery = False
        else:
            deadpool_damage = deadpool.action_attack()
            print(f"Deadpool ataca a Wolverine con un daño de {deadpool_damage}")
            if deadpool_damage == deadpool.get_critical():
                print("Wolverine no podrá atacar en el siguiente turno")
                flag_wolverine_recovery = True
                wolverine.health -= deadpool_damage
            else:
                if wolverine.action_evade():
                    print("Wolverine ha evadido el ataque")
                else:
                    wolverine.health -= deadpool_damage

        if flag_wolverine_recovery:
            print("Wolverine se está regenerando")
            flag_wolverine_recovery = False
        else:
            wolverine_damage = wolverine.action_attack()
            print(f"Wolverine ataca a Deadpool con un daño de {wolverine_damage}")
            if wolverine_damage == wolverine.get_critical():
                print("Deadpool no podrá atacar en el siguiente turno")
                flag_deadpool_recovery = True
                deadpool.health -= wolverine_damage
            else:
                if deadpool.action_evade():
                    print("Deadpool ha evadido el ataque")
                else:
                    deadpool.health -= wolverine_damage

        if deadpool.get_health() <= 0:
            print("\n===============================")
            print("!!!!! Wolverine ha ganado !!!!!")
            print("===============================\n")
            break
        if wolverine.get_health() <= 0:
            print("\n===============================")
            print("!!!!! Deadpool ha ganado !!!!!!")
            print("===============================\n")
            break
        
        print(f"====== Deadpool tiene {deadpool.get_health()} puntos de vida ======")

        print(f"====== Wolverine tiene {wolverine.get_health()} puntos de vida ======")

        turn += 1
        time.sleep(1) ## Espera
