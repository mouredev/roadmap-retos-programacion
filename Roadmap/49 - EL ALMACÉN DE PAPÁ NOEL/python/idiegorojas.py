"""
# 49 - Almacen de papa noel
"""
# Crea un programa donde introducir códigos y obtener pistas.

# Código:
# El código es una combinación de letras y números aleatorios de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
# No hay repetidos.
# Se genera de manera aleatoria al iniciar el programa.

# Usuario:
# Dispone de 10 intentos para acertarlo.
# En cada turno deberá escribir un código de 4 caracteres, y el programa le indicará para cada uno lo siguiente:
    # Correcto: Si el caracter está en la posición correcta.
    # Presente: Si el caracter existe, pero esa no es su posición.
    # Incorrecto: Si el caracter no existe en el código secreto.
# Deben controlarse errores de longitud y caracteres soportados.

# Finalización:
# Papa Noel gana si descifra el código antes de 10 intentos.
# Pierde si no lo logra, ya que no podría entregar los regalos.

import random

# Generar código secreto aleatorio (4 caracteres sin repetición)
posibles_caracteres = ['A', 'B', 'C', '1', '2', '3']
codigo_secreto = ''.join(random.sample(posibles_caracteres, 4))

# Configurar número de intentos
intentos_maximos = 10
intentos_usados = 0
victoria = False

# Lista de caracteres válidos para validación
caracteres_validos = set(posibles_caracteres)

print("¡Bienvenido al Almacén de Papa Noel!")
print("Tienes que adivinar el código secreto para entrar.")
print("El código tiene 4 caracteres (letras A-C y números 1-3) sin repeticiones.")
print(f"Tienes {intentos_maximos} intentos para adivinarlo.")

# Bucle principal del juego
while intentos_usados < intentos_maximos and not victoria:
    intentos_usados += 1
    print(f"\nIntento {intentos_usados} de {intentos_maximos}")
    
    # Obtener y validar la entrada del usuario
    while True:
        intento = input("Ingresa tu código de 4 caracteres: ").upper()
        
        # Verificar longitud
        if len(intento) != 4:
            print("Error: El código debe tener exactamente 4 caracteres.")
            continue
        
        # Verificar caracteres válidos
        if not all(c in caracteres_validos for c in intento):
            print("Error: Solo se permiten letras A-C y números 1-3.")
            continue
        
        # Verificar que no haya repeticiones
        if len(set(intento)) != 4:
            print("Error: El código no debe contener caracteres repetidos.")
            continue
        
        break  # Si pasamos todas las validaciones, salimos del bucle
    
    # Analizar el intento
    resultado = []
    aciertos = 0
    
    for i in range(4):
        if intento[i] == codigo_secreto[i]:
            resultado.append("Correcto")
            aciertos += 1
        elif intento[i] in codigo_secreto:
            resultado.append("Presente")
        else:
            resultado.append("Incorrecto")
    
    # Mostrar resultado
    for i in range(4):
        print(f"Posición {i+1} ({intento[i]}): {resultado[i]}")
    
    # Verificar victoria
    if aciertos == 4:
        victoria = True

# Mensaje final
if victoria:
    print(f"\n¡FELICIDADES! Has descifrado el código secreto en {intentos_usados} intentos.")
    print("Papa Noel podrá entregar los regalos a tiempo.")
else:
    print(f"\nLo siento, has agotado tus {intentos_maximos} intentos.")
    print(f"El código secreto era: {codigo_secreto}")
    print("Papa Noel no podrá entregar los regalos este año.")