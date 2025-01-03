import random

def generate_code():
    return ''.join(random.sample('ABC123', 4))

code = generate_code()
attempts = 10

print("¡Bienvenido! Tienes 10 intentos para descifrar el código.")

while attempts > 0:
    input_code = input(f"Intento #{attempts}. Ingresa un código de 4 caracteres: ").upper()

    if len(input_code) != 4 or not all(c in 'ABC123' for c in input_code):
        print("Código inválido. Debe tener 4 caracteres (letras A-C, números 1-3).")
        continue

    result = []
    for i, char in enumerate(input_code):
        if char == code[i]:
            result.append("Correcto")
        elif char in code:
            result.append("Presente")
        else:
            result.append("Incorrecto")

    print(", ".join(result))

    if input_code == code:
        print(f"¡Felicidades! Descifraste el código: {code}")
        break

    attempts -= 1

if attempts == 0:
    print(f"Lo siento, no lograste descifrar el código: {code}")
