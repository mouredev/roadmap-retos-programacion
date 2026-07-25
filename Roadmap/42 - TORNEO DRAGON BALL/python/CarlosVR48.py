import random

"""
EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador."""


"""
Yamcha , Jackie Chun , Krilin , Bacterian
Giran , Son Goku , Ranfan , Namu
"""
def esquivar_20(velocidad):
    # Calculamos numero entre 0 y 100. Como el 20% de 100 es 20 , si el numero que tiene esquivar_20 es menor
    # o igual a 20 , entoces esquiva el golpe. Retornamos un True
    esquivar_20 = random.randint(0,100)
    if esquivar_20 <= 20:
        return True
    else:
        return False

def luchar_1(tatami1_1,tatami1_2,tatami):
    # recupero la salud y la velocidad de los datos el diccionario, de cada luchador
    salud1 = int(luchadores[tatami1_1].get("Salud"))
    salud2 = int(luchadores[tatami1_2].get("Salud"))
    velocidad1 = luchadores[tatami1_1].get("Velocidad")
    velocidad2 = luchadores[tatami1_2].get("Velocidad")
    
    print (f"\nTATAMI {tatami}:\n {luchadores[tatami1_1].get("Nombre")} contra {luchadores[tatami1_2].get("Nombre")}")
    print (f" SALUD: {salud1}      SALUD: {salud2}")

    # el ataque primero es dependido de mayor velocidad
    if velocidad1 > velocidad2:
        primero = 1
        # Hay un 20% de posibilidades de esquivar el ataque con la velocidad del defensor.
        # True se guarda en esquivar si el 20% de velocidad es mayor a un numero aleatorio de velocidad
        esquivar = esquivar_20(velocidad2)

        if esquivar == False:
            # Si la defensa es mayor que el ataque se calculara un 10% de daño 
            if (luchadores[tatami1_2].get("Defensa")) > (luchadores[tatami1_1].get("Ataque")):
                salud2 = int(salud2 - -((luchadores[tatami1_1].get("Ataque") -  luchadores[tatami1_2].get("Defensa"))*10)/100)
                print (f"\n {luchadores[tatami1_1].get("Nombre")} GOLPEA A {luchadores[tatami1_2].get("Nombre")}")
            else:    
                salud2 = int(salud2 - (luchadores[tatami1_1].get("Ataque") -  luchadores[tatami1_2].get("Defensa")))
                print (f"\n {luchadores[tatami1_1].get("Nombre")} GOLPEA A {luchadores[tatami1_2].get("Nombre")}")
        else:
            print (f"\n  {luchadores[tatami1_2].get("Nombre")} ESQUIVA EL GOLPE")            

    else:
        primero = 2
        esquivar = esquivar_20(velocidad1)
        
        if esquivar == False:
            if (luchadores[tatami1_1].get("Defensa")) > (luchadores[tatami1_2].get("Ataque")):
                salud1 = int(salud1 - -((((luchadores[tatami1_2].get("Ataque") -  luchadores[tatami1_1].get("Defensa")))*10)/100))
                print (f"\n {luchadores[tatami1_2].get("Nombre")} GOLPEA A {luchadores[tatami1_1].get("Nombre")}")
            else:    
                salud1 = int(salud1 - (luchadores[tatami1_2].get("Ataque") -  luchadores[tatami1_1].get("Defensa")))
                print (f"\n {luchadores[tatami1_2].get("Nombre")} GOLPEA A {luchadores[tatami1_1].get("Nombre")}")
        else:
            print (f"\n {luchadores[tatami1_1].get("Nombre")} ESQUIVA EL GOLPE") 
    
    print (f"\n {luchadores[tatami1_1].get("Nombre")}--------{luchadores[tatami1_2].get("Nombre")}")
    print (f" SALUD: {salud1}      SALUD: {salud2}")
    #el valor de salud cambia y lo escribo en cada valor asignado
    luchadores[tatami1_1]["Salud"]=salud1
    luchadores[tatami1_2]["Salud"]=salud2
    return primero

def luchar_2(primero,tatami1_1,tatami1_2):
    ronda = int()
    salud1 = int(luchadores[tatami1_1].get("Salud"))
    salud2 = int(luchadores[tatami1_2].get("Salud"))
    #bucle repetitivo asta que el valor de salud de un luchador es igual o menor que 0
    while True:
        velocidad1 = luchadores[tatami1_1].get("Velocidad")
        velocidad2 = luchadores[tatami1_2].get("Velocidad")
        
        if primero == 1:
            if salud2<=0:
                #asigno al ganador 100 de salud
                luchadores[tatami1_1]["Salud"] = 100
                ronda=tatami1_1
                break
            esquivar = esquivar_20(velocidad1)
            primero = 2
            if esquivar == False:
                if (luchadores[tatami1_1].get("Defensa")) > (luchadores[tatami1_2].get("Ataque")):
                    print (f"\n {luchadores[tatami1_2].get("Nombre")} GOLPEA A {luchadores[tatami1_1].get("Nombre")}")
                    salud1 = int(salud1 - -((((luchadores[tatami1_2].get("Ataque") -  luchadores[tatami1_1].get("Defensa")))*10)/100))
                else:    
                    print (f"\n {luchadores[tatami1_2].get("Nombre")} GOLPEA A {luchadores[tatami1_1].get("Nombre")}")
                    salud1 = int(salud1 - (luchadores[tatami1_2].get("Ataque") -  luchadores[tatami1_1].get("Defensa")))
            else:
                print (f"\n {luchadores[tatami1_1].get("Nombre")} ESQUIVA EL GOLPE")
        else:   
            if salud1<=0:
                luchadores[tatami1_2]["Salud"] = 100
                ronda=tatami1_2
                break
            primero = 1
            esquivar = esquivar_20(velocidad2)

            if esquivar == False:
                #Si la defensa es mayor que el ataque se calculara un 10% de daño 
                if (luchadores[tatami1_2].get("Defensa")) > (luchadores[tatami1_1].get("Ataque")):
                    print (f"\n {luchadores[tatami1_1].get("Nombre")} GOLPEA A {luchadores[tatami1_2].get("Nombre")}")
                    salud2 = int(salud2 - -((luchadores[tatami1_1].get("Ataque") -  luchadores[tatami1_2].get("Defensa"))*10)/100)
                else:    
                    print (f"\n {luchadores[tatami1_1].get("Nombre")} GOLPEA A {luchadores[tatami1_2].get("Nombre")}")
                    salud2 = int (salud2 - (luchadores[tatami1_1].get("Ataque") -  luchadores[tatami1_2].get("Defensa")))
            else:
                print (f"\n {luchadores[tatami1_2].get("Nombre")} ESQUIVA EL GOLPE") 
        
        print (f"\n {luchadores[tatami1_1].get("Nombre")}--------{luchadores[tatami1_2].get("Nombre")}")
        print (f" SALUD: {salud1}      SALUD: {salud2}")
    return ronda

luchadores = [
            {"Nombre":"Son Goku","Velocidad": 95,"Ataque": 95,"Defensa": 91,"Salud": 100},
            {"Nombre":"Jackie Chun","Velocidad": 90,"Ataque": 95,"Defensa": 96,"Salud": 100},
            {"Nombre":"Yamcha","Velocidad": 92,"Ataque": 86,"Defensa": 85,"Salud": 100},
            {"Nombre":"Krilin","Velocidad": 88,"Ataque": 89,"Defensa": 93,"Salud": 100},
            {"Nombre":"Bacterian","Velocidad": 77,"Ataque": 95,"Defensa": 89,"Salud": 100},
            {"Nombre":"Giran","Velocidad": 77,"Ataque": 82,"Defensa": 88,"Salud": 100},
            {"Nombre":"Ranfan","Velocidad": 89,"Ataque": 88,"Defensa": 93,"Salud": 100},
            {"Nombre":"Namu","Velocidad": 69,"Ataque": 81,"Defensa": 92,"Salud": 100}]

#en estas listas se insertaran los ganadores de cada ronda
ronda2 = []
ronda3 = []
ronda4 = []
# creo una lista numerada con todo los participantes
lista = [0,1,2,3,4,5,6,7]
# Desordeno la lista para luego crear el soteo 
random.shuffle(lista)

tatami1_1 = lista[0] 
tatami1_2 = lista[1] 
tatami2_1 = lista[2]
tatami2_2 = lista[3]
tatami3_1 = lista[4]
tatami3_2 = lista[5]
tatami4_1 = lista[6]
tatami4_2 = lista[7]

print("                                               ------- GRAN TORNEO DE ARTES MARCIALES -------\n")

# Muestra todos los participantes y su ficha
for index in luchadores:
    print (index)
input("PULSA ENTER PARA CONTINUAR")

#llamamos a la funcion que se encarga de que luche primero el de mayor velocidad y asigna a primero el que ya ha dado golpe
tatami=1
primero = luchar_1(tatami1_1,tatami1_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
#una vez tenemos la sequencia de lucha guardada en la variable primero, continuamos y se guarda el ganador ronda2(lista)
ronda = luchar_2(primero,tatami1_1,tatami1_2)
ronda2.append(ronda)
luchador = ronda
print (f"\n--- EL GANADOR ES {luchadores[luchador].get("Nombre")} ---")
input("PULSA ENTER PARA CONTINUAR")

tatami = 2
primero = luchar_1(tatami2_1,tatami2_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
ronda = luchar_2(primero,tatami2_1,tatami2_2)
ronda2.append(ronda)
luchador = ronda
print (f"\n--- EL GANADOR ES {luchadores[luchador].get("Nombre")} ---")
input("PULSA ENTER PARA CONTINUAR")

tatami = 3
primero = luchar_1(tatami3_1,tatami3_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
ronda = luchar_2(primero,tatami3_1,tatami3_2)
ronda2.append(ronda)
luchador = ronda
print (f"\n--- EL GANAADOR ES {luchadores[luchador].get("Nombre")} ---")
input("PULSA ENTER PARA CONTINUAR")

tatami = 4
primero = luchar_1(tatami4_1,tatami4_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
ronda = luchar_2(primero,tatami4_1,tatami4_2)
ronda2.append(ronda)
luchador = ronda
print (f"\n--- EL GANADOR ES {luchadores[luchador].get("Nombre")} ---\n")
input("PULSA ENTER PARA CONTINUAR")
print (f"\n- CLASIFICADOS PARA LA SEMIFINAL:\n    {luchadores[ronda2[0]].get("Nombre")}\n    {luchadores[ronda2[1]].get("Nombre")}\n    {luchadores[ronda2[2]].get("Nombre")}\n    {luchadores[ronda2[3]].get("Nombre")} \n")

# Semifinal
# Ahora es una lucha de 4 participante y todo es igual que lo anterior
for index in ronda2:
    print(luchadores[index])

input("PULSA ENTER PARA CONTINUAR")    
tatami1_1 = ronda2 [0]
tatami1_2 = ronda2 [1]
tatami2_1 = ronda2 [2]
tatami2_2 = ronda2 [3]

tatami = 1
primero = luchar_1(tatami1_1,tatami1_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
ronda = luchar_2(primero,tatami1_1,tatami1_2)
ronda3.append(ronda)
luchador_semifinal = ronda
print (f"\n--- EL GANADOR ES {luchadores[luchador_semifinal].get("Nombre")} ---")
input("PULSA ENTER PARA CONTINUAR")

tatami = 2
primero = luchar_1(tatami2_1,tatami2_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
ronda = luchar_2(primero,tatami2_1,tatami2_2)
ronda3.append(ronda)
luchador_semifinal = ronda
print (f"\n--- EL GANADOR ES {luchadores[luchador_semifinal].get("Nombre")} ---")
input("PULSA ENTER PARA CONTINUAR")
print (f"\n- CLASIFICADOS PARA LA FINAL:\n    {luchadores[ronda3[0]].get("Nombre")}\n    {luchadores[ronda3[1]].get("Nombre")}\n") 

# Final 
for index in ronda3:
    print(luchadores[index])

input("PULSA ENTER PARA CONTINUAR")
    
tatami1_1 = ronda3 [0]
tatami1_2 = ronda3 [1]

tatami = 1
primero = luchar_1(tatami1_1,tatami1_2,tatami)
input("PULSA ENTER PARA CONTINUAR")
ronda = luchar_2(primero,tatami1_1,tatami1_2)
ronda4.append(ronda)
luchador_final = ronda
print (f"\n---EL VENCEDOR DEL GRAN TORNEO DE ARTES MARCIALES ES {luchadores[luchador_final].get("Nombre")}!!!!! ---")
input("PULSA ENTER PARA CONTINUAR")