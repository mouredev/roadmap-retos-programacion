"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# Tipo Listas
lista = [1, 2, 3, 4]
lista = list("1234")
lista = [1, "Hola", 3.67, [1, 2, 3]]
# inserción .append
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]
l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]
#Añade .Extend una lista a otra lista
l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]
#  actualizacion
lista1 = [1,2,3,4,5,10]
lista1[5] = 20
print(lista1)
#borrado .remove
l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]
#Ordenación .sort
l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]
# tambien podemos ordenar de mayor a menor si se pasa como parámetro reverse=True
l = [3, 1, 2]
l.sort(reverse=True)
print(l) #[3, 2, 1]

# Tuplas (son inmutables, no se pueden modificar)
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)
#se pueden declarar sin parentesis tambien
tupla = 1, 2, 3
print(tupla)       #(1, 2, 3)
# Ordenación
tupla = tuple(sorted(tupla))  
print(tupla)
print(type(tupla))  #<class 'tuple'>

#Set son muy similar a las listas, pero... no puede haber elementos duplicados, Los set son desordenados, Sus elementos deben ser inmutables
s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>
#Remove
s = set([1, 2])
s.remove(2)
print(s) #{1}
#Insertar
l = set([1, 2])
l.add(3)
print(l) #{1, 2, 3}

# Diccionario
d1 = {
  "Nombre": "Anvildestroyer",
  "Edad": 10,
  "Documento": 11111111
}
print(d1)
#{'Nombre': 'Anvildestroyer', 'Edad': 32, 'Documento': 11111111}

# Eliminación
#Remove .Clear 
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

del d1["Edad"]  
print(f"eliminando edad:",d1) 
# Inserción
d1["Nombre"] = "AnvilDevstroyer"  
print(f"insertando nuevo nombre:",d1)
# Acceso
print(d1["Nombre"])  
# get()
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado
# Actualización
d1["age"] = "32"  
print(f"Actualizando edad:",d1)
# Ordenación
d1 = dict(sorted(d1.items()))  
print(f"Ordenando el directorio:",d1)
print(type(d1))


"""
* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.

"""