#Function without parameters and without return
def say_hello():
    print("Function without parameters and return!")
    
say_hello()    

#Function with parameters and return 
def sum_numbers(a,b):
    return a + b

print("Result function with parameters and return: " + str(sum_numbers(3,5)))

#Function with parameters but no return

def print_sum_numbers(a,b):
    print("Result is: " + str(a+b))
    
print("Function with parameters but no return :")
print_sum_numbers(2,3)    

#Function with default parameter

def default_parameter(phrase = "Default parameter"):
    return phrase
    
print("Function with default parameter: ",default_parameter())
print("Function with default parameter: ",default_parameter("Modify default parameter"))


#Lambda function

f = lambda: "Message from a lambda function"

print("Lambda function : " + str(f()) )   

#Function with multiple arguments

def multiple_arguments(*args):
    for pos,argument in enumerate(args):
        print("Argument in pos: " + str(pos) +" "+ str(argument))
print("Function with multiple arguments: ")
multiple_arguments("Hello")
multiple_arguments("Open","Close")        
        
def multiple_arguments_keyword(**kargs):
    for key in kargs:
        print("Parameter key: " + str(key) + " parameter: " + str(kargs[key]))
        
multiple_arguments_keyword(string_parameter="Hi", number_parameter=5)       


def wrap_function():
    
    a = 5 

    def nested_function():
        return a**2
    
    result = nested_function()
    return result

print("Result of wrap/nested function: " + str(wrap_function()))

GLOBAL_VARIABLE = 3

number_variable = 3

def modify_variable():
    number_variable = 6
    print("Value is: ",number_variable)

modify_variable()
print("Value is: ", number_variable)    

#Language functions

text = "This is a text"
print("Funcrion Len:" + str(len(text)))

print("Uppercase function: ",  text.upper())



number_list = [5,2,6,16,7,3]
filtered_list = filter(lambda x: x%2 == 0,number_list)
print("Filter and list function", list(filtered_list))

def extra_exercise(arg1,arg2):
    
    counter = 0
    
    for number in range(1,101):
        
        if number % 3 == 0 and number % 5 == 0:
            print(arg1+arg2)
        elif number % 3 == 0:
            print(arg1) 
        elif number % 5 == 0:
            print(arg2)
        else:
            print(number)
            counter+=1
    return counter

numbers = extra_exercise("fizz","buzz")
print(numbers)        
            
    