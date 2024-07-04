# #03 ESTRUCTURAS DE DATOS
# Muestra ejemplos de creacion de todas las estructuras soportadas por defecto en tu lenguaje
# Utiliza operaciones de inserccion, borrado, actualizacion y ordenacion.

# Lista
print("List")
List = ["Python", "C", "JavaScript", "Ruby"]
print(List)

## Insercion
print("New element to append: 'Go'")
List.append("Go")
print("New List", List)

print("New element to insert: 'HTML' in position 1")
List.insert(1, "HTML")
print("New List", List)

## Borrado
print("Element to remove: 'Ruby'")
List.remove("Ruby")
print("New List", List)

print("Element to pop: 'Python'")
List.pop(0)
print("New List", List)

## Ordenamiento
print("Ordered List")
List.sort()
print("New List", List)

# Lista
List = ["Python", "C", "JavaScript", "Ruby"]
print(List)

## Insercion
print("New element to append: 'Go'")
List.append("Go")
print("New List", List)

print("New element to insert: 'HTML' in position 1")
List.insert(1, "HTML")
print("New List", List)

## Borrado
print("Element to remove: 'Ruby'")
List.remove("Ruby")
print("New List", List)

print("Element to pop: 'Python'")
List.pop(0)
print("New List", List)

## Ordenamiento
print("Ordered List")
List.sort()
print("New List", List)
## Primer elemento de la lista
print("First element of List")
print(List[0])

## Ultimo elemento de la lista
print("Last element of List")
print(List[-1])

print()

#----------------------------------------------------------
# Dictionary
print("Dictionary")
Dictionary = {0:"Python", 1:"C", 2:"JavaScript", 3:"Ruby"}

## Accessar por medio de clave
print("Accesing element using key")
print(Dictionary[0])

## Accessar usando get
print("Accesing element using get")
print(Dictionary.get(1))

print()
#----------------------------------------------------------
# Tuple
print("Tuple")
Tuple = ("Python", "C", "JavaScript", "Ruby")
print(Tuple)

## Primer elemento de la lista
print("First element of Tuple")
print(Tuple[0])

## Ultimo elemento de la lista
print("Last element of Tuple")
print(Tuple[-1])

print()
#----------------------------------------------------------
# Dificultad Extra
'''
 Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.
'''

agenda = {}

def search(data):
    if data.isdigit():
        for key, value in agenda.items():
            if value == int(data):
                print(f"{key}: {value}")
    else:
        if data in agenda:
            print(f"{data}: {agenda[data]}")

def insert(name, number):
    if name not in agenda:
        agenda[name] = number
    else:
        print(f"{name} is in the agenda")
def remove(name):
    print(f"{name}: {agenda[name]} was removed")
    del agenda[name]

def show():
    for item in agenda:
        print(f"{item}: {agenda[item]:>5}")
def update(name, number):
    agenda[name] = number

def main():
    while True:
        print("Phone Agenda")
        option = input("1: Serach\n2: Insert\n3: Remove\n4: Show\n5: Update\nX: Exit\n\t Option: ")
        if option == '1':
            data = input("Enter a name or number: ")
            search(data)
        if option == '2':
            name = input("Enter a name: ")
            while True:
                number = input("Enter a number: ")
                if not number.isdigit() or len(number) > 10:
                    print("Number is not valid, try again")
                else:
                    break
            insert(name, number)
        if option == '3':
            name = input("Enter a name: ")
            remove(name)
        if option == '4':
            show()
        if option == '5':
            name = input("Enter a name: ")
            number = int(input("Enter a number: "))
            update(name, number)
        if option == 'X':
            break
if __name__ == '__main__':
    main()
