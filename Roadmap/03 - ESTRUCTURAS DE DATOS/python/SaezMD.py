# #03 ESTRUCTURAS DE DATOS
#### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

#Lists
list = ["campo", "tierra", "playa", "montaña"]
print(list)
#add:
list.append("rio")
print(list)
#remove:
list.remove("campo")
print(list)
#remove:
list.pop(2)
print(list)
#insert:
list.insert(0,"huerto")
print(list)
#sort:
list.sort()
print(list)
list.sort(reverse=True)
print(list)
#access:
print(list[2])

#Tuples (inmutable lists)
numbs = (1,2,3,4,5,8)
print(numbs)
#Access:
print(numbs[4:6])
#Sort and generate a tuple:
myTuple = tuple(sorted(numbs))

#Sets (non sorted structure)
mySet = {"saul","Saez", 38}
print(mySet)
mySet.add("saul") #Error! Duplicated
mySet.remove("Saez")
print(mySet)
sortedSet = set(sorted(mySet)) #You can't use the sorted

#Matrix (define the type)
from array import array
numsMatrix = array('f',[1.5,4.5,7.5,2.5])
print(numsMatrix)
#modify:
numsMatrix[0]=3.5
print(numsMatrix)

# Dictionaries: key+value
books = {"title":"Ready Player One"}
print(books)
#add:
books["Autor"]="just one"
print(books)
#remove:
books.pop("Autor")
print(books)
#update:
books["title"]="The green book"
print(books)

#Search
#Get Value:
print(books["title"])
#Get Key:
for title, book in books.items():
    if book == "The green book":
        print(f"Key: {title} - Value: {book}")    



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""
import re

agenda = {
    "Name": "",
    "Telephone": ""
}

def checkTelephoneNumber(toCheck) -> bool:
    """function to check if the telephone number is a number and less than 12 digits"""
    if re.match('[0-9]{9,13}', toCheck):
        return True
    return False

def insert():
    """function to insert names and telephones"""
    insertNameUser = input("Enter name:")
    insertTelephoneUser = input("Enter phone number:")
    if not checkTelephoneNumber(insertTelephoneUser): #Check if the phone format is correct
        return print(f"Phone number is not valid. Wrong: {insertTelephoneUser}. Max lenght: 13. Min lenght: 9. Only numbers.")

    if insertNameUser in agenda:
        return print("Name already in agenda.")
    
    #add new name and phone
    agenda[insertNameUser]=insertTelephoneUser
    print(agenda)
    return print(f"New insert OK. Name: {insertNameUser} - Telephone: {insertTelephoneUser}")   

def search():
    """function to search by name or telephone"""
    searchNameOrTelephoneUser = input("Enter name or phone for search:")

    if checkTelephoneNumber(searchNameOrTelephoneUser): #Check if the phone format is correct and if it's a number
        for name, phone in agenda.items():
            if phone == searchNameOrTelephoneUser:
                return print(f"Name: {name} - Telephone: {phone}")     #return value or key
    else: #no digit
        if not searchNameOrTelephoneUser in agenda: #check if value exists
            return print("Name not in agenda.")
        return print(f"Name: {searchNameOrTelephoneUser} - Telephone: {agenda[searchNameOrTelephoneUser]}")
        
def update():
    """function to update name and telephone"""
    updateNameUser = input("Enter name to update:")
    #check if name exists
    if not updateNameUser in agenda:
        return print("Name not in agenda.")
    newUpdateNameUser = input("Enter New name to update:")
    newUpdateTelephoneUser = input("Enter New phone to update:")
    if not checkTelephoneNumber(newUpdateTelephoneUser): #Check if the phone format is correct
        return print(f"Phone number is not valid. Wrong: {newUpdateTelephoneUser}. Max lenght: 13. Min lenght: 9. Only numbers.")

    #remover and create again
    agenda.pop(updateNameUser)
    agenda[newUpdateNameUser]=newUpdateTelephoneUser
    return print(f"User updated. New register is Name: {newUpdateNameUser} - Telephone: {newUpdateTelephoneUser}")

def erase():
    """function to erase by name"""
    eraserNameUser = input("Enter name to erase:")
    #Check if register exist
    if not eraserNameUser in agenda:
        return print("Name not in agenda.")
    #Erase the register
    agenda.pop(eraserNameUser)
    return print(f"Register erased! {eraserNameUser}")

def mainCaller():
    """main function to control the agenda options"""
    while True:
        inputUser = input("Enter operation: (Search/Insert/Update/Erase or Exit)")
        if inputUser == "Exit":
            return print("Exiting and closing agenda! \nBye")
        elif inputUser == "Search":
            search()
        elif inputUser == "Insert":
            insert()
        elif inputUser == "Update":
            update()
        elif inputUser == "Erase":
            erase()
        else:
            print("Please select a correct option!")

mainCaller()

def maincaller2():
    while True:
        option = input("Enter operation: (Search/Insert/Update/Erase or Exit)")
        match option:
            case "Exit":
                break
            case "Search":
                pass
            case "Insert":
                pass
            case "Update":
                pass
            case "Erase":
                pass

        
        









