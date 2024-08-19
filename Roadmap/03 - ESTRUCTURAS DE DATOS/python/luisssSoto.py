# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.
#  */

"""Lists, Tuples, Dictionaries and Sets"""
'''Lists are mutable'''
zoo=['rhino', 'elephant']
print(zoo)

#looking forward
myfavoriteAnimal = zoo[0]
print(myfavoriteAnimal)

#insert an element
zoo.append('owl')
print(zoo)

#delete last element
anotherZoo = zoo.pop()
print(anotherZoo)

#remove one element
zoo.remove('rhino')
print(zoo)

#update
zoo.insert(1, 'lion')

#order a list
zoo.sort()
print(zoo)
print()

'''tuples'''
#they are immutable, so that there are lots of limitations
t = (1,2,2,4,6,1,3)
print(t)

print(1 in t)
print(2 not in t)

'''Dictionaries'''
d = {'dog': 'perro', 'cat': 'gato'}

'''iterate and indexar for the dictionaries'''
for americanAnimal in d:
    print(americanAnimal, end=' ')
print()

for spanishAnimal in d:
    print(d[spanishAnimal], end=' ')
print()

'''Set'''
#It couldn't exist more than 1 element in the set
s = {1,2,2,9}
print(s)
print()

'''Exercise'''
telephoneDiary = {'Luis': 3310147389}
conditional = True
welcome = '''Tell me what would you do first:
                    type...
                    1 to add a contact
                    2 to search a contact
                    3 to update a contact
                    4 to delete a contact
                    5 to exit the program: '''
def lookingContact(name):
    try:
        return telephoneDiary[name]
    except LookupError as e:
        print('The name was not found', e) 

while conditional == True:
    print('Welcome to your personal telephone diary')
    request = int(input(welcome))
    match request:
        case 1:
            addContact = input('what about if we add some names on it before start, what is the name of the contact:')
            if addContact in telephoneDiary:
                print(" Be careful, It seems like that contact already exist")
                request = "wanna you do...\n" + welcome
            else:
                addNumber = input('yes, now what about if you tell me a number of this contact only ten numbers please: ')
                if addNumber.isdigit() == True and len(addNumber) == 10:
                    addNumber = int(addNumber)
                    telephoneDiary[addContact] = addNumber
                    print(f'The contact: {addContact}, was added with the next number: {addNumber}')
                    print(telephoneDiary)
                else:
                    print('Only ten numbers please 🤨')
        case 2:
            searchContact = input('what is the exactly name, that we are looking forward: ')
            if searchContact in telephoneDiary:
                print(f'Here is your contact: {searchContact}', telephoneDiary[searchContact])
            else:
                print('Sorry but we can\'t find the contact')
        case 3:
            searchContact = input("What's the contact that you want to update: ")
            if searchContact in telephoneDiary:
                updateNumber = input('Tell me the new number: ')
                if updateNumber.isdigit() == True and len(updateNumber) == 10:
                    updateNumber = int(updateNumber)
                    telephoneDiary[searchContact] = updateNumber
                else: print('Only ten numbers 😤')
            else:
                print('Sorry but we can\'t find the contact')
        case 4:
            searchContact = input('What is the contact who you will get deleted from your list: ')
            if searchContact in telephoneDiary:
                telephoneDiary.pop(searchContact)
                print(f'the contact: {searchContact} was deleted')
            else:
                print('Sorry but we can\'t find the contact')
        case 5:
            conditional = False
print(telephoneDiary)
