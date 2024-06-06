'''
  VALOR Y REFERENCIA
'''

# Datos por valor

value_x = 5
value_y = value_x
value_y += 15

print(value_x)
print(value_y)


# Datos por referencia

my_dict_a = {
  'Mexico': 'Mexico City',
  'Spain': 'Madrid',
  'Chile': 'Santiago',
  'Argentina': 'Buenos Aires'
}

my_dict_b = my_dict_a
my_dict_b['France'] = 'Paris'
print(my_dict_a)
print(my_dict_b)


# Función con dato por valor

def modify_val(value_a):
  value_a = 'valor modificado'
  print(value_a)

value_b = 'valor inicial'
print(value_b)
modify_val(value_b)
print(value_b)


# Función con dato por referencia

def modify_ref(ref_j):
  ref_j['dato'] = 'dato modificado'
  print(ref_j)

ref_x = {
  'dato': 'dato inicial',
  'lenguaje': 'python'
}
print(ref_x)
modify_ref(ref_x)
print(ref_x)

'''
  EXTRA
'''

# Valor

def replace_val(value_x, value_y):
  aux = value_x
  value_x = value_y
  value_y = aux
  return value_x, value_y

name = 'César'
lastname = 'Carmona'
name_rep, lastname_rep = replace_val(name, lastname)
print(f'Name: {name}, Lastname: {lastname}')
print(f'Name replaced: {name_rep}, lastname replaced: {lastname_rep}')

# Referencia

def replace_ref(reference_x, reference_y):
  aux = reference_x
  reference_x = reference_y
  reference_y = aux
  return reference_x, reference_y

fruits = ['apple', 'orange', 'banana', 'grape']
vegetables = ['tomato', 'carrot', 'onion', 'radish']

fruits_rep, vegetables_rep = replace_ref(fruits, vegetables)

print(f'Vegetables: {vegetables}')
print(f'Fruits: {fruits}')
print(f'Vegetables replaced: {vegetables_rep}')
print(f'Fruits replaced: {fruits_rep}')