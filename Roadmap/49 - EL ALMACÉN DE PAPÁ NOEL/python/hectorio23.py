# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import random

def generate_secret_code():
    pool = ['A', 'B', 'C', '1', '2', '3']
    random.shuffle(pool)
    return ''.join(pool[:4])

def evaluate_guess(secret, guess):
    for i in range(4):
        if guess[i] == secret[i]:
            print(f"{guess[i]}: Correcto")
        elif guess[i] in secret:
            print(f"{guess[i]}: Presente")
        else:
            print(f"{guess[i]}: Incorrecto")

def is_valid_guess(guess):
    if len(guess) != 4:
        print("El código debe tener exactamente 4 caracteres.")
        return False

    valid_chars = {'A', 'B', 'C', '1', '2', '3'}
    for char in guess:
        if char not in valid_chars:
            print(f"Caracter inválido encontrado: {char}")
            return False

    return True

def main():
    secret_code = generate_secret_code()
    attempts = 10

    print("\n¡Bienvenido al juego del código secreto de Papá Noel!")
    print("Debes adivinar el código secreto de 4 caracteres.")
    print("Letras: A, B, C | Números: 1, 2, 3\n")

    while attempts > 0:
        print(f"\nIntentos restantes: {attempts}")
        guess = input("Introduce tu código: ").strip().upper()

        if not is_valid_guess(guess):
            continue

        if guess == secret_code:
            print(f"¡Felicidades! Has descifrado el código secreto: {secret_code}")
            return

        evaluate_guess(secret_code, guess)
        attempts -= 1

    print(f"\nLo siento, no has logrado descifrar el código secreto. Era: {secret_code}")

if __name__ == "__main__":
    main()
