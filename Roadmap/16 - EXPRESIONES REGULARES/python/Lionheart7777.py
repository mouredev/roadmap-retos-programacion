import re
# EJERCICIO

regex = r"\d+"  # \d equivale a [0-9] 

text = "Este es el ejercicio 16 publicado el 02/11/2026"

def find_numbers(text: str) -> list:
    return re.findall(regex, text)
    
print(find_numbers(text)) # ['16', '02', '11', '2026']

#EXTRA

def validate_email (email: str) -> bool:
    return bool(re.match(r"^[\w\.+-]+@[\w-]+(\.[\w-]+)$", email)) 

print(validate_email("kenbak220820@gmail.com"))


def validate_phone (phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone)) 

print(validate_phone("+51 9940 90 868"))


def validate_url (url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url)) 

print(validate_url("https://www.kenbak220820.dev"))