class C1:

    def __init__(self, value = "example"):
        self.c1_string = value

    def get_c1_string(self):
        return self.c1_string

    def set_c1_string(self, value):
        self.c1_string = value

    def __str__(self):
        return f"Class 1 value: {self.c1_string}"


class C2:

    def __init__(self, value = "example"):
        self.c2_string = value

    def get_c2_string(self):
        return self.c2_string

    def set_c2_string(self, value):
        self.c2_string = value

    def __str__(self):
        return f"Class 2 value: {self.c2_string}"


if __name__ == "__main__":

    example1 = C1()
    print(example1)
    example1.set_c1_string("Example 1")
    print(example1.get_c1_string())

    example2 = C2()
    print(example2)
    example2.set_c2_string("Example 2")
    print(example2.get_c2_string())
