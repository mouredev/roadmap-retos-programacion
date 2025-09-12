# list
list_i: list[int] = [1, 2, 3, 4, 5]
list_i.append(6)
list_i.remove(3)
list_i[0] = 10
list_i.sort()
print("list_i:", list_i)

# tuple
tuple_i: tuple = (1, 2, 3, 4, 5)
print("tuple_i", tuple_i)


# set
set_i: set[int] = {1, 2, 3, 4, 5}
set_i.add(6)
set_i.remove(3)
print("set_i:", set_i)

# dictionary
dict_i: dict[str, int] = {"a": 1, "b": 2, "c": 3}
dict_i["d"] = 4
del dict_i["b"]
dict_i["a"] = 10
dict_sorted_i = dict(sorted(dict_i.items(), key=lambda item: item[1]))


print("dict_i:", dict_i)
print("dict_i order:", dict_sorted_i)


# -- extra challenge
class Contact:
    def __init__(self, name: str, phone: int):
        self.name: str = name
        self.phone: int = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


class ContactValidator:
    @staticmethod
    def validate_name(name: str) -> bool:
        return len(name) > 0

    @staticmethod
    def validate_phone(phone: str) -> bool:
        try:
            int(str(phone).replace("+", ""))
            return len(phone) >= 11
        except ValueError:
            return False


class ContactRepository:
    def __init__(self):
        self.contacts: list = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, name: str):
        self.contacts: list = [c for c in self.contacts if c.name != name]

    def update_contact(self, name: str, new_contact: Contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                return

    def find_contact(self, name: str) -> Contact:
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        return sorted(self.contacts, key=lambda x: x.name)


class ContactService:
    def __init__(self, repository: ContactRepository, validator: ContactValidator):
        self.repository = repository
        self.validator = validator

    def add_contact(self, name: str, phone: int):
        if self.validator.validate_name(name) and self.validator.validate_phone(phone):
            contact = Contact(name, phone)
            self.repository.add_contact(contact)
        else:
            print("invalid contact information.")

    def remove_contact(self, name: str):
        self.repository.remove_contact(name)

    def update_contact(self, name: str, new_name: str, new_phone: int):
        if self.validator.validate_name(new_name) and self.validator.validate_phone(
            new_phone
        ):
            new_contact = Contact(new_name, new_phone)
            self.repository.update_contact(name, new_contact)
        else:
            print("invalid contact information.")

    def find_contact(self, name: str) -> Contact:
        return self.repository.find_contact(name)

    def list_contacts(self):
        return self.repository.list_contacts()


def main():
    repository = ContactRepository()
    validator = ContactValidator()
    service = ContactService(repository, validator)

    while True:
        print("\n--- Contacts Agenda ---")
        print("[1] insert contact")
        print("[2] delete contact")
        print("[3] update contact")
        print("[4] search contact")
        print("[5] show contacts")
        print("[6] exit")

        option = input("select an option: ")

        if option == "1":
            name = input("contact name: ")
            phone = input("contact phone: ")
            service.add_contact(name, phone)
        elif option == "2":
            name = input("enter contact name to delete: ")
            service.remove_contact(name)
        elif option == "3":
            name = input("enter contact name to update: ")
            new_name = input("new name of the contact: ")
            new_phone = input("new phone of the contact: ")
            service.update_contact(name, new_name, new_phone)
        elif option == "4":
            name = input("enter contact name to search: ")
            contact = service.find_contact(name)
            if contact:
                print(contact)
            else:
                print("contact not found.")
        elif option == "5":
            contacts = service.list_contacts()
            for contact in contacts:
                print(contact)
        elif option == "6":
            print("exiting program.")
            break
        else:
            print("invalid option. try again.")


if __name__ == "__main__":
    main()
