import re
from typing import Protocol
from functools import partial, lru_cache
from enum import StrEnum


type StrTuple = tuple[str, ...]


class SearcherFn(Protocol):
    def __call__(self, text: str) -> StrTuple: ...


class SearchPattern(StrEnum):
    ALL_NUMBERS = r"\d+"


@lru_cache
def generic_searcher(pattern: SearchPattern, text: str) -> StrTuple:
    return tuple(re.findall(pattern, text))


search_all_numbers = partial(generic_searcher, pattern=SearchPattern.ALL_NUMBERS)


class ValidatorFn(Protocol):
    def __call__(self, value: str) -> bool: ...


class ValidationPattern(StrEnum):
    pass


class EmailValidationPattern(ValidationPattern):
    EMAIL = r"^\w+@\w+\.\w+$"
    EMAIL2 = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    EMAIL3 = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class PhoneValidationPattern(ValidationPattern):
    PHONE = r"^\+?\d{10, 15}$"
    PHONE2 = r"^\+?1?\d{9,15}$"


class UrlValidationPattern(ValidationPattern):
    URL = r"^https?://.+$"
    URL2 = r"^(http|https)://[a-zA-Z0-9-\.].+\.[a-zA-Z]{2,4}(/\S*)?$"


@lru_cache
def generic_validator(pattern: ValidationPattern, value: str) -> bool:
    return re.match(pattern, value) is not None


validate_email = partial(generic_validator, pattern=EmailValidationPattern.EMAIL)
validate_phone = partial(generic_validator, pattern=PhoneValidationPattern.PHONE)
validate_url = partial(generic_validator, pattern=UrlValidationPattern.URL2)


def execute_validator(validator: ValidatorFn, value: str) -> bool:
    return validator(value=value)


def execute_searcher(searcher: SearcherFn, text: str) -> StrTuple:
    return searcher(text=text)


class Separator(StrEnum):
    LINE_BREAK = "\n"


def main() -> None:
    email_result = execute_validator(validator=validate_email, value="a@a.com")
    phone_result = execute_validator(validator=validate_phone, value="000000000000")
    url_result = execute_validator(
        validator=validate_url, value="https://wwwgoogle.com"
    )
    print(email_result, phone_result, url_result, sep=Separator.LINE_BREAK)

    search_result = execute_searcher(searcher=search_all_numbers, text="ke8i9")
    print(search_result)


if __name__ == "__main__":
    main()
