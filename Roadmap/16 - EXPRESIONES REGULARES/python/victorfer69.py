import re

#Ejercicio

regex = r"\d+"

text = "Este es el ejercicio 16 a fecha del 22 de enero de 2025."

def find_numbers(text:str) -> list:
    return re.findall(regex, text)

print(find_numbers(text))


#EJERCICIO EXTRA

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))


print(validate_email("qwert@sdf.com"))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))


print(validate_phone("+34 901 65 89 044"))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))


print(validate_url("http://www.moure.dev"))
