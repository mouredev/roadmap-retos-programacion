import re


# -- exercise
def extract_numbers(text: str) -> list:
    return re.findall(r"\d+", text)


any_text: str = "in the year 2024, the number 42 is the answer to everything."
print(extract_numbers(any_text))


# -- extra challenge
def validate_email(email: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?(\d{1,3})?\s?(\d{10})$", phone))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", url))


print(validate_email("qwikzgheib@gmail.com"))
print(validate_phone("+1234567890"))
print(validate_url("https://www.google.com"))
