### JSON, XML Files ###
import json
import xml.etree.ElementTree as xml
import os

info = {
  'name': 'Mark Doe',
  'age': 38,
  'birth_date': '15/18/1965',
  'languages': ['python', 'javascript', 'java']
  
}

#* JSON
filename_json = 'myjson.json'

with open(filename_json, 'w') as json_file:
  json.dump(info, json_file, indent=2)
  
with open(filename_json, 'r') as json_file:
  print(json_file.read())
  
#* XML
filename_xml = 'myxml.xml'

root = xml.Element('info')

for key,value in info.items():
  child = xml.SubElement(root, key)
  if isinstance(value, list):
    for item in value:
      xml.SubElement(child, 'item').text = item
  else:
    child.text = str(value)

tree = xml.ElementTree(root)
tree.write(filename_xml)

with open(filename_xml, 'r') as xml_file:
  print(xml_file.read())
  
#! Optional Challenge

class Data:
  def __init__(self, name, age, birth_date, languages) -> None:
    self.name = name
    self.age = age
    self.birth_date = birth_date
    self.languages = languages
    
with open(filename_xml, 'r') as xml_file:
  root = xml.fromstring(xml_file.read())
  name = root.find('name').text
  age = root.find('age').text
  birth_date = root.find('birth_date').text
  languages = []
  for item in root.find('languages'):
    languages.append(item.text)
    
  my_data = Data(name, age, birth_date, languages)
  print(my_data.__dict__)
    
    
with open(filename_json, 'r') as json_file:
  info = json.load(json_file)
  my_info = Data(info['name'], info['age'], info['birth_date'], info['languages'])
  print(my_info.__dict__)
  
os.remove(filename_xml)
os.remove(filename_json)
