"""
    Inheritance...
"""

from dataclasses import dataclass
from typing import Self, Literal


@dataclass
class Animal:
    """Animal class"""

    _average_speed: float
    _average_weight: float
    _name: str
    _sound: str | None

    def set_average_speed(self, average_speed: float) -> Self:
        """Set a new average speed"""
        self._average_speed = average_speed
        return self

    def set_average_weight(self, average_weight: float) -> Self:
        """Set a new average weight"""
        self._average_weight = average_weight
        return self

    def set_name(self, name: str) -> Self:
        """Set a new name"""
        self._name = name
        return self

    def set_sound(self, sound: str) -> Self:
        """Set a new sound"""
        self._sound = sound
        return self

    def get_average_speed(self) -> float:
        """Return average speed"""
        return self._average_speed

    def get_average_weight(self) -> float:
        """Return average weight"""
        return self._average_weight

    def get_name(self) -> str:
        """Return name"""
        return self._name

    def get_sound(self) -> str | None:
        """Return sound"""
        return self._sound

    def get_attributes(self) -> str:
        """Return all attributes"""
        return (
            f"Average speed --> {self.get_average_speed()}"
            + f"\nAverage_weight --> {self.get_average_weight()}"
            + f"\nName --> {self.get_name()}"
        )

    def print_sound(self) -> Self:
        """Print sound"""
        print(f"\n{self.get_sound()}")
        return self


@dataclass
class Dog(Animal):
    """Dog class"""

    _owner_name: str
    _owner_phone: str

    def get_owner_name(self) -> str:
        """Return owner name"""
        return self._owner_name

    def get_owner_phone(self) -> str:
        """Return owner phone"""
        return self._owner_phone

    def set_owner_name(self, owner_name: str) -> Self:
        """Set a new owner name"""
        self._owner_name = owner_name
        return self

    def set_owner_phone(self, owner_phone: str) -> Self:
        """Set a new owner phone"""
        self._owner_phone = owner_phone
        return self

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f"\nOwner name --> {self.get_owner_name()}"
            + f"\nOwner phone --> {self.get_owner_phone()}"
        )


@dataclass
class Cat(Animal):
    """Cat class"""

    _owner_name: str
    _owner_phone: str

    def get_owner_name(self) -> str:
        """Return owner name"""
        return self._owner_name

    def get_owner_phone(self) -> str:
        """Return owner phone"""
        return self._owner_phone

    def set_owner_name(self, owner_name: str) -> Self:
        """Set a new owner name"""
        self._owner_name = owner_name
        return self

    def set_owner_phone(self, owner_phone: str) -> Self:
        """Set a new owner phone"""
        self._owner_phone = owner_phone
        return self

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f"\nOwner name --> {self.get_owner_name()}"
            + f"\nOwner phone --> {self.get_owner_phone()}"
        )


print("Inheritance in Python...")

print(
    """\nfrom dataclasses import dataclass
from typing import Self


@dataclass
class Animal:
    \"\"\"Animal class\"\"\"

    _average_speed: float
    _average_weight: float
    _name: str
    _sound: str | None

    def set_average_speed(self, average_speed: float) -> Self:
        \"\"\"Set a new average speed\"\"\"
        self._average_speed = average_speed
        return self

    def set_average_weight(self, average_weight: float) -> Self:
        \"\"\"Set a new average weight\"\"\"
        self._average_weight = average_weight
        return self

    def set_name(self, name: str) -> Self:
        \"\"\"Set a new name\"\"\"
        self._name = name
        return self

    def set_sound(self, sound: str) -> Self:
        \"\"\"Set a new sound\"\"\"
        self._sound = sound
        return self

    def get_average_speed(self) -> float:
        \"\"\"Return average speed\"\"\"
        return self._average_speed

    def get_average_weight(self) -> float:
        \"\"\"Return average weight\"\"\"
        return self._average_weight

    def get_name(self) -> str:
        \"\"\"Return name\"\"\"
        return self._name

    def get_sound(self) -> str | None:
        \"\"\"Return sound\"\"\"
        return self._sound

    def get_attributes(self) -> str:
        \"\"\"Return all attributes\"\"\"
        return (
            f\"Average speed --> {self.get_average_speed()}\"
            + f\"\\nAverage_weight --> {self.get_average_weight()}\"
            + f\"\\nName --> {self.get_name()}\"
        )

    def print_sound(self) -> Self:
        \"\"\"Print sound\"\"\"
        print(f\"\\n{self.get_sound()}\")
        return self


@dataclass
class Dog(Animal):
    \"\"\"Dog class\"\"\"

    _owner_name: str
    _owner_phone: str

    def get_owner_name(self) -> str:
        \"\"\"Return owner name\"\"\"
        return self._owner_name

    def get_owner_phone(self) -> str:
        \"\"\"Return owner phone\"\"\"
        return self._owner_phone

    def set_owner_name(self, owner_name: str) -> Self:
        \"\"\"Set a new owner name\"\"\"
        self._owner_name = owner_name
        return self

    def set_owner_phone(self, owner_phone: str) -> Self:
        \"\"\"Set a new owner phone\"\"\"
        self._owner_phone = owner_phone
        return self

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f\"\\nOwner name --> {self.get_owner_name()}\"
            + f\"\\nOwner phone --> {self.get_owner_phone()}\"
        )


@dataclass
class Cat(Animal):
    \"\"\"Cat class\"\"\"

    _owner_name: str
    _owner_phone: str

    def get_owner_name(self) -> str:
        \"\"\"Return owner name\"\"\"
        return self._owner_name

    def get_owner_phone(self) -> str:
        \"\"\"Return owner phone\"\"\"
        return self._owner_phone

    def set_owner_name(self, owner_name: str) -> Self:
        \"\"\"Set a new owner name\"\"\"
        self._owner_name = owner_name
        return self

    def set_owner_phone(self, owner_phone: str) -> Self:
        \"\"\"Set a new owner phone\"\"\"
        self._owner_phone = owner_phone
        return self

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f\"\\nOwner name --> {self.get_owner_name()}\"
            + f\"\\nOwner phone --> {self.get_owner_phone()}\"
        )"""
)

dog = Dog(
    _average_speed=21,
    _average_weight=28,
    _name="Angela",
    _owner_name="Lucas Hoz",
    _owner_phone="1134465758",
    _sound="Woof",
)

print(
    """\n\ndog = Dog(
    _average_speed=21,
    _average_weight=28,
    _name=\"Angela\",
    _owner_name=\"Lucas Hoz\",
    _owner_phone=\"1134465758\",
    _sound=\"Woof\",
)"""
)

print("\nDog attributes...\n")
print(dog.get_attributes())

print("\nDog sound...")
dog.print_sound()

cat = Cat(
    _average_speed=16,
    _average_weight=14.68,
    _name="Mini",
    _owner_name="Martin Gonzales",
    _owner_phone="1134485978",
    _sound="Meow",
)

print(
    """\ncat = Cat(
    _average_speed=16,
    _average_weight=14.68,
    _name=\"Mini\",
    _owner_name=\"Martin Gonzales\",
    _owner_phone=\"1134485978\",
    _sound=\"Meow\",
)"""
)

print("\nCat attributes...\n")
print(cat.get_attributes())

print("\nCat sound...")
cat.print_sound()


"""
    Additional challenge...
"""

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

print("Additional challenge...")


@dataclass
class Employee:
    """Employee class"""

    _first_name: str
    _id: int
    _last_name: str
    _salary: float

    def set_first_name(self, first_name: str) -> Self:
        """Set a new first name"""
        self._first_name = first_name
        return self

    def set_id(self, new_id: int) -> Self:
        """Set a new first name"""
        self._id = new_id
        return self

    def set_last_name(self, last_name: str) -> Self:
        """Set a new first name"""
        self._last_name = last_name
        return self

    def set_salary(self, salary: float) -> Self:
        """Set a new first name"""
        self._salary = salary
        return self

    def get_first_name(self) -> str:
        """Return first name"""
        return self._first_name

    def get_id(self) -> int:
        """Return first name"""
        return self._id

    def get_last_name(self) -> str:
        """Return first name"""
        return self._last_name

    def get_salary(self) -> float:
        """Return first name"""
        return self._salary

    def get_attributes(self) -> str:
        """Get all attributes"""
        return (
            f"First name --> {self._first_name}"
            + f"\nId --> {self._id}"
            + f"\nLast name --> {self._last_name}"
            + f"\nSalary --> {self._salary}"
        )


type Side = Literal["Backend", "Frontend", "Full Stack"]




@dataclass
class Programmer(Employee):
    """Programmer class"""

    _languages: list[str]
    _side: Side

    def set_languages(self, languages: list[str]) -> Self:
        """Set new languages"""
        self._languages = languages
        return self

    def set_side(self, side: Side) -> Self:
        """Set new side"""
        self._side = side
        return self

    def get_languages(self) -> list[str]:
        """Get languages"""
        return self._languages

    def get_side(self) -> Side:
        """Get side"""
        return self._side

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f"\nLanguages --> {self.get_languages()}"
            + f"\nSide --> {self.get_side()}"
        )

    def write_code(self, language: str) -> str:
        """Write code in the programming language of the programmer"""
        return f"Writing code in {language}"


@dataclass
class ProjectManager(Employee):
    """Project manager class"""

    _functions: list[str]
    _programmers: list[Programmer]

    def set_functions(self, functions: list[str]) -> Self:
        """Set new functions"""
        self._functions = functions
        return self

    def set_programmers(self, programmers: list[Programmer]) -> Self:
        """Set new programmers"""
        self._programmers = programmers
        return self

    def get_functions(self) -> list[str]:
        """Return functions"""
        return self._functions

    def get_programmers(self) -> list[Programmer]:
        """Return programmers"""
        return self._programmers

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f"\nFunctions --> {self.get_functions()}"
            + f"\nProgrammers --> {self.get_programmers()}"
        )

    def make_management(self) -> str:
        """Make management stuffs"""
        return "Just a project manager doing everything expect programming."


@dataclass()
class Manager(Employee):
    """Manager class"""

    _department: str
    _functions: list[str]
    _project_managers: list[ProjectManager]

    def set_department(self, department: str) -> Self:
        """Set new department"""
        self._department = department
        return self

    def set_functions(self, functions: list[str]) -> Self:
        """Set new functions"""
        self._functions = functions
        return self

    def set_project_managers(self, project_managers: list[ProjectManager]) -> Self:
        """Set new project managers"""
        self._project_managers = project_managers
        return self

    def get_department(self) -> str:
        """Return department"""
        return self._department

    def get_functions(self) -> list[str]:
        """Return functions"""
        return self._functions

    def get_project_managers(self) -> list[ProjectManager]:
        """Return projects managers"""
        return self._project_managers

    def get_attributes(self) -> str:
        return (
            super().get_attributes()
            + f"\nFunctions --> {self.get_functions()}"
            + f"\nProject managers --> {self.get_project_managers()}"
        )

    def make_management(self) -> str:
        """Make management stuffs"""
        return "Just a manager doing management things."


programmer = Programmer(
    _first_name="Lucas",
    _id=0,
    _languages=["JavaScript", "TypeScript", "Python"],
    _last_name="Hoz",
    _salary=150000,
    _side="Full Stack",
)

print("\nProgrammer attributes...\n")
print(programmer.get_attributes())

print("\nProgrammer methods...")
print(f"\nprogrammer.write_code() --> {programmer.write_code(language="Python")}")

project_manager = ProjectManager(
    _first_name="Lucas",
    _functions=["Time management", "Team leardership"],
    _id=1,
    _last_name="Hoz",
    _programmers=[programmer],
    _salary=150000,
)

print("\nProject manager attributes...\n")
print(project_manager.get_attributes())

print("\nProject manager methods...")
print(f"\nproject_manager.make_management() --> {project_manager.make_management()}")

manager = Manager(
    _department="Development",
    _first_name="Lucas",
    _functions=["Time management", "Financial planning", "Department management"],
    _id=2,
    _last_name="Hoz",
    _project_managers=[project_manager],
    _salary=150000,
)

print("\nManager attributes...\n")
print(manager.get_attributes())

print("\nManager methods...")
print(f"\nmanager.make_management() --> {manager.make_management()}")
