""" /*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */ """

saludo = "hola"
lenguaje = "python"

#subcadena
print(saludo[0:3])
print(saludo[1:3])

#acceso caracteres especificos
print(saludo[0])

# logitud
print(len(saludo))

#concatenacion
print(saludo + " " + lenguaje)

#multiplicacion
print(saludo * 3)

#reccorido
for letra in saludo:
  print(letra)

for letra in lenguaje:
  print(letra)


#conversion a mayusculas
saludar = saludo + " " + lenguaje
saludar_mayusculas = saludar.upper()
print(saludar_mayusculas)

#convertir a minusculas
saludar_minusculas = saludar_mayusculas.lower()
print(saludar_minusculas)

#inicial mayuscula
print(saludar.capitalize())
print(saludar.title(), "este es ima ´riena de totñe()") # convierte la primera letra de cada palabra en mayuscula

# reemplazo
reemplazo = saludo.replace("h", "J")
print(reemplazo)

# divisio
division = saludar.split(" ")
print(division)

# union
# -> es una manera un poco burda de unir palabras pero funciona
oracion = " ".join(division)
print(oracion)

# Interporacion
Saludo_interpolado = f"{saludo} {lenguaje}"
print(Saludo_interpolado)

# verificacion
print("a" in lenguaje)
print("y" in lenguaje)

# busqueda
print(saludar.find("python"))

# transformacion en lista de caracteres
print(list(saludar))

# verificacion

print(saludar.isnumeric())
print(saludar.isalnum())
print(saludar.isalpha())

### dificulatad extra

def analisis(palabra1: str, palabra2: str):
  #palindromo
  print(f"{palabra1} es un palindromo --> {palabra1 == palabra1[::-1]}")
  print(f"{palabra2} es un palindromo --> {palabra2 == palabra2[::-1]}")

  #anagrama
  print(f"{palabra1} es un anagrama de {palabra2}? {sorted(palabra1) == sorted(palabra2)}")
  
  #isograma

  def isograma(palabra: str) -> bool:
    palabra_dic = dict()

    for letra in palabra:
      palabra_dic[letra] = palabra_dic.get(letra, 0) + 1

    isograma = True
    values = list(palabra_dic.values())
    isograma_len = values[0]

    for contar_palabras in values:
      if contar_palabras != isograma_len:
        isograma = False
        break
    return isograma

  print(f"{palabra1} es un isograma= -> {isograma(palabra1)}")
  print(f"{palabra1} es un isograma= -> {isograma(palabra2)}")
  
  isograma(palabra1)
  isograma(palabra2)
  
analisis("radar", "anilina")
analisis("cara", "arca")