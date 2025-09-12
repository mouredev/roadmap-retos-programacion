import dataclasses
from typing import Protocol, Optional, Callable, NamedTuple


diccionario = {"nombre": "Kevin", "apellido": "Elias", "edad": 23}
diccionario["direccion"] = "Calle falsa 123"
diccionario["edad"] = 24
del diccionario["direccion"]
print(dict(sorted(diccionario.items(), key=lambda x: x[0])))

lista = [1, 2, 3, 4, 5]
lista += [6, 7, 8, 9, 10]
lista.append(11)
lista.extend([12, 13, 14, 15, 16])
lista.insert(0, 0)
lista.remove(0)
lista.pop()
lista.clear()

tupla = (1, 2, 3, 4, 5)
fist_tuple_element = tupla[0]

conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.update({7, 8, 9, 10})
conjunto.remove(6)
conjunto.discard(7)
conjunto.pop()
print(conjunto)


@dataclasses.dataclass
class PersonalInfo:
    name: str
    phone: str


class AgendaManager(Protocol):
    contacts: dict[str, PersonalInfo] = {}
    running: bool = False

    def show(self) -> None:
        ...

    def add(self, name: str, info: dict) -> None:
        ...

    def remove(self, name: str) -> None:
        ...

    def update(self, name: str, info: dict) -> None:
        ...

    def search(self, name: str) -> Optional[PersonalInfo]:
        ...

    def print_menu(self) -> None:
        ...

    def start(self) -> None:
        ...


def show_contact_manager_menu() -> None:
    print("1. Show contacts")
    print("2. Add contact")
    print("3. Remove contact")
    print("4. Update contact")
    print("5. Search contact")
    print("6. Exit")


def user_input(prompt: str) -> str:
    return input(prompt)


def is_valid_phone_number(phone: str) -> bool:
    return phone.isdigit() and 9 < len(phone) <= 11


class SetupMessages(NamedTuple):
    choose_an_option: str = "Choose an option: "
    invalid_phone_number: Callable = lambda phone: f"Invalid phone number: {phone}"
    contact_not_found: Callable = lambda name: f"Contact {name} not found"
    contact_updated: Callable = lambda name: f"Contact {name} updated"
    contact_added: Callable = lambda name: f"Contact {name} added"
    contact_removed: Callable = lambda name: f"Contact {name} removed"
    contact_already_exists: Callable = lambda name: f"Contact {name} already exists"
    invalid_operation: str = "Invalid operation, choose a valid option from the menu"
    game_already_running: str = "Game already running"
    game_not_running: str = "Game not running"


class GameAlreadyRunningException(Exception):
    pass


@dataclasses.dataclass
class ContactManager:
    setup_messages: SetupMessages
    contacts: dict[str, PersonalInfo] = dataclasses.field(default_factory=dict)
    running: bool = dataclasses.field(default=False)

    def show(self) -> None:
        for name, info in self.contacts.items():
            print(f"{name}: {info}")

    def add(self, name: str, info: PersonalInfo) -> None:
        if self.search(name) is not None:
            print(self.setup_messages.contact_already_exists)
            return

        if not is_valid_phone_number(info.phone):
            print(self.setup_messages.invalid_phone_number(info.phone))
            return

        self.contacts[name] = info

    def remove(self, name: str) -> None:
        if self.search(name) is None:
            print(self.setup_messages.contact_not_found)
            return

        del self.contacts[name]

    def update(self, name: str, info: PersonalInfo) -> None:
        current_contact_info = self.search(name)
        if current_contact_info is None:
            print(self.setup_messages.contact_not_found)
            return

        if not is_valid_phone_number(info.phone):
            print(self.setup_messages.invalid_phone_number(info.phone))
            return

        current_contact_info_dict = dataclasses.asdict(current_contact_info)
        for key, new_value in dataclasses.asdict(info).items():
            if current_contact_info_dict[key] != new_value:
                setattr(current_contact_info, key, new_value)

        self.contacts[name] = current_contact_info

    def search(self, name: str) -> Optional[PersonalInfo]:
        return self.contacts.get(name, None)

    def print_menu(self) -> None:
        show_contact_manager_menu()

    def __exit(self) -> bool:
        return self.__is_running()

    def __is_running(self) -> bool:
        return self.running

    def __get_menu_options(self) -> dict[str, Callable]:
        return {
            "1": self.show,
            "2": self.add,
            "3": self.remove,
            "4": self.update,
            "5": self.search,
            "6": self.__exit,
        }

    def start(self) -> None:
        if self.__is_running():
            raise GameAlreadyRunningException(self.setup_messages.game_already_running)

        self.running = True
        options_menu = self.__get_menu_options()
        exit = True

        while self.__is_running():
            self.print_menu()
            user_option = user_input(prompt=self.setup_messages.choose_an_option)

            if options_menu[user_option] == exit:
                break

            if user_option not in options_menu:
                print(self.setup_messages.invalid_operation)
                continue

            options_menu[user_option]()


def main(manager: AgendaManager) -> None:
    manager.start()


if __name__ == "__main__":
    manager: AgendaManager = ContactManager(setup_messages=SetupMessages())
    main(manager=manager)
