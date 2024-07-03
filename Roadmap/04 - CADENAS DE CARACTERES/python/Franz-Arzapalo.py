"""
EJERCICIO: #04 CADENAS DE CARACTERES
- Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
  en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
  conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

  DIFICULTAD EXTRA (opcional):
- Crea un programa que analice dos palabras diferentes y realice comprobaciones
  para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""

# 1. Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#    en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):

# Definición:
"""
Las cadenas como se vio en los tipos de datos primitivos sabemos que se pueden definir con comillas dobles " 
o comillas simples '.
"""

c1 = "ejemplo"
c2 = 'otro ejemplo'

print(c1, c2) # ejemplo otro ejemplo

c3 = ' '

# Tambien se puede definir una cadena con espacio vacios.

# Concatenación:
"""
Existen varias formas de concatenar cadenas de texto, concatenar se puede definir como la accion de unir mas de una
cadena de texto en cualquier aspecto ya sea para definir una variable, o para imprimir el resultado de una función.
"""

# Uso de + para concatenar:

c4 = c1 + c3 + c2 
print(c4) # ejemplo otro ejemplo

# Uso 