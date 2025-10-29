#STRUCTURES

#List
my_list = ["Red", "Blue", "Violet", "Pink", "Green"]
print(my_list)
#Adding
my_list.append("Grey")
print(my_list)
#Insertion 
my_list.insert(4, "Brown")
print(my_list)
#Deletion
my_list.remove("Grey")
print(my_list)
#Update
my_list[2] = "Dark blue"
print(my_list)
#Sort
my_list.sort() #Asc
print(my_list)
my_list.sort(reverse=True) #Desc
print(my_list)
#Type
print(type(my_list))
print(hex(id(my_list)))
'''
Output
['Red', 'Blue', 'Violet', 'Pink', 'Green']
['Red', 'Blue', 'Violet', 'Pink', 'Green', 'Grey']
['Red', 'Blue', 'Violet', 'Pink', 'Brown', 'Green', 'Grey']
['Red', 'Blue', 'Violet', 'Pink', 'Brown', 'Green']
['Red', 'Blue', 'Dark blue', 'Pink', 'Brown', 'Green']
['Blue', 'Brown', 'Dark blue', 'Green', 'Pink', 'Red']
['Red', 'Pink', 'Green', 'Dark blue', 'Brown', 'Blue']
<class 'list'>
'''

#Set
my_set = {"Apple", "Banana", "Plum", "Orange"}
print(my_set)
#Adding
my_set.add("Cherry")
my_set.add("Plum") #It won’t be added, since sets don’t allow duplicates.
print(my_set)
#Deletion
my_set.remove("Plum")
print(my_set)
#Discard
my_set.discard("Banana")
print(my_set)
#Update
my_set2 = {"Kiwi", "Melon", "Raspberry"}
my_set.update(my_set2)
print(my_set)
#Clear(empties the set)
my_set2.clear()
print(my_set2)
#Delete
del my_set2
#Type
print(type(my_set))
'''
Output
0x1f4696cd900
{'Orange', 'Apple', 'Banana', 'Plum'}
{'Orange', 'Apple', 'Plum', 'Cherry', 'Banana'}
{'Orange', 'Apple', 'Cherry', 'Banana'}
{'Orange', 'Apple', 'Cherry'}
{'Orange', 'Raspberry', 'Melon', 'Apple', 'Kiwi', 'Cherry'}
set()
<class 'set'>
'''

#Tuple
my_tuple = ("Sara", "Daniel", "Saul", "Monica")
print(my_tuple)
#Access
print(my_tuple[3])
print(my_tuple[0])
#Sort. We can use the sort() method, but it will convert our tuple into a list, so we should be aware of that.
my_tuple = tuple(sorted(my_tuple))
#Type
print(type(my_tuple))
'''
Output
('Sara', 'Daniel', 'Saul', 'Monica')
Monica
Sara
<class 'tuple'>
'''

#Dictionary
my_dic = {
    "Name":"Oliver", 
    "Surname":"Sanchez", 
    "Age":"28", 
    "Email":"oliver@gmail.com"
    }
print(my_dic)
#Access
print(my_dic["Name"])

#Insertion 
my_dic["Pet"] = "Dog"
print(my_dic)
#Deletion
del my_dic["Surname"]
print(my_dic)
#Update
my_dic["Pet"] = "Parrot"
print(my_dic)
#Sort
my_dic = dict(sorted(my_dic.items()))
print(my_dic)
#Type
print(type(my_dic))
'''
Output
{'Name': 'Oliver', 'Surname': 'Sanchez', 'Age': '28', 'Email': 'oliver@gmail.com'}
Oliver
{'Name': 'Oliver', 'Surname': 'Sanchez', 'Age': '28', 'Email': 'oliver@gmail.com', 'Pet': 'Dog'}
{'Name': 'Oliver', 'Age': '28', 'Email': 'oliver@gmail.com', 'Pet': 'Dog'}
{'Name': 'Oliver', 'Age': '28', 'Email': 'oliver@gmail.com', 'Pet': 'Parrot'}
{'Age': '28', 'Email': 'oliver@gmail.com', 'Name': 'Oliver', 'Pet': 'Parrot'}
<class 'dict'>
'''

#Exercise

def my_agenda():
    agenda = {}
    def insert_contact(in_name):
        in_phone = input("Enter a telephone number: ").strip()
        if in_phone.isdigit() and 1 <= len(in_phone) <= 11:
                agenda[in_name] = in_phone
        else:
                print("Invalid phone. Use only digits, up to 11 characters.")
                
    while True:
       

        print("")
        print("1. Search contact")
        print("2. Insert contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")
        option = input("\nSelect an option: ")

        match option:
            case "1":
                in_name = str(input("Enter the name to search for: ")).strip()
                if in_name in agenda:
                    print(f"The telephone number of {in_name} is {agenda[in_name]}")
                else:
                    print(f"The contact name {in_name} does not exist.")
            case "2":
                in_name = str(input("Enter a name: ")).strip()
                insert_contact()
            
            case "3":
                in_name = str(input("Enter the name to update: ")).strip()
                if in_name in agenda:
                    insert_contact()
                else:
                    print(f"The contact name '{in_name}' does not exist.")

            case "4":
                in_name = str(input("Enter the name to delete: ")).strip()
                if in_name in agenda:
                    del agenda[in_name]
                else:
                    print(f"The contact name {in_name} does not exist.")
            case "5":
                print("Exiting agenda")
                break
            case _:
                print("No valid option. Please choose an option between 1 and 5.")

my_agenda()