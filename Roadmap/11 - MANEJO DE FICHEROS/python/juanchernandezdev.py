### Python File Handling ###
import os

file = 'juanchernandezdev.txt'

with open(file, 'w') as f:
  f.write('- Juan Carlos Hernandez.\n')
  f.write('- 36.\n')
  f.write('- Python and JavaScript.\n')

with open(file, 'r') as f_read:
  print(f_read.read())

os.remove(file)

#! Optional Challenge
#* Store Sales
def product_generator() -> str:
  name = input('Type the product name : ')
  quantity = int(input('Type the product quantity: '))
  price = float(input('Type the product price: $'))

  return f'{name}, {quantity}, {price}\n'

def lines_list(filename) -> list:
  with open(filename, 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
      print(f'{i + 1} - {line}')
      
  return lines

def create_file(filename):
  open(filename, 'w')
    
def add_product(filename):
  with open(filename, 'a') as f:
    product = product_generator()
    f.write(product)
    
def store_products(filename):
  with open(filename, 'r') as f:
    print('Current Products: ')
    print(f.read())
    
def update_product(filename):
  lines = lines_list(filename)
  line_num = int(input('Type the number of the product you want to update: '))
  new_product = product_generator()
  lines[line_num - 1] = new_product
  print('Product updated.')

  with open(filename, 'w') as f:
    f.writelines(lines)

def delete_product(filename):
  lines = lines_list(filename)
  line_num = int(input('Type the number of the product you want to delete: '))
  lines.remove(lines[line_num - 1])
  print('Product was deleted')
  
  with open(filename, 'w') as f:
    f.writelines(lines)
    
def total_sales(filename):
  total = 0
  
  products = lines_list(filename)
  for line in products:
    components = line.split(', ')
    quantity = int(components[1])
    price = float(components[2])
    total += price * quantity
  
  print(f'Total sales : ${total}')

def product_sales(filename):
  lines = lines_list(filename)
  line_num = int(input('Type the number of the product you want to see the total sales: '))
  components = lines[line_num - 1].split(', ')
  quantity = int(components[1])
  price = float(components[2])
  total = price * quantity
  
  print(f'The total sales for {components[0]} is: ${total}')
        
print('-----Welcome to your store manager-----')

store_name = 'mystore.txt'
open(store_name, 'w')
print('Store Created!!')

while True:
  user_option = input('''
  Please type an option to manage your store inventory:
  - "a" to add an item.
  - "i" to see your inventory.
  - "u" to update and item.
  - "d" to delete an item.
  - "t" to see the total sales.
  - "p" to see the sales of a product.
  - "q" to quit the program.
  ''').lower()

  if user_option == 'a':
    add_product(store_name)
  elif user_option == 'i':
    store_products(store_name)
  elif user_option == 'u':
    update_product(store_name)
  elif user_option == 'd':
    delete_product(store_name)
  elif user_option == 't':
    total_sales(store_name)
  elif user_option == 'p':
    product_sales(store_name) 
  elif user_option == 'q':
    os.remove(store_name)
    break
  