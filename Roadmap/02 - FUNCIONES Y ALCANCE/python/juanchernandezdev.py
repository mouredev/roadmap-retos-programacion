### Python Functions And Scope ###

#! Function Without Parameters

def my_func():
  print('Hello I\'m a function')
  
my_func()

#! Function Without Parameters or Return
def empty_func():
  pass

#! Function With Parameters

num_one = 1
num_two = 5

def add(num1, num2):
  print(num1 + num2)
  
add(num_one, num_two)

#! Function With Return

num_one = 1
num_two = 5

def add(num1, num2):
  return num1 + num2

my_sum = add(num_one, num_two)

print(my_sum)

#! Function Inside Another Function

def top_function():
  my_num = 20
  num_one = 5
  num_two = 10
  
  def inside_function(first_num, second_num):
    sum = first_num + second_num
    return sum
  
  inside_func_val = inside_function(num_one, num_two)
  
  print(inside_func_val + my_num)
  
top_function()

#! Python Built In Functions

# Range
my_range = range(1, 10)
print(*my_range)

# List
my_list = list(my_range)
print(my_list)

# Sorted
print(sorted(my_list))

# Len
print(len(my_list))

# Sum
print(sum(my_list))

# Max
print(max(my_list))

# Min
print(min(my_list))

# Round
print(round(20.85))

# Slice
print(my_list[1:4])

# Int
print(int('8'))

# Str
print(str(10))

# Type
print(type(int('8')))
print(type(str(10)))

#! Functions Global Scope

num_one = 50 # Global variable
num_two = 25 # Global variable

def function_global_vars():
  return num_one + num_two

print(function_global_vars())

num_one = 50 # Global variable
num_two = 25 # Global variable

def function_global_vars():
  num_one = 25 # Local variable
  num_two = 10 # Local variable
  
  return num_one + num_two

print(function_global_vars())

#! Functions Local Scope

def function_local_vars():
  num_one_local = 15
  num_two_local = 8
  
  return num_one_local - num_two_local

print(function_local_vars())

#* print(num_one_local) will throw an error since the variable is declared inside a function local scope

#! Lambda Functions

sum = lambda first_num, second_num: first_num + second_num
print(sum(10, 50))

sum_two = lambda first_num, second_num: first_num + second_num + 60
print(sum_two(10, 50))

def function_with_lambda(first_arg, second_arg):
  lam_sum = lambda first_lam_arg, second_lam_arg: first_lam_arg + second_lam_arg * 30
  return lam_sum(first_arg, second_arg) + 500

print(function_with_lambda(125, 500))

#! Optional Challenge
print('---Optional Challenge----')

def fizz_buzz_twist(txt1: str, txt2: str):
  times_when_num = 0
  
  for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
      print(f'{txt1} and {txt2}.')
    elif num % 3 == 0:
      print(f'{txt1}.') 
    elif num % 5 == 0:
      print(f'{txt2}.')
    else:
      times_when_num += 1
    
  return times_when_num

print(fizz_buzz_twist('It\'s multiple of 3', 'It\'s multiple of 5'))
      
  
