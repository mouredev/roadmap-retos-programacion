"""
    #12 JSON Y XML
"""

import json
import os

# Datos a guardar
datos = {
    "nombre": "cesar-ch",
    "edad": 3,
    "fechaNacimiento": "2021-02-03",
    "lenguajes": ["JavaScript", "Python", "Java"],
}

# Guardar en archivo XML
datosXML = f"""<?xml version="1.0" encoding="UTF-8"?>
<datos>
  <nombre>{datos["nombre"]}</nombre>
  <edad>{datos["edad"]}</edad>
  <fechaNacimiento>{datos["fechaNacimiento"]}</fechaNacimiento>
  <lenguajes>{",".join(datos["lenguajes"])}</lenguajes>
</datos>"""

with open("datos.xml", "w") as file:
    file.write(datosXML)
    print("Archivo XML creado")

# Guardar en archivo JSON
with open("datos.json", "w") as file:
    json.dump(datos, file, indent=2)
    print("Archivo JSON creado")

"""
    DIFICULTAD EXTRA
"""

# Leer archivo XML
with open("datos.xml", "r") as file:
    data = file.read()
    print(data)

# Leer archivo JSON
with open("datos.json", "r") as file:
    data = file.read()
    print(data)

# Borrar archivo XML
os.remove("datos.xml")
print("Archivo XML eliminado")

# Borrar archivo JSON
os.remove("datos.json")
print("Archivo JSON eliminado")
