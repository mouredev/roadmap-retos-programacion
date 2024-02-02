# ESTRUCTURAS DE DATOS

# LISTAS
print(f"This is my list:")
myList: list = ["Bruce", "Diana", "Barry", "Victor", "Kal-El", "Arthur"]
print(myList)

# Inserción
myList.append("Hal Jordan")
print(myList)

# Eliminación
myList.remove("Victor")
print(myList)

# Acceso
print(myList[4])
# Actualización
myList[4] = "Oliver Queen"
print(myList)

# Ordenación
myList.sort()
print(myList)
print(type(myList))

# TUPLAS
myTuple: tuple = ("Bruce", "Wayne", "Batman", "1988")
# Acceso
print(myTuple[2])
print(myTuple[1])
# Ordenación
myTuple = tuple(sorted(myTuple))
print(myTuple)
print(type(myTuple))

# SETS
mySet: set = {"Bruce", "Wayne", "Batman", "1988"}
print(mySet)
# Inserción
mySet.add("Wayne Enterprises")
print(mySet)
# Eliminación
mySet.remove("Batman")
print(mySet)
# Los sets no pueden ser ordenados
print(mySet)
print(type(mySet))

# DICCIONARIOS
myDict: dict = {
    "name": "Bruce",
    "surname" : "Wayne",
    "aka": "Batman",
    "year" : "1988",
}
# Inserción
myDict["Company"]="Wayne Enterprises" 
print(myDict)
# Eliminación
del myDict["aka"]
print(myDict)
# Acceso
print(myDict["name"])
# Actualización
myDict["year"] = "1989"
print(myDict)
# Ordenación
myDict = dict(sorted(myDict.items()))
print(myDict)
print(type(myDict))


# 🧩 DIFICULTAD EXTRA 🧩

def myAgenda():

    agenda = {}
    print("Welcome to the contact book Peacemaker")

    def insertContact():
        phone = input("Input the number of the new contact")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 9:
            agenda[name] = phone
        else:
            print("Invalid phone number")
    
    while True:
        print("OPTIONS")
        print("1.-Search")
        print("2.-Insert new contact")
        print("3.-Update a contact")
        print("4.-Delete contact")
        print("5.-Exit")

        option = input("\nSelect an option: ")

        match option:
            case "1":
                name = input ("Input the contact name: ")
                if name in agenda:
                    print(f"The {name}'s phone number is: {agenda[name]}.")
                else:
                    print("This contact does not exist")
            case "2":
                name = input ("Input the name of the new contact: ")
                insertContact()
            case "3":
                name = input("Input the contact name you want to update")
                if name in agenda:
                    insertContact()
                else:
                    print(f"The {name}'s contact does not exist")
            case "4":
                name = input("Input the contact you want to delete: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"This contact does not exist")
            case "5":
                print("Disconnecting")
                break
            case _:
                print("No valid option, select an option 1-5")

myAgenda()
