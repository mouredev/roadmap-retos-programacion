import json
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as tree
from typing import Optional


def main(data: dict) -> None:
    json_file = Path("data.json")
    run_json(data, json_file)

    xml_file = Path("data.xml")
    run_xml(data, xml_file)


def run_json(data: dict, json_file: Path, only_create: bool = False) -> None:
    json_str = json.dumps(data, ensure_ascii=False, indent=4)

    # Crear fichero:
    json_file.write_text(json_str, encoding="utf-8")

    if only_create:
        return

    # Mostrar fichero:
    print(json_file.read_text())

    # Borrar fichero:
    json_file.unlink()


def run_xml(data: dict, xml_file: Path, only_create: bool = False) -> None:
    root = tree.Element("persona")

    for k, v in data.items():
        element = tree.SubElement(root, k)
        if isinstance(v, list):
            for sub in v:
                sub_element = tree.SubElement(element, "item")
                sub_element.text = sub
        else:
            element.text = str(v)

    tree.indent(root)  # for pretty output
    xml_str = tree.tostring(root, encoding="utf-8")

    # Crear fichero:
    xml_file.write_bytes(xml_str)

    if only_create:
        return

    # Mostrar fichero:
    print(xml_file.read_text())

    # Borrar fichero:
    xml_file.unlink()


def extra(data: dict):

    for file_format in ("json", "xml"):
        file = Path(f"data.{file_format}")
        parser = JsonAndXML(file, file_format=file_format)
        parser.write_file(data)
        parser.read_file()
        parser.modify_data()
        parser.write_file()
        print(parser.file.read_text(encoding="utf-8"))
        parser.file.unlink()


class JsonAndXML:

    def __init__(self, file: Path, file_format: str = "json"):
        self.file = file
        self.file_format = file_format
        self.data = None

    def write_file(self, data: Optional[dict] = None, file_format: Optional[str] = None) -> None:
        data = data or self.data
        file_format = file_format or self.file_format

        if file_format == "json":
            run_json(data, self.file, only_create=True)
        elif file_format == "xml":
            run_xml(data, self.file, only_create=True)
        else:
            raise ValueError(f"No conozco el formato {file_format}")

    def read_file(self, file_format: Optional[str] = None) -> None:
        file_format = file_format or self.file_format

        if not self.file.is_file():
            print(f"No pudimos leer el fichero '{self.file}'. No existe.")
            return

        if file_format == "json":
            self.data = json.loads(self.file.read_text(encoding="utf-8"))
        elif file_format == "xml":
            root = tree.parse(self.file).getroot()

            self.data = {}
            for child in root:
                self.data[child.tag] = child.text
                values = [c.text for c in child]
                if values:
                    self.data[child.tag] = values
        else:
            raise ValueError(f"No conozco el formato {file_format}")

    def modify_data(self):
        if not self.data:
            return
        self.data["nombre"] = "Henry Cavill"


if __name__ == "__main__":
    persona = {
        "nombre": "Iñaki Silanes",
        "edad": 46,
        "fecha_de_nacimiento": datetime(1977, 6, 11, 9, 0).isoformat(),
        "lenguajes_de_programación": ["python", "bash", "perl", "fortran", "javascript"],
    }

    main(data=persona)
    extra(data=persona)
