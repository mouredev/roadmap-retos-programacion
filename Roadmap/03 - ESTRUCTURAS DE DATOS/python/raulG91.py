
'''List '''
print("--List--")
list1 = [6,19,5,3]
print("List: ", list1)
list1.append(1)
print("Append operation: ",list1)
list1.sort()
print("Sort list : " , list1)
list1[2] = 2
print("Update element at position 3: ",list1)
list1.pop(-1)
print("Remove last element :", list1)

'''Tuples'''
print("--Tuples--")
tuple = (4,10,3)
print("Tuple: ", tuple)

'''Set'''
print("--Set--")
set_int = {4,8,5}
print("Set: ", set_int)
set_int.add(16)
print("Add operation: ",set_int)
set_int.remove(8)
print("Romve operation: ", set_int)

'''Dictionary'''

print("--Dictionary--")

my_dict = {'blue':'azul','orange':'naranja'}
print("Dictionary: ",my_dict)
my_dict['green'] = 'verde'
print("Add operaion: ",my_dict)    
my_dict['green'] = 'azul'
print("Update operation: ",my_dict) 
del(my_dict['green'])
print("Delete operation: ", my_dict)          

def check_phone_number(number:str) -> bool:
    if number.isdigit() and len(number) == 9:
        return True
    else:
        return False
def telephone_agenda():
    
    agenda = {}
    
    while True:
        print("Enter 1 to create a new contact")
        print("Enter 2 to update a contact" )
        print("Enter 3 to look for a contact")
        print("Enter 4 to remove a contact")
        print("Enter 5 to exit the program")
        
        option = int(input())
        
        if option == 1:
            print("Enter name for new contact: ")
            name = input()
            print("Enter number for new contact: ")
            tel = input()
            if check_phone_number(tel):
                agenda[name] = tel
            else:
                print("Incorrect telephone number")
        
        elif option == 2:
            print("Enter name for contact to be updated: ")
            name = input()
            if name in agenda:
                print("Enter new telephone number: ")
                tel =input()
                if check_phone_number(tel):
                    agenda[name] = tel
                    print(agenda)
                else:
                    print("Incorrect telephone number")
            else:
                print("Contact doesn't exist in the agenda")    
        elif option == 3:
            print("Enter the name of the contact")
            name = input()
            if name in agenda:
                print("Phone number is: ",agenda[name])
            else:
                print("Contact is not in the agenda")    
        elif option == 4:
            print("Enter the name of the contact")
            name = input()
            if name in agenda:
                del(agenda[name])
                print("Phone number was deleted: ", agenda)
            else:
                print("Contact is not in the agenda")   
        else: 
            break

telephone_agenda()        