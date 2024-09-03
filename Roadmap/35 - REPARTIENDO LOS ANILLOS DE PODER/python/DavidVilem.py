import math

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def distribuir_anillos(total_anillos):
    if total_anillos < 4:
        return "Error: No es posible repartir los anillos con las reglas dadas."
    
    anillos_distribuidos = {
        "Elfos": [],
        "Enanos": [],
        "Hombres": [],
        "Sauron": [total_anillos]
    }

    total_anillos -= 1
    numero_actual = 0
    numeros_asignados = set()

    # Asignar los anillos en ciclos hasta que se acaben
    while total_anillos > 0:
        cambios_realizados = False

        # Asignar a los Elfos (impar)
        if total_anillos > 0 and numero_actual % 2 != 0:
            anillos_distribuidos["Elfos"].append(numero_actual)
            numeros_asignados.add(numero_actual)
            total_anillos -= 1
            cambios_realizados = True

        # Incrementar al siguiente número
        numero_actual += 1

        # Asignar a los Enanos (primo)
        if total_anillos > 0 and es_primo(numero_actual):
            anillos_distribuidos["Enanos"].append(numero_actual)
            numeros_asignados.add(numero_actual)
            total_anillos -= 1
            cambios_realizados = True

        # Incrementar al siguiente número
        numero_actual += 1

        # Asignar a los Hombres (par)
        if total_anillos > 0 and numero_actual % 2 == 0:
            anillos_distribuidos["Hombres"].append(numero_actual)
            numeros_asignados.add(numero_actual)
            total_anillos -= 1
            cambios_realizados = True

        # Incrementar al siguiente número
        numero_actual += 1

        # Si no se realizaron cambios en un ciclo, detener el proceso
        if not cambios_realizados:
            break

    return anillos_distribuidos

def formatear_salida(anillos_distribuidos):
    for raza, numeros in anillos_distribuidos.items():
        cantidad = len(numeros)
        numeros_asignados = ', '.join(map(str, numeros))
        print(f"Raza: {raza}, Cantidad: {cantidad}, Números: {numeros_asignados}")

if __name__ == "__main__":
    total_anillos = int(input("Introduce el número total de anillos a distribuir: "))
    resultado = distribuir_anillos(total_anillos)
    formatear_salida(resultado)
