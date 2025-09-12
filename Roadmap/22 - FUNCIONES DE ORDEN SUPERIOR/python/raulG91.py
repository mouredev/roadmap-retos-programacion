
from datetime import datetime
from functools import reduce

#Funciones de orden superior
list1 = [20,8,3,2,13,17,25]

#Python function that receive a function as argument
new_list = filter(lambda x: x%2 == 0,list1)

for element in new_list:
    print(element)

#FUnction that returns a function
def multiply_operation(value1,value2):
    return value1 * value2

def operation(value1,value2,function):
    return multiply_operation(value1,value2)

print("Result: ",operation(2,3,multiply_operation))

#Extra 

student_list = [
    {
        "name": "Raul",
        "birth_date": "11/09/1991",
        "qualifications": [10,9,10,9]
    },
    {
        "name":"Maria",
        "birth_date": "19/04/1992",
        "qualifications": [9,7,8,5.5]
    },
    {
        "name":"Juan",
        "birth_date": "20/10/2000",
        "qualifications": [5,6,3,9.5]
    }
]

#Averrage of qualifications
def averrage(iterable:list):
    return sum(iterable) / len(iterable)

#List with student name and averrage qualifications
list_averrage = list(map(lambda student: [student["name"],averrage(student["qualifications"])],student_list))

print(list_averrage)

#List with student with averrage qualifications bigger than 9
best_students = filter(lambda value: value[1]>=9,list_averrage)
print(list(best_students))

#Order lsit by birth date
birth_date_list=sorted(student_list,key=lambda student:datetime.strptime(student["birth_date"],"%d/%m/%Y"),reverse=True)
print(birth_date_list)

#Bigger qualification
all_qualifications = reduce(lambda x,y: x+y["qualifications"],student_list,[])
print(max(all_qualifications))