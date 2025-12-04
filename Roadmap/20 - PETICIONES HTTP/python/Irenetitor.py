#Exercise

def greet():
    print("Hello everyone")   # Function with no parameters and no return value


def my_name(name):
    print(f"Hello {name}")
print(my_name("Robert"))   # Function with one parameter, no return value

def my_number(number):
    return number * 2
print(my_number(3))   #Function with a return value

def my_profile(name, surname):
    print(f"My name is {name} {surname}")
print(my_profile("Marco", "Lee"))      # Function with two parameters

 
def my_profile2(name, surname):
    print(f"My surname is {surname} and my name {name}")
my_profile2(surname="Casas", name="Carol")  # We use named arguments so the order does not matter

def my_pet(pet = "dog"):
    print(f"My pet is a {pet}")      #Function with a default parameter
my_pet()

def categories():
    return "First", "Second", "Third"
one, two, three = categories()      #Function with multiple returns
print(one)
print(two)
print(three)

def my2_pet(animal = "cat", name = "Kuba"):
    print(f"My pet {name} is a {animal}")      #Function with argument(key = value)
my2_pet()

def my3_pet(**names):
    print("My pets list : ")
    for pet, animal in names.items():
        print(f"{pet} : {animal}")       #Function with a variable number of arguments (key = value)

my3_pet(
    pet1="Cat",
    pet2="Rabbit",
    pet3="Canary",
    pet4="Spider",
    pet5="Dog"
)

def participants(*names):
    print(f"The participants of this musical edition are : ")          
    for name in names:                   #Function with a variable number of arguments
        print(f" {name}")         
participants("- Julia", "- Cora", "- Marco", "- Jade", "- Tomas")

#Nested Functions
def outer_func():
    def inner_func():
        print(f"The outer function is calling correctly the inner function")
    inner_func()
outer_func()

#Built-in Functions
print(len("Pollution"))
print(type(4))
print("Magnitude".upper())
print("GOAL".lower())
print(max(3, 5, 8))
print(min(3, 1, 4))
print("granada".capitalize())
print(" This is fun ".strip())
print(round(5.3))
print("Cherry,Mango,Pear".split(","))
print(callable(print))
print(isinstance(5, float))
print(abs(-10))
print(pow(2, 3))


#Local and Global variables
variable = "Luca"  #Global

print(variable)

def greeting():
    print(f"Hi, {variable}!")
greeting()

def greeting2():
    variable = "Ramses"  #Local
    print(f"Hi, {variable}")
greeting2()


#Extra Exercise
