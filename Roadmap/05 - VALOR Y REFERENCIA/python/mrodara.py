'''
En Python, el paso de argumentos se hace por asignación de objetos y se puede considerar 
un modelo de "paso por referencia", pero con algunos matices:

Para tipos inmutables (como int, float, str, tuple), el comportamiento se asemeja a un paso por valor 
porque no puedes modificar el contenido del objeto en sí, solo puedes reasignarlo.
Para tipos mutables (como list, dict, set), se asemeja más a un paso por referencia, 
ya que cualquier cambio en el objeto dentro de una función afectará el objeto original fuera de ella.
'''

# Ejemplo de paso por valor
a = 5

print(a)

b = a

b = 7

print(a)
print(b)

# Ejemplo de paso por referencia
my_list = [1,2,3,4,5]

print(my_list)

my_list2 = my_list

my_list2[0] = 100

print(my_list) # El índice 0 de my_list se ve afectado por el cambio en el mismo índice en my_list2

# Si queremos copiar listas u otros tipo de datos mutables tenemos usar el método copy() o recorrerlos y añadir los campos

my_list3 = my_list2.copy()

print(my_list3)

my_list2[0] = 1

print(my_list2)
print(my_list3)


###############################  DIFICULTAD EXTRA   ###################################

# Programa 1 - Paso por valor (int)

num1 = int(input('Introduce un valor para num1: '))
num2 = int(input('Introduce un valor para num2: '))

print(f'num1 vale: {num1} y num2 vale: {num2}')

print('Intercambio de valores')
temp = num1
num1 = num2
num2 = temp

print(f'Ahora num1 vale: {num1} y num2 vale: {num2}')

# Programa 2 - Paso por referencia (list)

# Vamos a generar dos listas con valores entre dos rangos
list1 = [i for i in range (1,11)]
list2 = [i for i in range (11,21)]

print(list1)
print(list2)

def paso_referencia(list1: list, list2: list) -> tuple:
    temp = list1
    list1 = list2
    list2 = temp
    
    return list1, list2

list3, list4 = paso_referencia(list1=list1, list2=list2)

print(f'{list1}: {list3}')
print(f'{list2}: {list4}')


###############################  FIN DIFICULTAD EXTRA   ###################################