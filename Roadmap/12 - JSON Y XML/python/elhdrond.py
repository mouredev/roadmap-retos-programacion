import json
import os
import xml.etree.ElementTree as xml

"""
    JSON AND XML
"""

data = {
    "name": "Geralt of Rivia",
    "age": 97,
    "birth_date": "1173-05-02",
    "skills": ["Swordsmanship", "Alchemy", "Signs", "Witcher Sense"],
}

base_dir = os.path.dirname(__file__)
xml_file = os.path.join(base_dir, "elhdrond.xml")
json_file = os.path.join(base_dir, "elhdrond.json")


# XML


def create_xml():
    root = xml.Element("character")
    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
    xml.indent(root)
    xml.ElementTree(root).write(xml_file, encoding="unicode", xml_declaration=True)


create_xml()

with open(xml_file, "r") as f:
    print("--- XML ---")
    print(f.read())

os.remove(xml_file)


# JSON


def create_json():
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)


create_json()

with open(json_file, "r") as f:
    print("--- JSON ---")
    print(f.read())

os.remove(json_file)


"""
    EXTRA EXERCISE
"""

create_xml()
create_json()


class Character:
    def __init__(self, name: str, age: int, birth_date: str, skills: list):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.skills = skills

    def __str__(self):
        return (
            f"Name: {self.name} | Age: {self.age} | "
            f"Born: {self.birth_date} | Skills: {', '.join(self.skills)}"
        )


with open(xml_file, "r") as f:
    root = xml.fromstring(f.read())
    xml_character = Character(
        name=root.find("name").text,
        age=int(root.find("age").text),
        birth_date=root.find("birth_date").text,
        skills=[item.text for item in root.find("skills")],
    )
    print("From XML:", xml_character)

with open(json_file, "r") as f:
    d = json.load(f)
    json_character = Character(
        name=d["name"], age=d["age"], birth_date=d["birth_date"], skills=d["skills"]
    )
    print("From JSON:", json_character)

os.remove(xml_file)
os.remove(json_file)
