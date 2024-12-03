from random import randint

def is_prime(number:int):
    if number ==1:
        return False
    else:
        for index in range(2,int(number**0.5)+1):
            if number % index == 0:
                return False
    return True
    
def is_odd(number:int):
    return number % 2 != 0

THE_ONE_RING = 1

def repartir_anillos(rings: int):
        
    if rings <= 5:
        return "No hay suficientes anillos para repartir"
    
    sauron = THE_ONE_RING
    while True:
            rings_aux = rings-sauron
            men = randint(1, rings_aux//2) *2
            rings_aux -= men
            if rings_aux >= 3:
                    dwarven = randint(1,rings_aux)
                    if is_prime(dwarven):
                        rings_aux -= dwarven
                        if rings_aux > 0:
                            elven = rings_aux
                            if is_odd(elven):
                                if sauron+men+dwarven+elven == rings:
                                    print("LOS ANILLOS SE HAN REPARTIDO CORRECTAMENTE")
                                    return f"TOTAL DE ANILLOS: {rings}\n- SAURON: {sauron}\n- HOMBRES: {men}\n- ENANOS: {dwarven}\n- ELFOS: {elven}"


if __name__ == "__main__":
    rings = int(input("Dime el número de Anillos de Poder a Repartir: "))
    resultado = repartir_anillos(rings)
    print(resultado)
