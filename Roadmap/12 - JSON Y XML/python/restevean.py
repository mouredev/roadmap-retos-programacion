import xml.etree.ElementTree as ElT
import json
import os


# Sample data for demonstration
sample_data = {
    "Name": "Laura Gomez",
    "Age": 28,
    "Date of birth": "1995-08-23",
    "Programming languages": ["JavaScript", "Ruby", "Go"]
}

# Creating the XML file
root_demo = ElT.Element("Person")
for key, value in sample_data.items():
    sanitized_key = key.replace(" ", "_")
    if isinstance(value, list):
        subelement = ElT.SubElement(root_demo, sanitized_key)
        for item in value:
            ElT.SubElement(subelement, "Language").text = item
    else:
        ElT.SubElement(root_demo, sanitized_key).text = str(value)
tree_demo = ElT.ElementTree(root_demo)
tree_demo.write("demo_data.xml", encoding="utf-8")

# Creating the JSON file
with open("demo_data.json", "w") as json_file_demo:
    json.dump(sample_data, json_file_demo, indent=4)


class PersonalData:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.birth_date = ""
        self.programming_languages = []

    def load_from_json(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        self._assign_data(data)

    def load_from_xml(self, file_path):
        tree = ElT.parse(file_path)
        root = tree.getroot()
        data = {child.tag.replace("_", " "): child.text for child in root if not list(child)}
        languages = [elem.text for elem in root.find("Programming_languages")]
        if languages:
            # Convert the list to a string to match the expected type
            data["Programming languages"] = ", ".join(filter(None, languages))
        self._assign_data(data)

    def _assign_data(self, data):
        self.name = data.get("Name", "")
        self.age = int(data.get("Age", 0))
        self.birth_date = data.get("Date of birth", "")
        self.programming_languages = data.get("Programming languages", "")


# Using the class to load the data from the files
person_from_json = PersonalData()
person_from_json.load_from_json("demo_data.json")

person_from_xml = PersonalData()
person_from_xml.load_from_xml("demo_data.xml")

# Cleaning up by deleting the files
os.remove("demo_data.xml")
os.remove("demo_data.json")

print("Data loaded from JSON:", vars(person_from_json))
print("Data loaded from XML:", vars(person_from_xml))
