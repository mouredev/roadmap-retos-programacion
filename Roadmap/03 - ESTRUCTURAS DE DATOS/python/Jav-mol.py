# --- Estructuras ---

# Listas
print('--- Listas ---')

my_list = list(("Python", "JavaScript", "Go"))
print(my_list)

my_list.append("Php") # -> Insercion
my_list.append("Ruby")
print(my_list)

my_list.insert(0,'Typescript')
print(my_list)

my_list.extend(['Java', 'Rust'])
print(my_list)

my_list[0] = 'CSS' #-> Actualizacion
print(my_list)

my_list[0:2] = ['Typescript', 'Python3']
print(my_list)

my_list.sort(key=lambda x:len(x), reverse=True) # -> Ordenacion
print(my_list)

my_list.remove('JavaScript') # -> Eliminacion
print(my_list)

my_list.pop(0)
print(my_list)

del my_list[3:]
print(my_list)

my_list.clear()
print(my_list)


# Tuples
print('\n--- Tuplas ---')

my_tuple = tuple(('Samsung', 'Iphone', 'Huawei'))
print(my_tuple[1]) # -> Acceso
print(my_tuple[2])

print(sorted(my_tuple, key=lambda x:len(x))) # -> Ordenacion

# Sets
print('\n--- Sets ---')


my_set = set(('Samsung', 'Iphone', 'Huawei'))
print(my_set)

my_set.add('Motorola') # -> Insercion
print(my_set)

my_set.remove('Huawei') # -> Eliminacion
print(my_set)

print(sorted(my_set, reverse=True)) # -> Ordenacion

my_set.clear() # -> Eliminacion
print(my_set)

# Diccionarios
print('\n--- Diccionarios ---')

my_dict = dict({
    'name':'Javier',
    'surname':'Javi',
    'age': 22,
    'country':'Argentina'
})
print(my_dict)

my_dict['name'] = 'Javier Molina' # -> Actualizacion
print(my_dict)

my_dict.update({'email':'javi@example.com', 'name': 'Javier'}) # -> Insercion
print(my_dict)

my_dict.pop('email') # -> Eliminacion
print(my_dict)

print(my_dict.popitem())
print(my_dict)

my_dict = sorted(my_dict.items()) # -< Ordenacion
print(my_dict)


# --- Ejercicio --- -> Crea una agenda de contactos por terminal.
import json

class Contacto:
    def __init__(self) -> None:
        self.data = self.add_data()
    
    def add_data(self):
        """ 
        Solicita al usuario que ingrese el nombre y el número de teléfono del contacto.

        Returns:
            dict: Un diccionario con el nombre y el número de teléfono del contacto.
        """
        while True:
            name: str = input('Introduce el nombre: ')            
            phone_number: int = (input('Introduce el numero de telefono: '))
            
            if len(phone_number) < 9:
                print('Ingrese un numero con mas de 9 caracteres')
                continue
            
            return {'name':name, 'phone':int(phone_number)}
        
class AgendaContactos:
    cont_id:int = 0
    contactos:dict = {} 
    
    
    def agregar_contacto(self):
        """ 
        Agrega un nuevo contacto a la agenda de contactos.
        """
        self.cont_id += 1        
        contacto = Contacto()        
        self.contactos[f'id-{self.cont_id}'] = contacto.data
                
                
    def buscar_contacto(self):
        """
        Busca un contanto por su ID.
        """
        id:int = input('Introduce el Id: ')
        print(self.contactos.get(f'id-{id}', 'No se encontro ningun contacto con ese ID'))

    
    def actualizar_contacto(self):
        """ 
        Actualiza un contacto existente en la agenda de contactos.
        """
        id:int = input('Introduce el ID del contacto que deseas actualizar: ')
        
        if f'id-{id}' not in self.contactos.keys():
            print('Ingrese un ID valido')
            return        
        
        contacto = Contacto()
        self.contactos[f'id-{id}'] = contacto.data
    
        
    def borrar_contacto(self):
        """ 
        Elimina un contacto de la agenda de contactos.
        """
        id:int = input('Introduce el ID del contacto que deseas borrar: ')
        self.contactos.pop(f'id-{id}', None)
    
    
    def listar_contactos(self):   
        """ 
        Imprime la lista de contactos almacenados en la agenda.
        """       
        print(json.dumps(self.contactos, indent=4), '\n')
        

menu = """1-Agregar
2-Buscar
3-Actualizar
4-Borrar
5-Listar
6-Salir
-> """

agenda = AgendaContactos()

functions = {
    "1":agenda.agregar_contacto,
    "2":agenda.buscar_contacto,
    "3":agenda.actualizar_contacto,
    "4":agenda.borrar_contacto,
    "5":agenda.listar_contactos,
    "6":'exit'
}

while True:
    option = input(menu)    
    function = functions.get(option)
    if function == 'exit':
        break    
    elif not function:
        print('Ingrese un valor valido')
        continue
    function()
