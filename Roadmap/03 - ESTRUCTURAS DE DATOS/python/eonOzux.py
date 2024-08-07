# Instrucciones =>
# * EJERCICIO:
# * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
# *   en tu lenguaje.
# * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
# *

lista = [ 2, 56, 11, 32, 1, 9]

x = 1
lista.append(x)
print(lista) 
# Agrega un ítem al final de la lista. Equivale a Lista + x. 

lista.insert(3, x)
print(lista) 
# Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará, por lo tanto a.insert(0, x) inserta al principio de la lista y a.insert(len(a), x) equivale a a.append(x).

lista.remove(x)
print(lista) 
# Quita el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.

lista.pop(3)
print(lista) 
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

lista.clear()
print(lista) 
# Elimina todos los elementos de la lista. Equivalente a del a[:].

lista_ind = [4, 56, 34]
lista_ind.index(56)
print(lista_ind) 
# Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. Lanza una excepción ValueError si no existe tal elemento.

lista.count(x)
print(lista) 
# Retorna el número de veces que x aparece en la lista.

lista.sort(key=None, reverse=False)
print(lista) 
# Ordena los elementos de la lista in situ (los argumentos pueden ser usados para personalizar el orden de la lista, 

lista.reverse()
print(lista) 
# Invierte los elementos de la lista in situ. Es una manera distinta y corta de usar el metodo de list con la operacion -1

lista.copy()
print(lista) 
# Retorna una copia superficial de la lista. Equivalente a a[:].

#TUPLAS 

tuplas = ( 7, 15, 44, 2, 76)
tupla_lista = list(tuplas)
tupla_lista.sort()
print(tuple(tupla_lista))

# DICCIONARIOS

motofavorita = {
  "marca": "BMW",
  "model": "GS1250R",
  "año": 2024
}

print(motofavorita["model"])

motofavorita['nombre'] = 'Juan Ignacio'
print(motofavorita)

# * DIFICULTAD EXTRA (opcional):
# * Crea una agenda de contactos por terminal.
# * - Debes implementar funcionalidades de búsqueda, inserción, actualización
# *   y eliminación de contactos.
# * - Cada contacto debe tener un nombre y un número de teléfono.
# * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
# *   y a continuación los datos necesarios para llevarla a cabo.
# * - El programa no puede dejar introducir números de teléfono no númericos y con más
# *   de 11 dígitos (o el número de dígitos que quieras).
# * - También se debe proponer una operación de finalización del programa.
 
def validar_telefono(telefono):
  
  # Función para validar el número de teléfono.

  # Args:
    # telefono: El número de teléfono ingresado por el usuario (string).

  # Returns:
    #True si el número es válido, False en caso contrario.
    
  # Validar longitud del número (máximo 11 dígitos)
  if len(telefono) > 11:
    print("No puede ser mas de 11 digitos")
    return False
  

  # Validar que solo sean números enteros
  for digito in telefono:
    if not digito.isdigit():
      return False

  return True

def solicitar_informacion():
  """
  Función para solicitar información al usuario y validarla.

  Returns:
    Un diccionario con la información del usuario.
  """
  agenda = {}

  while True:
    nombre = input("Ingrese su nombre: ")
    if nombre:
      agenda["nombre"] = nombre
      break
    else:
      print("Error: El nombre no puede estar vacío.")

  while True:
    telefono = input("Ingrese su número de teléfono (máximo 11 dígitos): ")
    if validar_telefono(telefono):
      agenda["telefono"] = telefono
      break
    else:
      print("Error: El número de teléfono no es válido. Ingrese solo números enteros (máximo 11 dígitos).")

  while True:
    pais = input("Ingrese su país de residencia: ")
    if pais:
      agenda["pais"] = pais
      break
    else:
      print("Error: El país no puede estar vacío.")

  return agenda

def main():
  """
  Función principal para ejecutar el programa.
  """
  datos_usuario = solicitar_informacion()

  print("\nInformación del usuario:")
  for clave, valor in datos_usuario.items():
    print(f"{clave}: {valor}")

if __name__ == "__main__":
  main()
