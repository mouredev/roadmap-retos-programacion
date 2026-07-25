#Exercise

try:
    print(13/0)
except ZeroDivisionError:
    print("Cannot divide by zero")


#Extra exercise

class NegativeNumberError(Exception):
    """Raised when the input number is negative."""
    pass


def div_except(num: int):
    try:
        if not isinstance(num, int):
            raise ValueError("Only integers are allowed.")
        if num < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")
        
        result = 23 / num
        print(f"Result: {result}")

    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except NegativeNumberError as e:
        print("CustomError:", e)
    else:
        print("No error occurred.")
    finally:
        print("Execution finished.\n")

div_except(0)     # ZeroDivisionError
div_except(-3)    # Custom error
div_except("a")   # ValueError
div_except(10)    # Works fine
