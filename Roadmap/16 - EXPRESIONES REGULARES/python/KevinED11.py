import re
from typing import Protocol
from functools import partial
from enum import StrEnum


type IntTuple = tuple[int, ...]


class SearcherFn(Protocol):
    def __call__(self, text: str) -> IntTuple: ...


class SearchPattern(StrEnum):
    ALL_NUMBERS = r"\d+"


def generic_searcher(pattern: str, text: str) -> IntTuple:
    return tuple(re.findall(pattern, text))


search_all_numbers = partial(generic_searcher, pattern=SearchPattern.ALL_NUMBERS)


class ValidatorFn(Protocol):
    def __call__(self, value: str) -> bool: ...


class ValidationPattern(StrEnum):
    EMAIL = r"^\w+@\w+\.\w+$"
    PHONE = r"^\+?\d{10, 15}$"
    URL = r"^https?://.+$"


def generic_validator(pattern: str, value: str) -> bool:
    return re.search(pattern, value) is not None


validate_email = partial(generic_validator, pattern=ValidationPattern.EMAIL)
validate_phone = partial(generic_validator, pattern=ValidationPattern.PHONE)
validate_url = partial(generic_validator, pattern=ValidationPattern.URL)


def execute_validator(validator: ValidatorFn, value: str) -> bool:
    return validator(value=value)


def execute_searcher(searcher: SearcherFn, text: str) -> IntTuple:
    return searcher(text=text)


class Separator(StrEnum):
    LINE_BREAK = "\n"


def main() -> None:
    email_result = execute_validator(validator=validate_email, value="a@a.com")
    phone_result = execute_validator(validator=validate_phone, value="000000000000")
    url_result = execute_validator(
        validator=validate_url, value="https://www.google.com"
    )
    print(email_result, phone_result, url_result, sep=Separator.LINE_BREAK)

    search_result = execute_searcher(searcher=search_all_numbers, text="ke8i9")
    print(search_result)


if __name__ == "__main__":
    main()
