import random

letters = ["A", "B", "C"]
numbers = ["1", "2", "3"]
password_elements = letters + numbers


def generate_password() -> str:
    return "".join(random.sample(password_elements, 4))


secret_password = generate_password()
attempts = 1

print("Adivina la contraseña del almacén de Papá Noel.")

while attempts <= 10:

    print(f"Intento: {attempts}")

    password = input("Introduce la contraseña: ").upper()

    if len(password) != 4:
        print("Error: La contraseña debe tener 4 caracteres.")
        continue
    if not all(character in password_elements for character in password):
        print(f"Error: Sólo se permiten los caracteres {password_elements}.")
        continue

    if password == secret_password:
        print("¡Contraseña correcta! Has descifrado el código del almacén. Feliz Navidad.")
        break

    attempts += 1

    if attempts > 10:
        print("Lo siento, los 10 intentos para descifrar el código han finalizado.")
        print("Papá Noel no ha podido entregar los regalos.")
    else:
        for index, character in enumerate(password):
            if character == secret_password[index]:
                print(f"{character}: Correcto")
            elif character in secret_password:
                print(f"{character}: Presente")
            else:
                print(f"{character}: Incorrecto")
