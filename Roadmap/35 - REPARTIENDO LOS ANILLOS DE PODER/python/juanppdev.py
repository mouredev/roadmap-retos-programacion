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

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def distribuir_anillos(total_anillos):
    if total_anillos < 4:
        return "No es posible distribuir los anillos con los requisitos dados."

    # Sauron siempre recibe uno
    sauron = 1
    total_anillos -= sauron

    # Distribuir los anillos restantes
    elfos = 0
    enanos = 0
    hombres = 0

    for i in range(1, total_anillos + 1):
        if i % 2 != 0:  # Número impar para los Elfos
            elfos += 1
        elif es_primo(i):  # Número primo para los Enanos
            enanos += 1
        else:  # Número par para los Hombres
            hombres += 1

    if elfos + enanos + hombres == total_anillos:
        return f"Reparto final: Elfos: {elfos}, Enanos: {enanos}, Hombres: {hombres}, Sauron: {sauron}"
    else:
        return "No es posible distribuir los anillos con los requisitos dados."

# Ejemplo de uso
total_anillos = 20
print(distribuir_anillos(total_anillos))
