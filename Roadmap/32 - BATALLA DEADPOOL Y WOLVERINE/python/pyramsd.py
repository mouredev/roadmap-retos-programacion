import time
import random

class Personaje:
    def __init__(self, personaje, vida, evasion, damage):
        self.personaje = personaje
        self.vida = vida
        self.evasion = evasion
        self.damage = damage

    def set_vida(self, vida):
        self.vida = vida

    def atacar(self):
        return random.randint(10, self.damage)
    
    def evadir(self):
        return random.random() < self.evasion
    

def batalla(psj1, psj2):
    turno = 1
    print(f"Vidas iniciales:\nDeadpool: {psj1.vida} - Wolverine: {psj2.vida}")
    while psj1.vida > 0 and psj2.vida > 0:
        print("------------------------------")
        print(f"Turno: {turno}")

        if not psj2.evadir():
            damage = psj1.atacar()
            psj2.vida -= damage
            print(f"\033[38;5;214m[!!] {psj1.personaje} ataca a {psj2.personaje} y causa {damage} de daño.\033[0m")
        else:
            print(f"\033[34m[!] {psj2.personaje} esquiva el ataque de {psj1.personaje}!\033[0m")
        

        if psj2.vida <= 0:
            print(f"\033[31m[-] {psj2.personaje} ha sido derrotado!\033[0m")
            print(f"\033[32m[+] {psj1.personaje} es el ganador!\033[0m")
            break


        if not psj1.evadir():
            damage = psj2.atacar()
            psj1.vida -= damage
            print(f"\033[38;5;214m[!!] {psj2.personaje} ataca a {psj1.personaje} y causa {damage} de daño.\033[0m")
        else:
            print(f"\033[34m[!] {psj1.personaje} esquiva el ataque de {psj2.personaje}!\033[0m")

        
        if psj1.vida <= 0:
            print(f"\033[31m[-] {psj1.personaje} ha sido derrotado!\033[0m")
            print(f"\033[32m[+] {psj2.personaje} es el ganador!\033[0m")
            break

        print(f"Vida de {psj1.personaje}: {psj1.vida}")
        print(f"Vida de {psj2.personaje}: {psj2.vida}")

        turno += 1
        time.sleep(1)

deadpool = Personaje("Deadpool", 100, 0.25, 100)
wolverine = Personaje("Wolverine", 100, 0.20, 120)

batalla(deadpool, wolverine)
