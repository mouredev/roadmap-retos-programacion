# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from abc import ABCMeta, abstractmethod
from random import choice
from re import match

# ---------------------------------------------------------------------------- #
#                                    CLASSES                                   #
# ---------------------------------------------------------------------------- #


class AbcPasswordGenerator(metaclass=ABCMeta):
    @property
    @abstractmethod
    def fail_attempts(self) -> int:
        pass

    @property
    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def get_advice(self, *, password: str) -> str:
        pass

    @abstractmethod
    def is_password(self, *, password: str) -> bool:
        pass


class PasswordGenerator(AbcPasswordGenerator):
    __fail_attempts: int
    __length: int
    __password_hash: str
    __password: str

    def __init__(self, *, _hash: str, length: int) -> None:
        self.__fail_attempts = 0
        self.__password_hash = _hash
        self.__length = length

        password: str = ""
        while len(password) < self.__length:
            rnd_char: str = choice(seq=self.__password_hash)
            if not rnd_char in password:
                password += rnd_char

        self.__password = password

    def get_advice(self, *, password: str) -> str:
        advice: list[str] = []

        for i, char in enumerate(iterable=password):
            password_char: str = self.__password[i]

            if char == password_char:
                advice.append(f'  - "{char}" is in the correct position.')
                continue

            if char in self.__password:
                advice.append(
                    f'  - "{char}" exist but it\'s not in the {i + 1}th position.'
                )
                continue

            advice.append(f'  - "{char}" not exist in the password.')

        return "\n".join(advice)

    @property
    def fail_attempts(self) -> int:
        return self.__fail_attempts

    @property
    def length(self) -> int:
        return self.__length

    def is_password(self, *, password: str) -> bool:
        if self.__password == password:
            return True

        self.__fail_attempts += 1
        return False


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #

_hash: str = "ABC123"
_length: int = 4

passwordGenerator: AbcPasswordGenerator = PasswordGenerator(_hash=_hash, length=_length)

regex: str = rf"^[{_hash}]{{{_length}}}$"

userInput: str = input("> Enter the password (maximum of 4 chars): ").strip()

while match(pattern=regex, string=userInput) is None:
    print(
        "\n> Error! The password length must be 4 characters, "
        f'and it should contain any of these characters: "{_hash}". Try again...'
    )
    userInput = input("\n> Enter the password (maximum of 4 chars): ").strip()


while (
    not passwordGenerator.is_password(password=userInput)
    and passwordGenerator.fail_attempts < 10
):
    print(f"\n{passwordGenerator.get_advice(password=userInput)}")

    print("\n> Invalid password! Try again...")

    userInput: str = input("\n> Enter the password (maximum of 4 chars): ").strip()

    while match(pattern=regex, string=userInput) is None:
        print(
            "\n> Error! The password length must be 4 characters, "
            f'and it should contain any of these characters: "{_hash}". Try again...'
        )
        userInput = input("\n> Enter the password (maximum of 4 chars): ").strip()


if passwordGenerator.fail_attempts < 10:
    print(f'\n> Santa won! The password is "{userInput}".')
else:
    print("\n> Santa lost! Storage will be closed forever.")
