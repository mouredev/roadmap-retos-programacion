'''
Operaciones en Python
'''

t1 = 'Hola'
t2 = 'Python'
t3 = 'Py thon'

# Concatenación
print(t1 + t2)

# Repetición
print(t1 * 3)

# Indexing
print(t1[1])

# Slicing
print(t2[2:])

# Longitud
print(len(t1))

# Busqueda
print(t1.find('o'))
print('H' in t1)

# Reemplazo
print(t1.replace('H', 'Hh'))

# Division
print(t2.split('t'))
print(t3.split(' '))

# Mayusculas ó minúsculas
print(t2.lower())
print(t2.upper())

# Eliminar espacios al principio y al final de un string.
print(' Cinnamon Rat '.strip())

# Busqueda al principio y al final de un string.
print(t1.startswith('H'))
print(t1.endswith('a'))

# Busqueda de posición
print('Cinnamon Rat Rabbiting'.find('Ra'))
print('Cinnamon Rat Rabbiting'.find('Rab'))
print('Cinnamon Rat Rabbiting'.find('R', 11))

# Busqueda de coincidencias
print('Cinnamon Rat Rabbiting'.count('a'))

# Interpolacion
print(f'{t1}, estas viendo {t2}. O bueno, jeje, también {t3}')

# Formateo
print('{}, estás viendo {}, bienvenido!'.format(t1, t2))

# De caracteres a listas.
print(list(t3))

# De string a integer
num = '12345'
num_ = int(num)
print(type(num_))

# De string a float
dnum = '1234.56'
dnum_ = float(dnum)
print(type(dnum_))

# Comprobaciones
print(t1.isalnum())
print(t1.isalpha())
print(t1.islower())
print(t1.isdecimal())

'''
Crea un programa que analice dos palabras diferentes y realice comprobaciones para verificar si son palíndromos, anagramas ó isogramas.
'''

def check(w1: str, w2: str):
  print(f"Verifiquemos si {w1} es palíndromo. {w1 == w1[::-1]}") # Con el slicing [::-1] damos vuelta la palabra.
  print(f"Verifiquemos si {w2} es palíndromo. {w2 == w2[::-1]}") # La lógica es que si la palabra equivale a su misma palabra a la inversa, entonces es palíndroma.

  print(f"¿ Es {w1} anagrama de {w2}?: {sorted(w1) == sorted(w2)}")

  def isogram(word: str) -> bool:

        word_dict = dict() # Establecemos un diccionario vacío.
        for character in word: # Loopeamos entre los carácteres dentro de word.
            word_dict[character] = word_dict.get(character, 0) + 1 # Accedemos a cada valor.
        isogram = True # Valor inicial a 'isogram' seteado.
        values = list(word_dict.values()) # La lista de los word.dict.
        isogram_len = values[0] 
        
        for word_count in values: # Por cada valor dentro de values:
            if word_count != isogram_len: # Si el word_count NO es igual al valor de isogram_len, entonces es falso.
                isogram = False
                break

        return isogram

  print(f"¿Es {w1} un isograma?: {isogram(w1)}")
  print(f"¿Es {w2} un isograma?: {isogram(w2)}")

check('salas', 'subcampeon')
