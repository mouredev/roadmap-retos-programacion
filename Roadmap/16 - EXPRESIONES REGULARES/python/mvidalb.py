import re

"""
Ejercicio
"""

def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)

text = "Este es el ejercicio 16 publicado el 15/04/2024."
print(find_numbers(text))


"""
Ejercicio extra
"""
email = "mario.vidal@gmail.com"
number = "+34 654 32 13 21"
url = "https://www.retosdeprogramacion.com"


def validate_email(email : str) -> bool:
    return bool(re.match(r"^[\w.+-]{5,15}@[\w]+\.[a-zA-Z]{2,4}$", email))


def validate_number(number : str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", number))


def validate_url(url : str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,3}$", url))

print(validate_email(email))
print(validate_number(number))
print(validate_url(url))

