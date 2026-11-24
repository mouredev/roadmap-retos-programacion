import re

"""
    REGULAR EXPRESSIONS
"""


def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)  # Just int
    return re.findall(r"\d+\.?\d*", text)  # Decimal included


text = "In 2026 I wrote 3.5 hours of code across 16 exercises and fixed 42 bugs."
print(f"Numbers found: {find_numbers(text)}")


"""
    EXTRA EXERCISE
"""


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$", email))


def validate_phone(phone: str) -> bool:
    # Accepts: +44 7700 900077 / 07700 900077 / +1-800-555-0199
    return bool(re.match(r"^\+?[\d\s\-().]{7,15}$", phone))


def validate_url(url: str) -> bool:
    # Accepts http/https, optional www, domain with path/query
    return bool(
        re.match(r"^https?://(www\.)?[\w-]+(\.[\w-]+)+([\w.,@?^=%&:/~+#\-_]*)?$", url)
    )


emails = [
    "sergio@example.com",
    "sergio.cardo+test@gmail.co.uk",
    "not-an-email@",
    "@nodomain.com",
]

phones = [
    "+44 7700 900077",
    "07700 900077",
    "+1-800-555-0199",
    "123",
    "not a phone",
]

urls = [
    "https://www.github.com",
    "http://github.com/elhdrond",
    "https://roadmap.sh/python",
    "ftp://invalid.com",
    "not a url",
]

print("\n--- Email validation ---")
for email in emails:
    print(f"  {email:<35} {'✓' if validate_email(email) else '✗'}")

print("\n--- Phone validation ---")
for phone in phones:
    print(f"  {phone:<25} {'✓' if validate_phone(phone) else '✗'}")

print("\n--- URL validation ---")
for url in urls:
    print(f"  {url:<35} {'✓' if validate_url(url) else '✗'}")
