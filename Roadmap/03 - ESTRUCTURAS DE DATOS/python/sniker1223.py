my_list = ["orange", "apple", "banana"]
print(my_list)
my_list.append("grape")  # Insert
print(my_list)
my_list.remove("orange")  # Remove
print(my_list)
print(my_list[1])  # Get
my_list[1] = "watermelon"  # Update
print(my_list)
my_list.sort()  # Sort
print(my_list)

# Tuple
my_tuple: tuple = ("orange", "apple", "banana", "3")
print(my_tuple[1])  # Access
my_tuple = tuple(sorted(my_tuple))  # Sort
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"orange", "apple", "banana", "3"}
print(my_set)
my_set.add("sniker@gmail.com")  # Insert
print(my_set)
my_set.remove("orange")  # Remove
print(my_set)
my_set = set(sorted(my_set))  # It can't sorted
print(my_set)
print(type(my_set))

# Dictionary
my_dict: dict = {
    "name": "Sniker",
    "surname": "Dev",
    "age": "20"
}
my_dict["email"] = "sniker@gmail.com"  # Insert
print(my_dict)
del my_dict["surname"]  # Remove
print(my_dict)
print(my_dict["name"])  # Access
my_dict["age"] = "43"  # Update
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))

"""
Extra
"""

def my_contacts():
  
  contacts = {}
  
  while True:
    
    print("")
    print("1. Search contact")
    print("2. Enter contact")
    print("3. Update contact")
    print("4. Remove contact")
    print("5. Exit")

    option = input("\nSelect an option: ")
    
    match option:
      case "1":
        name = input("Enter the name of the contact to search ")
        if name in contacts:
          print(f"The phone number of the {name} is {contacts[name]}")
        else:
          print(f"The contact {name} doesnt exist")
      case "2":
        name = input("\nEnter contact name: ")
        phone = input("\nEnter contact phone: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
          contacts[name] = phone
        else:
          print("You must enter a phone with a maximum of 11 digits")
      case "3":
        name = input("Enter the name of the contact to update ")
        phone = input("\nEnter contact phone: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
          contacts[name] = phone
        else:
          print("You must enter a phone with a maximum of 10 digits")
      case "4":
        name = input("Enter the name of the contact to remove ")
        if name in contacts:
          del contacts[name]
      case "5":
        print("Exit of contacts")
        break
      case _:
        print("Select a valid option")

my_contacts()