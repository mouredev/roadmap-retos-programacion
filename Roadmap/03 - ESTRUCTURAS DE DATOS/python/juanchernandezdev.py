### Python Data Structures ###

#! List

my_list = [1, 6, 3, 10, 5]
print(my_list)

my_str = 'hello'
print(list(my_str))

# Append
my_list.append(8)
print(my_list)

# Remove
my_list.remove(8)
print(my_list)

# Insert
my_list.insert(2, 50)
print(my_list)

# Sort
my_list.sort()
print(my_list)

#! Dictionary

my_dict = { 'name': 'John', 'lastname': 'Doe', 'age': 44}
print(my_dict)

# Add
my_dict['country'] = 'Norway'
print(my_dict)

# Remove
my_dict.pop('name')
print(my_dict)

# Update
my_dict['lastname'] = 'new lastname'
print(my_dict)

# Order
print(sorted(my_dict.keys()))

#! Tuple

my_tuple = (1, 2, 3, 8, 7, 4)
print(my_tuple)

#* Since tuples are immutable you can't add or remove items.

# Order
print(sorted(my_tuple))

#! Set
my_set = {1, 2, 3, 5, 8, 12, 3, 3, 4, 5} # The 3 will be only one time since sets don't allow duplicated items.
print(my_set)

# Add
my_set.add(50)
print(my_set)

# Remove
my_set.remove(4)
print(my_set)

# Update
my_second_set = {100, 200, 500}
my_set.update(my_second_set)
print(my_set)

# Order
print(sorted(my_set))

#! Optional Challenge
print('---Optional Challenge---')

# Start the program
# Give the user a set of option, to insert, search, update, or remove a contact
# Ask the user for the data corresponding to the operation that was selected
# Execute the selected operation
# Verify that telephone number data type is numeric and contains no more than 11 digits
# Notify the user if the operation was successful or not
# Ask the user to add another contact or to end the programm

contacts_list = []
id = 1

user_start = input('Please type start to run the program: ')
run_program = False

if user_start == 'start':
  run_program = True
  
def search_contact(contact_name, list):
    for contact in list:
      if contact_name == contact['contact_name'].lower():
        return contact
      
def update_contact(contact_name, list):
    for contact in list:
      index = list.index(contact)
      if contact_name == list[index]['contact_name'].lower():
        print(list[index]['contact_name'])
        new_name = input('Type the new name for your contact: ').lower()
        new_phone = input('Type the new phone for your contact: ').lower()
        list[index]['contact_name'] = new_name
        list[index]['contact_phone'] = new_phone
        print(f'Contact updated: {list[index]['contact_name']} - {list[index]['contact_phone']}')
      
def delete_contact(contact_name, list):
    for contact in list:
      index = list.index(contact)
      if contact_name == list[index]['contact_name'].lower():
        print(list[index]['contact_name'])
        del list[index]
        print('Contact deleted')
        
def show_contacts(list):
    if len(list) == 0:
      print('Your contact list is empty')
    
    for contact in list:
      print(f'{contact['contact_name']} - {contact['contact_phone']}')
  
  
while run_program == True:
  print('----Choices----')
  user_choice = input('a: Add contact\nb: Search contact\nc: Update contact\nd: Remove contact\ne: Show all contacts\nType the corresponding letter to perform an action or type "exit" to end the program: ').lower()
  
  if user_choice== 'exit':
    run_program = False
  
  # Add Contact
  
  if user_choice == 'a':
    print('----New Contact----')
    contact_name: str = input('Enter your contact name: ').title()
    contact_phone: str = input('Enter your contact phone number: ')
    
    if not contact_phone.isnumeric():
      print('Phone number should contain only numbers!')
    
    if len(contact_phone) > 11:
      print('Phone number should contain only 11 digits or less')
    else:
      new_contact = {'id': id, 'contact_name': contact_name, 'contact_phone': contact_phone }
      id += 1
      contacts_list.append(new_contact)
    
  # Search Contact
      
  if user_choice == 'b':
    print('----Search Contact----')
    contact_name: str = input('Type the name of the contact you want to search: ').lower()
    contact = search_contact(contact_name, contacts_list)
    print(f'Contact name: {contact['contact_name'].title()}\nContact phone number: {contact['contact_phone']}')
  
  # Update Contact
  
  if user_choice == 'c':
    print('----Search Update----')
    contact_name: str = input('Type the name of the contact you want to update: ').lower()
    update_contact(contact_name, contacts_list)
  
  # Remove Contact
    
  if user_choice == 'd':
    print('----Remove Contact----')
    contact_name: str = input('Type the name of the user you want to remove: ').lower()
    delete_contact(contact_name, contacts_list)
  
  # Show Contacts
      
  if user_choice == 'e':
    print('----Contacts----')
    show_contacts(contacts_list)
  