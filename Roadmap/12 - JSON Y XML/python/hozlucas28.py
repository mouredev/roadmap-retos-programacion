"""Operation system module"""

from typing import TypedDict, Self
import datetime
import json
import os
import xml.etree.ElementTree as xmlTree


"""
    JSON and XML files...
"""

print("JSON and XML files...\n")

JsonContent = TypedDict(
    "JsonContent",
    {"age": int, "bornDate": str, "name": str, "programmingLanguages": list[str]},
)

XmlContent = TypedDict(
    "XmlContent",
    {
        "age": int,
        "born-date": str,
        "name": str,
        "programming-languages": dict[str, str],
    },
)

JSON_FILE_PATH: str = "author.json"
XML_FILE_PATH: str = "author.xml"

# Delete files if exist
if os.path.exists(path=JSON_FILE_PATH):
    os.remove(path=JSON_FILE_PATH)

if os.path.exists(path=XML_FILE_PATH):
    os.remove(path=XML_FILE_PATH)

# Create files and write content
born_date = datetime.datetime(year=2002, month=2, day=20)

with open(file=JSON_FILE_PATH, mode="w", encoding="utf8") as __file:
    json_content: JsonContent = {
        "age": 22,
        "bornDate": born_date.strftime(format="%d/%m/%Y, %H:%M:%S"),
        "name": "Lucas",
        "programmingLanguages": ["TypeScript", "Python", "Go (Golang)"],
    }

    stringified_json: str = json.dumps(obj=json_content, indent=4, sort_keys=True)
    __file.writelines(stringified_json)
    __file.close()


def dict_to_xml(
    dictionary: dict, parent: None | xmlTree.Element = None
) -> xmlTree.Element:
    """Transform a dictionary to a XML tree"""
    root: xmlTree.Element = xmlTree.Element("root") if parent is None else parent

    for key, value in dictionary.items():
        line: xmlTree.Element = xmlTree.SubElement(root, key)
        if isinstance(value, dict):
            line: xmlTree.Element = dict_to_xml(dictionary=value, parent=line)
            continue

        line.text = str(object=value)

    return root


with open(file=XML_FILE_PATH, mode="w", encoding="utf8") as __file:
    xml_content: XmlContent = {
        "age": 22,
        "born-date": born_date.strftime(format="%d/%m/%Y, %H:%M:%S"),
        "name": "Lucas",
        "programming-languages": {
            "typescript": "TypeScript",
            "python": "Python",
            "go": "Go (Golang)",
        },
    }

    xml: xmlTree.Element = dict_to_xml(dictionary=dict(xml_content))

    stringified_xml: str = xmlTree.tostring(element=xml).decode(encoding="utf8")
    __file.write(stringified_xml)
    __file.close()


# Print files content
with open(file=JSON_FILE_PATH, mode="r", encoding="utf8") as __file:
    for __line in __file.readlines():
        print(__line.replace("\n", ""))
    __file.close()

print()


with open(file=XML_FILE_PATH, mode="r", encoding="utf8") as __file:
    for __line in __file.readlines():
        print(__line)
    __file.close()

# Delete files
os.remove(path=JSON_FILE_PATH)
os.remove(path=XML_FILE_PATH)

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")


class JsonFile:
    """JSON file class"""

    __path: str
    __is_deleted: bool

    def __init__(self, path, initial_content: JsonContent) -> None:
        self.__path = path
        self.__is_deleted = False
        self.__write_content(content=initial_content)

    def get_content(self) -> JsonContent:
        """Return file content"""
        self.__validate()

        with open(file=self.__path, mode="r", encoding="utf8") as __file:
            __content: JsonContent = json.load(fp=__file)
            __file.close()

        return __content

    def __validate(self) -> None:
        if self.__is_deleted:
            raise FileNotFoundError

    def __write_content(self, content: JsonContent) -> Self:
        __stringified_content: str = json.dumps(obj=content, indent=4, sort_keys=True)

        with open(file=self.__path, mode="w", encoding="utf8") as __file:
            __file.write(__stringified_content)
            __file.close()

        return self

    def append_language(self, __programming_language: str) -> Self:
        """Append programming language to "programmingLanguages" key"""
        self.__validate()

        __content: JsonContent = self.get_content()
        __content["programmingLanguages"].append(__programming_language)
        self.__write_content(content=__content)

        return self

    def delete_file(self) -> None:
        """Delete file"""
        self.__validate()
        os.remove(path=self.__path)
        self.__is_deleted = True

    def remove_language(self, __programming_language: str) -> Self:
        """Delete programming language inside "programmingLanguages" key"""
        self.__validate()

        __content: JsonContent = self.get_content()

        try:
            for _, __language in enumerate(iterable=__content["programmingLanguages"]):
                if __language.upper() == __programming_language.upper():
                    __content["programmingLanguages"].remove(__language)
        except ValueError:
            pass

        self.__write_content(content=__content)

        return self

    def update_age(self, __age: int) -> Self:
        """Update age"""
        self.__validate()

        __content: JsonContent = self.get_content()
        __content["age"] = __age
        self.__write_content(content=__content)

        return self

    def update_born_date(self, __born_date: datetime.date) -> Self:
        """Update born date"""
        self.__validate()

        __content: JsonContent = self.get_content()
        __content["bornDate"] = __born_date.strftime(format="%d/%m/%Y, %H:%M:%S")
        self.__write_content(content=__content)

        return self

    def update_name(self, __name: str) -> Self:
        """Update name"""
        self.__validate()

        __content: JsonContent = self.get_content()
        __content["name"] = __name
        self.__write_content(content=__content)

        return self


class XmlFile:
    """XML file class"""

    __path: str
    __is_deleted: bool

    def __init__(self, path, initial_content: XmlContent) -> None:
        self.__path = path
        self.__is_deleted = False
        self.__write_content(content=initial_content)

    def get_content(self) -> XmlContent:
        """Return file content"""
        self.__validate()

        __content: XmlContent = {
            "age": 0,
            "born-date": "",
            "name": "",
            "programming-languages": {},
        }
        __xml: xmlTree.ElementTree = xmlTree.parse(self.__path)

        __age: xmlTree.Element | None = __xml.find("age")
        __born_date: xmlTree.Element | None = __xml.find("born-date")
        __name: xmlTree.Element | None = __xml.find("name")
        __programming_languages: xmlTree.Element | None = __xml.find(
            "programming-languages"
        )

        if __age is not None:
            __value: str | int = __age.text or __content["age"]
            __content["age"] = int(__value)

        if __name is not None:
            __content["name"] = __name.text or __content["name"]

        if __born_date is not None:
            __content["born-date"] = __born_date.text or __content["born-date"]

        if __programming_languages is not None:
            for __language in __programming_languages.iter():
                if __language.tag is not None and __language.text is not None:
                    __content["programming-languages"][
                        __language.tag.lower()
                    ] = __language.text

        return __content

    def __validate(self) -> None:
        if self.__is_deleted:
            raise FileNotFoundError

    def __write_content(self, content: XmlContent) -> Self:
        __xml: xmlTree.Element = dict_to_xml(dictionary=dict(content))
        __stringified_content: str = xmlTree.tostring(element=__xml).decode(
            encoding="utf8"
        )

        with open(file=self.__path, mode="w", encoding="utf8") as __file:
            __file.write(__stringified_content)
            __file.close()

        return self

    def append_language(self, __programming_language: str) -> Self:
        """Append programming language to "programmingLanguages" key"""
        self.__validate()

        __content: XmlContent = self.get_content()
        __content["programming-languages"][
            __programming_language
        ] = __programming_language
        self.__write_content(content=__content)

        return self

    def delete_file(self) -> None:
        """Delete file"""
        self.__validate()
        os.remove(path=self.__path)
        self.__is_deleted = True

    def remove_language(self, __programming_language: str) -> Self:
        """Delete programming language inside "programmingLanguages" key"""
        self.__validate()

        __content: XmlContent = self.get_content()
        __sanitized_content: XmlContent = __content.copy()
        __sanitized_content["programming-languages"].clear()

        try:
            for __key, __value in __content["programming-languages"].items():
                if __key.upper() != __programming_language.upper():
                    __sanitized_content["programming-languages"][__key] = __value
        except ValueError:
            pass

        self.__write_content(content=__sanitized_content)

        return self

    def update_age(self, __age: int) -> Self:
        """Update age"""
        self.__validate()

        __content: XmlContent = self.get_content()
        __content["age"] = __age
        self.__write_content(content=__content)

        return self

    def update_born_date(self, __born_date: datetime.date) -> Self:
        """Update born date"""
        self.__validate()

        __content: XmlContent = self.get_content()
        __content["born-date"] = __born_date.strftime(format="%d/%m/%Y, %H:%M:%S")
        self.__write_content(content=__content)

        return self

    def update_name(self, __name: str) -> Self:
        """Update name"""
        self.__validate()

        __content: XmlContent = self.get_content()
        __content["name"] = __name
        self.__write_content(content=__content)

        return self


json_file: JsonFile = JsonFile(
    path="additional-challenge.json",
    initial_content={
        "age": 22,
        "bornDate": datetime.datetime(day=20, month=2, year=2002).strftime(
            format="%d/%m/%Y, %H:%M:%S"
        ),
        "name": "Lucas",
        "programmingLanguages": ["Python"],
    },
)

SHOULD_EXIT: bool = False
while not SHOULD_EXIT:
    # pylint: disable=line-too-long
    operation: str = input(
        "\nSelect an operation ('append language', 'print', 'remove language', 'update age', 'update born date', 'update name', or 'exit'): "
    ).upper()

    if operation == "APPEND LANGUAGE":
        programming_language: str = input("\nNew programming language: ")
        json_file.append_language(programming_language)

    elif operation == "PRINT":
        print(f"\n{json_file.get_content()}", end="")

    elif operation == "REMOVE LANGUAGE":
        programming_language: str = input("\nNew programming language: ")
        json_file.remove_language(programming_language)

    elif operation == "UPDATE AGE":
        age: str = input("\nNew age: ")
        json_file.update_age(int(age))

    elif operation == "UPDATE BORN DATE":
        __born_date: str = input("\nNew born date (year-month-day): ")
        json_file.update_born_date(datetime.datetime.fromisoformat(__born_date))

    elif operation == "UPDATE NAME":
        name: str = input("\nNew name: ")
        json_file.update_name(name)

    elif operation == "EXIT":
        json_file.delete_file()
        SHOULD_EXIT = True

    else:
        print("\nInvalid operation! Try again...")

xml_file: XmlFile = XmlFile(
    path="additional-challenge.xml",
    initial_content={
        "age": 22,
        "born-date": datetime.datetime(day=20, month=2, year=2002).strftime(
            format="%d/%m/%Y, %H:%M:%S"
        ),
        "name": "Lucas",
        "programming-languages": {"python": "Python"},
    },
)

SHOULD_EXIT = False
while not SHOULD_EXIT:
    # pylint: disable=line-too-long
    operation: str = input(
        "\nSelect an operation ('append language', 'print', 'remove language', 'update age', 'update born date', 'update name', or 'exit'): "
    ).upper()

    if operation == "APPEND LANGUAGE":
        programming_language: str = input("\nNew programming language: ")
        xml_file.append_language(programming_language)

    elif operation == "PRINT":
        print(f"\n{xml_file.get_content()}\n", end="")

    elif operation == "REMOVE LANGUAGE":
        programming_language: str = input("\nNew programming language: ")
        xml_file.remove_language(programming_language)

    elif operation == "UPDATE AGE":
        age: str = input("\nNew age: ")
        xml_file.update_age(int(age))

    elif operation == "UPDATE BORN DATE":
        __born_date: str = input("\nNew born date (year-month-day): ")
        xml_file.update_born_date(datetime.datetime.fromisoformat(__born_date))

    elif operation == "UPDATE NAME":
        name: str = input("\nNew name: ")
        xml_file.update_name(name)

    elif operation == "EXIT":
        xml_file.delete_file()
        SHOULD_EXIT = True

    else:
        print("\nInvalid operation! Try again...")
