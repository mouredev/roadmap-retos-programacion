from datetime import datetime


def add_two_numbers(a: int, b: int) -> int:
    return a + b


def test_add_two_numbers():
    """
    GIVEN two numbers
    WHEN we add them
    THEN we get the sum
    """
    assert add_two_numbers(1, 2) == 3


def test_commutative():
    """
    GIVEN two numbers
    AND they are provided in any order
    WHEN we add them
    THEN the result does not depend on the order
    """
    assert add_two_numbers(2, 3) == add_two_numbers(3, 2)


def test_negative():
    """
    GIVEN two negative numbers
    WHEN we add them
    THEN we get the proper sum
    """
    assert add_two_numbers(-1, -3) == -4


def main():
    # Obviamente en un entorno real usaría Pytest, los test estarían
    # en un fichero separado, etc.
    test_add_two_numbers()
    test_commutative()
    test_negative()
    print("All main tests pass")


def test_person_has_all_fields(person: dict):
    """
    GIVEN a 'person' dictionary, containing personal info
    THEN it contains all the required fields
    """
    required_fields = ["name", "age", "birth_date", "programming_languages"]
    for field in required_fields:
        assert field in person, f"Person lacks required field '{field}'"


def test_person_data_is_congruent(person: dict):
    """
    GIVEN a 'person' dictionary, containing personal info
    THEN the name field is a string
    AND the age is an integer
    AND the birth_date is a date in ISO format
    AND the age matches the birth_date
    AND the programming_languages is a list of strings
    """
    assert isinstance(person["name"], str), "Person name must be a string"
    assert isinstance(person["age"], int), "Person age must be an integer"
    birth = datetime.strptime(person["birth_date"], "%Y-%m-%d")
    expected_age = get_age(birth)
    assert person["age"] == expected_age, f"Person's age {person['age']} does not match expected age {expected_age}"
    langs = person["programming_languages"]
    assert isinstance(langs, (list, tuple)), "Person's programming languages are not a list or tuple"
    assert len(langs) >= 1, "Person should know at least 1 programming language"
    for lang in langs:
        assert isinstance(lang, str), f"Language '{lang}' is not a valid programming language"


def get_age(birth: datetime) -> int:
    """Dates are a nasty thing."""
    now = datetime.now()
    delta_years = now.year - birth.year

    if (now.month, now.day) < (birth.month, birth.day):
        delta_years -= 1

    return delta_years


def extra():
    person = {
        "name": "Iñaki",
        "age": 46,
        "birth_date": "1977-06-11",
        "programming_languages": ["Python", "Bash", "Fortran"],
    }
    test_person_has_all_fields(person)
    test_person_data_is_congruent(person)
    print("All extra tests pass")


if __name__ == "__main__":
    main()
    extra()
