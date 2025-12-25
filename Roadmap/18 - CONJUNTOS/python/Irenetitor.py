#Exercise
data = [1, 5, 8, 3]
print(data)

data.append(2)
print(data)

data.insert(5, 4)
print(data)

data.extend([9, 6, 7])
print(data)

data[2:2] = [-2, -4, -6]
print(data)

del data[2]
print(data)

data[5] = -3
print(data)

if 9 in data:
    print(True)

data.clear()
print(data)

#Extra Exercise

first_ele = {1, 4, 6, 7, 8}
second_ele = {2, 3, 5, 7, 9}
list_ele = [3, 6, 0, 2]

#Union same as update
other_ele = first_ele | second_ele   #you can use this way if both are sets
print(other_ele)

first_ele = first_ele.union(list_ele)
print(first_ele)

#Intersection
first_ele = first_ele.intersection(second_ele)
print(first_ele)

#Difference
third_ele = second_ele - first_ele  #you can use this way if both are sets
print(third_ele)

fourth_ele = second_ele.difference(list_ele)
print(fourth_ele)

#Symmetric_difference

os_ele = first_ele ^ second_ele   #you can use this way if both are sets
print(os_ele)

me_ele = first_ele.symmetric_difference(list_ele)
print(me_ele)