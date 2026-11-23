import os

"""
    FILES
"""

file = os.path.join(os.path.dirname(__file__), "elhdrond.txt")

with open(file, "w") as f:
    f.write("Sergio Cardo\n")
    f.write("35\n")
    f.write("Python\n")

with open(file, "r") as f:
    print(f"File contents:\n{f.read()}")

os.remove(file)


"""
    EXTRA EXERCISE
"""

shop_file = os.path.join(os.path.dirname(__file__), "elhdrond_bookshop.txt")
open(shop_file, "a").close()


def find_book(title: str) -> str | None:
    with open(shop_file, "r") as f:
        for line in f:
            if line.split(", ")[0] == title:
                return line.strip()
    return None


def input_title(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Title cannot be empty.")


def input_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Must be a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def input_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


running = True
while running:
    print("\n--- Book Shop ---")
    print("1. Add book")
    print("2. Look up book")
    print("3. Update book")
    print("4. Delete book")
    print("5. List all books")
    print("6. Total sales")
    print("7. Sales by book")
    print("8. Quit")

    option = input("Select an option: ").strip()

    match option:
        case "1":
            title = input_title("Title: ")
            quantity = input_int("Quantity sold: ")
            price = input_float("Price: ")
            with open(shop_file, "a") as f:
                f.write(f"{title}, {quantity}, {price}\n")
            print(f"'{title}' added.")

        case "2":
            title = input_title("Title: ")
            book = find_book(title)
            if book:
                print(book)
            else:
                print(f"'{title}' not found.")

        case "3":
            title = input_title("Title: ")
            if not find_book(title):
                print(f"'{title}' not found.")
            else:
                quantity = input_int("New quantity sold: ")
                price = input_float("New price: ")
                with open(shop_file, "r") as f:
                    lines = f.readlines()
                with open(shop_file, "w") as f:
                    for line in lines:
                        if line.split(", ")[0] == title:
                            f.write(f"{title}, {quantity}, {price}\n")
                        else:
                            f.write(line)
                print(f"'{title}' updated.")

        case "4":
            title = input_title("Title: ")
            if not find_book(title):
                print(f"'{title}' not found.")
            else:
                with open(shop_file, "r") as f:
                    lines = f.readlines()
                with open(shop_file, "w") as f:
                    for line in lines:
                        if line.split(", ")[0] != title:
                            f.write(line)
                print(f"'{title}' deleted.")

        case "5":
            with open(shop_file, "r") as f:
                contents = f.read()
            print(contents if contents else "No books in stock.")

        case "6":
            total = 0
            with open(shop_file, "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    total += int(parts[1]) * float(parts[2])
            print(f"Total sales: £{total:.2f}")

        case "7":
            title = input_title("Title: ")
            book = find_book(title)
            if book:
                parts = book.split(", ")
                total = int(parts[1]) * float(parts[2])
                print(f"Sales for '{title}': £{total:.2f}")
            else:
                print(f"'{title}' not found.")

        case "8":
            os.remove(shop_file)
            print("Shop closed. Goodbye!")
            running = False

        case _:
            print("Invalid option. Please select a number between 1 and 8.")