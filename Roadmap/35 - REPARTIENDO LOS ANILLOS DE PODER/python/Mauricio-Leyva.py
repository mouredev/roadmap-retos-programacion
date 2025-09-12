from sympy import isprime

def distribuir_anillos(total_anillos):
    if total_anillos < 4:  # Mínimo 1 para Sauron, 1 impar para Elfos, 1 primo para Enanos, y 1 par para Hombres
        print("No es posible repartir los anillos con las reglas dadas.")
        return
    
    anillos_restantes = total_anillos - 1
    
    for elfos in range(1, anillos_restantes, 2):  
        for enanos in range(2, anillos_restantes):
            if isprime(enanos):  
                hombres = anillos_restantes - elfos - enanos
                if hombres > 0 and hombres % 2 == 0:  
                    if elfos + enanos + hombres == anillos_restantes:
                        print(f"Reparto de anillos: Elfos = {elfos}, Enanos = {enanos}, Hombres = {hombres}, Sauron = 1")
                        return
    
    print("No se encontró una combinación válida para repartir los anillos.")

# Ejemplo de uso
total_anillos = 20
distribuir_anillos(total_anillos)
