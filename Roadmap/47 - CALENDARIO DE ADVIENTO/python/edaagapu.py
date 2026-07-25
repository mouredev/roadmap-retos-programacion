
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

numbers = []

columns = 6
rows = 4

prices = ['Curso de lógica de programación', 'Diplomado sobre Metodologías Ágiles', 'Desarrollo de interfaces con Qt4', 
  'Introducción a la programación funcional', 'Desarrollo en C#', 'Buenas prácticas de programación en Java Springboot', 
  '¿Cómo hacer Smart Commits?', 'Uso básico de la terminal Linux', 'Primeros pasos en Django Rest Framework (DRF)',
  'Práctica aplicada de los patrones SOLID en Java', 'Introducción de Base de Datos', 'Buenas prácticas dentro de Python',
  'Paradigma de Metodologías Tradicionales ¿Aún tienen uso? ¿En qué casos es aplicable?', 'Data Science con Python y R',
  'GO ¿El lenguaje del futuro?', 'Patrones de Diseño de Software aplicados en Python', 'Algoritmos de optimización aplicados en C++',
  'Fundamentos de la Inteligencia Artificial', 'Aplicación en la actualidad del IoT', 'Uso de librería numpy y pandas dentro de Python',
  'POO aplicada en Java', '0 a héroe en PostgreSQL', 'Generación de servicios REST con AWS Api Gateway y Lambda',
  'Programación básica en C#'
]

def gen_grid(width:int=4):
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
  gen_grid()
  while (num!=0):
    num = int(input('Escriba un dia entre 1 y 24 (O si desea terminar el proceso escriba 0): '))
    if (num in numbers):
      print('El numero ya fue escogido. Intente nuevamente')
      continue
    if (1<=num<=24):
      print(f'¡Felicitaciones! Su premio es: "{prices[num-1]}"')
      numbers.append(num)
      gen_grid()
