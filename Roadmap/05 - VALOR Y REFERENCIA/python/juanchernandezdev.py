### Python Value and Reference ###

#! Variables By Reference

my_list = [1, 4, 5, 3, 6, 8]
my_list_second = my_list
my_list_second.remove(8)
print(my_list)
print(my_list_second)

def more_items(list):
  list.append(10)
  
more_items(my_list)
print(my_list)

more_items(my_list_second)
print(my_list_second)

#! Variables By Value

my_num = 55
my_num_second = my_num
my_num_second = 60
print(my_num)
print(my_num_second)

my_str = 'Hello Python.'
my_str_second = my_str
my_str_second = 'Hello Python, And Hello World!!'
print(my_str)
print(my_str_second)

def my_sum(num_one, num_two):
  return num_one + num_two

print(my_sum(10, 5))

#! Optional Challenge

num_a = 50
num_b = 30

def value_params(num1, num2):
  num1, num2 = num2, num1
  return num1, num2

new_num_1, new_num_2 = value_params(num_a, num_b)
print(new_num_1, new_num_2)
print(num_a, num_b)

list_a = [1, 5, 4, 8, 10]
list_b = [100, 500, 600, 800]

def ref_params(list1, list2):
  list1, list2 = list2, list1
  return list1, list2

new_list_1, new_list_2  = ref_params(list_a, list_b)
print(new_list_1, new_list_2)
print(list_a, list_b)
