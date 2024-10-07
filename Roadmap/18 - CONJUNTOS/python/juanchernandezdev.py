### Python Data Structures ###

my_data = [1, 4, 5, 8, 10, 50, 100, 500]

my_data.append(800)
print(my_data)

my_data.insert(0, 200)
print(my_data)

my_data.extend([4, 8, 15])
print(my_data)

my_data[4:5] = [12, 14, 16]
print(my_data)

my_data.pop(-1)
my_data.pop(5)
print(my_data)

my_data[2] = 800
print(my_data)

print(800 in my_data)

my_data.clear()
print(my_data)

#! Optional Challenge
list_one = [1, 5, 8, 10, 12, 15]
list_two = [20, 11, 15, 45, 8, 50]

#? Union
new_list = list_one + list_two
new_list = [*list_one, *list_two]
print(new_list)

#? Intersection
intersection_list = [num for num in list_one if num in list_two]
print(intersection_list)

#? Differece
difference_list = [num for num in list_one if num not in list_two]
print(difference_list)

#? Symmetric Difference
symm_diff_list = list(set(list_one).symmetric_difference(set(list_two)))
print(symm_diff_list)
