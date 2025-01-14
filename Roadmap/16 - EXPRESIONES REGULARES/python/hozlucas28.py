import re
from typing import TypedDict

"""
    Regular expressions...
"""

print("Regular expressions...")

TEXT: str = "¡Hola Mundo! Hoy es 15/04/2024. Quedan 263 días para terminar el año 2024."
numbers: str = "".join(element for element in re.findall(r"[0-9]", TEXT))

print(f"\n{TEXT = }")

print(f"\nNumbers inside `TEXT` --> {numbers}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")

RegularExpressions = TypedDict(
    "RegularExpressions",
    {
        "email": str,
        "phone_number": str,
        "url": str,
    },
)

regular_expressions: RegularExpressions = {
    "email": r"^[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-zA-Z]{2,3}$",
    "phone_number": r"^\+[0-9]{1,4} [0-9]{4} [0-9]{4}$",
    "url": r"^https?://([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.[a-zA-Z]{2,3}/?$",
}

EMAILS: list[str] = [
    "hozlucas28@gmail.com",
    "hozlucas28@dev.com",
    "hozlucas-28@hotmail.com",
    "hozlucas28@melí.com",
    "hozlucas28@edu.com",
]

PHONE_NUMBERS: list[str] = [
    "+12 3456 7890",
    "+1 1234 5890",
    "+1234 1234 5690",
    "+123456789",
    "+123456789 1234 5678",
]

URLS: list[str] = [
    "https://www.example.cóm",
    "http://example.com",
    "https://subdomain.example.com",
    "http://www.example.c2.uk",
    "https://www.example.org",
]

print("\nEmails...")
for email in EMAILS:
    is_valid: bool = len(re.findall(regular_expressions["email"], email)) > 0
    print(f"Is '{email}' a valid email? {is_valid}")

print("\nPhone numbers...")
for phone_number in PHONE_NUMBERS:
    is_valid: bool = (
        len(re.findall(regular_expressions["phone_number"], phone_number)) > 0
    )
    print(f"Is '{phone_number}' a valid phone number? {is_valid}")

print("\nUrls...")
for url in URLS:
    is_valid: bool = len(re.findall(regular_expressions["url"], url)) > 0
    print(f"Is '{url}' a valid url? {is_valid}")
