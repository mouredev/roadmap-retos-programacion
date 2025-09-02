"""
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
"""
import random

# Función para comprobar el total
def comprobar_total(num_anillos: int, total_anillos: int, anillos_enanos : int) -> bool:
    if num_anillos == total_anillos and anillos_enanos >= 2:
        return True
    else:
        return False

# Función para número par
def numero_par(numero: int) -> list:
    lista_pares = []
    for num in range(2, numero + 1, 2):
        lista_pares.append(num)
    return lista_pares
        
    
# Funcion para numero impar
def numero_impar(numero: int) -> list:
    lista_impares = []
    for num in range(1, numero + 1, 2):
        lista_impares.append(num)
    return lista_impares
        
# Función para comprobar si un número es primo
def es_primo(num: int):
    lista_primos = []
    count = 0
    for i in range(2, num + 1):
        for j in range(2, int(i/2 + 1)):
            if i % j == 0:
                count += 1
        if count == 0:
            lista_primos.append(i)
        count = 0
    return lista_primos
    
    
# Función para distribuir los anillos

def distribucion_anillos(num_anillos : int):
           
    if num_anillos < 6:
        print("No es posible hacer una repartición de los anillos")
    else:
        continuar = True
        numero_anillos = num_anillos
        total_anillos = 0
        anillos_hombres = 0
        anillos_elfos = 0
        anillos_enanos = 0
        while continuar == True:    
            sauron_anillos = 1
            numero_anillos -= sauron_anillos
            
            lista_hombres = numero_par(numero_anillos)
            anillos_hombres = random.choice(lista_hombres)
            numero_anillos -= anillos_hombres
            lista_elfos = numero_impar(numero_anillos)
            anillos_elfos = random.choice(lista_elfos)
            numero_anillos -= anillos_elfos
            if sauron_anillos + anillos_elfos + anillos_hombres <= num_anillos-2:
                lista_enanos = es_primo(numero_anillos)
                anillos_enanos = random.choice(lista_enanos)
                total_anillos = sauron_anillos + anillos_elfos + anillos_enanos + anillos_hombres
            
                condicion = comprobar_total(num_anillos, total_anillos, anillos_enanos)
                if condicion == True:
                    print(
                        f"""Sauron : {sauron_anillos}\nHombres : {anillos_hombres}\nElfos : {anillos_elfos}\nEnanos : {anillos_enanos}"""
                        )
                    continuar = False
                else:
                    numero_anillos = num_anillos
                    total_anillos = 0
                    anillos_hombres = 0
                    anillos_elfos = 0
                    anillos_enanos = 0
                    continue
            
            else:
                numero_anillos = num_anillos
                total_anillos = 0
                anillos_hombres = 0
                anillos_elfos = 0
                anillos_enanos = 0
                continue
            
                
                          

# Pedir los anillos por consola
try:
    num_anillos = int(input("Introduce el número de anillos para repartir: "))
    distribucion_anillos(num_anillos)

except ValueError:
    print("No has introducido un número entero")

