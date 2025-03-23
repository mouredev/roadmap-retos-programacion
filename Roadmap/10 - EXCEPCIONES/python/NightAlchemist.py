'''
Exercise
'''

#exceptions

try:
    print(1/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Something else went wrong.")
finally:
    print("This always runs on success or failure.")
    
#raise exception

try:
    raise ValueError("This is an argument")
except ValueError as e:
    print(e)

#custom exceptions

class MyCustomError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
try:
    raise MyCustomError(2*2)
except MyCustomError as e:
    print("My exception occurred, value:", e.value)

'''
Extra
'''

# Custom exception
class CustomError(Exception):
    pass

# Function that processes parameters
def process_data(value):
    if not isinstance(value, int):
        raise TypeError("The value must be an integer.")
    if value < 0:
        raise ValueError("The value must be non-negative.")
    if value == 13:
        raise CustomError("13 is not an allowed value (unlucky number).")
    
    return value * 2  # some basic processing

# Call the function and handle exceptions
try:
    result = process_data(13)  # Try changing this value to test other cases
except Exception as e:
    print(f"An error occurred: {type(e).__name__} - {e}")
else:
    print(f"Success! The result is: {result}")
finally:
    print("Execution finished.")

'''
Examples You Can Try
process_data("a string") → Raises TypeError
process_data(-5) → Raises ValueError
process_data(13) → Raises CustomError
process_data(10) → Success, prints result
'''