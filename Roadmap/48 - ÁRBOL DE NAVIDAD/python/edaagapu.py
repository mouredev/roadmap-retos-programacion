# EJERCICIO:
# ¡Ha comenzado diciembre! Es hora de montar nuestro
# árbol de Navidad...
# 
# Desarrolla un programa que cree un árbol de Navidad
# con una altura dinámica definida por el usuario por terminal.
# 
# Ejemplo de árbol de altura 5 (el tronco siempre será igual):
# 
#     *
#    ***
#   *****
#  *******
# *********
#    |||
#    |||
# 
# El usuario podrá seleccionar las siguientes acciones:
# 
# - Añadir o eliminar la estrella en la copa del árbol (@)
# - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
# - Añadir o eliminar luces de tres en tres (+) aleatoriamente
# - Apagar (*) o encender (+) las luces (conservando su posición)
# - Una luz y una bola no pueden estar en el mismo sitio
# 
# Sólo puedes añadir una estrella, y tantas luces o bolas
# como tengan cabida en el árbol. El programa debe notificar
# cada una de las acciones (o por el contrario, cuando no
# se pueda realizar alguna).

# 0 = ' ' Vacio
# 1 = '*' Rama
# 2 = 'o' Bola
# 3 = '*' Luz apagada
# 4 = '+' Luz encendida
# 5 = '@' Estrella
# 6 = '|' Tronco

from random import randint

class ChristmasTree:
  def __init__(self, height=3):
    self.height = height
    self.ml_holiday_tree = [[0 for _ in range(2*height -1 )]]
    self.mapper_dict = ' ,*,o,*,+,@,|'.split(',')
    self.md_holiday_tree = []

    for i_row in range(1,height+1):
      tree_cells = [1 for _ in range((2*i_row - 1))]
      empty_cells = [0 for _ in range(height-i_row)]
      self.ml_holiday_tree.append(empty_cells + tree_cells + empty_cells)

    empty_cells = [0 for _ in range(height-2)]
    base_cells = [6, 6, 6]
    for _ in range(2):
      self.ml_holiday_tree.append(empty_cells + base_cells + empty_cells)

  def change_star(self, put):
    self.ml_holiday_tree[0][self.height-1] = 5 if put else 0

  def __change_object__(self, put, obj, quantity):
    flag = 0
    while not put and flag < quantity:
      options = []
      for row in self.ml_holiday_tree[1:-2]:
        i_row = self.ml_holiday_tree.index(row)
        if obj in row:
          options.extend([(i_row, index) for index in range(len(row)) if row[index] == obj])
      
      if 0 <= len(options) <= quantity:
        for i_row, i_cell in options:
          self.ml_holiday_tree[i_row, i_cell] = 1
        flag = quantity + 1
      
      if len(options) > quantity:
        while flag < quantity:
          i_row, i_cell = options.pop(randint(0, len(options)-1))
          self.ml_holiday_tree[i_row][i_cell] = 1
          flag+=1
  
    while flag < quantity and put:
      i_row = randint(0, len(self.ml_holiday_tree)-1)
      i_cell = randint(0, len(self.ml_holiday_tree[i_row])-1)
      if self.ml_holiday_tree[i_row][i_cell] == 1:
        self.ml_holiday_tree[i_row][i_cell] = obj
        flag+=1

  def change_lights(self, put):
    self.__change_object__(put, 4, 3)

  def change_balls(self, put):
    self.__change_object__(put, 2, 2)

  def display(self):
    print('\n'.join(
      [''.join(
        [self.mapper_dict[cell] for cell in row]
      ) for row in self.ml_holiday_tree if max(row) > 0]
    ))
    print()
  
  def turn_on_lights(self):
    for i_row in range(len(self.ml_holiday_tree)):
      self.ml_holiday_tree[i_row] = [4 if value == 3 else value for value in self.ml_holiday_tree[i_row]]
      
  def turn_off_lights(self):
    for i_row in range(len(self.ml_holiday_tree)):
      self.ml_holiday_tree[i_row] = [3 if value == 4 else value for value in self.ml_holiday_tree[i_row]]


if __name__ == '__main__':
  menu_list = [
    'Terminar ejecución', 'Mostrar árbol de navidad', 'Agregar luces', 'Quitar luces',
    'Encender luces', 'Apagar luces', 'Agregar bolas navideñas', 'Quitar bolas navideñas', 
    'Agregar estrella', 'Quitar estrella'
  ]

  height = 0
  while height <= 1:
    try:
      height = int(input('¿Cuál será la altura del árbol?: '))
      if 1 >= height:
        raise Exception()
    except:
      print('Dato incorrecto, por favor ingresar un número positivo mayor a 1.')
  
  tree = ChristmasTree(height)
  tree.display()

  option = 1

  while option:
    menu_string = ['Ingresa la opción según corresponda:']
    menu_string.extend([f'({menu_list.index(menu_option)}) {menu_option}' for menu_option in menu_list[1:]])
    menu_string.append('-'*25)
    menu_string.append(f'(0) {menu_list[0]}')
    menu_string.append('-'*25)
    menu_string.append('Escribe una opción: ')

    menu = '\n'.join(menu_string)
    try:
      option = int(input(menu))
      match option:
        case 0:
          continue
        case 1:
          tree.display()
        case 2:
          tree.change_lights(True)
          tree.display()
        case 3:
          tree.change_lights(False)
          tree.display()
        case 4:
          tree.turn_on_lights()
          tree.display()
        case 5:
          tree.turn_off_lights()
          tree.display()
        case 6:
          tree.change_balls(True)
          tree.display()
        case 7:
          tree.change_balls(False)
          tree.display()
        case 8:
          tree.change_star(True)
          tree.display()
        case 9:
          tree.change_star(False)
          tree.display()

        case _:
          raise Exception()
    except:
      print('Dato incorrecto. Intente nuevamente.')