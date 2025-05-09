import os, platform, random

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
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
 *   así como el ganador."""

class Character:
    def __init__(self, items) -> None:
        self.items = items
    def __getitem__(self, index):
        return self.items[index]

son_goku = Character(["Son Goku", 83, 69, 54])
vegeta = Character(["Vegeta", 78, 77, 49])
son_gohan = Character(["Son Gohan", 76, 59, 50])
trunks = Character(["Trunks", 77, 61, 39])
freezer = Character(["Freezer", 73, 69, 41])
piccolo = Character(["Piccolo", 87, 55, 32])
krilin = Character(["Krilin", 49, 78, 25])
bulma = Character(["Bulma", 66, 56, 44])
cell = Character(["Cell", 59, 80, 22])
broly = Character(["Broly", 70, 52, 29])
kame_sennin = Character(["Kame Sennin", 83, 48, 33])
ten_shin_han = Character(["Ten Shin Han", 67, 59, 31])
raditz = Character(["Raditz", 59, 77, 18])
beerus = Character(["Beerus", 63, 80, 15])
kaio = Character(["Kaiõ", 71, 52, 39])
mr_satan = Character(["Mr. Satán", 80, 51, 36])
zamasu = Character(["Zamasu", 69, 71, 43])
yamcha = Character(["Yamcha", 72, 59, 29])
majin_boo = Character(["Majin Boo", 70, 49, 45])
vegetto = Character(["Vegetto", 82, 54, 37])#20
androide_n_17 = Character(["Androide nº17", 58, 84, 12])
gotenks = Character(["Gotenks", 81, 52, 35])
bardock = Character(["Bardock", 76, 59, 30])
whis = Character(["Whis", 52, 73, 23])
chi_chi = Character(["Chi-Chi", 56, 86, 20])
shenlong = Character(["Shenlong", 58, 80, 26])
yamoshi = Character(["Yamoshi", 68, 50, 48])
videl = Character(["Videl", 81, 52, 46])
nappa = Character(["Nappa", 75, 51, 42])
bra = Character(["Bra", 81, 54, 39])
dabra = Character(["Dabra", 53, 87, 16])
jeice = Character(["Jeice", 80, 58, 45])

characters = [son_goku, vegeta, son_gohan, trunks, freezer, piccolo, krilin, bulma, cell, broly,
              kame_sennin, ten_shin_han, raditz, beerus, kaio, mr_satan, zamasu, yamcha, majin_boo,
              vegetto, androide_n_17, gotenks, bardock, whis, chi_chi, shenlong, yamoshi, videl, 
              nappa, bra, dabra, jeice]

def couples(characters:list)->list:
    tournament_list = []
    random.shuffle(characters)
    counter = 0
    for i in range (len(characters)//2):
        tournament_list.append([])
        tournament_list[i].append(characters[counter])
        tournament_list[i].append(characters[counter+1])
        counter += 2
    return tournament_list

def show_battles(tournament:list):
    for battle in tournament:
        print(f"{battle[0][0]} ---VS--- {battle[1][0]}") 

def fight1vs1(fighter1:object, fighter2:object)->object:
    score1, score2 = 100, 100
    damage1, damage2 = 0, 0
    power1, shield1 = int(fighter1[2]), int(fighter1[3])
    power2, shield2 = int(fighter2[2]), int(fighter2[3])
    print(f"\nBatalla entre {fighter1[0]} y {fighter2[0]}")
    print("--------------------------------------------")
    print(f"Ataca primero {fighter1[0] if fighter1[1] >= fighter2[1] else fighter2[0]}\n")
    while score1 > 0 and score2 > 0:
        if fighter1[1] >= fighter2[1]:

            if power1 >= shield2:

                if random.random() > 0.2:
                    damage2 = power1 - shield2
                    score2 -= damage2
                    print(f"-El ataque de {fighter1[0]} le resta {damage2} puntos a {fighter2[0]}", end=" ")

                    if score2 < 0: score2 = 0
                    print(f"que se queda con {score2} puntos")
                    damage2 = 0

                    if score2 <= 0:
                        print(f"\nEl ganador de la batalla es {fighter1[0]}\n")
                        return fighter1
                        
                else:
                    print(f"-{fighter2[0]} repele el ataque de {fighter1[0]} , turno para {fighter2[0]}")
                    
                if random.random() > 0.2:
                    damage1 = power2 - shield1
                    score1 -= damage1

                    print(f"-El ataque de {fighter2[0]} le resta {damage1} puntos a {fighter1[0]}", end=" ")
                    if score1 < 0: score1 = 0
                    print(f"que se queda con {score1} puntos")
                    damage1 = 0

                    if score1 <= 0:
                        print(f"\nEl ganador de la batalla es {fighter2[0]}\n")
                        return fighter2
                        
                else:
                    print(f"-{fighter1[0]} repele el ataque de {fighter2[0]}, turno para {fighter1[0]}")
                    continue
            elif power1 < shield2:
                 damage2 = power1 // 10
                 score2 -= damage2
        
        else:
            if power2 >= shield1:

                if random.random() > 0.2:

                    damage1 = power2 - shield1
                    score1 -= damage1
                    print(f"-El ataque de {fighter2[0]} le resta {damage1} puntos a {fighter1[0]}", end=" ")

                    if score1 < 0: score1 = 0
                    print(f"que se queda con {score1} puntos")
                    damage1 = 0

                    if score1 <=0:
                        print(f"\nEl ganador de la batalla es {fighter2[0]}\n")
                        return fighter2
                        
                else:
                    print(f"-{fighter1[0]} repele el ataque de {fighter2[0]}, turno para {fighter1[0]}")
                    
                if random.random() > 0.2:
                    damage2 = power1 - shield2
                    score2 -= damage2
                    print(f"-El ataque de {fighter1[0]} le resta {damage2} puntos a {fighter2[0]}", end=" ")

                    if score2 < 0: score2 = 0
                    print(f"que se queda con {score2} puntos")
                    damage2 = 0

                    if score2 <= 0:
                        print(f"\nEl ganador de la batalla es {fighter1[0]}\n")
                        return fighter1
                        
                else:
                    print(f"-{fighter2[0]} repele el ataque de {fighter1[0]}, turno para {fighter2[0]}")
                    continue

            elif power2 < shield1:
                    damage1 = fighter2[1] // 10
                    score1 -= damage1

rounds = ["Eliminatoria de dieciseisavos","Eliminatoria de octavos","Eliminatoria de cuartos","Semifinal","Final"]
for i, round in enumerate(rounds):
    
    print ("\n",round)
    print("----------------------------------------------------------------------------------------")
    if i == 0:
        fights = couples(characters)
        show_battles(fights)
    else:
        fights = couples(winners)
        show_battles(fights)
    winners = []   
    for fight in fights:
        winner = fight1vs1(fight[0], fight[1])
        winners.append(winner)
print(f"\n---------------------- EL GANADOR DEL TORNEO ES: {winner[0]} ----------------------\n")
    


