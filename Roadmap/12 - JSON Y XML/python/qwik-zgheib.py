# -- exersice
class Data:
    def __init__(
        self, name: str, age: int, birth_date: str, programming_languages: list[str]
    ) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages


data: Data = Data(
    "qwik", 22, "2002-11-09", ["Python", "JavaScript", "Typescript", "go"]
)
file_name: str = "data"


def create_xml(data: Data, file_name: str) -> None:
    with open(f"{file_name}.xml", "w") as file:
        file.write(
            f"""<?xml version="1.0"?>
                <data>
                    <name>{data.name}</name>
                    <age>{data.age}</age>
                    <birth_date>{data.birth_date}</birth_date>
                    <programming_languages>
                        <language>{data.programming_languages[0]}</language>
                        <language>{data.programming_languages[1]}</language>
                        <language>{data.programming_languages[2]}</language>
                        <language>{data.programming_languages[3]}</language>
                    </programming_languages>
                </data>"""
        )
        print(f"{file_name}.xml created")


def create_json(data: Data, file_name: str) -> None:
    with open(f"{file_name}.json", "w") as file:
        file.write(
            f"""{{
                "name": "{data.name}",
                "age": {data.age},
                "birth_date": "{data.birth_date}",
                "programming_languages": [
                    "{data.programming_languages[0]}",
                    "{data.programming_languages[1]}",
                    "{data.programming_languages[2]}",
                    "{data.programming_languages[3]}"
                ]
            }}"""
        )
        print(f"{file_name}.json created")


def read_file(file_name: str, extension: str) -> None:
    with open(f"{file_name}.{extension}", "r") as file:
        print(file.read())


def delete_file(file_name: str, extension: str) -> None:
    import os

    os.remove(f"{file_name}.{extension}")
    print(f"{file_name}.{extension} deleted")


create_xml(data, file_name)
read_file(file_name, "xml")
delete_file(file_name, "xml")
create_json(data, file_name)
read_file(file_name, "json")
delete_file(file_name, "json")


# -- extra challenge
class CustomData:
    def __init__(
        self, name: str, age: int, birth_date: str, programming_languages: list[str]
    ) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.birth_date} {self.programming_languages}"

    @staticmethod
    def from_xml(file_name: str) -> "CustomData":
        import xml.etree.ElementTree as ET

        tree = ET.parse(f"{file_name}.xml")
        root = tree.getroot()

        name = root.find("name").text
        age = int(root.find("age").text)
        birth_date = root.find("birth_date").text
        programming_languages = [
            language.text for language in root.find("programming_languages")
        ]

        return CustomData(name, age, birth_date, programming_languages)

    @staticmethod
    def from_json(file_name: str) -> "CustomData":
        import json

        with open(f"{file_name}.json", "r") as file:
            data = json.load(file)

        return CustomData(
            data["name"], data["age"], data["birth_date"], data["programming_languages"]
        )

    def to_xml(self, file_name: str) -> None:
        with open(f"{file_name}.xml", "w") as file:
            file.write(
                f"""<?xml version="1.0"?>
                    <data>
                        <name>{self.name}</name>
                        <age>{self.age}</age>
                        <birth_date>{self.birth_date}</birth_date>
                        <programming_languages>
                            <language>{self.programming_languages[0]}</language>
                            <language>{self.programming_languages[1]}</language>
                            <language>{self.programming_languages[2]}</language>
                            <language>{self.programming_languages[3]}</language>
                        </programming_languages>
                    </data>"""
            )
            print(f"{file_name}.xml created")

    def to_json(self, file_name: str) -> None:
        with open(f"{file_name}.json", "w") as file:
            file.write(
                f"""{{
                    "name": "{self.name}",
                    "age": {self.age},
                    "birth_date": "{self.birth_date}",
                    "programming_languages": [
                        "{self.programming_languages[0]}",
                        "{self.programming_languages[1]}",
                        "{self.programming_languages[2]}",
                        "{self.programming_languages[3]}"
                    ]
                }}"""
            )
            print(f"{file_name}.json created")


create_json(data, file_name)
custom_data = CustomData.from_json(file_name)
print(custom_data)
custom_data.to_xml(file_name)
read_file(file_name, "xml")
delete_file(file_name, "xml")
custom_data.to_json(file_name)
read_file(file_name, "json")
delete_file(file_name, "json")
