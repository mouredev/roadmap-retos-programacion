def verbose(func: callable) -> callable:

    def wrapper(*args, **kwargs):
        print(f"Llamamos a {func.__name__}() con argumentos: {args} y {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def main():
    print("===== MAIN =====")

    @verbose
    def suma(a: int, b: int) -> int:
        return a + b

    @verbose
    def resta(a: int, b: int) -> int:
        return a - b

    print(suma(1, 2))
    print(suma(a=1, b=3))
    print(resta(1, 2))


if __name__ == "__main__":
    main()
