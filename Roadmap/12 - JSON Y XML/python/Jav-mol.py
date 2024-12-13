# --- 12 JSON Y XML ---
# --- Javier Molina ---

name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
date_birth = input("Ingrese su fecha de nacimiento: ")
dev_leng = input("Ingrese sus lenguajes de programacion separedos por una coma: ").replace(" ","").split(",")
 
# --- Json ---
import json
with open('Jav-mol.json', 'w') as file:
    
    files = {'name':name, 'age':age, "date of birth": date_birth,'dev-lenguages':dev_leng}    
    arch_json = json.dumps(files, indent=4)
    file.write(arch_json)

with open('Jav-mol.json') as file:
    data = file.read()
    print()
    print(" Json ".center(20, "-"))
    print(data)


# --- Xml ---
with open('Jav-mol.xml', 'w') as file:
    
    file.write(f'<name>{name}</name>\n')
    file.write(f'<age>{age}</age>\n')
    file.write(f'<date-birth>{date_birth}</date-birth>\n')
    file.write(f'<dev-leng>{dev_leng}</dev-leng>')

with open('Jav-mol.xml') as file:
    data = file.read()
    print()
    print(" Xml ".center(20,"-"))
    print(data)

