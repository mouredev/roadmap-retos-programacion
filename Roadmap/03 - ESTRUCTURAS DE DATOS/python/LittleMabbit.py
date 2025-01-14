'''
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

# Listas - Arreglo o lista de elementos en forma ordenada, es mutable (puede modificarse)
work_elements = ['Cuchillos', 'Tabla para cortar', 'Peso', 'Mesa', 'Aro']
prices = [200, 800, 600, 12000, 2000, 500]

prices.append(4000) # Inserción.
print(prices)

work_elements.remove('Peso') # Borrado
print(work_elements)

work_elements[1] = 'Tabla para picar' # Actualizado a traves del acceso y reasignación del indice accedido.
print(work_elements)

work_elements.sort() # Ordenado de lista.
print(work_elements)
prices.sort() # Ordena la lista de los números.
print(prices)

# Tuplas - Estructuras de datos mas estrictas, indicado por un paréntesis. Son inmutables, no pueden modificarse sus valores a no ser que se cambie a una lista, se modifique y luego se transforme de nuevo a una tupla.

user_data = ('Little', 'Mabbit', '@LittleMabit', '5')
new_data = tuple(sorted(user_data))
print(new_data)

# Sets - Es una colección de datos no ordenada, no cambiable (solo se puede añadir y remover nuevos items) y no indexada. Es decir no tiene orden, no se le puede acceder por indice y solo puedes añadir y removes items. Tampoco permiten valores duplicados.

set_of_applications = {'Facebook', 'Twitter', 'Instagram', 'X'}
print(type(set_of_applications))
set_of_applications.add('LinkedIn') # Inserción
print(set_of_applications)
set_of_applications.remove('Facebook') # Borrado
print(set_of_applications)
# set_of_applications[0] # No es indexable. Tampoco ordenable como ya vimos antes.

# Diccionarios - Grupo de valores que llevan una llave y un valor (key:value). La colección de valores es modificable, es ordenada, pero no permite valores duplicados.
car = {
  "brand": "McLaren",
  "year": 2024,
  "model": "720S"
   
}

car['Tires'] = 4 # Inerseción, entre corchetes el valor key, y el valor asignado es el value.
print(car)
print(car['brand']) # Acceso, entre corchetes la key a acceder.
car['year'] = 2023 # Actualización.
print(car)
del car['Tires'] # Eliminación, para la eliminación utilizamos la palabra reservada 'del'.
print(car)
sorted_cars = dict(sorted(car.items())) # Items sorteados, ordenación.
print(sorted_cars)
print(type(sorted_cars))

'''
EXTRA
'''
def agenda():
    contacts = {'Cesar': '3125632154', 'Kira': '85463215', 'Jose': '521456325'}
    while True:

      print("1. Buscar contacto")
      print("2. Insertar contacto")
      print("3. Actualizar contacto")
      print("4. Eliminar contacto")
      print("5. Salir")

      chosen_option = input('Por favor, selecciona la opción que necesitas: ')

      if chosen_option == '2':
          phone_number = input('Por favor, ingresa el número de celular: ')
          contact_name = input('Por favor, ingresa nombre del contacto: ')
          if phone_number.isdigit() and len(phone_number) > 0 and len(phone_number) <= 11:
            if phone_number not in contacts:
              contacts[contact_name] = phone_number
              print('Contacto añadido exitosamente!')
          else:
            print('El número debe tener entre 1 y 11 dígitos. No puedes poner texto aquí. \nPor favor, verifica el numero e intenta nuevamente')
            
      elif chosen_option == '3':
        old_contact = input('Ingresa el nombre del contacto que deseas actualizar: ')
        if old_contact in contacts:
          phone_number = input('Por favor, ingresa el número de celular: ')
          if phone_number.isdigit() and len(phone_number) > 0 and len(phone_number) <= 11:
            contact_name = input('Por favor, ingresa nombre del contacto: ')
            del contacts[old_contact]
            contacts[contact_name] = phone_number
            print(f'Tu contacto ha sido actualizado: Nuevo nombre: {contact_name}, nuevo número de teléfono: {contacts[contact_name]}')
          else:
             print('El número debe tener entre 1 y 11 dígitos. No puedes poner texto aquí. \nPor favor, verifica el numero e intenta nuevamente')
        else:
            print('No pudimos encontrar la información, intenta de nuevo.')

      elif chosen_option == '1':
        find_contact = input('¿Qué contacto deseas encontrar?: ')
        if find_contact in contacts:
          print(f'El número telefónico de {find_contact} es: {contacts[find_contact]}.')
        else:
          print('Tu contacto no ha sido encontrado, por favor intenta nuevamente.')
    
      elif chosen_option == '4':
        name = input('Qué contacto deseas eliminar? ')
        if name in contacts:
            print(f"Eliminaste el contacto especificado")
            del contacts[name]
        else:
            print('El contacto que quieres eliminar no ha sido encontrado.')

      elif chosen_option == '5':
        print('Saliendo del programa')
        break

      else:
        print('Opción no válida')

agenda()
