#import os
import xml.etree.ElementTree as xml
import json

xml_file = "Irenetitor.xml"
json_file = "Irenetitor.json"

user = {
  "name": "Ana",
  "age": 25,
  "birth_date": "23-02-2000",
  "languages": ["Python", "JavaScript", "Java"]
}

#XML

def save_xml():
    
    root = xml.Element("user")

    for key, value in user.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for language in value:
                xml.SubElement(child, "language").text = language
        else:
            child.text = str(value)

    # ✔ Write the file inside the function
    tree = xml.ElementTree(root)
    tree.write(xml_file)


save_xml()

with open(xml_file) as xml_user:
    print(xml_user.read())

#os.remove(xml_file)


'''
<data>
    <name>Ana</name>
    <age>25</age>
    <birth_date>23-02-2000</birth_date>
    <languages>
        <language>Python</language>
        <language>JavaScript</language>
        <language>Java</language>
    </languages>
</data>

'''

#JSON

with open(json_file, "w") as json_user:
    json.dump(user, json_user)

with open(json_file, "r") as json_user:
    print(json_user.read())

#os.remove(json_file)

'''
{
  "name": "Ana",
  "age": 25,
  "birth_date": "23-02-2000",
  "languages": ["Python", "JavaScript", "Java"]
}
'''

#EXTRA EXERCISE

xml_file = "user_parsed.xml"
json_file = "user_parsed.json"

user_data = {
    "name": "Juan",
    "age": 29,
    "birth_date": "23-02-1996",
    "languages": ["Python", "JavaScript", "Java"]
}

# Save data as XML

def save_xml(data: dict, filename: str) -> None:
    root = xml.Element("user")  # <user> ... </user>

    for key, value in data.items():
        child = xml.SubElement(root, key)

        if isinstance(value, list):
            # For lists -> create "<language>" for each item
            for language in value:
                xml.SubElement(child, "language").text = language
        else:
            # Simple values -> just put text
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

# Save data as JSON

def save_json(data: dict, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as json_user:
        json.dump(data, json_user, indent=4)


# USER CLASS

class User:
    def __init__(self, name, age, birth_date, languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.languages = languages

    def __repr__(self):
        return (
            f"User(name={self.name!r}, age={self.age}, "
            f"birth_date={self.birth_date!r}, languages={self.languages!r})"
        )

    @classmethod
    def from_json(cls, filename: str):
        """Create a User object from a JSON file."""
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        return cls(
            name=data["name"],
            age=data["age"],
            birth_date=data["birth_date"],
            languages=data["languages"],
        )

    @classmethod
    def from_xml(cls, filename: str):
        """Create a User object from an XML file."""
        tree = xml.parse(filename)
        root = tree.getroot()

        # Simple elements
        name = root.find("name").text
        age = int(root.find("age").text)
        birth_date = root.find("birth_date").text

        # Languages (list)
        languages = []
        langs_node = root.find("languages")
        if langs_node is not None:
            for lang_tag in langs_node.findall("language"):
                languages.append(lang_tag.text)

        return cls(name, age, birth_date, languages)


# RUN THE FULL FLOW

save_xml(user_data, xml_file)
save_json(user_data, json_file)

print("\n--- XML FILE CONTENT ---")
with open(xml_file, "r", encoding="utf-8") as xml_user:
    print(xml_user.read())

print("\n--- JSON FILE CONTENT ---")
with open(json_file, "r", encoding="utf-8") as json_user:
    print(json_user.read())

# Create User objects
user_from_xml = User.from_xml(xml_file)
user_from_json = User.from_json(json_file)

print("\n--- USER OBJECTS ---")
print("From XML: ", user_from_xml)
print("From JSON:", user_from_json)

# Optional delete:
# os.remove(xml_file)
# os.remove(json_file)
