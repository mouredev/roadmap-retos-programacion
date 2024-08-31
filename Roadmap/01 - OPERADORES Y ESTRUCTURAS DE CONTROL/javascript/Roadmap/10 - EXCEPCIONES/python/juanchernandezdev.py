### Python Exceptions ###

#! Zero Division

try:
  division = 10/0
except Exception as err:
  print(f'Can\'t divide by Zero!!, error info: {err}')
  
#! Index Error

try:
  my_list = [1, 2, 3, 4]
  my_list[8]
except Exception as err:
  print(f'Not a valid index, error info: {err}')
  
#! Optional Challenge
class FirstElementError(Exception):
  pass

def test_func(params: list):
  if type(params) != list:
    raise TypeError()
  elif len(params) > 4:
    raise IndexError()
  elif params[2] == 0:
    raise ZeroDivisionError()
  elif type(params[0]) == str:
    raise FirstElementError()


try:
  test_func(['try', 2, 4])
except TypeError as err:
  print(f'Param should be of type list.')
except IndexError as err:
  print(f'The length of the list should be less than 4.')
except ZeroDivisionError as err:
  print(f'The element at index 2 can\'t be a 0.')
except FirstElementError as err:
  print(f'The first element should be of type int.')
else:
  print('Not error was found.')
finally:
  print('Program ends!!')
  