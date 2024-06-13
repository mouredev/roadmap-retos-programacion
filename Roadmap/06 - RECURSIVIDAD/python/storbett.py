# ejericio


def contador(number: int):
    
    if number >= 0:
        print (number)
        contador(number - 1)

contador(100)


"""
extra 
"""

def factorial (number: int) -> int:
    if number < 0:
        print("los numero negativos no son validos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial (number -1 )

print (factorial (5))


def fibonacci( number: int ) -> int:
    if number <= 0:
        print("la psicion tiene que ser mayor que cero")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci (number - 1) + fibonacci (number - 2)

print (fibonacci (-7))


def hanoi(n, origen, destino, auxiliar):
    # Paso base: si solo hay un disco, se mueve directamente al destino
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # Paso 1: Mover n-1 discos del origen al auxiliar, usando destino como auxiliar
    hanoi(n - 1, origen, auxiliar, destino)
    
    # Paso 2: Mover el disco n del origen al destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Paso 3: Mover n-1 discos del auxiliar al destino, usando origen como auxiliar
    hanoi(n - 1, auxiliar, destino, origen)

# Llamada a la función con 3 discos
hanoi(5, 'A', 'C', 'B')
