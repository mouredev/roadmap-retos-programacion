from functools import wraps

#Exercise

def operator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print("Finished.")
        return result
    return wrapper

@operator
def add(a, b):
    return a + b

print(add(3, 4))

@operator
def multi(*nums):
    if not nums:
        return 0
    total = 1
    for num in nums:
        total *= num
    return total
    
print(multi(2, 5, 7))
print(multi(8, 4, 1, 9))

@operator
def greet(name: str):
    return f"Hi {name}, how are you today?" 

print(greet("Holly"))


#Extra Exercise

def counting_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} called {wrapper.calls} times")
        return func(*args, **kwargs)
    
    wrapper.calls = 0
    return wrapper

@counting_calls
def ice_cream_shop(flavour):
    print(f"Your {flavour} ice cream is ready. Enjoy it ! :)")


ice_cream_shop("Vanilla")
ice_cream_shop("Chocolate")
ice_cream_shop("Cream and cookies")

#Creating a different function to verify it takes its own counter

@counting_calls
def multi_counted(*nums):
    if not nums:
        return 0
    total = 1
    for num in nums:
        total *= num
    return total
    
print(multi_counted(2, 5, 7))
print(multi_counted(8, 4, 1, 9))
print(multi_counted(23, 45, 2))
print(multi_counted(3, 56, 4))