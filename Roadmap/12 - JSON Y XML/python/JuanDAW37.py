"""* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos."""

import os

fichero_xml ='JuanDAW37.xml'
fichero_json ='JuanDAW37.json'

nombre ='Juan Jesús Tenreiro Rodríguez'
edad = 56
fecha_nacimiento = '01-05-1968'
lenguajes = ['JavaScript', 'Java', 'Python', 'PHP', 'Cobol']

def datosXml(fich_xml):    
    fich_xml.write('<persona>\n')
    fich_xml.write(f'<nombre> {nombre} </nombre>\n')
    fich_xml.write(f'<edad> {edad} </edad>\n')
    fich_xml.write(f'<fecha_nacimiento> {fecha_nacimiento} </fecha_nacimiento>\n')
    fich_xml.write('<Lenguajes>\n')
    for lenguaje in lenguajes:
        fich_xml.write(f'<lenguaje> {lenguaje} </lenguaje>\n')
    fich_xml.write('</Lenguajes>\n')
    fich_xml.write('</persona>\n')
    
def datosJson(fich_xml):    
    fich_xml.write('{\n')
    fich_xml.write(f'"nombre":"{nombre}",\n')
    fich_xml.write(f'"edad":{edad},\n')
    fich_xml.write(f'"fecha_nacimiento":"{fecha_nacimiento}",\n')
    fich_xml.write('"lenguajes":[\n')
    for i,lenguaje in enumerate(lenguajes):
        fich_xml.write('{')
        fich_xml.write(f'"lenguaje":"{lenguaje}"')
        if i == len(lenguajes) - 1:        
            fich_xml.write('}\n')
            fich_xml.write(']\n')
        else:
            fich_xml.write('},\n')        
    fich_xml.write('}\n')    

#Fichero XML
if os.path.isfile(fichero_xml):
    with open(fichero_xml, 'r') as fich_xml:
        lineas = fich_xml.readlines()
        for  linea in lineas:                        
            if '</Personas>' in linea:
                lineas.remove('</Personas>')                
                with open(fichero_xml, 'w') as fich_xml:                    
                    for linea in lineas:                                            
                        fich_xml.write(linea)                    
                    datosXml(fich_xml)                    
                    fich_xml.write('</Personas>')
else:
    with open(fichero_xml, 'w') as fich_xml:
        fich_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fich_xml.write('<Personas>\n')
        datosXml(fich_xml)
        fich_xml.write('</Personas>')
        
#Fichero JSON
if os.path.isfile(fichero_json):
    with open(fichero_json, 'r') as fich_json:
        lineas = fich_json.readlines()
        for linea in lineas:                        
            if ']' in linea:
                lineas.remove(']')                
                with open(fichero_json, 'w') as fich_json:                    
                    for linea in lineas:                                            
                        fich_json.write(linea)                    
                    fich_json.write('\n,')
                    datosJson(fich_json)                    
                    fich_json.write(']')
else:
    with open(fichero_json, 'w') as fich_json:
        fich_json.write('[\n')
        datosJson(fich_json)
        fich_json.write(']')
        
os.remove(fichero_xml)
os.remove(fichero_json)
        
# EXTRA
class Persona:
    nombre:str = ''
    fecha_nacimiento:str = ''
    edad:int = 0
    lenguajes:list = []
    
    def __init__(self):
        pass
    
    def setNombre(self, nombre:str):
        self.nombre = nombre
    
    def setEdad(self, edad:int):
        self.edad = edad
    
    def setFechaNacimiento(self, fecha_nacimiento:str):
        self.fecha_nacimiento = fecha_nacimiento
    
    def setlenguajes(self, lenguajes:list):
        self.lenguajes = lenguajes
        
    def imprimeDatosPersona(self):
        print(f'Nombre: {self.nombre}, Fecha de nacimiento: {self.fecha_nacimiento}, edad: {self.edad}') 
        if len(self.lenguajes) > 0:
            print('Lenguajes:')
            for lenguaje in self.lenguajes:
                print(f'- {lenguaje}')
    
def leerXML():
    nombre,  fecha_nacimiento, edad, lenguajes = '', '', 0, []
    persona = Persona()
    try:
        with open(fichero_xml, 'w') as fich_xml:
            datosXml(fich_xml)
        archivo = open(fichero_xml, 'r')        
        for linea in archivo:            
            lista = linea.split(' ')            
            if len(lista) > 1:
                if '<nombre>' in lista:
                    if len(lista)== 6:
                        nombre = lista[1] + ' ' + lista[2]+ ' ' + lista[3] + ' ' + lista[4]
                    elif len(lista) == 5:
                        nombre = lista[1] + ' ' + lista[2]+ ' ' + lista[3]
                    elif len(lista) == 4:
                        nombre = lista[1] + ' ' + lista[2]
                    persona.setNombre(nombre)
                elif '<edad>' in lista:
                    edad = int(lista[1])
                    persona.setEdad(edad) 
                elif '<fecha_nacimiento>' in lista:
                    fecha_nacimiento = lista[1]                    
                    persona.setFechaNacimiento(fecha_nacimiento)
                elif '<lenguaje>' in lista:
                    lenguajes.append(lista[1])
        persona.setlenguajes(lenguajes)
        print('******DATOS OBJETO DE TIPO PERSONA EXTRAIDOS DEL XML******')
        persona.imprimeDatosPersona()
        archivo.close()
        os.remove(fichero_xml)
    except FileExistsError as error:
        print(f'Error de acceso al archivo {error}')
        
def leerJSON():
    nombre,  fecha_nacimiento, edad, lenguajes = '', '', 0, []
    comillas ='"'
    coma = ','
    llave = '}'
    persona = Persona()
    try:
        with open(fichero_json, 'w') as fich_json:
            datosJson(fich_json)
        archivo = open(fichero_json, 'r')        
        for linea in archivo:                        
            if '"nombre":' in linea:
                nombre = linea.split(':')[1].strip()                
                nombre = nombre.replace(comillas, '')
                nombre = nombre.replace(coma, '')
                persona.setNombre(nombre)
            elif '"edad":' in linea:
                edad = linea.split(':')[1].strip()
                edad = edad.replace(comillas, '')
                edad = edad.replace(coma, '')
                persona.setEdad(edad)
            elif '"fecha_nacimiento":' in linea:
                fecha_nacimiento = linea.split(':')[1].strip()
                fecha_nacimiento = fecha_nacimiento.replace(comillas,'')
                fecha_nacimiento = fecha_nacimiento.replace(coma,'')
                persona.setFechaNacimiento(fecha_nacimiento)
            elif '"lenguaje":' in linea:
                lenguaje = linea.split(':')[1].strip()
                lenguaje = lenguaje.replace(comillas, '')
                lenguaje = lenguaje.replace(coma, '')
                lenguaje = lenguaje.replace(llave, '')
                lenguajes.append(lenguaje)
            persona.setlenguajes(lenguajes)            
        print('******DATOS OBJETO DE TIPO PERSONA OBTENIDOS DEL JSON******')
        persona.imprimeDatosPersona()
        archivo.close()
        os.remove(fichero_json)
        
    except FileExistsError as error:
        print(f'Error de acceso al archivo {error}')

leerXML()

leerJSON()