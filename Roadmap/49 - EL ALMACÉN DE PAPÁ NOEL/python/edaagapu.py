#  EJERCICIO:
#  Papá Noel tiene que comenzar a repartir los regalos...
#  ¡Pero ha olvidado el código secreto de apertura del almacén!

#  Crea un programa donde introducir códigos y obtener pistas.
 
#  Código:
#  - El código es una combinación de letras y números aleatorios
#    de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
#  - No hay repetidos.
#  - Se genera de manera aleatoria al iniciar el programa.
 
#  Usuario:
#  - Dispone de 10 intentos para acertarlo.
#  - En cada turno deberá escribir un código de 4 caracteres, y 
#    el programa le indicará para cada uno lo siguiente:
#    - Correcto: Si el caracter está en la posición correcta.
#    - Presente: Si el caracter existe, pero esa no es su posición.
#    - Incorrecto: Si el caracter no existe en el código secreto.
#  - Deben controlarse errores de longitud y caracteres soportados.
 
#  Finalización:
#  - Papa Noel gana si descrifra el código antes de 10 intentos.
#  - Pierde si no lo logra, ya que no podría entregar los regalos.

from random import randint

class Password:
  def __init__(self):
    self.available_characters = ['1', '2', '3', 'A', 'B', 'C']
    self.password_size = 4
    self._password = self.__generate_password__()
  
  def __generate_password__(self) -> str:
    password = ''
    while len(password) < self.password_size:
      select_character = self.available_characters[randint(0, len(self.available_characters)-1)]
      if select_character not in password:
        password += select_character
    return password
  
  def __eq__(self, value : list) -> tuple:
    validation = []
    if len(value) != self.password_size:
      raise Exception(f'La longitud de la contraseña debe ser de {self.password_size}')

    for f_char, s_char in zip(list(self._password), value):
      if s_char not in self.available_characters:
        raise Exception(f'El/los caracter(es) ingresados no hacen parte del vocabulario, recuerde que los permitidos son: {self.available_characters}')
      if f_char == s_char:
        validation.append((s_char, 'Correcto'))
      elif s_char in self._password:
        validation.append((s_char, 'Presente'))
      else:
        validation.append((s_char, 'Incorrecto'))
    
    return (''.join(value) == self._password, validation)

if __name__ == '__main__':
  pass_obj = Password()
  print(f"""Bienvenido al almacén de Papá Noel:
  Tu objetivo es adivinar la contraseña del almacen para poder entregar los regalos a tiempo.
  ¡Tienes 10 intentos!
  Recuerda:
    - Los caracteres permitidos son: {pass_obj.available_characters}
    - La longitud de la contraseña es: {pass_obj.password_size}
  """)
  for turn in range(1,11):
    try:
      user_password = list(input(f'(Turno No. {turn}) Ingresa tu contraseña: '))
      validation, position_chars = pass_obj == user_password
      if validation:
        break
      print(' | '.join([f'({character}) {validation}' for character, validation in position_chars]))
    except Exception as error:
      print(error)
      continue
  if validation and turn <= 10:
    print('Felicitaciones has logrado descifrar la contraseña del almacen')
  else:
    print('Infortunadamente Papá Noel no podrá entregar los regalos, ya que no descifraste la contraseña del almacen')