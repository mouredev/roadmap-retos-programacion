#Basic decorator
def my_decorator(function):
    def my_wrapper(*args,**kwargs):
        print("Initialize wrapper")
        result = function(*args,**kwargs)
        print("Finishing wrapper")
        return result

    return my_wrapper    

@my_decorator
def suma(a,b):
    return a + b

print(suma(2,3))

#Extra
def my_decorator2(function):
    execution = 0
    def my_wrapper2(*args,**kwargs):
        nonlocal execution
        execution += 1
        function(*args,**kwargs)
        return execution
    return my_wrapper2

@my_decorator2
def multiply(value1,value2):
    print(f'Value of multiplication {value1 * value2}')

print(f'Number of executions {multiply(4,2)}')
print(f'Number of executions {multiply(8,7)}')
