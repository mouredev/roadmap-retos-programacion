#49 { Retos para Programadores } ALMACEN DE PAPÁ NOEL 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.

"""

log = print

import random
import re

# Function to generate a random code
def generate_code():
    characters = ['A', 'B', 'C', '1', '2', '3']
    code_set = set()

    while len(code_set) < 4:
        random_character = random.choice(characters)
        code_set.add(random_character)

    return ''.join(code_set)

# Function to provide feedback on the user's guess
def provide_feedback(secret_code, user_guess):
    feedback = {
        'correct': 0,
        'present': 0,
        'incorrect': 0
    }

    checked_indices = set()
    guess_checked = [False] * len(user_guess)

    # Check for correct positions
    for i in range(len(secret_code)):
        if user_guess[i] == secret_code[i]:
            feedback['correct'] += 1
            checked_indices.add(i)
            guess_checked[i] = True

    # Check for present characters
    for i in range(len(user_guess)):
        if not guess_checked[i]:
            for j in range(len(secret_code)):
                if user_guess[i] == secret_code[j] and j not in checked_indices:
                    feedback['present'] += 1
                    checked_indices.add(j)
                    guess_checked[i] = True
                    break

    # Calculate incorrect characters
    feedback['incorrect'] = len(user_guess) - feedback['correct'] - feedback['present']

    return feedback

def start_game():
    secret_code = generate_code()
    attempts = 10
    game_won = False

    log("Welcome to the Secret Code Game!")
    log("You have 10 attempts to guess the 4-character code.")
    log("The code consists of letters (A, B, C) and numbers (1, 2, 3) without repetitions.")

    def ask_for_guess():
        nonlocal attempts, game_won
        user_guess = input(f"You have {attempts} attempts left. Enter your guess (4 characters): ")

        # Validate input
        if len(user_guess) != 4 or not re.match(r'^[A-C1-3]+$', user_guess):
            log("Invalid input. Please enter exactly 4 characters using A, B, C, 1, 2, or 3.")
            ask_for_guess()  # Ask again
            return

        feedback = provide_feedback(secret_code, user_guess)
        log(f"Feedback: Correct: {feedback['correct']}, Present: {feedback['present']}, Incorrect: {feedback['incorrect']}")

        if feedback['correct'] == 4:
            game_won = True
            log("Congratulations! You've guessed the secret code!")
            return

        attempts -= 1
        if attempts > 0:
            ask_for_guess()  # Ask for the next guess
        else:
            log(f"Sorry, you've run out of attempts. The secret code was: {secret_code}")

    ask_for_guess()

start_game()

