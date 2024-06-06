import unittest
from typing import TypeVar, TypedDict


"""
    Tests...
"""

print("Tests...")

print(
    """\nParameters = TypeVar("Parameters", int, float)


def add(a: Parameters, b: Parameters) -> Parameters:
    \"\"\"Add two numbers\"\"\"
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid arguments! Both of them should be integers, or floats")

    return a + b


class TestAdd(unittest.TestCase):
    \"\"\"Tests of \"add\" (function).\"\"\"

    def test_add_integers(self) -> None:
        \"\"\"Test if \"add\" (function) can be executed with integer parameters.\"\"\"
        result: int = add(a=1, b=4)
        self.assertEqual(first=result, second=5)

    def test_add_floats(self) -> None:
        \"\"\"Test if \"add\" (function) can be executed with float parameters.\"\"\"
        result: float = add(a=1.75, b=5.25)
        self.assertEqual(first=result, second=7)

    def test_add_strings(self) -> None:
        \"\"\"Test if \"add\" (function) throw an error if it receive string parameters.\"\"\"

        with self.assertRaises(expected_exception=TypeError):
            add(a=\"4\", b=\"4\")"""
)

Parameters = TypeVar("Parameters", int, float)


def add(a: Parameters, b: Parameters) -> Parameters:
    """Add two numbers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid arguments! Both of them should be integers, or floats")

    return a + b


class TestAdd(unittest.TestCase):
    """Tests of "add" (function)."""

    def test_add_integers(self) -> None:
        """Test if "add" (function) can be executed with integer parameters."""
        result: int = add(a=1, b=4)
        self.assertEqual(first=result, second=5)

    def test_add_floats(self) -> None:
        """Test if "add" (function) can be executed with float parameters."""
        result: float = add(a=1.75, b=5.25)
        self.assertEqual(first=result, second=7)

    def test_add_strings(self) -> None:
        """Test if "add" (function) throw an error if it receive string parameters."""

        with self.assertRaises(expected_exception=TypeError):
            add(a="4", b="4")


print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...\n")

Author = TypedDict(
    "Author",
    {"name": str, "age": str, "birth_date": str, "programming_languages": list[str]},
)

AUTHOR: Author = {
    "age": "22",
    "birth_date": "2002-02-20",
    "name": "Lucas",
    "programming_languages": ["TypeScript", "Python", "Go (Golang)"],
}


class TestAuthor(unittest.TestCase):
    """Tests of "AUTHOR" (constant)."""

    def test_schema(self) -> None:
        """Test "AUTHOR" (constant) schema."""
        author_schema: Author = {
            "age": "0",
            "birth_date": "0000-00-00",
            "name": "",
            "programming_languages": [],
        }

        self.assertIn(member="age", container=author_schema)
        self.assertIn(member="birth_date", container=author_schema)
        self.assertIn(member="name", container=author_schema)
        self.assertIn(member="programming_languages", container=author_schema)

    def test_data_types(self) -> None:
        """Test the data types of "AUTHOR" (constant) properties."""
        expected_author: Author = {
            "age": "22",
            "birth_date": "2002-02-20",
            "name": "Lucas",
            "programming_languages": ["TypeScript", "Python", "Go (Golang)"],
        }

        self.assertDictEqual(d1=expected_author, d2=AUTHOR)


unittest.main()
