#----------------------------------------
#Lists - is a collection which is ordered and changeable. Allows duplicate members.
#----------------------------------------

#Creating a list

first_list = [1, 2, 3, 4, 5]    #Note the square brackets
print(first_list)

#Lists can contain different types of data

mixed_list = [1, 2.5, "string", True]
print(mixed_list)

#Lists can be nested

nested_list = [1, 2, [3, 4, 5], 6]
print(nested_list)

#Empty list

empty_list = []
print(empty_list)

#----------------------------------------
#tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
#----------------------------------------

#Creating a tuple

first_tuple = (1, 2, 3, 4, 5)   #Note the parentheses
print(first_tuple)

#Tuples can contain different types of data

mixed_tuple = (1, 2.5, "string", True)
print(mixed_tuple)

#Tuples can be nested

nested_tuple = (1, 2, (3, 4, 5), 6)
print(nested_tuple)

#Single element tuple

single_element_tuple = (1,)    #Note the comma
print(single_element_tuple)

#Empty tuple

empty_tuple = ()
print(empty_tuple)

#----------------------------------------
#set - is a collection which is unordered, unchangeable and unindexed. No duplicate members.
#----------------------------------------

#Creating a set

first_set = {1, 2, 3, 4, 5}   #Note the curly braces
print(first_set)

#Sets can contain different types of data

mixed_set = {1, 2.5, "string", True}
print(mixed_set)

#Empty set

empty_set = set()
print(empty_set)

#----------------------------------------
#dictionary - is a collection which is ordered and changeable. No duplicate members.
#----------------------------------------

#Creating a dictionary

first_dict = {   #Note the curly braces
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(first_dict)

#Dictionaries can contain different types of data

mixed_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": True
}
print(mixed_dict)

#Nested dictionary

nested_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "Main Street",
        "city": "New York"
    }
}
print(nested_dict)

#Empty dictionary

empty_dict = {}
print(empty_dict)

#----------------------------------------
#inserting elements in a list, tuple, set, dictionary
#----------------------------------------

#lists

#append() - adds an element at the end of the list

first_list = [1, 2, 3, 4, 5]
first_list.append(6)    #Append 6 at the end
print(first_list)   #Output: [1, 2, 3, 4, 5, 6]

#insert() - adds an element at the specified position

first_list = [1, 2, 3, 4, 5]
first_list.insert(2, 6)   #Insert 6 at index 2
print(first_list)   #Output: [1, 2, 6, 3, 4, 5]

#extend() - adds elements of a list to another list

first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8]
first_list.extend(second_list)    #Add elements of second_list to first_list
print(first_list)   #Output: [1, 2, 3, 4, 5, 6, 7, 8]

#tuples

#Tuples are immutable, so you can't add elements to them

#sets

#add() - adds an element to the set

first_set = {1, 2, 3, 4, 5}
first_set.add(6)    #Add 6 to the set
print(first_set)    #Output: {1, 2, 3, 4, 5, 6}

#update() - adds elements of a set to another set

first_set = {1, 2, 3, 4, 5}
second_set = {6, 7, 8}
first_set.update(second_set)    #Add elements of second_set to first_set
print(first_set)    #Output: {1, 2, 3, 4, 5, 6, 7, 8}

#dictionaries

#update() - adds elements of a dictionary to another dictionary

first_dict = {
    "name": "John",
    "age": 30
}
second_dict = {
    "city": "New York"
}
first_dict.update(second_dict)    #Add elements of second_dict to first_dict

print(first_dict)    #Output: {'name': 'John', 'age': 30, 'city': 'New York'}

#----------------------------------------
#deleting elements in a list, tuple, set, dictionary
#----------------------------------------

#lists

#remove() - removes the first occurrence of the element with the specified value

first_list = [1, 2, 3, 4, 5]
first_list.remove(3)    #Remove 3 from the list
print(first_list)    #Output: [1, 2, 4, 5]

#pop() - removes the element at the specified position

first_list = [1, 2, 3, 4, 5]
first_list.pop(2)    #Remove element at index 2
print(first_list)    #Output: [1, 2, 4, 5]

#del - removes the element at the specified position

first_list = [1, 2, 3, 4, 5]
del first_list[2]    #Remove element at index 2
print(first_list)    #Output: [1, 2, 4, 5]

#del - removes the entire list

first_list = [1, 2, 3, 4, 5]
del first_list    #Remove the entire list
#print(first_list)    #This will raise an error

#clear() - removes all elements from the list

first_list = [1, 2, 3, 4, 5]
first_list.clear()    #Remove all elements
print(first_list)    #Output: []

#tuples

#Tuples are immutable, so you can't delete elements from them

#sets

#remove() - removes the specified element

first_set = {1, 2, 3, 4, 5}
first_set.remove(3)    #Remove 3 from the set
print(first_set)    #Output: {1, 2, 4, 5}

#discard() - removes the specified element

first_set = {1, 2, 3, 4, 5}
first_set.discard(3)    #Remove 3 from the set
print(first_set)    #Output: {1, 2, 4, 5}

#pop() - removes a random element

first_set = {1, 2, 3, 4, 5}
first_set.pop()    #Remove a random element
print(first_set)    #Output: {2, 3, 4, 5}

#clear() - removes all elements from the set

first_set = {1, 2, 3, 4, 5}
first_set.clear()    #Remove all elements
print(first_set)    #Output: set()

#dictionaries

#pop() - removes the element with the specified key

first_dict = {
    "name": "John",
    "age": 30
}
first_dict.pop("age")    #Remove the element with key "age"
print(first_dict)    #Output: {'name': 'John'}

#popitem() - removes the last inserted key-value pair

first_dict = {
    "name": "John",
    "age": 30
}
first_dict.popitem()    #Remove the last inserted key-value pair
print(first_dict)    #Output: {'name': 'John'}

#del - removes the element with the specified key

first_dict = {
    "name": "John",
    "age": 30
}
del first_dict["age"]    #Remove the element with key "age"
print(first_dict)    #Output: {'name': 'John'}

#del - removes the entire dictionary

first_dict = {
    "name": "John",
    "age": 30
}
del first_dict    #Remove the entire dictionary
#print(first_dict)    #This will raise an error

#clear() - removes all elements from the dictionary

first_dict = {
    "name": "John",
    "age": 30
}
first_dict.clear()    #Remove all elements
print(first_dict)    #Output: {}

#----------------------------------------
#accessing elements in a list, tuple, set, dictionary
#----------------------------------------

#lists

#Accessing elements by index

first_list = [1, 2, 3, 4, 5]
print(first_list[2])    #Output: 3

#Accessing elements by negative index

first_list = [1, 2, 3, 4, 5]
print(first_list[-2])    #Output: 4

#Accessing elements by range of indices

first_list = [1, 2, 3, 4, 5]
print(first_list[1:4])    #Output: [2, 3, 4]

#Accessing elements by negative range of indices

first_list = [1, 2, 3, 4, 5]
print(first_list[-4:-1])    #Output: [2, 3, 4]

#Accessing elements by range of indices with step

first_list = [1, 2, 3, 4, 5]
print(first_list[1:4:2])    #Output: [2, 4] (start:stop:step)

#tuples

#Accessing elements by index

first_tuple = (1, 2, 3, 4, 5)
print(first_tuple[2])    #Output: 3

#Accessing elements by negative index

first_tuple = (1, 2, 3, 4, 5)
print(first_tuple[-2])    #Output: 4

#Accessing elements by range of indices

first_tuple = (1, 2, 3, 4, 5)
print(first_tuple[1:4])    #Output: (2, 3, 4)

#Accessing elements by negative range of indices

first_tuple = (1, 2, 3, 4, 5)
print(first_tuple[-4:-1])    #Output: (2, 3, 4)

#Accessing elements by range of indices with step

first_tuple = (1, 2, 3, 4, 5)
print(first_tuple[1:4:2])    #Output: (2, 4) (start:stop:step)

#sets

#Sets are unordered, so you can't access elements by index

#dictionaries

#Accessing elements by key

first_dict = {
    "name": "John",
    "age": 30
}
print(first_dict["name"])    #Output: John

#Accessing elements using get()

first_dict = {
    "name": "John",
    "age": 30
}
print(first_dict.get("name"))    #Output: John

#Accessing elements using items()

first_dict = {
    "name": "John",
    "age": 30
}
for key, value in first_dict.items():
    print(key, value)    #Output: name John, age 30

#----------------------------------------
#ordering elements in a list, tuple, set, dictionary
#----------------------------------------

#lists

#sort() - sorts the list

first_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
first_list.sort()
print(first_list)    #Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

#reverse() - reverses the list

first_list = [1, 2, 3, 4, 5]
first_list.reverse()
print(first_list)    #Output: [5, 4, 3, 2, 1]

#tuples

#Tuples are immutable, so you can't order them

#sets

#Sets are unordered, so you can't order them

#dictionaries

#sorted() - sorts the dictionary by key

first_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
sorted_dict = dict(sorted(first_dict.items()))
print(sorted_dict)    #Output: {'age': 30, 'city': 'New York', 'name': 'John'}

#----------------------------------------
#Extra - Contact List
#----------------------------------------

def my_agenda():
    contacts = {}  # Dictionary to store contacts

    while True:
        print("\nContact Agenda")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show Contacts")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        match choice:
            case "1":
                name = input("Enter contact name: ").strip()
                phone = input("Enter phone number (max 11 digits): ").strip()
                if phone.isdigit() and len(phone) <= 11:
                    contacts[name] = phone
                    print(f"Contact {name} added successfully.")
                else:
                    print("Invalid phone number. It must be numeric and up to 11 digits.")
            
            case "2":
                name = input("Enter contact name to search: ").strip()
                if name in contacts:
                    print(f"{name}: {contacts[name]}")
                else:
                    print("Contact not found.")

            case "3":
                name = input("Enter contact name to update: ").strip()
                if name in contacts:
                    new_phone = input("Enter new phone number (max 11 digits): ").strip()
                    if new_phone.isdigit() and len(new_phone) <= 11:
                        contacts[name] = new_phone
                        print(f"Contact {name} updated successfully.")
                    else:
                        print("Invalid phone number. It must be numeric and up to 11 digits.")
                else:
                    print("Contact not found.")

            case "4":
                name = input("Enter contact name to delete: ").strip()
                if name in contacts:
                    del contacts[name]
                    print(f"Contact {name} deleted successfully.")
                else:
                    print("Contact not found.")

            case "5":
                if contacts:
                    print("\nYour Contacts:")
                    for name, phone in contacts.items():
                        print(f"{name}: {phone}")
                else:
                    print("No contacts available.")

            case "6":
                print("Exiting program. Goodbye!")
                break

            case _:
                print("Invalid option. Please choose between 1 and 6.")

# Run the contact agenda
my_agenda()
