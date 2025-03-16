'''
  EJERCICIO
'''

my_list = [1, 2, 3, 'c', True, 'texto']
print(f'Lista original:\n{my_list}')
# - Añade un elemento al final.
my_list.append('elemento final')
print(f'Lista después de agregar un elemento al final:\n{my_list}')
# - Añade un elemento al principio.
my_list.insert(0, 'primer elemento')
print(f'Lista después de agregar un elemento al principio:\n{my_list}')
# - Añade varios elementos en bloque al final.
my_list.extend("Mundo")
print(f'Lista después de agregar varios elementos al final:\n{my_list}')
# - Añade varios elementos en bloque en una posición concreta.
my_list[8:8] = "Hola"
print(f'Lista después de agregar varios elementos en una posición concreta:\n{my_list}')
# - Elimina un elemento en una posición concreta.
del my_list[3]
print(f'Lista después de1 eliminar un elemento en una posición concreta:\n{my_list}')
# - Actualiza el valor de un elemento en una posición concreta.
my_list[5] = 'Py'
print(f'Lista después de actualizar un elemento en una posición concreta:\n{my_list}')
# - Comprueba si un elemento está en un conjunto.
print(f'6 esta en la lista?: {6 in my_list}')
# - Elimina todo el contenido del conjunto.
my_list.clear()
print(f'Lista después de eliminar todo su contenido:\n{my_list}')

'''
  EXTRA
'''

A = {12, 45, 76, 24, 65, 75, 13, 54}
B = {56, 65, 12, 13, 67, 23, 87, 23}

print(f'''
Dado los siguientes conjuntos:
  A = {A}
  B = {B}
Estas son su operaciones entre ellos: ''')

print(f'''
Unión: A U B = {A | B}
Todo elemento tal que pertence a por lo menos uno de los conjuntos
Intersección: A ∩ B = {A & B}
Todo elemento que pertenece a ambos conjuntos
Diferencia: A - B = {A - B}
Todos los elementos de A que no estan en B
Diferencia: B - A = {B - A}
Todos los elementos de B que no estan en A
Diferencia simétrica: A Δ B = {A ^ B}
Todos los elementos que estan en A o en B pero
no en ambos a la vez
''')