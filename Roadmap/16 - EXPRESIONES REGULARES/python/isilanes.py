import re

TEXT = """
This is 1 funny text with 2 or 3 numbers, but not 1000 numbers,
because more than 999.9 numbers are too much. Numb3rs c4n appear 1ns1de
words, and be fl0.4ts"""
EXPECTED_NUMBERS = [1, 2, 3, 1000, 999.9, 3, 4, 1, 1, 0.4]


def extract_numbers(text: str) -> list[int]:
    pattern = re.compile(r"\d+\.?\d*")
    match = pattern.findall(text) or []
    return [float(n) if "." in n else int(n) for n in match]


def main(text: str, expected: list[int]) -> None:
    numbers = extract_numbers(text)
    assert numbers == expected
    print("Todos los números se extrajeron.")
    print("Texto:", text)
    print("Números:", numbers)


if __name__ == "__main__":
    main(text=TEXT, expected=EXPECTED_NUMBERS)
