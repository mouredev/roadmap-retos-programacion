"""Module for HEAP structure"""
import heapq
from collections import deque


"""
    Structures...
"""

# List - Array of elements
LIST = [1, 2, 3]
print("List structure: <LIST NAME> = [<ELEMENTS...>]")
print(f"LIST = [1, 2, 3] --> LIST = {LIST}")

# Tuple - Immutable array of elements
TUPLE = (1, 2, 3)
print("\nTuple structure: <TUPLE NAME> = (<ELEMENTS...>)")
print(f"TUPLE = (1, 2, 3) --> TUPLE = {TUPLE}")

# Set - Collection of unique elements
SET = {"first", "second", "third"}
print("\nSet structure: <SET NAME> = {<ELEMENTS...>}")
print("SET = {'first', 'second', 'third'} --> SET =", SET)

# Dictionary - An object like JavaScript
DICTIONARY = {
    "first_name": "Lucas",
    "last_name": "Hoz",
}
print("\nDictionary structure: <DICTIONARY NAME> = {<PROPERTIES...>}")
print(
    "DICTIONARY = { 'first_name': 'Lucas', 'last_name': 'Hoz' } --> DICTIONARY =",
    DICTIONARY,
)

# Heap - Binary tree
HEAP = [1, 5, 3, 4, 2, 8, 7, 9]
heapq.heapify(HEAP)
print("\nHeap structure: <HEAP NAME> = [<ELEMENTS...>]; heapq.heapify(<HEAP NAME>)")
print(f"HEAP = [1, 5, 3, 4, 2, 8, 7, 9]; heapq.heapify(HEAP) --> HEAP = {HEAP}")

# Stacks and Queues
STACK = deque([20, 21, 22])
print("\nStack structure: <STACK NAME> = deque([<ELEMENTS...>])")
print(f"STACK = deque([20, 21, 22]) --> STACK = {STACK}")


print(
    "\n# ---------------------------------------------------------------------------------- #"
)

"""
    Insert, delete, update, and sort operations
"""

MY_LIST = [1, 2, 3]

MY_TUPLE = (1, 2, 3)

MY_SET = {"first", "second", "third"}

MY_DICTIONARY = {
    "first_name": "Lucas",
    "last_name": "Hoz",
}


# Insert an element at the end of a List structure
MY_LIST.append(4)
print(
    "\nInsert an element at the end of a List structure: <LIST NAME>.append(<ELEMENT>)"
)
print(f"[1, 2, 3].append(4) --> MY_LIST = {MY_LIST}")

# Delete an element of a List structure
MY_LIST.remove(2)
print(
    "\nDelete an element of a List structure: <LIST NAME>.remove(<ELEMENT TO DELETE>)"
)
print(f"[1, 2, 3, 4].remove(2) --> MY_LIST = {MY_LIST}")

# Update an element of a List structure
MY_LIST[1] = 3 * 2
print(
    "\nUpdate an element of a List structure: <LIST NAME>[<INDEX OF THE ELEMENT TO UPDATE>] = <NEW VALUE>"
)
print(f"[1, 3, 4][1] = 3 * 2 --> MY_LIST = {MY_LIST}")

# Sort elements of a List structure
MY_LIST.sort(reverse=True)
print("\nSort elements of a List structure: <LIST NAME>.sort(<ARGUMENTS...>)")
print(f"[1, 6, 4].sort(reverse=True) --> MY_LIST = {MY_LIST}")


# Insert an element in a Set structure
MY_SET.add("fourth")
print("\nInsert an element in a Set structure: <SET NAME>.add(<ELEMENT>)")
print("{'first', 'second', 'third'}.add('fourth') --> MY_SET =", MY_SET)

# Delete an element of a Set structure
MY_SET.discard("second")
print("\nDelete an element of a Set structure: <SET NAME>.add(<ELEMENT>)")
print("{'first', 'second', 'third', 'fourth'}.discard('second') --> MY_SET =", MY_SET)


# Insert an property in a Dictionary structure
MY_DICTIONARY["country"] = "Argentina"
print(
    "\nInsert an property in a Dictionary structure: <DICTIONARY NAME>[<KEY OF THE NEW PROPERTY>] = <VALUE OF THE NEW PROPERTY>"
)
print(
    "{ 'first_name': 'Lucas', 'last_name': 'Hoz' }['country'] = 'Argentina' --> MY_DICTIONARY =",
    MY_DICTIONARY,
)

# Delete a property of a Dictionary structure
MY_DICTIONARY.pop("last_name")
print(
    "\nDelete a property of a Dictionary structure: <DICTIONARY NAME>.pop(<KEY OF THE PROPERTY TO DELETE>)"
)
print(
    "{ 'first_name': 'Lucas', 'last_name': 'Hoz', 'country': 'Argentina' }.pop('last_name') --> MY_DICTIONARY =",
    MY_DICTIONARY,
)

# Update a property of a Dictionary structure
MY_DICTIONARY.update({"first_name": "Nahuel"})
print(
    "\nUpdate a property of a Dictionary structure: <DICTIONARY NAME>.update({ <KEY OF THE PROPERTY TO UPDATE>: <NEW VALUE> })"
)
print(
    "{ 'first_name': 'Lucas', 'country': 'Argentina' }.update({ 'first_name': 'Nahuel' }) --> MY_DICTIONARY =",
    MY_DICTIONARY,
)


print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

CONTACTS: list[dict[str, str]] = []


def find_contact_index(name: str):
    """Find index of the contact using the name"""
    i = 0
    for contact in CONTACTS:
        if contact["name"].upper() == name.upper():
            return i
        i += 1

    return -1


def get_contact_name(message: str, message_on_invalid: str, should_exist: bool):
    """Get contact name from an input"""
    name = input(message)
    if name == "":
        return ""

    while (
        find_contact_index(name=name) == -1
        if should_exist
        else find_contact_index(name=name) != -1
    ):
        name = input(message_on_invalid)
        if name == "":
            break

    return name


def get_contact_phone_number(message: str, message_on_invalid: str):
    """Get contact name from an input"""
    phone_number = input(message)
    if phone_number == "":
        return ""

    while not is_valid_phone_number(phone_number):
        phone_number = input(message_on_invalid)
        if phone_number == "":
            break

    return phone_number


def is_valid_phone_number(phone_number: str):
    """Check if phone number is a valid one"""
    return len(phone_number) <= 11 and phone_number.isdigit()


EXIT = False

while not EXIT:
    OPERATION = input(
        "Select an operation ('Show', 'Find', 'Insert', 'Update', 'Delete' or 'Exit'):"
    ).upper()

    if OPERATION == "SHOW":
        print(f"Contacts: {CONTACTS}")
    elif OPERATION == "FIND":
        NAME = get_contact_name(
            message="Enter the name of the contact:",
            message_on_invalid="The contact doesn't exists! Enter another name:",
            should_exist=True,
        )
        if NAME == "":
            continue

        PHONE_NUMBER = CONTACTS[find_contact_index(name=NAME)]["phone_number"]
        print(f"Contact info: {NAME} / {PHONE_NUMBER}")

    elif OPERATION == "INSERT":
        NAME = get_contact_name(
            message="Enter the name of the new contact:",
            message_on_invalid="The contact already exists! Try with another name:",
            should_exist=False,
        )
        if NAME == "":
            continue

        PHONE_NUMBER = get_contact_phone_number(
            message="Enter the phone number of new contact:",
            message_on_invalid="Invalid phone number! Enter a valid one:",
        )
        if PHONE_NUMBER == "":
            continue

        CONTACTS.append({"name": NAME, "phone_number": PHONE_NUMBER})
        print("Contact inserted!")

    elif OPERATION == "UPDATE":
        NAME = get_contact_name(
            message="Enter the name of the contact to update:",
            message_on_invalid="The contact doesn't exists! Enter another name:",
            should_exist=True,
        )
        if NAME == "":
            continue

        NEW_NAME = get_contact_name(
            message="Enter the new name:",
            message_on_invalid="There is a contact with this name! Try another one:",
            should_exist=False,
        )
        if NEW_NAME == "":
            continue

        NEW_PHONE_NUMBER = get_contact_phone_number(
            message="Enter the new phone number:",
            message_on_invalid="Invalid phone number! Enter a valid one:",
        )
        if NEW_PHONE_NUMBER == "":
            continue

        CONTACTS[find_contact_index(name=NAME)] = {
            "name": NEW_NAME,
            "phone_number": NEW_NAME,
        }
        print("Contact updated!")

    elif OPERATION == "DELETE":
        NAME = get_contact_name(
            message="Enter the name of the contact to delete:",
            message_on_invalid="The contact doesn't exists! Enter another name:",
            should_exist=True,
        )
        if NAME == "":
            continue

        del CONTACTS[find_contact_index(name=NAME)]
        print("Contact deleted!")

    elif OPERATION == "EXIT":
        EXIT = True
        print("Program finished!")
