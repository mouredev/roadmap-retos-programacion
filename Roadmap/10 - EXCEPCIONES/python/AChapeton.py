myList = ['a', 'b', 'c', 'd']

#  TRY - Bloque del codigo que se va a evaluar

# EXCEPT - Bloque del codigo que se ejecuta si se encuentra un error en el bloque TRY

# FINALLY - Bloque de codigo (opcional) que se va a ejecutar una vez haya terminado el bloque TRY, independientemente de su resultado

# try:
#   len(myList[8])
# except:
#   print('No se puede acceder a una posiocion que no existe en la lista')
# finally:
#   print('Ancho de la lista: ', len(myList))

# try:
#   result = 10 / 0
#   print(result)
# except:
#   print('No se puede dividir entre 0')

# DIFICULTAD EXTRA

class customException:
  def __init__(self, name, message):
    self.name = name
    self.message = message

  def showMessage(self):
    print(f"{self.name}: {self.message}")

def myFunction(num1, num2):
  try:
    if(num1 <= 0):
      print("El primer valor no puede ser menor o igual a cero.")

    if((num2 % 2) != 0):
      print("El segundo valor debe ser un numero par.")
    
    if((num1 + num2) > 99):
      error = customException('Custom Error', "La suma de los valores no puede sobrepasar de 100.")
      error.showMessage()
  except:
    print('Error general.')
  finally:
    print('Fin del ejercicio')
  
myFunction(-1, 6)
myFunction(10, 5)
myFunction(51, 50)
myFunction(3, 6)