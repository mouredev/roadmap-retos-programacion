import re

# Ejercicio


def find_numbers_in_string(text: str) -> list:
    regex = r"\d+"

    return re.findall(regex, text)


# Extra


def validate_email(email: str) -> bool:
    regex = r"^[\w_.+-]+@[\w-]+\.[a-zA-Z.]+$"
    return bool(re.match(regex, email))


def validate_phone_number(phone_number: str) -> bool:
    regex = r"^\+\d{2}\s{1}[\d{2}\s?\-?}]+$"
    return bool(re.match(regex, phone_number))


def validate_url(url: str) -> bool:
    regex = r"^(https?:\/\/)?((www.)?[a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})([\/\w .-]*)*\/?$"
    return bool(re.match(regex, url))


if __name__ == "__main__":
    text = "Este es el ejercicio 16 publicado el 15/04/2024"
    print(find_numbers_in_string(text))

    email = "mario.vidal-klm@midominio-1.com.mx"
    print(validate_email(email))
    phone = "+52 5523458970"

    url = "http://www.midominio.com.mx/sitio/mundo"
    print(validate_url(url))
