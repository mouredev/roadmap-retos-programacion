'''
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
'''
import random

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(100):  
    enanos = random.choice([i for i in range(1, 20) if primo(i)])
    elfos = random.choice([i for i in range(1, 20, 2)])
    humanos = random.choice([i for i in range(2, 21, 2)])
    sauron = 1

    if enanos + elfos + humanos + sauron == 20:
        print(f'''
    Enanos -> {enanos}
    Elfos -> {elfos}
    Sauron -> {sauron}
    Humanos -> {humanos}''')
        break
else:
    print("No se encontró una combinación válida.")
