"""
#32 - Batalla Deadpool y Wolverine
"""
# ¡Deadpool y Wolverine se enfrentan en una batalla épica!
# Crea un programa que simule la pelea y determine un ganador.
# El programa simula un combate por turnos, donde cada protagonista posee unos
# puntos de vida iniciales, un daño de ataque variable y diferentes cualidades de regeneración y evasión de ataques.

"""
Requisitos:
"""
# 1. El usuario debe determinar la vida inicial de cada protagonista.
# 2. Cada personaje puede impartir un daño aleatorio:
    # Deadpool: Entre 10 y 100.
    # Wolverine: Entre 10 y 120.
# 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
# siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
# 4. Cada personaje puede evitar el ataque contrario:
    # Deadpool: 25% de posibilidades.
    # Wolverine: 20% de posibilidades.
# 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.

"""
Acciones:
"""
# 1. Simula una batalla.
# 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
# 3. Muestra qué pasa en cada turno.
# 4. Muestra la vida en cada turno.
# 5. Muestra el resultado final.

import random
import time

class SimulacionBatalla:
    def __init__(self, vida_deadpool, vida_wolverine):
        self.vida_deadpool = vida_deadpool
        self.vida_wolverine = vida_wolverine
        self.turno = 0
        self.deadpool_puede_atacar = True
        self.wolverine_puede_atacar = True
    
    def batalla(self):
        while self.vida_deadpool > 0 and self.vida_wolverine > 0:
            self.turno += 1
            print(f"\n--- TURNO {self.turno} ---")
            time.sleep(1)
            
            # Ataque de Deadpool
            if self.deadpool_puede_atacar:
                self.ataque_deadpool()
            else:
                print("¡Deadpool está regenerándose y no puede atacar!")
                self.deadpool_puede_atacar = True
            
            # Verificar si Wolverine aún tiene vida
            if self.vida_wolverine <= 0:
                break
                
            # Ataque de Wolverine
            if self.wolverine_puede_atacar:
                self.ataque_wolverine()
            else:
                print("¡Wolverine está regenerándose y no puede atacar!")
                self.wolverine_puede_atacar = True
                
            # Mostrar vida actual
            print(f"Vida Deadpool: {self.vida_deadpool}")
            print(f"Vida Wolverine: {self.vida_wolverine}")
        
        # Mostrar resultado final
        self.mostrar_resultado()
    
    def ataque_deadpool(self):
        # Deadpool ataca (10-100 daño)
        daño = random.randint(10, 100)
        
        # Comprobar evasión de Wolverine (20%)
        if random.random() < 0.20:
            print(f"¡Wolverine ha evitado el ataque de Deadpool!")
            return
        
        # Aplicar daño
        self.vida_wolverine -= daño
        print(f"¡Deadpool ataca y causa {daño} de daño a Wolverine!")
        
        # Comprobar si es un golpe crítico
        if daño == 100:
            print("¡GOLPE CRÍTICO! Wolverine necesita regenerarse")
            self.wolverine_puede_atacar = False
    
    def ataque_wolverine(self):
        # Wolverine ataca (10-120 daño)
        daño = random.randint(10, 120)
        
        # Comprobar evasión de Deadpool (25%)
        if random.random() < 0.25:
            print(f"¡Deadpool ha evitado el ataque de Wolverine!")
            return
        
        # Aplicar daño
        self.vida_deadpool -= daño
        print(f"¡Wolverine ataca y causa {daño} de daño a Deadpool!")
        
        # Comprobar si es un golpe crítico
        if daño == 120:
            print("¡GOLPE CRÍTICO! Deadpool necesita regenerarse")
            self.deadpool_puede_atacar = False
    
    def mostrar_resultado(self):
        print("\n--- FIN DE LA BATALLA ---")
        if self.vida_deadpool <= 0 and self.vida_wolverine <= 0:
            print("¡EMPATE! Ambos cayeron al mismo tiempo")
        elif self.vida_deadpool <= 0:
            print("¡WOLVERINE GANA!")
        else:
            print("¡DEADPOOL GANA!")

# Código principal
if __name__ == "__main__":
    print("--- BATALLA ÉPICA: DEADPOOL VS WOLVERINE ---")
    vida_deadpool = int(input("Vida inicial de Deadpool: "))
    vida_wolverine = int(input("Vida inicial de Wolverine: "))
    
    batalla = SimulacionBatalla(vida_deadpool, vida_wolverine)
    batalla.batalla()