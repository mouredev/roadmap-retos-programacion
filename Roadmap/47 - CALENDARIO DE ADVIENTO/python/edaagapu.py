
# EJERCICIO:
# ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
# developers. Del 1 al 24 de diciembre: https://adviento.dev
# 
# Dibuja un calendario por terminal e implementa una
# funcionalidad para seleccionar días y mostrar regalos.
# - El calendario mostrará los días del 1 al 24 repartidos
#   en 6 columnas a modo de cuadrícula.
# - Cada cuadrícula correspondiente a un día tendrá un tamaño 
#   de 4x3 caracteres, y sus bordes serán asteríscos.
# - Las cuadrículas dejarán un espacio entre ellas.
# - En el medio de cada cuadrícula aparecerá el día entre el
#   01 y el 24.
#
# Ejemplo de cuadrículas:
# **** **** ****
# *01* *02* *03* ...
# **** **** ****
#
# - El usuario seleccioná qué día quiere descubrir.
# - Si está sin descubrir, se le dirá que ha abierto ese día
#   y se mostrará de nuevo el calendario con esa cuadrícula
#   cubierta de asteríscos (sin mostrar el día).
#
# Ejemplo de selección del día 1
# **** **** ****
# **** *02* *03* ...
# **** **** ****
#   
# - Si se selecciona un número ya descubierto, se le notifica
#   al usuario.

selected_nums = []

q_col = 6
q_row = 4

def gen_grid(columns:int, rows:int, numbers:list = [], width:int=4, height:int=3):
  borders = ['*'*width for _ in range(columns)]

  matrix = []
  for i in range(rows):
    row = []
    for j in range(columns):
      value = (j+1)+(columns*(i))
      number = f'*{str(value).zfill(width-2)}*' if value not in numbers else '*'*width
      row.append(number)
    matrix.append(row[:])

  print(' '.join(borders))
  for row in matrix:
    print(' '.join(row))
    print(' '.join(borders))

if __name__ == '__main__':
  num = 1
  gen_grid(q_col, q_row)
  while (num!=0):
    num = int(input('Escriba un dia entre 1 y 24 (O si desea terminar el proceso escriba 0): '))
    if (num in selected_nums):
      print('El numero ya fue escogido. Intente nuevamente')
      continue
    if (1<=num<=24):
      selected_nums.append(num)
      gen_grid(q_col, q_row, selected_nums)
