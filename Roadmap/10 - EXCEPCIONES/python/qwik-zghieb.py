# -- exercise
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"err: {e}"
    except Exception as e:
        return f"err: {e}"
    finally:
        print("the execution has finished")


def access_list_element(l, i):
    try:
        return l[i]
    except IndexError as e:
        return f"err: {e}"
    except Exception as e:
        return f"err: {e}"
    finally:
        print("the execution has finished")


print(divide(10, 0))
print(access_list_element([1, 2, 3], 4))


# -- extra challenge
def process_parameters(a, b, c):
    if a < 0:
        raise ValueError("a must be positive")
    elif b < 0:
        raise ValueError("b must be positive")
    elif c < 0:
        raise ValueError("c must be positive")
    return a + b + c


print("------ extra challenge ------")

try:
    print(process_parameters(1, 2, 3))
except ValueError as e:
    print(f"err: {e}")
except Exception as e:
    print(f"err: {e}")
finally:
    print("the execution has finished")
