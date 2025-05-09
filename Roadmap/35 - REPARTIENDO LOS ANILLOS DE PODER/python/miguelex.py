import math

def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def repartir_anillos(total_anillos):
    if total_anillos < 4:
        return "Error: No hay suficientes anillos para cumplir con los requisitos."
    
    anillos_sauron = 1
    total_anillos -= 1
    
    mejor_diferencia = float('inf')
    mejor_reparto = None
    
    for anillos_elfos in range(1, total_anillos + 1, 2):
        for anillos_enanos in range(2, total_anillos + 1):
            if es_primo(anillos_enanos):
                anillos_hombres = total_anillos - anillos_elfos - anillos_enanos
                
                if anillos_hombres > 0 and anillos_hombres % 2 == 0:
                    diferencia = max(anillos_elfos, anillos_enanos, anillos_hombres) - min(anillos_elfos, anillos_enanos, anillos_hombres)
                    
                    if diferencia < mejor_diferencia:
                        mejor_diferencia = diferencia
                        mejor_reparto = (anillos_elfos, anillos_enanos, anillos_hombres, anillos_sauron)
    
    if mejor_reparto:
        return f"Reparto exitoso: Elfos = {mejor_reparto[0]}, Enanos = {mejor_reparto[1]}, Hombres = {mejor_reparto[2]}, Sauron = {mejor_reparto[3]}"
    else:
        return "Error: No se encontró una combinación válida para repartir los anillos."

# Solicitar el número total de anillos por teclado
total_anillos = int(input("Ingresa el número total de anillos: "))
resultado = repartir_anillos(total_anillos)
print(resultado)
