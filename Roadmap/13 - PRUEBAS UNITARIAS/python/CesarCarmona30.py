'''
  EJERCICIO

  Pruebas elaboradas con el modulo doctest
  Ejecutado en terminal con python -m doctest -v file.py
'''

def suma(num1, num2):
  '''
  Función que suma dos números
  y retorna su valor

  >>> suma(10, 20)
  30

  >>> suma(324, 562)
  886

  >>> suma(432, 'hola')
  'Error: Valor no númerico recibido.'

  >>> suma(1e312, 1)
  'Error: Exceso del valor númerico.'
  
  '''
  try:
    result = num1 + num2
    if result == float('inf'):
      raise OverflowError
    return result
  except TypeError:
    return f'Error: Valor no númerico recibido.'
  except OverflowError:
    return f'Error: Exceso del valor númerico.'
  
'''
  EXTRA
'''


def createData(name = None, age = None, birth_date = None, languages = None):
  '''
  Función que crea un diccionario
  con los datos proporcionados

  >>> name, age, birth_date, languages = 'César', 19, '30-07-2004', ['Java', 'Python', 'C++', 'JavaScript']
  >>> data = createData(name, age, birth_date, languages)
  >>> validateFields(data)
  True
  >>> validateData(data)
  True
  >>> name_2, age_2, birth_date_2 = 'Ale', '22', '01-11-01'
  >>> createData(name_2, age_2, birth_date_2)
  'Algunos argumentos no se introdujeron.'
  >>> data_3 = createData(name_2, age_2, birth_date_2, ['JavaScript', 'C'])
  >>> validateData(data_3)
  False
  >>> data_4 = { "name": "Diego", "age": 15 }
  >>> validateFields(data_4)
  False
  '''

  if None in (name, age, birth_date, languages):
    return 'Algunos argumentos no se introdujeron.'
  return {
    "name": name,
    "age": age,
    "birth_date": birth_date,
    "programming_languages": languages
  }

def validateFields(data_dict):
  return all(key in data_dict for key in ["name", "age", "birth_date", "programming_languages"])

def validateData(data):
  return all([
    isinstance(data.get('name'), str),
    isinstance(data.get('age'), int),
    isinstance(data.get('birth_date'), str),
    isinstance(data.get('programming_languages'), list)
  ])