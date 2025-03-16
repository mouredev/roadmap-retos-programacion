"""
/*
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 */
"""
class Anillos:

    def __init__(self,total) -> None:
        self.total = int(total)
        self.dar_anillos()
    
    def dar_anillos(self):
        restantes = self.total
        contador = 1
        sauron = 1
        restantes -= sauron
        primos = self.generar_primos(restantes)
        if primos:
            for num in primos:
                posible = restantes - num
                if posible % 2 != 0:
                    enanos = num
                    humanos = posible // 2
                    elfos = posible - humanos
                    if enanos + humanos + elfos + sauron == self.total and humanos % 2 == 0 and humanos > 0:
                        print(f"Posible reparto de {self.total} anillos de poder Nº {contador}:")
                        print(f"Elfos: {elfos}, Enanos: {enanos}, Humanos: {humanos}, Sauron: {sauron}")
                        print()
                        contador += 1
        if contador == 1:
            print(f"{self.total} no pueden repartirse")

    def generar_primos(self,restante):
        es_primo = [True] * (restante + 1)
        p = 2
        while p ** 2 <= restante:
            if es_primo[p]:
                for i in range(p * p, restante + 1, p):
                    es_primo[i] = False
            p += 1
        primos = [p for p in range(2, restante + 1) if es_primo[p]]
        return primos

# Pruebas
Anillos(12)
Anillos(20)
Anillos(150)
Anillos(251)
