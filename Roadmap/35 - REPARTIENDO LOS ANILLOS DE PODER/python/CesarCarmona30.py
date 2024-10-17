import math

def is_prime(num):
    if num <= 1 or (num % 2 == 0 and num > 2):
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

def prime_below_half(n):
    for i in range(n-1, 1, -1):
        if is_prime(i):
            return i
    return 2 

def distribute_rings(rings):
    if rings < 6:
        return "No hay suficientes anillos para repartir, deben ser por lo menos 6."
    
    half = rings // 2
    dwarves = prime_below_half(half)
    sauron = 1
    remaining = rings - dwarves - sauron  
    
    elves = (remaining // 2) | 1  
    men = remaining - elves 
    
    return f'''Anillos totales: {rings}
    Cantidad por grupo:
      Elfos   - {elves}
      Enanos  - {dwarves}
      Hombres - {men}
      Sauron  - {sauron}
    '''

# Usage examples
print(distribute_rings(4))
print(distribute_rings(5))
print(distribute_rings(6))
print(distribute_rings(10))
print(distribute_rings(20))
print(distribute_rings(30))
print(distribute_rings(40))
print(distribute_rings(97))
