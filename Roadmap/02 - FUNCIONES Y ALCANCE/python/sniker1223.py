# Functions
def noParameterNoReturn():
    print("Function no parameter and no Return!")
noParameterNoReturn()

# Function one parameter
def sayHello(name):
    print("Hello " + name + "!")
sayHello("Sniker")

# Function with return
def add(number1, number2):
    return number1+number2
print(f"Function with return: {add(1, 2)}")

# This function contains a function
def sayHelloAndAdd(name, number1, number2):
    sayHello(name)
    print(f"The add is: {add(number1, number2)}")
sayHelloAndAdd("Sniker", 5, 10)

def returnTheLargest(list):
    return max(list)

# global variable
myList = [3, 10, 1]
print(f"max() function: {returnTheLargest(myList)}")

# Lambda function to calculate the square of a number
def square(x): return x ** 2
print(f"Lambda function: {square(3)}")

# Challenge
def printTheChallenge(text1, text2):
    # local variable
    count = 0
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print(text1+text2)
        elif (i % 3 == 0):
            print(text1)
        elif (i % 5 == 0):
            print(text2)
        else:
            print(i)
            count += 1
    return count

print(f"Number of times the number has been printed: {
      printTheChallenge("Star", "Wars")}")
