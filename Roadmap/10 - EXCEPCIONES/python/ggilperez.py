# 10 Exceptions


# Complete structure
try:
    pass  # Some error may occurs
except Exception:
    pass  # The error is caught
else:
    pass  # If no error happens, continue with this code
finally:
    pass  # Always execute this code

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(f"The division is {result}")
finally:
    print("Ending program")
print()


# Extra

class NotKwargsError(Exception): pass


def func(*args, **kwargs):
    print(args[0])  # May raise IndexError

    print(int(args[0]))  # May raise ValueError

    if not kwargs:
        raise NotKwargsError("Kwargs are mandatory")  # Custom exception

# 1st Exception
print("1st Exception")
try:
    func()
except Exception as e:
    print(f"An error occurs: ({e.__class__.__name__}): {e.__str__()}")
else:
    print("Function ended without errors")
finally:
    print("Ending program")
print()

# 2nd Exception
print("2nd Exception")
try:
    func("foo bar")
except Exception as e:
    print(f"An error occurs: ({e.__class__.__name__}): {e.__str__()}")
else:
    print("Function ended without errors")
finally:
    print("Ending program")
print()

# 3rd Exception (Custom)
print("3rd Exception (Custom)")
try:
    func(1)
except Exception as e:
    print(f"An error occurs: ({e.__class__.__name__}): {e.__str__()}")
else:
    print("Function ended without errors")
finally:
    print("Ending program")
print()

# All OK
print("All OK")
try:
    func(1, one=1)
except Exception as e:
    print(f"An error occurs: ({e.__class__.__name__}): {e.__str__()}")
else:
    print("Function ended without errors")
finally:
    print("Ending program")
print()
