import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def first_prime_in_range(end: int) -> int:
    for num in range(0, end + 1):
        if is_prime(num):
            return num
    return -1  # Return -1 if no prime number is found


def main():
    sauron = 1
    dwarves = 0
    elfs = 0
    men = 0

    try:
        rings = int(input("> "))
        rings -= 1

        dwarves = first_prime_in_range(rings) if first_prime_in_range(rings) != -1 else 0
        rings -= dwarves

        if dwarves != 0 and rings % 2 != 0:
            elfs = math.ceil(rings / 2)
            men = rings - elfs

            print(f"Sauron - {sauron}")
            print(f"Enanos - {dwarves}")
            print(f"Elfos - {elfs}")
            print(f"Hombres - {men}")
        else:
            print("No se ha podido hacer el reparto")

    except Exception as e:
        print("Número incorrecto")


if __name__ == '__main__':
    main()
