"""
    EXCEPTIONS
"""

try:
    print(10 / 0)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"An error occurred: {e} ({type(e).__name__})")

"""
    EXTRA EXERCISE
"""

# Custom exception
class InvalidParameterError(Exception):
    pass


def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError("The list must contain at least 3 elements.")
    if parameters[1] == 0:
        raise ZeroDivisionError("The second element cannot be zero.")
    if type(parameters[2]) == str:
        raise InvalidParameterError("The third element cannot be a string.")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)


try:
    process_params([1, 2, 3, 4])
    #process_params([1, 0, 3, 4])
    #process_params([1, "a", 3, 4])
except IndexError as e:
    print(f"Index error: {e}")
except ZeroDivisionError as e:
    print(f"Division error: {e}")
except InvalidParameterError as e:
    print(f"Invalid parameter: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred.")
finally:
    print("Execution finished.")
