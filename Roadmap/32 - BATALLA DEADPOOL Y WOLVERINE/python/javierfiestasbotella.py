'''
```
/*
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
 */'''
import random
import time

class Heroe:
    def __init__(self,nombre,daño,defensa,puntos_vida=300):
        self.nombre=nombre
        self.daño=daño
        self.defensa=defensa
        self.puntos_vida=puntos_vida

    def __str__(self):
        return f'''
        {self.nombre}
        Daño: {self.daño}
        Defensa: {self.defensa}%'''
    
    def ataque(self):
        return random.randint(10, self.daño)
    
    def defensa(self):
        return random.randint(1, int(10*(self.defensa/100)))
    
    def resta_vida(self,n):
        self.puntos_vida-=n




if __name__ == "__main__":
    turno=1
    final=False
    vida_1=int(input('Introduce vida inicial de Deadpool: '))
    vida_2=int(input('Introduce vida inicial de Wolverine: '))

    Deadpool=Heroe('Deadpool',100,25,vida_1)
    Wolverine=Heroe('Wolverine',120,20,vida_2)

    print(f'''
        Comienza La Batalla Wolverine VS Deadpool
          
    Deadpool comienza con {vida_1} puntos de vida
    Wolverine comienza con {vida_2} puntos de vida   ''')

    def lucha(heroe):
        if heroe.ataque()==heroe.daño:
            return True
        else:
            return heroe.ataque()
    
    def golpe_defensa(h1,h2): 
        l=lucha(h1)
        if l==True:
            golpe_defensa(h1,h2)
            h2.resta_vida(l)
            time.sleep(1) 
            print(f'''{h1.nombre} Golpéa con el máximo de fuerza 
                  dejando a {h2.nombre} con {h2.puntos_vida} puntos de vida.
                  Repite el turno mientras {h2.nombre} se regenera.''')
            time.sleep(1)
            
                
            print()
        else:
            d=l-h2.defensa
            h2.resta_vida(d)
            time.sleep(1)
            print(f'''{h1.nombre} Golpéa con {l} de fuerza 
                  dejando a {h2.nombre} con {h2.puntos_vida} puntos de vida.
                  Ahora el turno es para {h2.nombre}.''') 
            time.sleep(1) 
            
                
            print()

    while final==False:
        golpe_defensa(Deadpool,Wolverine)
        if Wolverine.puntos_vida<=0:
            print(f'{Deadpool.nombre} GANADOR!!!!')
            final=True
            break

        golpe_defensa(Wolverine,Deadpool)
        if Deadpool.puntos_vida<=0:
            print(f'{Wolverine.nombre} GANADOR!!!!')
            final=True 
            break
    print('FINAL DEL JUEGO')
    print(f'''
{Deadpool.nombre} --> {Deadpool.puntos_vida}
{Wolverine.nombre} --> {Wolverine.puntos_vida}''')



    