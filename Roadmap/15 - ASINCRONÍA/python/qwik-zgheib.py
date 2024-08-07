import time


# -- synchronous exercise
def function_async(name: str, seconds: int) -> None:
    print(f"{name} starts")
    time.sleep(seconds)
    print(f"{name} ends")


function_async("A", 3)


# -- extra challenge
function_async("C", 3)
function_async("B", 2)
function_async("A", 1)
function_async("D", 1)
