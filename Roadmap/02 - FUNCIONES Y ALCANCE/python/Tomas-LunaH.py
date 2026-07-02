'''Functions'''
#Simple

def greet ():
    print("Hi, Python ")

greet()

#Function with return

def return_greet():
    return "Hi Python"

print(return_greet())

#with aurgemnts
def arg_greet(name):
    print(f"Hi {name}")
arg_greet("tomas")

#several arguments
def args_greet(greet, name):
    print(greet , name)
args_greet("hello", "tomas")

#default argument
def default_greet(name = "Python"):
    print(f"Hello {name}")
default_greet("tomas")

#with arguments and returns
def return_args_greet(greet, name):
    return f"{greet}, {name}"
print (return_args_greet("Hello", "Tomas"))


#return with several values
def multiple_return_greet():
    return "Hello" , "Python"
greet, name = multiple_return_greet()
print(greet)
print(name)

#with a viable number of arguments
def mult_numbe_greet(*names):
    for name in names:
        print(f"Hello, {name}")
mult_numbe_greet("tomas", "luna", "juan")

#With viable numbers e and keywords
def mult_numb_key_greet(**names):
    for key, values in names.items():
        print(f" {values} ({key})")


mult_numb_key_greet(
    lenguaje = "Python",
    name="tomas",
    alias ="tomy",
    age = 19
    )

#function within functions

def outer_function():
    def inner_function():
        print("Fuction inner: Hello, Python")
    inner_function()

outer_function()

#Functions Lenguages
#Print it's used to printing on screen
print("Tomas")

#len it's used to count elements
print(len("tomas"))

#input it's used to request date from user
name= str(input("enter your  name: "))
print(f"hi ,{name}")

#type it's used to determine  data type
print(type(36))

#int it's used to convert integer
number = int("10")
print(number)

#float it's used to convert decimal
num_decimal = float(10)
print(num_decimal)

#str it's used to convert text
text = 10
print(str(text))

#bool it-s used to convert bolean
print(bool(1))
print(bool(0))

#list it's used to convert lists
lenguage = "python"
print(list(lenguage))

#tuple it's used to convert tuple
tple = [1,2,3]
print(tuple(tple))

#set it's used to remove duplcates
list_num = [1,2,3,4,2,4,1,5]
print(set(list_num))

#dict used to create ductionaries
person = dict(name = "tomas", age = 20)
print(person)

#range it's used to generate sequences
for n in range(1,6):
    print(n)

#sum it's used to add elements
sum_elements = [1,2,3,4]
print(sum(sum_elements))

#max it's used to determine value maximum
max_number = [1,10,25,90] 
print(max(max_number))

#min it's used to determine value minimum
min_number =[1,0,78,10,0.1]
print(min(min_number))

#abs it's used to determine absolute value
print(abs(-100))

#round it's used to round decimal numbers
print(round(4.15686,2))

#pow it's used for exponent numbers
print(pow(3,2))

#sorted it's used to order
list_desorder = [1,2,9,8,5]
print(sorted(list_desorder))

#reversed it's used to reverse elements
num_rever = [1,2,3]
print(list(reversed(num_rever))) 

#enumerate it's used to list elements
fruts = {"grape","pineapple"}
for indice,frut in enumerate(fruts):
    print(indice,fruts)

#zip it's used to join list
list_names = ["Tomas","Juan"]
list_age = [20,30]
print(list(zip(list_names,list_age))) 

#map it's used to apply functions
numbers_lam = [1,2,3]
resul = list(map(lambda x: x*2, numbers_lam))
print(resul)

# it's used to fliter elemntos
numbers_fl = [1,2,3,4,5,6]
pars = list(filter(lambda x: x % 2 == 0,numbers_fl ))
print(pars)

#all It is used to verify if everything is true
true = [True, False, True]
print(all(true))

#any it's used to verify if at least one is true
numers_any = [True, False, False]
print (any(numers_any))

#id it's used to show de directions object
object_direc = "Python"
print(id(object_direc))

#open it's used to open flies
file = open("text.txt", "w")



'''Extra'''
def return_number(nummlt3 , nummlt5):
    count=0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{nummlt3} and  {nummlt5}") 
        elif number % 3 == 0:
            print( nummlt3)
        elif number % 5 == 0:
            print( nummlt5)
        else:
            print(number)
            count += 1
    return count
print (return_number("it's multipl of 3", "it's multipl of 5" ))