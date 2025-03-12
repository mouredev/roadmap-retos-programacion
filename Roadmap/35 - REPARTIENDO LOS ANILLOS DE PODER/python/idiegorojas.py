"""
35 - Los Anillos de Poder
"""
# Desarrolla un programa que se encargue de distribuirlos.

# Requisitos:
# 1. Los Elfos recibirán un número impar.
# 2. Los Enanos un número primo.
# 3. Los Hombres un número par.
# 4. Sauron siempre uno.

# Acciones:
# 1. Crea un programa que reciba el número total de anillos y busque una posible combinación para repartirlos.
# 2. Muestra el reparto final o el error al realizarlo.


import math
import random
from abc import ABC, abstractmethod

def es_primo(num):
    """Verifica si un número es primo"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

class Distribuidor:
    def __init__(self, total_anillos):
        try:
            self.total = int(total_anillos)
            self.anillos_disponibles = list(range(1, self.total + 1))
            self.anillos_asignados = []
        except ValueError:
            print("Por favor ingrese un número válido")
            self.total = 0
            self.anillos_disponibles = []
            self.anillos_asignados = []

    def distribuir_anillos(self):
        if self.total < 20:  # 3 + 7 + 9 + 1 = 20 anillos mínimo
            print(f"No hay suficientes anillos ({self.total}) para la distribución. Se necesitan al menos 20.")
            return False
            
        # Obtener anillos para elfos (3 impares)
        anillos_impares = [a for a in self.anillos_disponibles if a % 2 == 1]
        if len(anillos_impares) < 3:
            print("No hay suficientes anillos impares para los elfos")
            return False
        anillos_elfos = random.sample(anillos_impares, 3)
        self.anillos_asignados.extend(anillos_elfos)
        
        # Obtener anillos para enanos (7 primos)
        anillos_primos = [a for a in self.anillos_disponibles 
                        if es_primo(a) and a not in self.anillos_asignados]
        if len(anillos_primos) < 7:
            print("No hay suficientes anillos primos para los enanos")
            return False
        anillos_enanos = random.sample(anillos_primos, 7)
        self.anillos_asignados.extend(anillos_enanos)
        
        # Obtener anillos para hombres (9 pares)
        anillos_pares = [a for a in self.anillos_disponibles 
                       if a % 2 == 0 and a not in self.anillos_asignados]
        if len(anillos_pares) < 9:
            print("No hay suficientes anillos pares para los hombres")
            return False
        anillos_hombres = random.sample(anillos_pares, 9)
        self.anillos_asignados.extend(anillos_hombres)
        
        # Obtener anillo para Sauron (cualquiera que quede)
        anillos_restantes = [a for a in self.anillos_disponibles 
                           if a not in self.anillos_asignados]
        if not anillos_restantes:
            print("No queda ningún anillo para Sauron")
            return False
        anillo_sauron = random.choice(anillos_restantes)
        self.anillos_asignados.append(anillo_sauron)
        
        # Mostrar resultados
        print(f"Los elfos recibieron anillos: {anillos_elfos}")
        print(f"Los enanos recibieron anillos: {anillos_enanos}")
        print(f"Los hombres recibieron anillos: {anillos_hombres}")
        print(f"Sauron recibió el anillo: {anillo_sauron}")
        
        return True

# Programa principal
if __name__ == "__main__":
    anillos = input("Ingrese el número total de anillos a repartir: ")
    distribuidor = Distribuidor(anillos)
    distribuidor.distribuir_anillos()