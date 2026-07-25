#35 { Retos para Programadores } REPARTIENDO LOS ANILLOS DEL PODER 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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

log = print

import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if num <= 3:
        return True  # 2 and 3 are prime numbers
    if num % 2 == 0 or num % 3 == 0:
        return False  # Eliminate even numbers and multiples of 3

    # Check for factors from 5 to the square root of num
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False  # Check i and i + 2
    return True  # If no factors were found, num is prime

# Function to find the largest prime number less than a given number
def first_prime(num):
    for i in range(num - 1, 1, -1):
        if is_prime(i):
            return i  # Return the first prime found
    return 2  # Return 2 if no prime found (should not happen for valid input)

def is_odd(num):
    return num % 2 != 0  # Return true if the number is odd

# Function to assign rings based on the rules
def assign_rings(num):
    # Check if the number of rings is odd and greater than or equal to 7
    if not is_odd(num) or num < 7:
        log('The number of rings must be an odd number and greater than or equal to 7')
        start()  # Prompt for input again
        return

    arr_of_rings = [0, 0, 0, 1]  # Sauron always gets 1 ring
    f_prime = first_prime(num)  # Find the largest prime less than num
    r = num - f_prime  # Remaining rings after giving to Dwarves

    # Adjust remaining rings if less than 4
    if r < 4:
        f_prime = first_prime(num - 3)
        r = num - f_prime 

    # Distribute rings based on the remaining count
    if r == 4:
        arr_of_rings[0] = (r // 2) - 1  # Elves
        arr_of_rings[1] = f_prime        # Dwarves
        arr_of_rings[2] = r // 2          # Men
    elif r == 6:
        arr_of_rings[0] = (r - 1) // 2  # Elves
        arr_of_rings[1] = f_prime        # Dwarves
        arr_of_rings[2] = (r - 1) // 2  # Men
    elif r == 8:
        arr_of_rings[0] = (r - 1) // 2  # Elves
        arr_of_rings[1] = f_prime        # Dwarves
        arr_of_rings[2] = (r - 1) // 2  # Men
    else:
        # Alternative distribution logic for other values of r
        alternative_distribution(arr_of_rings, f_prime, r)

    # Output the distribution of rings
    log(f'\n{arr_of_rings[0]} rings to: Elves, {arr_of_rings[1]} rings to: Dwarves, '
          f'{arr_of_rings[2]} rings to: Men, and {arr_of_rings[3]} ring to: Sauron')

# Function for alternative distribution logic
def alternative_distribution(arr_of_rings, f_prime, r):
    # Dwarves get the prime
    arr_of_rings[1] = f_prime  # Dwarves
    arr_of_rings[3] = 1  # Sauron gets 1 ring

    # Calculate remaining rings after assigning to Dwarves and Sauron
    remaining_for_elves_and_men = r - arr_of_rings[3]  # Only subtract Sauron's ring

    # Ensure Elves get an odd number and Men get an even number
    if is_odd(remaining_for_elves_and_men):
        arr_of_rings[0] = max(1, (remaining_for_elves_and_men + 1) // 2)  # Ensure Elves get an odd number
        arr_of_rings[2] = remaining_for_elves_and_men - arr_of_rings[0]  # Calculate remaining rings for Men
    else:
        log("It's not possible to do the distribution according to the rules.")

# Function to start the input process
def start():
    total_rings = input('Indicate the number of rings to distribute: ')
    try:
        total_rings = int(total_rings)
        assign_rings(total_rings)
    except ValueError:
        log('Please enter a valid number.')  # Prompt for valid input
        start()  # Prompt again for valid input

# Start the program
if __name__ == "__main__":
    start()

# Output Example:
"""   
Indicate the number of rings to distribute: 102
The number of rings must be an odd number and greater than or equal to 7
Indicate the number of rings to distribute: 103

2 rings to: Elves, 97 rings to: Dwarves, 2 rings to: Men, and 1 ring to: Sauron

"""