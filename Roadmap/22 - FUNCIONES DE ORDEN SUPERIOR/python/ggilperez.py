# higher-order functions
import time


def sum_nums(num_1: int, num_2: int) -> int:
    return num_1 + num_2


def higher_order_function(num_1: int, num_2: int, func):
    start = time.time()
    result = func(num_1, num_2)
    end = time.time()
    print(f"{func.__name__}({num_1}, {num_2}) = {result}. Function time: {end - start:.2f}")
    return result


print(higher_order_function(1, 2, sum_nums))

# EXTRA

