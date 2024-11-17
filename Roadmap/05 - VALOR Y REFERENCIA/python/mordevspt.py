"""
- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según su tipo de dato.
"""

'''
En Python, las variables no se asignan por valor ni por referencia en el sentido estricto. 
En su lugar, Python utiliza un enfoque llamado “pasaje de objetos” o “pasaje de objetos por referencia”.
'''

# ASIGNACIÓN DE VARIABLES POR VALOR - VALORES PRIMITIVOS

# Asignación de valor numérico
print("\nAsignación de valor numérico\n")
valor1 = 10
valor2 = 33
print(valor1)
print(valor2)
valor2 = valor1
valor1 = 3 * 5
print(valor1)
print(valor2)

# Asignación de cadena de texto
print("\nAsignación de cadena de texto\n")
cadena1 = "Hola"
cadena2 = "Python!"
print(cadena1)
print(cadena2)
cadena2 = cadena1
cadena1 = "Adios"
print(cadena1)
print(cadena2)

# Asignación de valores Booleanos
print("\nAsignación de valores Booleanos\n")
semaforo_en_verde = False
senal_peatones = True
print(semaforo_en_verde)
print(senal_peatones)
semaforo_en_verde = senal_peatones
senal_peatones = False
print(semaforo_en_verde)
print(senal_peatones)

# Asignación de valores flotante
print("\nAsignación de valores flotante\n")
PI = 3.14
radio = 4.56
print(PI)
print(radio)
PI = radio
radio = 25.8
print(PI)
print(radio)

# ASIGNACIÓN DE VARIABLES POR REFERENCIA - NO PRIMITIVOS
# Heredan la posición de memoria

# Listas
print("\nListas\n")
lista_compra = ["fruta", "verdura", "carne"]
lista_embutidos = ["jamon", "chorizo", "butifarra"]
print(lista_compra)
print(lista_embutidos)
lista_embutidos = lista_compra
lista_embutidos.append("chistorra")
print(lista_compra) # Imprime la modificación realizada posteriormente sobre al lista "lista_embutidos"
print(lista_embutidos)

# Diccionario
print("\nDiccionario\n")
dict_dias_de_la_semana = {
    1:"Luneas",
    2:"Martes",
    3:"Miércoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sábado",
    7:"Domingo"
}
dict_meses_del_ano = {
  1:"Enero",
  2:"Febrero",
  3:"Marzo",
  4:"Abril",
  5:"Mayo",
  6:"Junio",
  7:"Julio",
  8:"Agosto",
  9:"Septiembre",
  10:"Octubre",
  11:"Noviembre",
  12:"Diciembre"
}
print(dict_dias_de_la_semana)
print(dict_meses_del_ano)
dict_meses_del_ano = dict_dias_de_la_semana
dict_dias_de_la_semana[13] = "Nuevo"
print(dict_dias_de_la_semana)
print(dict_meses_del_ano) # Imprime la modificación realizada posteriormente sobre el diccionario "dict_dias_de_la_semana"

# Sets
print("\nSets\n")
set_numeros_dado_6 = {1,2,3,4,5,6}
set_numeros_dado_20 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
print(set_numeros_dado_6)
print(set_numeros_dado_20)
set_numeros_dado_20 = set_numeros_dado_6
set_numeros_dado_20.add(21)
print(set_numeros_dado_6)
print(set_numeros_dado_20) # Imprime la modificación realizada posteriormente sobre el set "set_numeros_dado_6"

"""
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
  "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
  (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
"""
print("\nFUNCIONES\n")

# POR VALOR

# Asignación de valor numérico
print("\nAsignación de valor numérico\n")

def modify_int(value):
  value = 11
  print(value)

valor3 = 33
modify_int(valor3)
print(valor3)

# Asignación de cadena de texto
print("\nAsignación de valor numérico\n")

def modify_string(chain):
  chain = "java"
  print(chain)
  
cadena3 = "Hola, Python!"
modify_string(cadena3)
print(cadena3)

# Asignación de valores Booleanos
print("\nAsignación de valores Booleanos\n")

def modify_booleano(bool):
  bool = True
  print(bool)

letra_devuelta = True
modify_booleano(letra_devuelta)
print(letra_devuelta)

# Asignación de valores flotante
print("\nAsignación de valores flotante\n")

def modify_float(float):
  float = 7.85
  print(float)

diametro = 15.87
modify_float(diametro)
print(diametro)

# POR REFERENCIA

# Listas
print("\nListas\n")
lista_marcas = ["samsung", "apple"]

def modify_list(lst):
  lst.append("chocolate")
  print(lst)

modify_list(lista_marcas)
print(lista_marcas)

# Diccionario
print("\nDiccionario\n")

def modify_dict(dict):
  dict[3] = "Laboral"
  print(dict)

dict_sexo = {
  1:"Hombre",
  2:"Mujer"
}
modify_dict(dict_sexo)
print(dict_sexo)

# Set
set_numero_meses = {1,2,3,4,5,6,7,8,9,10,11,12}

def modify_set(set):
  set.add(13)
  print(set)

print("\nSet\n")
modify_set(set_numero_meses)
print(set_numero_meses)

"""
DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

print("\nEXTRA\n")

# Program one
def transforming_values(value1, value2):
  primer_valor = value1
  value1 = value2
  value2 = primer_valor
  return value1, value2

# Program two
def transforming_references(reference1, reference2):
  primer_valor = reference1
  reference1 = reference2
  reference2 = primer_valor
  return reference1, reference2

print("\nPrimer programa\n")
# Variables
mi_value1 = 45
mi_value2 = 4.5
# Función por valor
a,b = transforming_values(mi_value1,mi_value2)
# Imprimimos el resultado
print(f"Valores pasados a la función: {mi_value1} y {mi_value2}:")
print(f"Primer valor devuelto: {a}")
print(f"Segundo valor devuelto: {b}")
print(f"Los valores originales: {mi_value1} y {mi_value2}:")

print("\nPrimer programa\n")
# Variables
mi_list1 = [1,2,3,4,5]
mi_list2 = [6,7,8,9,10]
# Función por referencia
c,d = transforming_references(mi_list1,mi_list2)
print(f"Valores pasados a la función: {mi_list1} y {mi_list2}:")
print(f"Primer valor devuelto: {c}")
print(f"Segundo valor devuelto: {d}")
print(f"Los valores originales: {mi_list1} y {mi_list2}:")