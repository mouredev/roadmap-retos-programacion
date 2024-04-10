import os
import json
import xml.etree.ElementTree as ET

# ------ Ejercicio

JSONFILE = "data.json"
XMLFILE = "data.xml"

my_dict = {
    "name": "Yair Canas",
    "age": 24,
    "birth": "03/01/2000",
    "languages": ["Python", "C", "C++", "Java", "Matlab"]
}

# I. json

with open(JSONFILE, 'w') as f:
    json.dump(my_dict, f)

with open(JSONFILE, 'r') as f:
    print(json.load(f))

# II. xml

p = ET.Element("data")

for key, value in my_dict.items():
    c = ET.SubElement(p, key)
    
    if isinstance(value, list):
        for item in value:
            ET.SubElement(c, "item").text = item

    else:
        c.text = str(value)

tree = ET.ElementTree(p)
tree.write(XMLFILE)

with open(XMLFILE, "r") as f:
    print(f.read())


# ------ Extra

class DataTransform:

    extension: str = ""

    def __init__(self, file: str):
        self.file = file
        self.extension = self.file.split('.')

    
    def read(self) -> dict:
        data = dict()
        if self.extension[1] == "json":
            with open(JSONFILE, 'r') as f:
                data = json.load(f)

        else:
            tree = ET.parse(XMLFILE)
            root = tree.getroot()

            for item in root:
                if len(item) == 0:
                    data[item.tag] = int(item.text) if item.text.isdigit() else item.text

                else:
                    data[item.tag] = [attrib.text for attrib in item]

        return data


data = DataTransform(XMLFILE)
print(data.read())

os.remove(JSONFILE)
os.remove(XMLFILE)
