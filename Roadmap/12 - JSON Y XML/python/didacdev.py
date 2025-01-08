import json
import xml.etree.ElementTree as ET
import os

from xml.etree.ElementTree import parse


class Programmer:

    def __init__(self, name: str, age: int, birth: str, languages: list):

        self.name = name
        self.age = age
        self.birth = birth
        self.languages = languages

    def to_json(self):
        data = {
            'name': self.name,
            'age': self.age,
            'birth': self.birth,
            'languages': self.languages
        }

        with open(f'{self.name}.json', 'w') as json_file:
            json.dump(data, json_file)

    def to_xml(self):
        programmer = ET.Element(self.name)

        name = ET.SubElement(programmer, 'name')
        name.text = self.name

        age = ET.SubElement(programmer, 'age')
        age.text = str(self.age)

        birth = ET.SubElement(programmer, 'birth')
        birth.text = self.birth

        languages = ET.SubElement(programmer, 'languages')
        for language in self.languages:
            lang = ET.SubElement(languages, 'language')
            lang.text = language

        with open(f'{self.name}.xml', 'w') as xml_file:
            xml_file.write(ET.tostring(programmer, encoding='unicode'))

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)

        name = data['name']
        age = data['age']
        birth = data['birth']
        languages = data['languages']

        if os.path.exists(json_file):
            os.remove(json_file)
        else:
            print(f"El fichero {json_file} no existe")

        return cls(name, age, birth, languages)

    @classmethod
    def from_xml(cls, xml_file):
        tree = parse(xml_file)
        root = tree.getroot()

        name = root.find('name').text
        age = int(root.find('age').text)
        birth = root.find('birth').text
        languages = [lang.text for lang in root.find('languages')]

        if os.path.exists(xml_file):
            os.remove(xml_file)
        else:
            print(f"El fichero {xml_file} no existe")

        return cls(name, age, birth, languages)


if __name__ == "__main__":
    programmer = Programmer(name="Diego", age=28, birth="10-03-1996",
                            languages=["Python", "Java", "Kotlin", "Swift"])

    programmer.to_json()
    programmer.to_xml()

    programmer2 = Programmer.from_json("Diego.json")

    programmer3 = Programmer.from_xml("Diego.xml")
