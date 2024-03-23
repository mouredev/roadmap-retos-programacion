import json
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET


def main() -> None:
    data = {
        "nombre": "Iñaki Silanes",
        "edad": 46,
        "fecha_de_nacimiento": datetime(1977, 6, 11, 9, 0).isoformat(),
        "lenguajes_de_programación": ["python", "bash", "perl", "fortran", "javascript"],
    }

    run_json(data)
    run_xml(data)


def run_json(data: dict) -> None:
    json_file = Path("data.json")
    json_str = json.dumps(data, ensure_ascii=False, indent=4)

    # Crear fichero:
    json_file.write_text(json_str, encoding="utf-8")

    # Mostrar fichero:
    print(json_file.read_text())

    # Borrar fichero:
    json_file.unlink()


def run_xml(data: dict) -> None:
    xml_file = Path("data.xml")

    root = ET.Element("persona")

    for k, v in data.items():
        element = ET.SubElement(root, k)
        if isinstance(v, list):
            for sub in v:
                sub_element = ET.SubElement(element, "item")
                sub_element.text = sub
        else:
            element.text = str(v)

    ET.indent(root)  # for pretty output
    xml_str = ET.tostring(root, encoding="utf-8")

    # Crear fichero:
    xml_file.write_bytes(xml_str)

    # Mostrar fichero:
    print(xml_file.read_text())

    # Borrar fichero:
    xml_file.unlink()


if __name__ == "__main__":
    main()
