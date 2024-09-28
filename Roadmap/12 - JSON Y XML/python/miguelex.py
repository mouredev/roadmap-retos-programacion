import json
import xml.etree.ElementTree as ET
import xml.dom.minidom

datos = {
    'nombre': 'Miguelex',
    'edad': 48,
    'fechanacimiento': '1975-09-13',
    'Lenguajes': ['php', 'javascript', 'python', 'c#', 'java', 'pascal']
}

# Generar archivo JSON
with open('miguelex.json', 'w') as file:
    json.dump(datos, file, indent=4)

# Mostrar contenido del archivo JSON
with open('miguelex.json', 'r') as file:
    datos_json = file.read()
    print("JSON:")
    print(datos_json)

# Generar archivo XML
root = ET.Element('root')
for key, value in datos.items():
    if isinstance(value, list):
        lenguajes = ET.SubElement(root, key)
        for lenguaje in value:
            ET.SubElement(lenguajes, 'lenguaje').text = lenguaje
    else:
        ET.SubElement(root, key).text = str(value)

tree = ET.ElementTree(root)

# Guardar archivo XML con formato ordenado
xml_str = ET.tostring(root, encoding='utf-8')
dom = xml.dom.minidom.parseString(xml_str)
pretty_xml_str = dom.toprettyxml(indent="  ")

with open('miguelex.xml', 'w', encoding='utf-8') as file:
    file.write(pretty_xml_str)


# Mostrar contenido del archivo XML
with open('miguelex.xml', 'r') as file:
    datos_xml = file.read()
    print("XML:")
    print(datos_xml)

# Extra

class Miguelex:
    def __init__(self, nombre, edad, fecha_nacimiento, lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes

    @classmethod
    def from_json(cls):
        with open('miguelex.json', 'r') as file:
            data = json.load(file)
            return cls(data['nombre'], data['edad'], data['fechanacimiento'], data['Lenguajes'])

    @classmethod
    def from_xml(cls):
        tree = ET.parse('miguelex.xml')
        root = tree.getroot()
        nombre = root.find('nombre').text
        edad = int(root.find('edad').text)
        fecha_nacimiento = root.find('fechanacimiento').text
        lenguajes = [lenguaje.text for lenguaje in root.find('Lenguajes')]
        return cls(nombre, edad, fecha_nacimiento, lenguajes)

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha de nacimiento: {self.fecha_nacimiento}\nLenguajes: {', '.join(self.lenguajes)}"

print("\n\nDe JSON a clase:\n")
miguelex_from_json = Miguelex.from_json()
print(miguelex_from_json)

print("\n\nDe XML a clase:\n")
miguelex_from_xml = Miguelex.from_xml()
print(miguelex_from_xml)
