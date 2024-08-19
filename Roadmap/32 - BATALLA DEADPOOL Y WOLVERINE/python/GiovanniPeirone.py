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
import random
import os


LimpiarPantalla = "cls" # si usas Linux o mac coloca "clear"

class Personaje:
    def __init__(self, Vida, Ataque, Defensa,Nombre , AtaqueMax):
        self.vida = Vida
        self.ataque = Ataque
        self.defensa = Defensa
        self.nombre = Nombre
        self.ataquemax = AtaqueMax
    
    def Atacar(self, Enemigo ):
        self.vida -= self.ataque
        print(f"{self.nombre} a recibido {self.ataque} de daño" )

class main():

    Turno = 0

    def MAIN(self):

        vidaDeadpool = int(input("Vida de Deadpool:"))
        vidaWolverine = int(input("Vida de Wolverine:"))
        Deadpool = Personaje(vidaDeadpool, random.randrange(10, 100), random.randrange(25, 100) ,"Deadpool",100)
        Wolverine = Personaje(vidaWolverine, random.randrange(10, 120), random.randrange(20, 100) ,"Wolverine",120)

        while True:
            Deadpool.ataque = random.randrange(10,100)
            Wolverine.ataque = random.randrange(10,120)
            Deadpool.defensa = random.randrange(0,100)
            Wolverine.defensa = random.randrange(0,100)
            print(f"---------------------- Turno {main.Turno} ----------------------")
            print(f'''
            {Deadpool.nombre}       | {Wolverine.nombre}
            Vida = {Deadpool.vida}       | Vida = {Wolverine.vida}
            ''')
            if self.Turno % 2 == 0: 
                #Ataca Wolverine
                if Deadpool.defensa < 20:
                    print("Deadpool se a defendido")
                if Wolverine.ataque == 120:
                    Deadpool.Atacar(Wolverine)
                    print("Wolverine a echo el maximo de daño, Deadpool debe utilizar su turno para recuperarse")
                    main.Turno += 1
                else:
                    Wolverine.Atacar(Deadpool)

            if self.Turno % 2 != 0:
                #Ataca Deadpool
                if Wolverine.defensa < 25:
                    print("Wolverine se a defendido")
                if Deadpool.ataque == 100:
                    Deadpool.Atacar(Wolverine)
                    print("Deadpool a echo el maximo de daño Wolverine debe utilizar el turno para recuperarse")
                    main.Turno +1
                else:
                    Deadpool.Atacar(Wolverine)
            
            if Deadpool.vida <= 0:
                print(f"Deadpool a muerto vida = {Deadpool.vida}")
                break
            if Wolverine.vida <= 0:
                print(f"Wolverine a muerto vida = {Wolverine.vida}")
                break
            os.system("pause")
            main.Turno += 1
            os.system(LimpiarPantalla)
aplicacion = main()
aplicacion.MAIN()
exit()