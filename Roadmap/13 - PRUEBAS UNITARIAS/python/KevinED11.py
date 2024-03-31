from functools import lru_cache, partial, wraps
from typing import TypeAlias, TypeVar, Protocol, NamedTuple, Iterable, Union
import pytest
from enum import StrEnum


Number: TypeAlias = Union[int, float]


T = TypeVar("T", bound=Number)


class OperationFn(Protocol):
    def __call__(self, a: T, b: T) -> T:
        ...


TypeTupleOrType: TypeAlias = Union[type, tuple[type, ...]]


def any_is_instance_of(*args, types: TypeTupleOrType) -> bool:
    return any(isinstance(arg, types) for arg in args)


def all_is_instance_of(*args, types: TypeTupleOrType) -> bool:
    return all(isinstance(arg, types) for arg in args)


def is_instance_of(obj: object, types: TypeTupleOrType) -> bool:
    return isinstance(obj, types)


def validate_operation(fn: OperationFn) -> OperationFn:
    @wraps(fn)
    def wrapper(a: T, b: T) -> T:
        if not any_is_instance_of(a, b, types=(int, float)):
            raise TypeError("a and b must be numbers")

        return fn(a, b)

    return wrapper


@validate_operation
def add(a: T, b: T) -> T:
    return a + b


@validate_operation
def multiply(a: T, b: T) -> T:
    return a * b


def execute_operation(operation: OperationFn, a: T, b: T) -> T:
    return operation(a, b)


class Case(NamedTuple):
    a: Number
    b: Number
    expected: Number


def test_add_valid_cases() -> None:
    cases = [
        Case(1, 2, 3),
        Case(1, 2.2, 3.2),
        Case(1.1, 2, 3.1),
        Case(1, 2, 3),
        Case(4, 6, 10),
        Case(-2, -3, -5),
    ]

    for case in cases:
        result = add(case.a, case.b)
        assert result == case.expected, f"{case} failed"
        assert is_instance_of(result, (int, float)), f"{case} failed"
        print(f"{case} passed")


def test_add_invalid_cases() -> None:
    cases = [Case("a", 2, 3), Case(1, "b", 4), Case(3, 5, 9)]

    for case in cases:
        a_is_int_or_float = is_instance_of(case.a, (int, float))
        b_is_int_or_float = is_instance_of(case.b, (int, float))

        if not a_is_int_or_float or not b_is_int_or_float:
            with pytest.raises(TypeError):
                add(case.a, case.b)

        if a_is_int_or_float and b_is_int_or_float:
            result = add(case.a, case.b)
            assert result != case.expected


def create_programmer(
    name: str, age: int, birth_date: str, programming_languages: Iterable[str]
) -> dict:
    return dict(
        name=name,
        age=age,
        birth_date=birth_date,
        programming_languages=programming_languages,
    )


kevin_programmer = partial(
    create_programmer,
    name="kevin",
    age=23,
    birth_date="01/01/2000",
    programming_languages=["python", "go", "javascript", "typescript"],
)


class KeysObj(StrEnum):
    NAME = "name"
    AGE = "age"
    BIRTH_DATE = "birth_date"
    PROGRAMMING_LANGUAGES = "programming_languages"


@lru_cache(maxsize=None)
def dict_keys():
    return [key.value for key in KeysObj]


def test_field_exist() -> None:
    kevin = kevin_programmer()
    assert all(field in kevin for field in dict_keys()), f"{field} does not exist"


def test_field_type() -> None:
    kevin = kevin_programmer()

    assert all_is_instance_of(
        kevin[KeysObj.NAME], kevin[KeysObj.BIRTH_DATE], types=str
    ), "name or birth_date is not a string"
    assert is_instance_of(kevin[KeysObj.AGE], int), "age is not an integer"
    assert is_instance_of(
        kevin[KeysObj.PROGRAMMING_LANGUAGES], list
    ), "programming_languages is not a list"


def main() -> None:
    ...


if __name__ == "__main__":
    main()
