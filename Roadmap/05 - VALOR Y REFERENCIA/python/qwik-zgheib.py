# -- exercise --
# assignment by value
a: int = 5
b: int = a
b = 10
print(f"a: {a}, b: {b}")

# assignment by reference
list_i: list[int] = [1, 2, 3]
list_ii: list = list_i
list_ii.append(4)
print(f"list_i: {list_i}, list_ii: {list_ii}")


def modify_value(num: int) -> None:
    num = 10
    print(f"num in modify_value: {num}")


def modify_reference(lista) -> None:
    lista.append(4)


# "by value" with an integer (immutable)
x: int = 5
modify_value(x)
print(f"x after modify_value: {x}")

# "by reference" with a list (mutable)
list_numbers: list[int] = [1, 2, 3]
print(f"list before modify_reference: {list_numbers}")
modify_reference(list_numbers)
print(f"list after modify_reference: {list_numbers}")


# -- extra challenge --
print("\n------ extra challenge ------")


# parameters exchange
class ValueSwapper:
    def swap(self, x, y):
        return y, x


class ReferenceSwapper:
    def swap(self, lista1, lista2):
        lista1[:], lista2[:] = lista2[:], lista1[:]


def main():
    # values by value
    a: int = 1
    b: int = 2
    swapper_val = ValueSwapper()
    a_new, b_new = swapper_val.swap(a, b)
    print(f"Original a: {a}, b: {b}")
    print(f"Swapped a_new: {a_new}, b_new: {b_new}")
    # values by reference
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    swapper_ref = ReferenceSwapper()
    swapper_ref.swap(list_1, list_2)
    print(f"Original list_1: {list_1}, list_2: {list_2}")


if __name__ == "__main__":
    main()
