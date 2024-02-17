from collections import deque


"""
    Stack methods for insert and recover items...
"""

print("Stack methods for insert and recover items...")

STACK: list[int] = [5, 8, 9, 4, 3, 2]

print("\nSTACK: list[int] = [5, 8, 9, 4, 3, 2]")

print("\nInsert an element at the end of the stack...")

STACK.append(10)

print(f"\nSTACK.append(10) --> STACK = {STACK}")

print("\nRecover an element of the stack...")

STACK_ELEMENT = STACK.pop()

print(f"\nSTACK.pop() --> STACK_ELEMENT = {STACK_ELEMENT}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Queue methods for insert and recover items...
"""

print("Queue methods for insert and recover items...")

MY_DEQUE: deque[str] = deque(["Hello", "World"])

print('\nMY_DEQUE: deque[str] = deque(["Hello", "World"])')

print("\nInsert an element at the end of the queue...")

MY_DEQUE.append("Python")

print(f'\nMY_DEQUE.append("Python") --> MY_DEQUE = {MY_DEQUE}')

print("\nRecover an element of the queue...")

DEQUE_ELEMENT = MY_DEQUE.popleft()

print(f"\nMY_DEQUE.popleft() --> DEQUE_ELEMENT = '{DEQUE_ELEMENT}'")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

# Stack exercise
print("Stack exercise...")

BROWSER_HISTORY: list[str] = []

while True:
    print(f"\nBrowser history --> {BROWSER_HISTORY}")

    try:
        OPERATION: str = input(
            "\nEnter an operation ('Back', 'Forward', or 'Exit'): "
        ).upper()
    except KeyboardInterrupt:
        OPERATION: str = ""

    if OPERATION == "BACK":
        if len(BROWSER_HISTORY) > 0:
            BROWSER_HISTORY.pop()
    elif OPERATION == "FORWARD":
        LAST_PAGE_NUMBER: str = (
            BROWSER_HISTORY[len(BROWSER_HISTORY) - 1][-2:]
            if (len(BROWSER_HISTORY) > 0)
            else "0"
        )
        BROWSER_HISTORY.append(f"Page {int(LAST_PAGE_NUMBER) + 1}")
    elif OPERATION == "EXIT":
        break

# Queue exercise
print("\nQueue exercise...")

DOCUMENTS: deque[str] = deque()

while True:
    print(f"\nDocuments --> {DOCUMENTS}")

    try:
        USER_INPUT: str = input(
            "\nAdd a document to print, or write 'Print' to print the document in the queue: "
        )
    except KeyboardInterrupt:
        USER_INPUT: str = ""

    USER_INPUT_FORMATTED = USER_INPUT.upper()

    if USER_INPUT_FORMATTED == "PRINT":
        if len(DOCUMENTS) > 0:
            PRINTED_DOCUMENT: str = DOCUMENTS.popleft()
            print(f"\nPrinted document --> '{PRINTED_DOCUMENT}'")
    elif USER_INPUT_FORMATTED == "EXIT":
        break
    elif USER_INPUT_FORMATTED != "":
        DOCUMENTS.append(USER_INPUT)
