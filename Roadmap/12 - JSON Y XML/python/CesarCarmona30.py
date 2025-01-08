'''
  EJERCICIO
'''

import json
import os
import xml.etree.ElementTree as ET

user_data = {
  'name': 'César',
  'age': 19,
  'birthDate': '30-07-2004',
  'progLanguages': ['Java', 'C++', 'Python', 'JavaScript']
}

json_name = "CesarCarmona30.json"

with open(json_name, "w", encoding="UTF-8") as file:
  json.dump(user_data, file, indent=2, ensure_ascii=False)

with open(json_name, "r", encoding="UTF-8") as file:
  json_data = json.load(file)

print(json_data)

os.remove(json_name)

xml_name = "CesarCarmona30.xml"
root = ET.Element("userData")

name = ET.SubElement(root, "name")
name.text = "César"

age = ET.SubElement(root, "age")
age.text = "19"

birth_date = ET.SubElement(root, "birthDate")
birth_date.text = "30-07-2004"

prog_languages = ET.SubElement(root, "progLanguages")

lang_1 = ET.SubElement(prog_languages, "Language")
lang_1.text = "Java"

lang_2 = ET.SubElement(prog_languages, "Language")
lang_2.text = "C++"

lang_3 = ET.SubElement(prog_languages, "Language")
lang_3.text = "Python"

lang_4 = ET.SubElement(prog_languages, "Language")
lang_4.text = "JavaScript"

tree= ET.ElementTree(root)
tree.write(xml_name, "utf-8", True)

xml_data = ET.parse(xml_name)
root_data= xml_data.getroot()
for data in root_data:
  if data.tag == "progLanguages":
    print(f'{data.tag}:')
    for lang in data.findall('Language'):
      print(f"\t{lang.tag}: {lang.text}")
  else:
    print(f'{data.tag}: {data.text}')

os.remove(xml_name)

'''
  EXTRA
'''

class UserData:
    def __init__(self, name, age, birth_date, prog_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.prog_languages = prog_languages

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['name'], json_data['age'], json_data['birthDate'], json_data['progLanguages'])

    @classmethod
    def from_xml(cls, xml_data):
        name = xml_data.find('name').text
        age = int(xml_data.find('age').text)
        birth_date = xml_data.find('birthDate').text
        prog_languages = [lang.text for lang in xml_data.find('progLanguages')]
        return cls(name, age, birth_date, prog_languages)

    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Birth Date: {self.birth_date}')
        print('Programming Languages:')
        for lang in self.prog_languages:
            print(f'\t- {lang}')

file_name = "user"

with open(f'{file_name}.json', 'w', encoding='utf-8') as json_file:
    json.dump(user_data, json_file, indent=2, ensure_ascii=False)

with open(f'{file_name}.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    user_from_json = UserData.from_json(json_data)
    print('\nData from JSON:')
    user_from_json.display()

tree.write(f'{file_name}.xml', "utf-8", True)

xml_data = ET.parse(f'{file_name}.xml').getroot()
user_from_xml = UserData.from_xml(xml_data)
print('\nData from XML:')
user_from_xml.display()

os.remove(f'{file_name}.json')
os.remove(f'{file_name}.xml')