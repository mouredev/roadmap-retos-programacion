import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
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
 * 2. Muestra el reparto final o el error al realizarlo."""

def prime_generator(num)->list:# Creamos una función que nos devuelva una lista de números primos  
    prime_list = []       #  hasta el número de anillos introducido
    for i in range(2, num + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            prime_list.append(i)                   
    return prime_list

while True:
    rings = input("\nEscriba el número de anillos a repartir: ")
    if not rings.isdigit() or int(rings) < 6: # Condicional para evitar que se introduzcan caracteres no numéricos o menores a 6
            print("Sólo se pueden introducir números a partir de 6, intente de nuevo")
            continue
    else:
            rings = int(rings) # Casteamos la cifra introducida a int 
            start_rings = rings # Guardamos un backup de esa cifra para imprimir al final

    adjust = rings//70 # Creamos una variable para dar más precisión a la cifra del número primo
    div = len(prime_generator(rings))//2 #Dividimos entre 2 redondeando a int para seleccionar un nº primo a la mitad del total
    if adjust == 0:
         adjust = 1
    if div == 1:
         div = 2
    dwarves = prime_generator(rings)[div-adjust-1] # Asignamos el nº primo restando la variable de ajuste según los anillos 
    sauron = 1                                   #  disponibles , 1 unidad por cada 50 anillos para hacer el reparto equitativo
    rings = rings - dwarves - sauron # Restamos la cantidad de anillos en nº primo de los enanos y el anillo fijo de Saurom

    if rings % 2 == 0: # Si lo que queda es par asignamos justo la mitad a los hombres y la otra mitad menos 1 a los elfos
        men = rings / 2
        elves = men - 1
        if men % 2 != 0: # Comprobamos de nuevo por si tras la división anterior hubiera resultado impar
            elves = men  # y le hubiéramos asignado una cifra impar a los hombres, se la asignamos a los elfos
            men += 1 # y le asignamos ese valor mas 1 a los hombres
        
    else:
        men = (rings-1) / 2 # Si es impar le quitamos 1 al total y dividimos entre 2 para los hombres 
        elves = men + 1 #  y el resto mas el que hemos restado antes se lo asignamos a los elfos
        if men % 2 != 0: # Comprobamos de nuevo por si tras la división anterior hubiera vuelto a dar impar
            elves = men   # y le hubiéramos asignado una cifra impar a los hombres, se la asignamos a los elfos
            men += 1 # y le asignamos ese valor mas 1 a los hombres 
        
    rings = rings - men - elves
    if rings < 0:#Condicionamos para que no se asignen más anillos de los disponibles
        men -= 2
        rings += 2
    elif rings == 2:# ni sobren 2 en cuyo caso se los asignamos a los elfos
        elves += 2
        rings -=2 

    print (f"""De los {start_rings} anillos se han repartido {sauron} para Sauron, {int(elves)} para los elfos, {int(dwarves)} para los enanos y {int(men)} para los hombres""")
    print ("Anillos sobrantes: ",int(rings))
    print()
    break



