"""
/*
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
"""
def es_par(numero):
    if numero%2 == 0:
        return True
    else:
        return False

def es_primo(numero):
    es_primo = True
    if numero<2:
        return False
    for i in range(2, int(numero/2 + 1 )):
        if numero % i == 0:
            es_primo = False
    if es_primo:
        return True
    else:
        return False
    
def distribucion_anillos(anillos):
    sauron = 1
    anillos -= sauron
    distribuciones = []
    for hombres in range (2, anillos, 2):
        for elfos in range (1, anillos, 2):
            enanos = anillos - hombres - elfos
            if enanos > 0 and es_primo(enanos):
                distribuciones.append(
                    {
                        "Hombres": hombres, 
                        "Elfos": elfos,
                        "Enanos": enanos,
                        "Saruon": sauron
                    }
                )
    if distribuciones:
        return distribuciones
    else:
        return "No es posible repartir los anillos según las normas. "
try:    
    anillos_user = int(input("Introduce el número de anillos de poder a repartir: "))
    distribucion_user = distribucion_anillos(anillos_user)
    if isinstance(distribucion_user, list):
        for index, item in enumerate(distribucion_user):
            print(f"{index}. {item}")

        print(f"La distribución elegida/media es: \n {distribucion_user[int(len(distribucion_user)/2)]}")
    else:
        print(distribucion_user)
except ValueError:
    print("Introduce un número válido. ")