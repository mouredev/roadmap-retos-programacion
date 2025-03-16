import os

user = 'CesarCarmona30'
data = ['César Carmona\n', '19\n', 'Python']

with open(f'{user}.txt', "w", encoding='utf-8') as file:
  file.writelines(data)

with open(f'{user}.txt', "r", encoding='utf-8') as file:
  content = file.read()

print(content)

os.remove(f'{user}.txt')
print(f'El archivo {user}.txt ha sido eliminado con éxito')

file_name = 'ventas.txt'
def menu():
  print('\n\nGestión de ventas: ')
  print('1. Añadir producto')
  print('2. Consultar producto')
  print('3. Listar productos')
  print('4. Actualizar producto')
  print('5. Eliminar producto')
  print('6. Calcular venta por producto')
  print('7. Calcular venta total')
  print('8. Salir')

def addProduct():
  product = input("Nombre del producto: ")
  amount = input("Cantidad vendida: ")
  price = input("Precio del producto:")
  with open(file_name, 'a') as file:
    file.write(f'{product}, {amount}, {price}')
  print('Producto añadido correctamente')

def seeProduct():
  product_name = input('Nombre del producto a consultar: ')
  with open(file_name, 'r') as file:
    lines = file.readlines()
  for line in lines:
    data = line.split(', ')
    if product_name in data:
      print(f'Nombre: {line[0]}, Cantidad vendida: {line[1]}, Precio: {line[2]}')
    else:
      print('Producto no encontrado')

def seeProducts():
  with open(file_name, 'r') as file:
    lines = file.readlines()
  for line in lines:
    data = line.split(', ')
    print(f'Nombre: {line[0]}, Cantidad vendida: {line[1]}, Precio: {line[2]}')

def updateProduct():
  product_name = input('Nombre del producto a actualizar: ')
  new_amount = input('Nueva cantidad vendida: ')
  with open(file_name, 'r') as file:
    lines = file.readlines()
  with open(file_name, 'w') as file:
    for line in lines:
      if product_name in line:
        file.write(f'{product_name}, {new_amount}, {line[2]}')
      else:
        file.write(line)

def deleteProduct():
  product_name = input('Nombre del producto a eliminar: ')
  with open(file_name, 'r') as file:
    lines = file.readlines()
  with open(file_name, 'w') as file:
    for line in lines:
      if product_name not in line:
        file.write(line)
    print('Producto eliminado')

def productSales():
  product_name = input('Nombre del producto a consultar: ')
  with open(file_name, 'r') as file:
    lines = file.readlines()
  for line in lines:
    data = line.split(', ')
    if product_name in data:
      amount = int(data[1])
      price = int(data[2])
      sales = amount * price
      print(f'Venta del producto: {sales}')
    else:
      print('Producto no encontrado')

def totalSales():
  with open(file_name, 'r') as file:
    lines = file.readlines()
  total_sales = 0  
  for line in lines:
    data = line.split(', ')
    amount = int(data[1])
    price = int(data[2])
    total_sales += amount * price
    print(f'Venta total: {total_sales}')

def managerSales():
  while True:
    menu()
    option = input('Eliga una opción: ')
    if option == '1':
      addProduct()
    elif option == '2':
      seeProduct()
    elif option == '3':
      seeProducts()
    elif option == '4':
      updateProduct()
    elif option == '5':
      deleteProduct()
    elif option == '6':
      productSales()
    elif option == '7':
      totalSales()
    elif option == '8':  
      if os.path.exists(file_name):
        os.remove(file_name)
      print("Saliendo del programa...")
      break
    else:
      print("Opción no válida.")

managerSales()