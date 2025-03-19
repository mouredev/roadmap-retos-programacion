## Ejercicio
import os
import json
import xml.etree.ElementTree as xml

data = {
    'name' : 'Nombre Apellido',
    'age' : 24,
    'birth_date' : '01/01/2000',
    'programming_languages' : [
        'Python',
        'JavaScript',
        'Bash'
    ]
}

xml_file = 'ejercicio.xml'
json_file = 'ejercicio.json'

def xml_create(data, file):
    print('[+] Iniciando creacion de archivo xml')
    
    # Creamos el elemento raíz
    print('[+] Creando elemento raiz')
    root = xml.Element('person')

    # Para cada clave y valor en el diccionario data
    for key, value in data.items():
        # Creamos un elemento hijo con el nombre de la clave y el valor como su texto
        print('[+] Creando elemento hijo')
        child = xml.SubElement(root, key)

        # Si el valor es una lista, creamos elementos para cada elemento de la lista
        if isinstance(value, list):
            for item in value:
                print('[+] Creando subelemento hijo')
                subelement = xml.SubElement(child, 'language')
                subelement.text = item
        else:
            child.text = str(value)  # Convertimos el valor a cadena si es necesario
    
    # Creamos un objeto ElementTree con el elemento raíz
    print('[+] Creando arbol de elmentos')
    tree = xml.ElementTree(root)

    # Escribimos el contenido del ElementTree en un archivo XML
    print('[+] Creando archivo con los elementos del arbol')
    tree.write(file)
    
    with open(file, 'r') as f:
        print('[+] Leyendo e imprimiendo archivo creado')
        print(f.read())

    #print('[+] Borrando archivo creado')
    #os.remove(file)

def json_create(data :dict, file :str):
    print('\n[+] Iniciando creacion de archivo json')

    print('[+] Creando archivo json')
    with open(file, 'w') as f:
        json.dump(data, f,  indent=4)
    
    print('[+] Leyendo e imprimiendo archivo json')
    with open(file, 'r') as f:
        print(json.load(f))
    
    #print('[+] Borrando archivo json')
    #os.remove(file)

xml_create(data=data, file=xml_file)
json_create(data=data, file=json_file)


# Extra

class Datos:
    def __init__(self):
        self.name = None
        self.age = None
        self.birth_date = None
        self.programming_languages = []

    def cargar_desde_xml(self, archivo):
        tree = xml.parse(archivo)
        root = tree.getroot()
        
        self.name = root.find('name').text
        self.age = int(root.find('age').text)
        self.birth_date = root.find('birth_date').text
        
        languages = root.find('programming_languages')
        if languages:
            self.programming_languages = [language.text for language in languages.findall('language')]

    def cargar_desde_json(self, archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            self.name = data['name']
            self.age = data['age']
            self.birth_date = data['birth_date']
            self.programming_languages = data['programming_languages']

# Crear instancia de la clase Datos
datos = Datos()

# Cargar datos desde el archivo XML y JSON
datos.cargar_desde_xml(xml_file)
datos.cargar_desde_json(json_file)

# Imprimir los datos cargados
print('\n[+] Datos cargados desde el archivo:')
print('[+] Nombre:', datos.name)
print('[+] Edad:', datos.age)
print('[+] Fecha de nacimiento:', datos.birth_date)
print('[+] Lenguajes de programación:', datos.programming_languages)

# Borrar los archivos XML y JSON
os.remove(xml_file)
os.remove(json_file)
