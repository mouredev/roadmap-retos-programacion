# Exercise
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"An error occurred: {error}")


try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as error:
    print(f"An error occurred: {error}")


# Extra
class CustomException(Exception):
    pass


def process(param):
    if param < 0:
        raise ValueError("Negative value")
    elif param > 100:
        raise OverflowError("Value too large")
    elif param == 42:
        raise CustomException("Don't like 42")


def main():
    try:
        param = int(input("Enter a number: "))
        process(param)
        print("No error occurred.")
    except ValueError as error_message:
        print(f"Caught an error: {error_message}")
    except OverflowError as error_message:
        print(f"Caught an error: {error_message}")
    except CustomException as error_message:
        print(f"Caught an error: {error_message}")
    finally:
        print("Execution has finished.")


if __name__ == "__main__":
    main()
