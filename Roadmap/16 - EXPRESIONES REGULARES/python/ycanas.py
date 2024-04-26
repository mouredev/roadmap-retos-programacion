import re

# ------ I. Ejercicio

def extract(text: str) -> list[int]:
    pattern: str = r"\d+"
    numbers: list[str] = re.findall(pattern, text)
    return [int(n) for n in numbers]


my_text: str = "hol4 a tod0s s0y un str1ng hell0 de numerb0s y l3tr45"
numbers: int = extract(my_text)

print(f"Números encontrados → {numbers}, total de números encontrados → {len(numbers)}")


# ------ II. Extra

def is_valid_email(email: str) -> bool:
    pattern: str = r"^[\w.-]+@\w+\.[a-z.]{2,}$"
    return bool(re.match(pattern, email))


def is_valid_number(cellnumber: str) -> bool:
    pattern: str = r"^\+\d{1,3}\s[\d\s]+$"
    return bool(re.match(pattern, cellnumber))


def is_valid_url(url: str) -> bool:
    pattern: str = r"^https?://(www.)?[\w/-]+\.[a-z]{2,}/?$"
    return bool(re.match(pattern, url))


print(is_valid_email("em4il.example@gmail.edu.co"))
print(is_valid_number("+57 311 567 8976"))
print(is_valid_url("https://github/io.co/"))
