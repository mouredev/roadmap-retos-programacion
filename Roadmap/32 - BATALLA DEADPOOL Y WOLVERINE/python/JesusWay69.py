import os, platform, random, time

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

    """* EJERCICIO:
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
 * 5. Muestra el resultado final."""
    
class Deadpool:
    name = "Deadpool"
    max_damage = 100
    shield = 25

class Wolverine:
    name = "Wolverine"
    max_damage = 120
    shield = 20

def battle(local_name, foreign_name, shield, max_damage, local_points, enemy_points, regenerate_state ):
    if regenerate_state:
        print(f" {local_name} pierde su turno por haber recibido daño máximo y tener que regenerarse ")
        regenerate_state = False
        
    elif random.random() > shield/100:
        damage = random.randint(10, max_damage)
        print (f" El ataque de {local_name} le ha restado {damage} puntos de vida a {foreign_name}")
        if damage == 100:
            print(f" ¡¡Ataque máximo de {local_name}!!")
            regenerate_state = True
        enemy_points -= damage
        if enemy_points <= 0:
            print(f" {foreign_name} se ha quedado sin puntos de vida")
            print(f"\n----- {local_name} gana el torneo con {local_points} puntos de vida restantes -----")
        else:
            print(f" A {foreign_name} le quedan {enemy_points} puntos")
    else:
        print(f" {foreign_name} repele el ataque de {local_name} y no pierde puntos, conserva sus {enemy_points} puntos")
    return  tuple((enemy_points, regenerate_state))

deadpool = Deadpool()
wolverine = Wolverine()

d_points = int(input("Introduzca los puntos de inicio de Deadpool: "))
w_points = int(input("Introduzca los puntos de inicio de Wolverine: "))
regenerate_state = False
round = 1
while d_points>0 and w_points>0:
    print("Ronda: ",round)
    ####################Ataca Deadpool####################
    w_points, regenerate_state = battle(deadpool.name, wolverine.name, wolverine.shield, deadpool.max_damage, d_points, w_points, regenerate_state)
    print()
    if w_points <=0:
        break
    ####################Ataca Wolverine####################
    d_points, regenerate_state = battle(wolverine.name, deadpool.name, deadpool.shield, wolverine.max_damage, w_points, d_points, regenerate_state)
    round+=1
    print()
    time.sleep(1)
    
