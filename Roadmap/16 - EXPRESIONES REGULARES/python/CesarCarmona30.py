import re

text = input("Introduce un texto (incluye números): ")
numbers = re.findall(r"\d+", text)

print(f"Numeros del texto introducido: {numbers}")

'''
  EXTRA
'''

email = input("Introduce un email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
# Iteramos hasta que el usuario ingrese un email valido
while not re.search(pattern, email):
  email = input("Introduce un email válido (email@example.com): ")
print(f"Email válido: {email}")


# number_phone = input("Introduce un número de teléfono")
pattern = r'^(\(\+\d{1,3}\)\s?)?(\d{2}\s?(-|\s)?\d{4}\s?(-|\s)?){2}\d{2}$'
# lista de posibles formatos teléfonicos con algunos incorrectos
number_list = [
  "(+55) 5555555555",
  "(+55) 55 5555 5555",
  "(+55) 55 55 55 55 55",
  "(+55) 55-5555-5555",
  "6532ww732"
  "(+55) 55-55-55-55-55",
  "+55 5555555555",
  "+55 55 5555 5555",
  "+55 55 55 55 55 55",
  "543654563"
  "+55 55-5555-5555",
  "+55 55-55-55-55-55",
  "46525365426423642"
  "5555555555",
  "55 5555 5555",
  "55-5555-5555",
  "534264236426246432"
  "55 55 55 55 55",
  "55-55-55-55-55",
  "53452grfsyrw"
]
  # Iteramos hasta que el usuario ingrese un número válido
  # while not re.search(pattern, number_phone):
    # number_phone = input("Introduce un número de teléfono válido: (+55 5555555555)")

# Recorremos la lista para validar los formatos
for number_phone in number_list:
  if not re.search(pattern, number_phone):
    print(f'{number_phone} es válido')
  else:
    print(f'{number_phone} no válido')

pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/\S*)?$'

urls_list = [
  "https://www.ejemplo.com",
  "http://ejemplo.com",
  "https://subdominio.ejemplo.com",
  "http://www.subdominio.ejemplo.com",
  "https://ejemplo.com/ruta",
  "http://ejemplo.com/ruta/ejemplo",
  "https://www.ejemplo.com/ruta/ejemplo.html",
  "http://ejemplo.com/ruta?parametro=valor",
  "https://www.ejemplo.com/ruta?parametro1=valor1&parametro2=valor2",
  "http://subdominio.ejemplo.com/ruta",
  "https://ejemplo.com/ruta#seccion",
  "http://www.ejemplo.com#seccion",
  "https://www.ejemplo.com/ruta#seccion",
  "http://subdominio.ejemplo.com/ruta#seccion",
  "https://www.ejemplo.com/ruta/ejemplo.html?parametro=valor#seccion",
  "http://ejemplo.com/ruta/ejemplo?parametro1=valor1&parametro2=valor2#seccion",
  "https://subdominio.ejemplo.com/ruta/ejemplo.html?parametro=valor#seccion"
  "www.ejemplo.com",
  "ejemplo.com",
  "ftp://ejemplo.com",
  "http://ejemplo",
  "http://ejemplo.com?",
  "http://ejemplo.com#",
  "http://ejemplo.com/ruta/",
  "http://ejemplo.com//ruta",
  "http://ejemplo.com/ruta//",
  "http://ejemplo.com/?parametro=valor",
  "http://ejemplo.com/#seccion",
  "http://ejemplo.com/ruta//ejemplo.html",
  "http://ejemplo.com//ruta/ejemplo",
  "http://ejemplo.com/ruta/?parametro=valor",
  "http://ejemplo.com/ruta#seccion/"
  "http://ejemplo.com/ruta//ejemplo.html?parametro=valor",
  "http://ejemplo.com/ruta/ejemplo?parametro1=valor1&parametro2=valor2#seccion/",
  "http://subdominio ejemplo.com",
  "http://ejemplo .com",
  "http://.ejemplo.com",
  "http://ejemplo..com",
  "http://ejemplo.com:abc",
  "http://ejemplo.com:80abc",
  "http://ejemplo.com:80abc/ruta",
  "http://ejemplo.com:80abc/ruta/ejemplo.html",
  "http://ejemplo.com:80abc/ruta?parametro=valor",
  "http://ejemplo.com:80abc/ruta#seccion",
  "http://ejemplo.com:80abc/ruta/ejemplo.html?parametro=valor#seccion",
  "https://chat.openai.com/c/8c6fa1c0-7590-4c21-be8c-ff8d48edbfa1",
  "https://docs.python.org/es/3/library/re.html",
  "https://www.youtube.com/watch?v=ehTuatSx5Wc"
]
# url = input("Introduce una URL válida: ")

# Validar la URL
for url in urls_list:
  if re.match(pattern, url):
      print("La URL es válida.")
  else:
      print("La URL no es válida.")
