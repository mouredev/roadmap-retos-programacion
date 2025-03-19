
my_set = [1,4,3]

#Add element at the end
my_set.append(8)
print(f'Adding element to the end {my_set}')

#Add element at the begining
my_set.insert(0,24)
print(f'Adding element to the begining {my_set}')

#Add multiple elments at the end
my_set.extend([10,23,32])
print(f'After adding multiple elements {my_set}')

#Add multiple elements in a given postion
my_set[2:3] = [98,97,12]
print(f'Adding multiple elements at postion 3 {my_set}')

#Delete element in a specfic postion
del(my_set[2])
print(f'Deleting element at postion 2 {my_set}')

#Update element in a position
my_set[1] = 100
print(f'Updating element at postion 2 {my_set}')

#Check if an element is in the set

if 3 in my_set:
    print("Element 3 is in the set")
else:
    print("Element 3 is not in the set")    

#Delete set
del(my_set)

#Extra

set1 = {1,2,4}
set2 = {9,3,4}
#Union
union = set1.union(set2)
print(f'Union {union}')

#Intersection
intersection = set1.intersection(set2)
print(f'Intersection {intersection}')

#Diference
diference = set1.difference(set2)
print(f'Diference {diference}')

#Symetric diference

symetric_diference = set1.symmetric_difference(set2)
print(f'Symetric diference {symetric_diference}')