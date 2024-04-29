# Varaibles por Valor

a = 'Hola Mundo'
b = a # El valor de "a" se asigna a "b", creando como una copia de este

a += "!" # Se modifica el valor solo de "a"

print('a', a)
print('b', b)

# Variables por Referencia
# Con estructuras, no se crea un nuevo valor, sino que ambas variables apuntan a un mismo espacio en memoria

c = [1, 2, 3]
d = c

c.insert(0, 4)

print('c', c)
print('d', d)


# Funciones utilizando Variables por Valor

def firstFunction(str):
  str = 'Nuevo valor dentro de la funcion'
  return str

strOriginal = 'Fuera de la funcion'
print('Por valor - Dentro de la funcion: ', firstFunction(strOriginal))
print('Por valor - Fuera de la funcion: ', strOriginal)

# Funciones utilizando Variables por Referencia

def secondFunction(arr):
  arr.insert(0, 'Moure')
  return arr

arrOriginal = ['Andres', 'Brais', 'Chape']
print('Por referencia - Dentro de la funcion: ', secondFunction(arrOriginal))
print('Por referencia - Fuera de la funcion: ', arrOriginal)


# DIFICULTAD EXTRA

# Funcion para intercambiar variables por valor

def intercambiarValor(num1, num2):
  temp = num1
  num1 = num2
  num2 = temp
  return [num1, num2]

primerValor = 10
segundoValor = 5

print('Valores antes del intercambio')
print('primerValor: ', primerValor)
print('segundoValor" ', segundoValor)

nuevosValores = intercambiarValor(primerValor, segundoValor)

print('Valores despues del intercambio')
print('primerValor: ', primerValor)
print('segundoValor ', segundoValor)

print('Nuevos valores intercambiados')
print('primerValor: ', nuevosValores[0])
print('segundoValor ', nuevosValores[1])


# Funcion para intercambiar variables por referencia

nombresOriginal = ['Andres', 'Edith', 'Chape', 'Yc']

def intercambiarReferencias(arr):
  temp = arr[1]
  arr[1] = arr[3]
  arr[3] = temp
  return arr

print('Referencias antes del intercambio')
print('Lista original', nombresOriginal)

nombresNuevo = intercambiarReferencias(nombresOriginal)

print('Referencias despues del intercambio')
print('Lista original', nombresOriginal)

print('Nuevas referencias intercambiadas')
print('nombresNuevo', nombresNuevo)
