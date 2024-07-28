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

c4 = c1 + ',' + c3 + c2 
print(c4) # ejemplo, otro ejemplo  

# Repeticion:

print(c1*3) # ejemploejemploejemplo   

# Pertenencia o busqueda:

print('e' in  c1) # True
print('1' in c1) # False

# Secuencia de escape:
"""
Se puede tener problemas si se intante usar las comillas dobles o las comillas simples porque los tomara como cierre de la cadena
para ello podemos usar un ruta de escape con la digonal inversa pero tambien sirve para hacer otra cosa:
"""

# \" o \'

print("ejemplo \" ejemplo2 \' ") # ejemplo " ejemplo2 ' 

# Como vemos la diañonal invertida no se ve en la impresion y en este caso le quita sus propiedades a las comillas.

# \n

print(" Linea 1 \n linea 2 \n linea 3")
# Linea 1
# linea 2
# linea 3

# \n siver para hacer un salto de linea.

# Tambien sirve para escribir asi con el unicode.
# https://www.freecodecamp.org/news/everything-you-need-to-know-about-encoding/ (Pagina de referencia.)(Columna Oct)

print("\105\152\145\155\160\154\157") # Ejemplo

# ord() seia la funcion inversa porque so le damos un caracter nos devuelve el unicode pero de html no de Oct.

print(ord('E')) # 69

# Solo se puede usar con un caracter y de forma inversa seria chr().

# Asi como letras se pueden imprimir otro tipo de caracteres especiales.

# Formateo de cadenas con %:

x = 'cadena'
x1 = "Ejemplo de formateo %s" % x
print(x1)

# %d es para numeros y %s es para cadenas el formato es el mismo y se puede hacer con mas variables y las pones dentro de un parentesis
# y las separamos con comas.

# Indexar:
"""
Al igual que con las listas y tipos de datos parecidos con las cadenas se pueden indexar sus caracterres y se hace de la
misma forma.
"""
x = 'cadena'
print(x[0]) # c
print(x[0:2]) # ca
print(x[2:]) # dena

# Como se ve se pueden indexar rangos de caracteres de la cadena.
# si no ponemos ningun rango por defecto estara hasta el minimo y/o maximo.

# Saltos o zancadas:

print(x[::2]) # cdn

# Al utilizar esta forma de indexar se puede usar un tercer parametro que por defecto esta en 1
# Esto es un salto en las cadena por eso el resultado es cdn.

# invertir:

print(x[::-1]) # anedac

# Como se ve se puede invertir una cadena poniendo -1 en el tercer parametro.
# Si variamos el numero como -2 se invertira la cadena y comenzara a realizar los saltos desde el nuevo inicio.

# Métodos:

# capitalize():

print(x.capitalize()) # Cadena

# Esto convierte el primer caracter de la cadena ingresada en mayuscula si ya lo esta entoces no hace nada.

# lower():

y = 'CADENA'
print(y.lower()) # cadena

# Esto convierte todas los caracteres de una cadena en minuscula y si ya lo estaban entonces no pasa nada.

# upper():

print(x.upper()) # CADENA

# Esto convierte todos los caracteres de una cadena a mayusculas y si ya lo estaban no pasa nada.

# swapcase():

z = 'CaDeNa'
print(z.swapcase()) # cAdEnA

# Esto convierte los caracteres mayusculas de una cadena en minusculas y biseversa.

# count():

print(x.count('a')) # 2

# Esto cuenta la cantidad de veces que se repite una cadena de texto dentro de otras.

# isalnum():

x2 = 'Jose1234'
print(x2.isalnum()) # True

# Esta devuelve true si todos los caracteres de una cadena seleccionala son alphanumericos osea numeros o letras.
# Tambien decir que si en la cadena solo hay careacteres alphanumericos y espacios en blanco devolvera false por los espacios.

# isalpha():

print(x2.isalpha()) # # False

# Esta devuelve true si todos los caracteres de una cadena son letras solo letras si hay espacio o numeros devolvera false.

# strip():

x3 = 'hola mundo'
print(x3.strip('h')) # ola mundo

# Esto compara el caracter de cada extremo con el parametro y si lo encuentra lo elimina sino no hace nada.

# zfill():

x4 = 'nada'
print(x4.zfill(5)) # 0nada

# Esto rellena la cadena con 0 a la izquierda hasta que la cadena tenga la longitud pasada como parametro.

# join():

x5 = ' y '.join(['1','2','3','4','5'])
print(x5) # 1 y 2 y 3 y 4 y 5

# Aqui vemos que tenemos que poner la cadena que separar los datos de la lista antes del elemento .join()
# dentro del parametro tiene que ir una lista que ojo tiene que ser de datos tipo string.

# split():

x6 = '1y3y4y5y6y7'
print(x6.split('y')) # ['1', '3', '4', '5', '6', '7']

# Esto utiliza como parametro un caracter del cual usara para saber cuando separar un dato de otro y ponerlo en una lista.

# replace:

print(x6.replace('y', ' ')) # 1 3 4 5 6 7

# Esto intercambia la cadena que se pasa como primer parametro por la cadena que se pasa como segundo parametro de la cadena original.

# sorted:

print(sorted('cadena'))

# La funcion sorted tiene muchas utilidades una de ellas es convertir y ordenar cadenas dentro de una lista(hipotesis: los ordena por 
# orden alfabetico) y al ser una lista si hay mas de una misma letra no se juntan o eliminan solo se almacenan.

"""
  DIFICULTAD EXTRA (opcional):
- Crea un programa que analice dos palabras diferentes y realice comprobaciones
  para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""

def vpai ():
    X = input('Ingrese la primer palabra: ')
    Y = input('Ingrese la segunda palabra: ')
    x = X.lower()
    y = Y.lower()
    # Palíndromos
    print(f"{X} es un palindromo." if x == x[::-1] else f"{X} no es un palindromo.")
    print(f"{Y} es un palindromo." if y == y[::-1] else f"{Y} no es un palindromo.")
    # Anagramas
    print(f"{X} y {Y} son anagramas." if sorted(x) == sorted(y) else f"{X} y {Y} no son anagramas.")
    # Isogramas
    def isograma(w):
        wd = {}
        for c in w:
            wd[c] = wd.get(c,0)+1
        wdn = list(wd.values())
        r = ''
        for l in wd:
            if wd[l] != wdn[0]:
                r = 'no '
                break
        return r
    print(f"{X} {isograma(x)}es un isograma.")
    print(f"{Y} {isograma(y)}es un isograma.")    
vpai()	

# Fin.