# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def distribute_rings(total_rings):
    # Sauron always gets one ring
    sauron_rings = 1
    remaining_rings = total_rings - sauron_rings
    
    # We need at least 1 ring for each race
    for elves_rings in range(1, remaining_rings, 2):  # Elves get an odd number
        for dwarves_rings in range(2, remaining_rings):
            if is_prime(dwarves_rings):  # Dwarves get a prime number
                humans_rings = remaining_rings - elves_rings - dwarves_rings
                if humans_rings > 0 and humans_rings % 2 == 0:  # Humans get an even number
                    return {
                        "Elves": elves_rings,
                        "Dwarves": dwarves_rings,
                        "Humans": humans_rings,
                        "Sauron": sauron_rings
                    }

    return "Error: No valid distribution found."

# Example usage
total_rings = 20
result = distribute_rings(total_rings)
print(result)
