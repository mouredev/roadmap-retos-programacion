"""
*JSON y XML
"""
import json
from os import remove

#!Json
#?persona es un objeto de python (diccionario)
persona = {
    "nombre" : "sorubadguy",
    "edad" : 30,
    "f_nac" : "27/03/94",
    "leng_progra" : "python"
}

#?convierto a persona en un JSON
with open("archivo.json", "w") as j:
    json.dump(persona, j)

#?leer y mostrar el archivo.json
with open("archivo.json", "r") as j:
    #?Leo el archivo Json
    objson = json.load(j)
    
print(objson)
print(type(objson))

remove("archivo.json")

