import xml.etree.ElementTree as ET
import os
import json

class ArchivoXML:
    def __init__(self, path):
        self.archivo = f'{path}.xml'

    def create_xml(self):
        root = ET.Element('data')

        nombre = ET.SubElement(root, 'nombre')
        nombre.text = 'Sergio'
        edad = ET.SubElement(root,'edad')
        edad.text = '18'
        nacimiento = ET.SubElement(root, 'nacimiento')
        nacimiento.text = '12/07/2005'
        languages = ET.SubElement(root, 'languages')
        languages.text = str(['Python', 'Javascript', 'C#', 'C++'])

        tree = ET.ElementTree(root)

        tree.write(self.archivo, encoding="utf-8", xml_declaration=True)

    def showXML(self):
        tree = ET.parse(self.archivo)
        root = tree.getroot()

        for i in root:
            print(f'{i.tag}: {i.text}')

    def remove_xml(self):
        if os.path.exists(self.archivo):
            os.remove(self.archivo)
            print(f"El archivo '{self.archivo}' ha sido eliminado.")
        else:
            print(f"El archivo '{self.archivo}' no existe.")


class ArchivoJSON:
    def __init__(self, path):
        self.archivo = f'{path}.json'

    def create_json(self):
        data = {
            'nombre': 'Sergio',
            'edad': 18,
            'nacimiento': '12/07/2005',
            'languages': ['Python', 'Javascript', 'C#', 'C++']
        }
        with open(self.archivo, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def showjson(self):
        with open(self.archivo, "r") as json_file:
            data = json.load(json_file)
        print(json.dumps(data, indent=4))

    def remove_json(self):
        if os.path.exists(self.archivo):
            os.remove(self.archivo)
            print(f'El archivo "{self.archivo}" ha sido eliminado.')
        else:
            print(f'El archivo "{self.archivo}" no existe.')

'''
EXTRA
'''
def trans_information(nombre, edad, nacimiento, lenguajes):
    print(f'nombre: {nombre}\n'
        f'edad: {edad}\n'
        f'nacimiento: {nacimiento}\n'
        f'lenguajes: {lenguajes}')


def read_transform_json(path):
    file_path = f'{path}.json'

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    nombre = data['nombre']
    edad = data['edad']
    nacimiento = data['nacimiento']
    languages = data['languages']
    trans_information(nombre, edad, nacimiento, languages)


def read_transform_xml(path):
    file_path = f'{path}.xml'
    tree = ET.parse(file_path)
    root = tree.getroot()

    nombre = root.find('nombre').text
    edad = root.find('edad').text
    nacimiento = root.find('nacimiento').text
    language = root.find('languages').text
    trans_information(nombre, edad, nacimiento, language)

print('\nXML')
nombrefilexml = 'dataXML'
archivoXML = ArchivoXML(nombrefilexml)
archivoXML.create_xml()
print('\n**** Transformed values from the XML file ****')
read_transform_xml(nombrefilexml)
print('\n**** XML File ****')
archivoXML.showXML()
archivoXML.remove_xml()

print('\nJSON')
nombrefilejson = 'dataJSON'
archivoXML = ArchivoJSON(nombrefilejson)
archivoXML.create_json()
print('\n**** Transformed values from the JSON file ****')
read_transform_json(nombrefilejson)
print('\n**** JSON File ****')
archivoXML.showjson()
archivoXML.remove_json()
