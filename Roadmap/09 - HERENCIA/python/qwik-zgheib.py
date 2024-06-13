# -- exercise
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> None:
        print("The animal makes a sound")


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def make_sound(self) -> None:
        print(f"{self.name} does wow wow!")


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def make_sound(self) -> None:
        print(f"{self.name} does meow meow!")


dog: Dog = Dog("Firulais")
dog.make_sound()

cat: Cat = Cat("Silveter")
cat.make_sound()
print("\n----- extra challenge -----")


# -- extra challenge
class Employee:
    def __init__(self, employee_id: int, name: str):
        self.employee_id = employee_id
        self.name = name

    def get_details(self):
        return f"ID: {self.employee_id}, Name: {self.name}"


class Manager(Employee):
    def __init__(self, employee_id: int, name: str):
        super().__init__(employee_id, name)
        self.subordinates = []

    def add_subordinate(self, employee: Employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee: Employee):
        self.subordinates.remove(employee)

    def list_subordinates(self):
        return [employee.get_details() for employee in self.subordinates]


class ProjectManager(Manager):
    def __init__(self, employee_id: int, name: str, project_name: str):
        super().__init__(employee_id, name)
        self.project_name = project_name

    def get_project_details(self):
        return f"Project: {self.project_name}, Managed by: {self.name}"


class Developer(Employee):
    def __init__(self, employee_id: int, name: str, programming_languages: list):
        super().__init__(employee_id, name)
        self.programming_languages = programming_languages

    def add_programming_language(self, language: str):
        if language not in self.programming_languages:
            self.programming_languages.append(language)

    def list_programming_languages(self):
        return self.programming_languages


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)

    def find_employee_by_id(self, employee_id: int) -> Employee:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def list_all_employees(self):
        return [employee.get_details() for employee in self.employees]


def main():
    company = Company()

    # Create employees
    dev1 = Developer(
        employee_id=1, name="Qwik", programming_languages=["Python", "Java"]
    )
    dev2 = Developer(
        employee_id=2, name="Rahman", programming_languages=["JavaScript", "TypeScript"]
    )
    pm1 = ProjectManager(employee_id=3, name="Mohammed", project_name="Project Alpha")
    manager1 = Manager(employee_id=4, name="Ahmed")

    # Add employees to company
    company.add_employee(dev1)
    company.add_employee(dev2)
    company.add_employee(pm1)
    company.add_employee(manager1)

    # Manager assigns subordinates
    manager1.add_subordinate(dev1)
    manager1.add_subordinate(dev2)
    pm1.add_subordinate(manager1)

    # List all employees
    print("All employees in the company:")
    for details in company.list_all_employees():
        print(details)

    # List subordinates for each manager
    print("\nManager's subordinates:")
    for details in manager1.list_subordinates():
        print(details)

    print("\nProject Manager's subordinates:")
    for details in pm1.list_subordinates():
        print(details)

    # Developer adds a new programming language
    dev1.add_programming_language("Rust")
    print("\nDeveloper's programming languages:")
    print(dev1.list_programming_languages())


if __name__ == "__main__":
    main()
