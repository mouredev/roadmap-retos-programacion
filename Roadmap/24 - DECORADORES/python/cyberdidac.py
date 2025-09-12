def count_calls(func):
    def wrapper():
        wrapper.count += 1
        print(f"La función {func.__name__} ha sido llamada {wrapper.count} veces")
        return func()

    wrapper.count = 0
    return wrapper


@count_calls
def say_hello():
    print("Hola!")


def main():
    say_hello()
    say_hello()


if __name__ == '__main__':
    main()
