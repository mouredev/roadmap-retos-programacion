import os


def show_name() -> None:
    print("Kevin ED11")


print_name = lambda: print("Kevin ED11")


def full_name(first_name: str, last_name: str) -> None:
    print(f"{first_name} {last_name}")


def sum(a: int, b: int) -> int:
    return a + b


def check_server_password(password: str) -> bool:
    correct_password = os.getenv("PASSWORD", "mouredev")

    def is_correct_password() -> bool:
        return password == correct_password

    return is_correct_password()


cities = ["Madrid", "Barcelona", "Valencia"]


def get_cities() -> list:
    global cities
    return cities


def set_citie(citie: str) -> None:
    global cities
    cities += [citie]


def counter(init: str, end: str) -> int:
    intern_counter = 0

    for n in range(1, 101):
        if n % 15 == 0:
            print(init + end)
        elif n % 5 == 0:
            print(end)
        elif n % 3 == 0:
            print(init)
        else:
            print(n)
            intern_counter += 1

    return intern_counter


if __name__ == "__main__":
    show_name()
    print_name()
    full_name("Kevin", "ED11")
    print(sum(1, 2))
    print(check_server_password("mourede"))
    print(get_cities())
    set_citie("Sevilla")
    print(get_cities())
    print(counter("a", "b"))
