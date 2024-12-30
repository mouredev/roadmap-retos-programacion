import random
from dataclasses import dataclass

def gen_values():
    while True:
        yield random.randint(0, 100)
gen = gen_values()

def es_potencia_de_dos(n):
    return n > 0 and (n & (n - 1)) == 0

def gen_parejas(luchadores_con_poderes):
    # Creamos una lista de luchadores que aún no han sido emparejados
    disponibles = luchadores_con_poderes[:]
    parejas = []
    
    while len(disponibles) > 1:
        # Elegimos dos luchadores aleatorios de la lista de luchadores disponibles
        luchador1 = random.choice(disponibles)
        disponibles.remove(luchador1)  # Quitamos el luchador1 de la lista
        luchador2 = random.choice(disponibles)
        disponibles.remove(luchador2)  # Quitamos el luchador2 de la lista
        
        # Añadimos la pareja a la lista de parejas
        parejas.append((luchador1, luchador2))
    
    return parejas

@dataclass
class Luchador:
    nombre: str
    velocidad: int
    ataque: int
    defensa: int
    salud: int = 100

lista_luchadores = ["Goku", "Vegeta", "Piccolo", "Gohan", "Krillin", "Trunks", "Freezer", "Majin Buu"]
luchadores_con_poderes = []

if not es_potencia_de_dos(len(lista_luchadores)):
        raise ValueError("El número de luchadores debe ser una potencia de 2.")

print("+"+"-"*16+"+")
print("| Participantes: |")
print("+"+"-"*51+"+")
print(f"| {'Nombre':<10} {'|':<3} {'Velocidad':<11} {'|':<3} {'Ataque':<8} | {'Defensa'} |")
print("="*52+"+")

for luchador in lista_luchadores:
    luchador_valores = Luchador(luchador, next(gen), next(gen), next(gen))
    luchadores_con_poderes.append(luchador_valores)
    print(f"| {luchador_valores.nombre:<10} {'|':<7} {luchador_valores.velocidad:<7} {'|':<5} {luchador_valores.ataque:<6} {'|':<4} {luchador_valores.defensa:<4} |")
    print("+------------+---------------+------------+---------+")

parejas = gen_parejas(luchadores_con_poderes)

print("\n+"+"-"*35+"+")
print(f"| {'Parejas de batalla:':<34}|")
print("+"+"-"*35+"+")
for pareja in parejas:
    print(f"| {pareja[0].nombre:<10} {'|':<3} {'vs':<4} {'|':<3} {pareja[1].nombre:<9} |")
print("+"+"-"*35+"+")

def batalla(luchador1, luchador2):
    print(f"\n\033[38;5;214m[!!] Inicia batalla: {luchador1.nombre} vs {luchador2.nombre}\033[0m")

    # Determinar quién ataca primero
    atacante, defensor = (luchador1, luchador2) if luchador1.velocidad >= luchador2.velocidad else (luchador2, luchador1)

    while luchador1.salud > 0 and luchador2.salud > 0:
        print(f"\nTurno de {atacante.nombre} atacando a {defensor.nombre}")

        # Determinar si el ataque es esquivado
        if random.random() < 0.2:
            print(f"{defensor.nombre} esquiva el ataque!")
        else:
            # Calcular daño
            if atacante.ataque > defensor.defensa:
                dano = atacante.ataque - defensor.defensa
            else:
                dano = int(atacante.ataque * 0.1)

            defensor.salud -= dano
            print(f"\033[31m[-] {defensor.nombre} recibe {dano} de daño. Salud restante: {defensor.salud} \033[0m")

        # Cambiar roles para el siguiente turno
        atacante, defensor = defensor, atacante

    ganador = luchador1 if luchador1.salud > 0 else luchador2
    return ganador


def torneo(parejas_iniciales):

    ronda = 1
    
    print("\n¡Comienza el torneo!")

    luchadores = [l for pareja in parejas_iniciales for l in pareja]

    while len(luchadores) > 1:
        print(f"\n--- Ronda {ronda} ---")
        
        # Usar las parejas iniciales en la primera ronda
        if ronda == 1:
            parejas = parejas_iniciales
        else:
            parejas = gen_parejas(luchadores)  # Generar nuevas parejas en rondas siguientes
    
        ganadores = []

        for pareja in parejas:
            ganador = batalla(pareja[0], pareja[1])
            ganadores.append(ganador)
            print(f"\n\033[34m[!] Ganador de la batalla entre {pareja[0].nombre} y {pareja[1].nombre}: {ganador.nombre}\033[0m")

        luchadores = ganadores
        ronda += 1

    print("\n¡El torneo ha terminado!")
    print(f"\033[32m[+] El ganador del torneo es: {luchadores[0].nombre}\033[0m")

torneo(parejas)
