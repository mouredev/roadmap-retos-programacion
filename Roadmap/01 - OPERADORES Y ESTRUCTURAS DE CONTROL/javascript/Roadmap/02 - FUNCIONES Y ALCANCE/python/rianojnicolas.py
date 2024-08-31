import random

# Variable global y funcion ya creada por el lenguaje
variableGlobal = "Paso por aca, a desearte muchos exitos!!!\n"
variableGlobal = variableGlobal.upper()

# (Funcion sin parametros ni retorno)
# Funcion de bienvenida
def welcomePlayer():
    print("""
        Hola People !!, este es un juego improvisado de
        piedra, papel o tijera.
        
        las reglas son las siguientes:
        """)
    # Funcion dentro de otra funcion
    def reglas():
        print("""
            1. Debes ingresar el objeto con el que jugaras
            2. El pc elegira aleatoriamente un objeto
            3. Recuerda que: papel le gana a piedra,
                            piedra le gana a tijera,
                            tijera le gana a papel.
            
            Muchos Exitooooss !!!
            """)
    reglas()


# Funcion sin parametros con retorno
# Funcion para pedir el objeto a jugar
def functionInput():
    option = input("Ingresa tu objeto con el que vas a jugar: ")
    while(option != "piedra" and option != "tijera" and option != "papel"):
        option = input("Ingresa tu objeto con el que vas a jugar: ")
    return option


# (Funcion con un parametro y sin retorno)
# Funcion competencia
def playCompetition(optionPlayer):
    # Concepto de Variable Local
    optionList = ["piedra", "papel", "tijera"]
    optionPC = random.choice(optionList)
    print(f'la opcion del pc fue: {optionPC}\n')
    if (optionPC == optionPlayer):
        print("Emptados")
    elif (optionPC == "papel"):
        if (optionPlayer == "piedra"):
            print("perdiste")
        elif(optionPlayer == "tijera"):
            print("ganaste")
    elif(optionPC == "tijera"):
        if (optionPlayer == "papel"):
            print("perdiste")
        elif (optionPlayer == "piedra"):
            print("ganaste")
    elif(optionPC == "piedra"):
        if (optionPlayer == "papel"):
            print("ganaste")
        elif (optionPlayer == "tijera"):
            print("perdiste")


def run():
    welcomePlayer()
    print(variableGlobal)
    option_player = functionInput()
    playCompetition(option_player)


def extraDifficult(param1, param2):
    contador = 0
    for i in range(0,101):
        if (i%3 == 0 and i%5 == 0):
            print(f'para el numero {i}: {param1} {param2}')
        elif(i%3 == 0):
            print(f'para el numero {i}: {param1}')
        elif(i%5 == 0):
            print(f'para el numero {i}: {param2}')
        else:
            contador += 1
            print(f'para el numero {i} no hay texto')
    return contador


if __name__ == '__main__':
    run()
    print("\nAhora vamos con el ejercicio extra\n")
    print(extraDifficult("hola","mundo"))